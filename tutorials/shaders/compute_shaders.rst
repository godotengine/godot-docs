.. _doc_compute_shaders:

Using compute shaders
=====================


Think of compute shaders as blocks of code that are executed on the GPU for any purpose we want.
Compute shaders are independent from the graphics pipeline and do not have much fixed-functionality.
Contrast this with fragment shaders which are used specifically for assigning a color to a fragment in a render target.
The big benefit of compute shaders over code executed on a CPU is the high amount of parallelization that GPUs provide.

Because compute shaders are independent of the graphics pipeline we don't have any user defined inputs or outputs
(like a mesh going into the vertex shader or a texture coming out of a fragment shader). Instead, compute shaders
make changes directly to memory stored on the GPU from which we can read and write using scripts.

How they work
-------------

Compute shaders can be thought of as a mass of small computers called work groups.
Much like super computers they are aligned in rows and columns but also stacked on top of each other
essentially forming a 3D array of them.

When creating a compute shader we can specify the number of work groups we wish to use.
Keep in mind that these work groups are independent from each other and therefore can not depend on the results from other work groups.

In each work group we have another 3D array of threads called invocations, but unlike work groups, invocations can communicate with each other. The number of invocations in each work group is specified inside the shader.

So now lets work with a compute shader to see how it really works.

Creating a ComputeShader
------------------------

To begin using compute shaders, create a new text file called "compute_example.glsl". When you write compute shaders in Godot, you write them in GLSL directly. The Godot shader language is based off of GLSL so if you are familiar with normal shaders in Godot the syntax below will look somewhat familiar.

Let's take a look at this compute shader code:

.. code-block:: glsl

    #[compute]
    #version 450

    // Invocations in the (x, y, z) dimension
    layout(local_size_x = 2, local_size_y = 1, local_size_z = 1) in;

    // A binding to the buffer we create in our script
    layout(set = 0, binding = 0, std430) restrict buffer MyDataBuffer {
        double data[];
    }
    my_data_buffer;

    // The code we want to execute in each invocation
    void main() {
        // gl_GlobalInvocationID.x uniquely identifies this invocation across all work groups
        my_data_buffer.data[gl_GlobalInvocationID.x] *= 2.0;
    }

This code takes an array of doubles, multiplies each element by 2 and store the results back in the buffer array.

To continue copy the code above into your newly created "compute_example.glsl" file.

Create a local RenderingDevice
------------------------------

To interact and execute a compute shader we need a script. So go ahead and create a new script in the language of your choice and attach it to any Node in your scene.

Now to execute our shader we need a local :ref:`RenderingDevice <class_RenderingDevice>` which can be created using the :ref:`RenderingServer <class_RenderingServer>`:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Create a local rendering device.
    var rd := RenderingServer.create_local_rendering_device()

 .. code-tab:: csharp

    // Create a local rendering device.
    var rd = RenderingServer.CreateLocalRenderingDevice();

After that we can load the newly created shader file "compute_example.glsl" and create a pre-compiled version of it using this:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Load GLSL shader
    var shader_file := load("res://compute_example.glsl")
    var shader_spirv: RDShaderSPIRV = shader_file.get_spirv()
    var shader := rd.shader_create_from_spirv(shader_spirv)

 .. code-tab:: csharp

    // Load GLSL shader
    var shaderFile = GD.Load<RDShaderFile>("res://compute_example.glsl");
    var shaderBytecode = shaderFile.GetSpirv();
    var shader = rd.ShaderCreateFromSpirv(shaderBytecode);


Provide input data
------------------

As you might remember we want to pass an input array to our shader, multiply each element by 2 and get the results.

To pass values to a compute shader we need to create a buffer. We are dealing with an array of doubles, so we will use a storage buffer for this example.
A storage buffer takes an array of bytes and allows the CPU to transfer data to and from the GPU.

So let's initialize an array of doubles and create a storage buffer:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Prepare our data. We use doubles in the shader, so we need 64 bit.
    var input := PackedFloat64Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    var input_bytes := input.to_byte_array()

    # Create a storage buffer that can hold our double values.
    # Each double has 8 byte (64 bit) so 10 x 8 = 80 bytes
    var buffer := rd.storage_buffer_create(input_bytes.size(), input_bytes)

 .. code-tab:: csharp

    // Prepare our data. We use doubles in the shader, so we need 64 bit.
    var input = new double[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    var inputBytes = new byte[input.Length * sizeof(double)];
    Buffer.BlockCopy(input, 0, inputBytes, 0, inputBytes.Length);

    // Create a storage buffer that can hold our double values.
    // Each double has 8 byte (64 bit) so 10 x 8 = 80 bytes
    var buffer = rd.StorageBufferCreate((uint)inputBytes.Length, inputBytes);

With the buffer in place we need to tell the rendering device to use this buffer.
To do that we will need to create a uniform (like in normal shaders) and assign it to a uniform set which we can pass to our shader later.

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
5. Execute the logic of our shader
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

Note that we are dispatching the compute shader with 5 work groups in the x-axis, and one in the others.
Since we have 2 local invocations in the x-axis (specified in our shader) 10 compute shader invocations will be launched in total.
If you read or write to indices outside of the range of your buffer, you may access memory outside of your shaders control or parts of other variables which may cause issues on some hardware.


Execute a compute shader
------------------------

After all of this we are done, kind of.
We still need to execute our pipeline, everything we did so far was only definition not execution.

To execute our compute shader we just need to submit the pipeline to the GPU and wait for the execution to finish:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Submit to GPU and wait for sync
    rd.submit()
    rd.sync()

 .. code-tab:: csharp

    // Submit to GPU and wait for sync
    rd.Submit();
    rd.Sync();

Ideally, you would not synchronize the RenderingDevice right away as it will cause the CPU to wait for the GPU to finish working. In our example we synchronize right away because we want our data available for reading right away. In general, you will want to wait at least a few frames before synchronizing so that the GPU is able to run in parellel with the CPU.

Congratulations you created and executed a compute shader. But wait, where are the results now?

Retrieving results
------------------

You may remember from the beginning of this tutorial that compute shaders don't have inputs and outputs, they simply change memory. This means we can retrieve the data from our buffer we created at the start of this tutorial.
The shader read from our array and stored the data in the same array again so our results are already there.
Let's retrieve the data and print the results to our console.

.. tabs::
 .. code-tab:: gdscript GDScript

    # Read back the data from the buffer
    var output_bytes := rd.buffer_get_data(buffer)
    var output := output_bytes.to_float64_array()
    print("Input: ", input)
    print("Output: ", output)

 .. code-tab:: csharp

    // Read back the data from the buffers
    var outputBytes = rd.BufferGetData(outputBuffer);
    var output = new double[input.Length];
    Buffer.BlockCopy(outputBytes, 0, output, 0, outputBytes.Length);
    GD.Print("Input: ", input)
    GD.Print("Output: ", output)

Conclusion
----------

Working with compute shaders is a little cumbersome to start, but once you have the basics working in your program  you can scale up the complexity of your shader without making many changes to your script.
