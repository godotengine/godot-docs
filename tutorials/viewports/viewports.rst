.. _doc_viewports:

Viewports
=========

Introduction
------------

Think of a :ref:`Viewport <class_Viewport>` as a screen onto which the game is projected. In order
to see the game, we need to have a surface on which to draw it; that surface is
the Root :ref:`Viewport <class_Viewport>`.

.. image:: img/viewportnode.png


:ref:`Viewports <class_Viewport>` can also be added to the scene so that there
are multiple surfaces to draw on. When we are drawing to a :ref:`Viewport <class_Viewport>`
that is not the Root, we call it a render target. We can access the contents
of a render target by accessing its corresponding :ref:`texture <class_ViewportTexture>`.
By using a :ref:`Viewport <class_Viewport>` as a render target,
we can either render multiple scenes simultaneously or we can render to
a :ref:`texture <class_ViewportTexture>` which is applied to an object in the scene, for example a dynamic
skybox.

:ref:`Viewports <class_Viewport>` have a variety of use cases, including:

- Rendering 3D objects within a 2D game
- Rendering 2D elements in a 3D game
- Rendering dynamic textures
- Generating procedural textures at runtime
- Rendering multiple cameras in the same scene

What all these use cases have in common is that you are given the ability to
draw objects to a texture as if it were another screen and can then choose
what to do with the resulting texture.

Input
-----

:ref:`Viewports <class_Viewport>` are also responsible for delivering properly adjusted and
scaled input events to all their children nodes. Typically, input is received by the
nearest :ref:`Viewport <class_Viewport>` in the tree, but you can set :ref:`Viewports <class_Viewport>` not to receive input by checking
'Disable Input' to 'on'; this will allow the next nearest :ref:`Viewport <class_Viewport>` in the tree to capture
the input.

.. image:: img/input.png

For more information on how Godot handles input, please read the :ref:`Input Event Tutorial<doc_inputevent>`.

Listener
--------

Godot supports 3D sound (in both 2D and 3D nodes); more on this can be
found in the :ref:`Audio Streams Tutorial<doc_audio_streams>`. For this type of sound to be
audible, the :ref:`Viewport <class_Viewport>` needs to be enabled as a listener (for 2D or 3D).
If you are using a custom :ref:`Viewport <class_Viewport>` to display your :ref:`World <class_World>`, don't forget
to enable this!

Cameras (2D & 3D)
-----------------

When using a :ref:`Camera <class_Camera>` /
:ref:`Camera2D <class_Camera2D>`, cameras will always display on the
closest parent :ref:`Viewport <class_Viewport>` (going towards the root). For example, in the
following hierarchy:

.. image:: img/cameras.png

CameraA will display on the Root :ref:`Viewport <class_Viewport>` and it will draw MeshA. CameraB
will be captured by the :ref:`Viewport <class_Viewport>` Node along with MeshB. Even though MeshB is in the scene
hierarchy, it will still not be drawn to the Root :ref:`Viewport <class_Viewport>`. Similarly MeshA will not
be visible from the :ref:`Viewport <class_Viewport>` node because :ref:`Viewport <class_Viewport>` nodes only
capture nodes below them in the hierarchy.

There can only be one active camera per :ref:`Viewport <class_Viewport>`, so if there is more
than one, make sure that the desired one has the "current" property set,
or make it the current camera by calling:

::

    camera.make_current()

By default, cameras will render all objects in their world. In 3D, cameras can use their
:ref:`cull_mask <class_Camera_property_cull_mask>` property combined with the
:ref:`VisualInstance's <class_VisualInstance>` :ref:`layer <class_VisualInstance_property_layers>`
property to restrict which objects are rendered.

Scale & stretching
------------------

:ref:`Viewports <class_Viewport>` have a "size" property, which represents the size of the :ref:`Viewport <class_Viewport>`
in pixels. For :ref:`Viewports <class_Viewport>` which are children of :ref:`ViewportContainers <class_viewportcontainer>`,
these values are overridden, but for all others, this sets their resolution.

It is also possible to scale the 2D content and make the :ref:`Viewport <class_Viewport>` resolution
different from the one specified in size, by calling:

::

    viewport.set_size_override(true, Vector2(width, height)) # Custom size for 2D
    viewport.set_size_override_stretch(true) # Enable stretch for custom size.

The root :ref:`Viewport <class_Viewport>` uses this for the stretch options in the project
settings. For more information on scaling and stretching visit the :ref:`Multiple Resolutions Tutorial <doc_multiple_resolutions>`

Worlds
------

For 3D, a :ref:`Viewport <class_Viewport>` will contain a :ref:`World <class_World>`. This
is basically the universe that links physics and rendering together.
Spatial-based nodes will register using the :ref:`World <class_World>` of the closest
:ref:`Viewport <class_Viewport>`. By default, newly created :ref:`Viewports <class_Viewport>` do not contain a :ref:`World <class_World>` but
use the same as their parent :ref:`Viewport <class_Viewport>` (the root :ref:`Viewport <class_Viewport>` always contains a
:ref:`World <class_World>`, which is the one objects are rendered to by default). A :ref:`World <class_World>` can
be set in a :ref:`Viewport <class_Viewport>` using the "world" property, and that will separate
all children nodes of that :ref:`Viewport <class_Viewport>` from interacting with the parent
:ref:`Viewport's <class_Viewport>` :ref:`World <class_World>`. This is especially useful in scenarios where, for
example, you might want to show a separate character in 3D imposed over
the game (like in StarCraft).

As a helper for situations where you want to create :ref:`Viewports <class_Viewport>` that
display single objects and don't want to create a :ref:`World <class_World>`, :ref:`Viewport <class_Viewport>` has
the option to use its own :ref:`World <class_World>`. This is useful when you want to
instance 3D characters or objects in a 2D :ref:`World <class_World2D>`.

For 2D, each :ref:`Viewport <class_Viewport>` always contains its own :ref:`World2D <class_World2D>`.
This suffices in most cases, but in case sharing them may be desired, it
is possible to do so by setting the :ref:`Viewport's <class_Viewport>` :ref:`World2D <class_World2D>` manually.

For an example of how this works, see the demo projects `3D in 2D <https://github.com/godotengine/godot-demo-projects/tree/master/viewport/3d_in_2d>`_ and `2D in 3D <https://github.com/godotengine/godot-demo-projects/tree/master/viewport/2d_in_3d>`_ respectively.

Capture
-------

It is possible to query a capture of the :ref:`Viewport <class_Viewport>` contents. For the root
:ref:`Viewport <class_Viewport>`, this is effectively a screen capture. This is done with the
following code:

::

   # Retrieve the captured Image using get_data().
   var img = get_viewport().get_texture().get_data()
   # Flip on the Y axis.
   # You can also set "V Flip" to true if not on the root Viewport.
   img.flip_y()
   # Convert Image to ImageTexture.
   var tex = ImageTexture.new()
   tex.create_from_image(img)
   # Set Sprite Texture.
   $sprite.texture = tex

But if you use this in ``_ready()`` or from the first frame of the :ref:`Viewport's <class_Viewport>` initialization,
you will get an empty texture because there is nothing to get as texture. You can deal with
it using (for example):

::

   # Wait until the frame has finished before getting the texture
   yield(VisualServer, "frame_post_draw")
   # You can get the image after this.

Viewport Container
------------------

If the :ref:`Viewport <class_Viewport>` is a child of a :ref:`ViewportContainer <class_viewportcontainer>`, it will become active and display anything it has inside. The layout looks like this:

.. image:: img/container.png

The :ref:`Viewport <class_Viewport>` will cover the area of its parent :ref:`ViewportContainer <class_viewportcontainer>` completely
if :ref:`Stretch<class_viewportcontainer_property_stretch>` is set to ``true`` in :ref:`ViewportContainer <class_viewportcontainer>`.
Note: The size of the :ref:`ViewportContainer <class_viewportcontainer>` cannot be smaller than the size of the :ref:`Viewport <class_Viewport>`.

Rendering
---------

Due to the fact that the :ref:`Viewport <class_Viewport>` is an entryway into another rendering surface, it exposes a few
rendering properties that can be different from the project settings. The first is MSAA; you can
choose to use a different level of MSAA for each :ref:`Viewport <class_Viewport>`; the default behavior is DISABLED.
You can also set the :ref:`Viewport <class_Viewport>` to use HDR, HDR is very useful for when you want to store values in the texture that are outside the range 0.0 - 1.0.

If you know how the :ref:`Viewport <class_Viewport>` is going to be used, you can set its Usage to either 3D or 2D. Godot will then
restrict how the :ref:`Viewport <class_Viewport>` is drawn to in accordance with your choice; default is 3D.
The 2D usage mode is slightly faster and uses less memory compared to the 3D one. It's a good idea to set the :ref:`Viewport <class_Viewport>`'s Usage property to 2D if your viewport doesn't render anything in 3D.

.. note::

    If you need to render 3D shadows in the viewport, make sure to set the viewport's *Shadow Atlas Size* property to a value higher than 0.
    Otherwise, shadows won't be rendered. For reference, the Project Settings define it to 4096 by default.

Godot also provides a way of customizing how everything is drawn inside :ref:`Viewports <class_Viewport>` using “Debug Draw”.
Debug Draw allows you to specify one of four options for how the :ref:`Viewport <class_Viewport>` will display things drawn
inside it. Debug Draw is disabled by default.

.. image:: img/default_scene.png

*A scene drawn with Debug Draw disabled*

The other three options are Unshaded, Overdraw, and Wireframe. Unshaded draws the scene
without using lighting information so all the objects appear flatly colored the color of
their albedo.

.. image:: img/unshaded.png

*The same scene with Debug Draw set to Unshaded*

Overdraw draws the meshes semi-transparent with an additive blend so you can see how the meshes overlap.

.. image:: img/overdraw.png

*The same scene with Debug Draw set to Overdraw*

Lastly, Wireframe draws the scene using only the edges of triangles in the meshes.

.. note::

    The effects of the Wireframe mode are only visible in the editor, not while the project is running.

Render target
-------------

When rendering to a :ref:`Viewport <class_Viewport>`, whatever is inside will not be
visible in the scene editor. To display the contents, you have to draw the :ref:`Viewport's <class_Viewport>` :ref:`ViewportTexture <class_ViewportTexture>` somewhere.
This can be requested via code using (for example):

::

    # This gives us the ViewportTexture.
    var rtt = viewport.get_texture()
    sprite.texture = rtt

Or it can be assigned in the editor by selecting "New ViewportTexture"

.. image:: img/texturemenu.png

and then selecting the :ref:`Viewport <class_Viewport>` you want to use.

.. image:: img/texturepath.png

Every frame, the :ref:`Viewport <class_Viewport>`'s texture is cleared away with the default clear color (or a transparent
color if :ref:`Transparent Bg<class_Viewport_property_transparent_bg>` is set to ``true``). This can be changed by setting :ref:`Clear Mode<class_Viewport_property_render_target_clear_mode>` to Never or Next Frame.
As the name implies, Never means the texture will never be cleared, while next frame will
clear the texture on the next frame and then set itself to Never.

By default, re-rendering of the :ref:`Viewport <class_Viewport>` happens when the
:ref:`Viewport <class_Viewport>`'s :ref:`ViewportTexture <class_ViewportTexture>` has been drawn in a frame. If visible, it will be
rendered; otherwise, it will not. This behavior can be changed to manual
rendering (once), or always render, no matter if visible or not. This flexibility
allows users to render an image once and then use the texture without
incurring the cost of rendering every frame.


Make sure to check the Viewport demos! Viewport folder in the demos
archive available to download, or
https://github.com/godotengine/godot-demo-projects/tree/master/viewport
