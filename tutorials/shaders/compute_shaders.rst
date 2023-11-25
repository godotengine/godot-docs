.. _doc_compute_shaders:

Using compute shaders
=====================

This tutorial will walk you through the process of creating a minimal compute
shader. But first, a bit of background on compute shaders and how they work with
Godot.

.. note::

   This tutorial assumes you are familiar with shaders generally. If you are new
   to shaders please read :ref:`doc_introduction_to_shaders` and :ref:`your
   first shader <toc-your-first-shader>` before proceeding with this tutorial.

A compute shader is a special type of shader program that is orientated towards
general purpose programming. In other words, they are more flexible than vertex
shaders and fragment shaders as they don't have a fixed purpose (i.e.
transforming vertices or writing colors to an image). Unlike fragment shaders
and vertex shaders, compute shaders have very little going on behind the scenes.
The code you write is what the GPU runs and very little else. This can make them
a very useful tool to offload heavy calculations to the GPU.

Now let's get started by creating a short compute shader.

First, in the **external** text editor of your choice, create a new file called
``compute_example.glsl`` in your project folder. When you write compute shaders
in Godot, you write them in GLSL directly. The Godot shader language is based on
GLSL. If you are familiar with normal shaders in Godot, the syntax below will
look somewhat familiar.

.. note::

   Compute shaders can only be used from RenderingDevice-based renderers (the
   Forward+ or Mobile renderer). To follow along with this tutorial, ensure that
   you are using the Forward+ or Mobile renderer. The setting for which is
   located in the top right-hand corner of the editor.

   Note that compute shader support is generally poor on mobile devices (due to
   driver bugs), even if they are technically supported.

Let's take a look at this compute shader code:

.. code-block:: glsl

    #[compute]
    #version 450

    // Invocations in the (x, y, z) dimension
    layout(local_size_x = 2, local_size_y = 1, local_size_z = 1) in;

    // A binding to the buffer we create in our script
    layout(set = 0, binding = 0, std430) restrict buffer MyDataBuffer {
        float data[];
    }
    my_data_buffer;

    // The code we want to execute in each invocation
    void main() {
        // gl_GlobalInvocationID.x uniquely identifies this invocation across all work groups
        my_data_buffer.data[gl_GlobalInvocationID.x] *= 2.0;
    }

This code takes an array of floats, multiplies each element by 2 and store the
results back in the buffer array. Now let's look at it line-by-line.

.. code-block:: glsl

    #[compute]
    #version 450

These two lines communicate two things:

 1. The following code is a compute shader. This is a Godot-specific hint that is needed for the editor to properly import the shader file.
 2. The code is using GLSL version 450.

You should never have to change these two lines for your custom compute shaders.

.. code-block:: glsl

    // Invocations in the (x, y, z) dimension
    layout(local_size_x = 2, local_size_y = 1, local_size_z = 1) in;

Next, we communicate the number of invocations to be used in each workgroup.
Invocations are instances of the shader that are running within the same
workgroup. When we launch a compute shader from the CPU, we tell it how many
workgroups to run. Workgroups run in parallel to each other. While running one
workgroup, you cannot access information in another workgroup. However,
invocations in the same workgroup can have some limited access to other invocations.

Think about workgroups and invocations as a giant nested ``for`` loop.

.. code-block:: glsl

    for (int x = 0; x < workgroup_size_x; x++) {
      for (int y = 0; y < workgroup_size_y; y++) {
         for (int z = 0; z < workgroup_size_z; z++) {
            // Each workgroup runs independently and in parallel.
            for (int local_x = 0; local_x < invocation_size_x; local_x++) {
               for (int local_y = 0; local_y < invocation_size_y; local_y++) {
                  for (int local_z = 0; local_z < invocation_size_z; local_z++) {
                     // Compute shader runs here.
                  }
               }
            }
         }
      }
    }


Workgroups and invocations are an advanced topic. For now, remember that we will
be running two invocations per workgroup.

.. code-block:: glsl

    // A binding to the buffer we create in our script
    layout(set = 0, binding = 0, std430) restrict buffer MyDataBuffer {
        float data[];
    }
    my_data_buffer;

Here we provide information about the memory that the compute shader will have
access to. The ``layout`` property allows us to tell the shader where to look
for the buffer, we will need to match these ``set`` and ``binding`` positions
from the CPU side later.

The ``restrict`` keyword tells the shader that this buffer is only going to be
accessed from one place in this shader. In other words, we won't bind this
buffer in another ``set`` or ``binding`` index. This is important as it allows
the shader compiler to optimize the shader code. Always use ``restrict`` when
you can.

This is an *unsized* buffer, which means it can be any size. So we need to be
careful not to read from an index larger than the size of the buffer.

.. code-block:: glsl

    // The code we want to execute in each invocation
    void main() {
        // gl_GlobalInvocationID.x uniquely identifies this invocation across all work groups
        my_data_buffer.data[gl_GlobalInvocationID.x] *= 2.0;
    }

Finally, we write the ``main`` function which is where all the logic happens. We
access a position in the storage buffer using the ``gl_GlobalInvocationID``
built in variables. ``gl_GlobalInvocationID`` gives you the global unique ID for
the current invocation.

To continue, write the code above into your newly created ``compute_example.glsl``
file.

Create a local RenderingDevice
------------------------------

To interact with and execute a compute shader, we need a script.
Create a new script in the language of your choice and attach it to any Node
in your scene.

Now to execute our shader we need a local :ref:`class_RenderingDevice`
which can be created using the :ref:`class_RenderingServer`:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Create a local rendering device.
    var rd := RenderingServer.create_local_rendering_device()

 .. code-tab:: csharp

    // Create a local rendering device.
    var rd = RenderingServer.CreateLocalRenderingDevice();

After that, we can load the newly created shader file ``compute_example.glsl``
and create a precompiled version of it using this:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Load GLSL shader
    var shader_file := load("res://compute_example.glsl")
    var shader_spirv: RDShaderSPIRV = shader_file.get_spirv()
    var shader := rd.shader_create_from_spirv(shader_spirv)

 .. code-tab:: csharp

    // Load GLSL shader
    var shaderFile = GD.Load<RDShaderFile>("res://compute_example.glsl");
    var shaderBytecode = shaderFile.GetSpirV();
    var shader = rd.ShaderCreateFromSpirV(shaderBytecode);

.. warning::

    Local RenderingDevices cannot be debugged using tools such as
    `RenderDoc <https://renderdoc.org/>`__.

Provide input data
------------------

As you might remember, we want to pass an input array to our shader, multiply
each element by 2 and get the results.

We need to create a buffer to pass values to a compute shader. We are dealing
with an array of floats, so we will use a storage buffer for this example. A
storage buffer takes an array of bytes and allows the CPU to transfer data to
and from the GPU.

So let's initialize an array of floats and create a storage buffer:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Prepare our data. We use floats in the shader, so we need 32 bit.
    var input := PackedFloat32Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    var input_bytes := input.to_byte_array()

    # Create a storage buffer that can hold our float values.
    # Each float has 4 bytes (32 bit) so 10 x 4 = 40 bytes
    var buffer := rd.storage_buffer_create(input_bytes.size(), input_bytes)

 .. code-tab:: csharp

    // Prepare our data. We use floats in the shader, so we need 32 bit.
    var input = new float[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    var inputBytes = new byte[input.Length * sizeof(float)];
    Buffer.BlockCopy(input, 0, inputBytes, 0, inputBytes.Length);

    // Create a storage buffer that can hold our float values.
    // Each float has 4 bytes (32 bit) so 10 x 4 = 40 bytes
    var buffer = rd.StorageBufferCreate((uint)inputBytes.Length, inputBytes);

With the buffer in place we need to tell the rendering device to use this
buffer. To do that we will need to create a uniform (like in normal shaders) and
assign it to a uniform set which we can pass to our shader later.

.. tabs::
 .. code-tab:: gdscript GDScript

    # Create a uniform to assign the buffer to the rendering device
    var uniform := RDUniform.new()
    uniform.uniform_type = RenderingDevice.UNIFORM_TYPE_STORAGE_BUFFER
    uniform.binding = 0 # this needs to match the "binding" in our shader file
    uniform.add_id(buffer)
    var uniform_set := rd.uniform_set_create([uniform], shader, 0) # the last parameter (the 0) needs to match the "set" in our shader file

 .. code-tab:: csharp

    // Create a uniform to assign the buffer to the rendering device
    var uniform = new RDUniform
    {
        UniformType = RenderingDevice.UniformType.StorageBuffer,
        Binding = 0
    };
    uniform.AddId(buffer);
    var uniformSet = rd.UniformSetCreate(new Array<RDUniform> { uniform }, shader, 0);


Defining a compute pipeline
---------------------------

The next step is to create a set of instructions our GPU can execute.
We need a pipeline and a compute list for that.

The steps we need to do to compute our result are:

1. Create a new pipeline.
2. Begin a list of instructions for our GPU to execute.
3. Bind our compute list to our pipeline
4. Bind our buffer uniform to our pipeline
5. Specify how many workgroups to use
6. End the list of instructions

.. tabs::
 .. code-tab:: gdscript GDScript

    # Create a compute pipeline
    var pipeline := rd.compute_pipeline_create(shader)
    var compute_list := rd.compute_list_begin()
    rd.compute_list_bind_compute_pipeline(compute_list, pipeline)
    rd.compute_list_bind_uniform_set(compute_list, uniform_set, 0)
    rd.compute_list_dispatch(compute_list, 5, 1, 1)
    rd.compute_list_end()

 .. code-tab:: csharp

    // Create a compute pipeline
    var pipeline = rd.ComputePipelineCreate(shader);
    var computeList = rd.ComputeListBegin();
    rd.ComputeListBindComputePipeline(computeList, pipeline);
    rd.ComputeListBindUniformSet(computeList, uniformSet, 0);
    rd.ComputeListDispatch(computeList, xGroups: 5, yGroups: 1, zGroups: 1);
    rd.ComputeListEnd();

Note that we are dispatching the compute shader with 5 work groups in the
X axis, and one in the others. Since we have 2 local invocations in the X axis
(specified in our shader), 10 compute shader invocations will be launched in
total. If you read or write to indices outside of the range of your buffer, you
may access memory outside of your shaders control or parts of other variables
which may cause issues on some hardware.

Execute a compute shader
------------------------

After all of this we are almost done, but we still need to execute our pipeline.
So far we have only recorded what we would like the GPU to do; we have not
actually run the shader program.

To execute our compute shader we need to submit the pipeline to the GPU and
wait for the execution to finish:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Submit to GPU and wait for sync
    rd.submit()
    rd.sync()

 .. code-tab:: csharp

    // Submit to GPU and wait for sync
    rd.Submit();
    rd.Sync();

Ideally, you would not call ``sync()`` to synchronize the RenderingDevice right
away as it will cause the CPU to wait for the GPU to finish working. In our
example, we synchronize right away because we want our data available for reading
right away. In general, you will want to wait *at least* 2 or 3 frames before
synchronizing so that the GPU is able to run in parallel with the CPU.

.. warning::

    Long computations can cause Windows graphics drivers to "crash" due to
    :abbr:`TDR (Timeout Detection and Recovery)` being triggered by Windows.
    This is a mechanism that reinitializes the graphics driver after a certain
    amount of time has passed without any activity from the graphics driver
    (usually 5 to 10 seconds).

    Depending on the duration your compute shader takes to execute, you may need
    to split it into multiple dispatches to reduce the time each dispatch takes
    and reduce the chances of triggering a TDR. Given TDR is time-dependent,
    slower GPUs may be more prone to TDRs when running a given compute shader
    compared to a faster GPU.

Retrieving results
------------------

You may have noticed that, in the example shader, we modified the contents of the
storage buffer. In other words, the shader read from our array and stored the data
in the same array again so our results are already there. Let's retrieve
the data and print the results to our console.

.. tabs::
 .. code-tab:: gdscript GDScript

    # Read back the data from the buffer
    var output_bytes := rd.buffer_get_data(buffer)
    var output := output_bytes.to_float32_array()
    print("Input: ", input)
    print("Output: ", output)

 .. code-tab:: csharp

    // Read back the data from the buffers
    var outputBytes = rd.BufferGetData(buffer);
    var output = new float[input.Length];
    Buffer.BlockCopy(outputBytes, 0, output, 0, outputBytes.Length);
    GD.Print("Input: ", string.Join(", ", input));
    GD.Print("Output: ", string.Join(", ", output));

With that, you have everything you need to get started working with compute
shaders.

.. seealso::

   The demo projects repository contains a
   `Compute Shader Heightmap demo <https://github.com/godotengine/godot-demo-projects/tree/master/misc/compute_shader_heightmap>`__
   This project performs heightmap image generation on the CPU and
   GPU separately, which lets you compare how a similar algorithm can be
   implemented in two different ways (with the GPU implementation being faster
   in most cases).
