.. _doc_viewports:

Using Viewports
===============

Introduction
------------

Think of a :ref:`Viewport <class_Viewport>` as a screen onto which the game is projected. In order
to see the game, we need to have a surface on which to draw it. That surface is
the Root Viewport.

.. image:: img/subviewportnode.webp

:ref:`SubViewports <class_SubViewport>` are a kind of Viewport that can be added to the scene so that there
are multiple surfaces to draw on. When we are drawing to a SubViewport, we call it a render target. We can access the contents
of a render target by accessing its corresponding :ref:`texture <class_Viewport_method_get_texture>`.
By using a SubViewport as render target, we can either render multiple scenes simultaneously or we can render to
a :ref:`ViewportTexture <class_ViewportTexture>` which is applied to an object in the scene, for example a dynamic
skybox.

:ref:`SubViewports <class_SubViewport>` have a variety of use cases, including:

- Rendering 3D objects within a 2D game
- Rendering 2D elements in a 3D game
- Rendering dynamic textures
- Generating procedural textures at runtime
- Rendering multiple cameras in the same scene

What all these use cases have in common is that you are given the ability to
draw objects to a texture as if it were another screen and can then choose
what to do with the resulting texture.

Another kind of Viewports in Godot are :ref:`Windows <class_Window>`. They allow their content to be projected onto a window. While the Root Viewport is a Window, they are less
flexible. If you want to use the texture of a Viewport, you'll be working with :ref:`SubViewports <class_SubViewport>` most of the time.

Input
-----

:ref:`Viewports <class_Viewport>` are also responsible for delivering properly adjusted and
scaled input events to their children nodes. By default :ref:`SubViewports <class_SubViewport>` don't
automatically receive input, unless they receive it from their direct
:ref:`SubViewportContainer <class_SubViewportContainer>` parent node. In this case, input can be
disabled with the :ref:`Disable Input <class_Viewport_property_gui_disable_input>` property.

.. image:: img/input.webp

For more information on how Godot handles input, please read the :ref:`Input Event Tutorial <doc_inputevent>`.

Listener
--------

Godot supports 3D sound (in both 2D and 3D nodes). More on this can be
found in the :ref:`Audio Streams Tutorial <doc_audio_streams>`. For this type of sound to be
audible, the :ref:`Viewport <class_Viewport>` needs to be enabled as a listener (for 2D or 3D).
If you are using a :ref:`SubViewport <class_SubViewport>` to display your :ref:`World3D <class_World3D>` or
:ref:`World2D <class_World2D>`, don't forget to enable this!

Cameras (2D & 3D)
-----------------

When using a :ref:`Camera3D <class_Camera3D>` or
:ref:`Camera2D <class_Camera2D>`, it will always display on the
closest parent :ref:`Viewport <class_Viewport>` (going towards the root). For example, in the
following hierarchy:

.. image:: img/cameras.webp

``CameraA`` will display on the Root :ref:`Viewport <class_Viewport>` and it will draw ``MeshA``. ``CameraB``
will be captured by the :ref:`SubViewport <class_SubViewport>` along with ``MeshB``. Even though ``MeshB`` is in the scene
hierarchy, it will still not be drawn to the Root Viewport. Similarly, ``MeshA`` will not
be visible from the SubViewport because SubViewports only
capture nodes below them in the hierarchy.

There can only be one active camera per :ref:`Viewport <class_Viewport>`, so if there is more
than one, make sure that the desired one has the :ref:`current <class_Camera3D_property_current>` property set,
or make it the current camera by calling:

::

    camera.make_current()

By default, cameras will render all objects in their world. In 3D, cameras can use their
:ref:`cull_mask <class_Camera3D_property_cull_mask>` property combined with the
:ref:`VisualInstance3D's <class_VisualInstance3D>` :ref:`layer <class_VisualInstance3D_property_layers>`
property to restrict which objects are rendered.

Scale & stretching
------------------

:ref:`SubViewports <class_SubViewport>` have a :ref:`size<class_SubViewport_property_size>` property, which represents the size of the SubViewport
in pixels. For SubViewports which are children of :ref:`SubViewportContainers <class_SubViewportContainer>`,
these values are overridden, but for all others, this sets their resolution.

It is also possible to scale the 2D content and make the :ref:`SubViewport <class_SubViewport>` resolution
different from the one specified in size, by calling:

::

    sub_viewport.set_size_2d_override(Vector2i(width, height)) # Custom size for 2D.
    sub_viewport.set_size_2d_override_stretch(true) # Enable stretch for custom size.

For information on scaling and stretching with the Root Viewport visit the :ref:`Multiple Resolutions Tutorial <doc_multiple_resolutions>`

Worlds
------

For 3D, a :ref:`Viewport <class_Viewport>` will contain a :ref:`World3D <class_World3D>`. This
is basically the universe that links physics and rendering together.
Node3D-based nodes will register using the World3D of the closest Viewport.
By default, newly created Viewports do not contain a World3D but
use the same as their parent Viewport. The Root Viewport always contains a
World3D, which is the one objects are rendered to by default.

A :ref:`World3D <class_World3D>` can
be set in a :ref:`Viewport <class_Viewport>` using the :ref:`World 3D<class_Viewport_property_world_3d>` property, that will separate
all children nodes of this :ref:`Viewport <class_Viewport>` and will prevent them from interacting with the parent
Viewport's World3D. This is especially useful in scenarios where, for
example, you might want to show a separate character in 3D imposed over
the game (like in StarCraft).

As a helper for situations where you want to create :ref:`Viewports <class_Viewport>` that
display single objects and don't want to create a :ref:`World3D <class_World3D>`, Viewport has
the option to use its :ref:`Own World3D <class_Viewport_property_own_world_3d>`. This is useful when you want to
instance 3D characters or objects in :ref:`World2D <class_World2D>`.

For 2D, each :ref:`Viewport <class_Viewport>` always contains its own :ref:`World2D <class_World2D>`.
This suffices in most cases, but in case sharing them may be desired, it
is possible to do so by setting :ref:`world_2d<class_Viewport_property_world_2d>` on the Viewport through code.

For an example of how this works, see the demo projects `3D in 2D <https://github.com/godotengine/godot-demo-projects/tree/master/viewport/3d_in_2d>`_ and `2D in 3D <https://github.com/godotengine/godot-demo-projects/tree/master/viewport/2d_in_3d>`_ respectively.

Capture
-------

It is possible to query a capture of the :ref:`Viewport <class_Viewport>` contents. For the Root
Viewport, this is effectively a screen capture. This is done with the
following code:

::

   # Retrieve the captured Image using get_image().
   var img = get_viewport().get_texture().get_image()
   # Convert Image to ImageTexture.
   var tex = ImageTexture.create_from_image(img)
   # Set sprite texture.
   sprite.texture = tex

But if you use this in ``_ready()`` or from the first frame of the :ref:`Viewport's <class_Viewport>` initialization,
you will get an empty texture because there is nothing to get as texture. You can deal with
it using (for example):

::

   # Wait until the frame has finished before getting the texture.
   await RenderingServer.frame_post_draw
   # You can get the image after this.

Viewport Container
------------------

If the :ref:`SubViewport <class_SubViewport>` is a child of a :ref:`SubViewportContainer <class_SubViewportContainer>`, it will become active and display anything it has inside. The layout looks like this:

.. image:: img/container.webp

The :ref:`SubViewport <class_SubViewport>` will cover the area of its parent :ref:`SubViewportContainer <class_SubViewportContainer>` completely
if :ref:`Stretch<class_SubViewportContainer_property_stretch>` is set to ``true`` in the SubViewportContainer.

.. note::

    The size of the :ref:`SubViewportContainer <class_SubViewportContainer>` cannot be smaller than the size of the :ref:`SubViewport <class_SubViewport>`.

Rendering
---------

Due to the fact that the :ref:`Viewport <class_Viewport>` is an entryway into another rendering surface, it exposes a few
rendering properties that can be different from the project settings. You can
choose to use a different level of :ref:`MSAA <class_Viewport_property_msaa_2d>` for each Viewport. The default behavior is ``Disabled``.

If you know that the :ref:`Viewport <class_Viewport>` is only going to be used for 2D, you can :ref:`Disable 3D<class_Viewport_property_disable_3d>`. Godot will then
restrict how the Viewport is drawn.
Disabling 3D is slightly faster and uses less memory compared to enabled 3D. It's a good idea to disable 3D if your viewport doesn't render anything in 3D.

.. note::

    If you need to render 3D shadows in the viewport, make sure to set the viewport's :ref:`positional_shadow_atlas_size<class_Viewport_property_positional_shadow_atlas_size>` property to a value higher than ``0``.
    Otherwise, shadows won't be rendered. By default, the equivalent project setting is set to ``4096`` on desktop platforms and ``2048`` on mobile platforms.

Godot also provides a way of customizing how everything is drawn inside :ref:`Viewports <class_Viewport>` using :ref:`Debug Draw<class_Viewport_property_debug_draw>`.
Debug Draw allows you to specify a mode which determines how the Viewport will display things drawn
inside it. Debug Draw is ``Disabled`` by default. Some other options are ``Unshaded``, ``Overdraw``, and ``Wireframe``. For a full list, refer to the :ref:`Viewport Documentation<class_Viewport_property_debug_draw>`.

-  **Debug Draw = Disabled** (default): The scene is drawn normally.

  .. image:: img/default_scene.webp

-  **Debug Draw = Unshaded**: Unshaded draws the scene without using lighting information so all the objects appear flatly colored in their albedo color.

  .. image:: img/unshaded.webp

-  **Debug Draw = Overdraw**: Overdraw draws the meshes semi-transparent with an additive blend so you can see how the meshes overlap.

  .. image:: img/overdraw.webp

-  **Debug Draw = Wireframe**: Wireframe draws the scene using only the edges of triangles in the meshes.

  .. image:: img/wireframe.webp

.. note::

    Debug Draw modes are currently **not** supported when using the
    Compatibility rendering method. They will appear as regular draw modes.

Render target
-------------

When rendering to a :ref:`SubViewport <class_SubViewport>`, whatever is inside will not be
visible in the scene editor. To display the contents, you have to draw the SubViewport's :ref:`ViewportTexture <class_ViewportTexture>` somewhere.
This can be requested via code using (for example):

::

    # This gives us the ViewportTexture.
    var tex = viewport.get_texture()
    sprite.texture = tex

Or it can be assigned in the editor by selecting "New ViewportTexture"

.. image:: img/texturemenu.webp

and then selecting the :ref:`Viewport <class_Viewport>` you want to use.

.. image:: img/texturepath.webp

Every frame, the :ref:`Viewport's <class_Viewport>` texture is cleared away with the default clear color (or a transparent
color if :ref:`Transparent BG<class_Viewport_property_transparent_bg>` is set to ``true``). This can be changed by setting :ref:`Clear Mode<class_SubViewport_property_render_target_clear_mode>` to ``Never`` or ``Next Frame``.
As the name implies, Never means the texture will never be cleared, while next frame will
clear the texture on the next frame and then set itself to Never.

By default, re-rendering of the :ref:`SubViewport <class_SubViewport>` happens when
its :ref:`ViewportTexture <class_ViewportTexture>` has been drawn in a frame. If visible, it will be
rendered, otherwise, it will not. This behavior can be changed by setting :ref:`Update Mode<class_SubViewport_property_render_target_update_mode>` to ``Never``, ``Once``, ``Always``, or ``When Parent Visible``.
Never and Always will never or always re-render respectively. Once will re-render the next frame and change to Never afterwards. This can be used to manually update the Viewport.
This flexibility allows users to render an image once and then use the texture without incurring the cost of rendering every frame.

.. note::

    Make sure to check the Viewport demos. They are available in the 
    viewport folder of the demos archive, or at
    https://github.com/godotengine/godot-demo-projects/tree/master/viewport.
