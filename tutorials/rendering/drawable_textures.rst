.. _doc_drawable_textures:

Using DrawableTextures
======================

DrawableTextures are a type of Texture2D with additional functions for modifying
the texture via the GPU. This can be used for procedural texturing, real-time effects,
and much more.

Basic rectangle blitting
------------------------

The most basic operation on a drawable texture is
:ref:`blit_rect() <class_DrawableTexture2D_method_blit_rect>`.
Blitting (copying) the whole of one texture into the given rectangle on the ``DrawableTexture``.

.. code-block:: gdscript

    texture.blit_rect(Rect2(20, 50, 60, 60), preload("res://circle.svg"))
    texture.blit_rect(Rect2(20, 50, 60, 60), preload("res://circle.svg"), Color.WHITE, 0)

The code above blits the circle texture into the rectangle ``(20, 50, 60, 60)``
on the ``DrawableTexture``. ``(20, 50)`` is the top left corner of the rectangle
being drawn to, and ``(60, 60)`` is its size. If you wanted to draw over the
whole texture, simply match the ``rect`` parameter to the ``DrawableTexture``'s
size.

The third parameter in ``blit_rect()`` is an optional parameter, ``modulate``.
This is a color that the output is multiplied by (in the default behavior). This
can be used to recolor, or even mask the drawn output of ``blit_rect()``. For
example, using a modulate of ``Color(0, 0, 1, 0)`` will only draw to and update
the blue values of each pixel on the ``DrawableTexture``.

``blit_rect()``'s fourth parameter, ``mipmap``, can specify a mipmap level to
draw to. You only need to use this if you want fine control over each mipmap
layer. Keep in mind, you do not need to adjust the rectangle size; it is
converted to a portion of the texture's whole size. If you just want to update
all the mipmap layers, you should draw to the texture, then call
``generate_mipmaps()`` on it.

Blend modes and texture blit shaders
------------------------------------

The drawing process for ``blit_rect()`` and DrawableTextures is governed by a
:ref:`texture blit shader <doc_texture_blit_shader>`. Even when the user does
not supply one, the engine has a default texture blit shader it uses.

.. code-block:: glsl

    // Default texture blit shader.

    shader_type texture_blit;
    render_mode blend_mix;

    uniform sampler2D source_texture0 : hint_blit_source0;
    uniform sampler2D source_texture1 : hint_blit_source1;
    uniform sampler2D source_texture2 : hint_blit_source2;
    uniform sampler2D source_texture3 : hint_blit_source3;

    void blit() {
        // Copies from each whole source texture to a rect on each output texture.
        COLOR0 = texture(source_texture0, UV) * MODULATE;
        COLOR1 = texture(source_texture1, UV) * MODULATE;
        COLOR2 = texture(source_texture2, UV) * MODULATE;
        COLOR3 = texture(source_texture3, UV) * MODULATE;
    }

The blend mode specified in ``render_mode`` defines how the output color value
is blended with the current color of the pixel on the DrawableTexture. The
engine defaults to ``blend_mix`` if no blend mode is specified in
``render_mode``. Texture blit shaders also support ``blend_add`` (additive),
``blend_sub`` (subtractive), ``blend_mul`` (multiply), and ``blend_disabled``
(alpha does not act as transparency and is written as-is).
The premultiplied alpha blend mode is *not* supported here.

It is also possible to use a different blend mode than the one specified in the shader.
To do so, you can instantiate and pass in a new :ref:`class_BlitMaterial`
in the script.

.. code-block:: gdscript

    var blit_material = BlitMaterial.new()
    blit_material.blend_mode = BlitMaterial.BLEND_MODE_DISABLED
    texture.blit_rect(Rect2(0, 0, 200, 200), load("res://icon.svg"), Color.WHITE, 0, blit_material)

If you want more complex behavior, you can write your own texture blit shader.
Create a new shader with the ``texture_blit`` shader type, write your shader
code, and load it into a material to pass to the function.

.. note::

    The material is passed as a function parameter, rather than bound to the
    resource. This makes it easier to perform multiple types of draws to the
    same texture.

Using multiple blits in a single texture
----------------------------------------

DrawableTextures also have a :ref:`blit_rect_multi() <class_DrawableTexture2D_method_blit_rect_multi>`
method, which allows for up to 4 inputs and outputs in the same step.

.. code-block:: gdscript

    texture.blit_rect_multi(
            Rect2(0, 0, 200, 200),
            [preload("res://icon.svg"), preload("res://circle.svg")],
            [other_drawable_texture]
        )

The default behavior of this is to just match each input and output in order.
For example, this can be useful for drawing to an albedo, normal, and height
texture simultaneously.

Of course, this behavior can also be customized via the texture blit shader.
In the shader, the extra outputs are written to via ``COLOR1``, ``COLOR2``,
and ``COLOR3`` (with ``COLOR0`` being the primary output). The extra inputs
can be read as uniforms with ``hint_blit_source1``, ``hint_blit_source2``,
and ``hint_blit_source3``.

.. _doc_drawable_textures_example_1:

Example 1: Simple painting
--------------------------

One of the most intuitive uses for DrawableTextures is for, well, drawing!
For this example, we're going to start a new project, and create
a new UI scene with a Control node at its root.

Next, you'll need to create a :ref:`class_TextureRect` node, which is going to
be our user's canvas. Size it appropriately for your screen, and then attach a
new script to it. The start of this script should initialize the TextureRect's
texture to a new DrawableTexture.

.. code-block:: gdscript

    extends TextureRect

    func _ready():
        texture = DrawableTexture2D.new()
        # Be careful; if the dimensions of the node are not equal to the size set here,
        # our draw call later will seem to happen at the wrong spot.
        texture.setup(500, 500, DrawableTexture2D.DRAWABLE_FORMAT_RGBA8, false)

Next, we need the TextureRect to respond to the player clicking and dragging as
if they are painting. To do this, we can override the ``_on_gui_input()`` method
from the TextureRect in our script, and parse InputMouseButton and
InputMouseMotion events:

.. code-block:: gdscript

    var drawing = false

    func _on_gui_input(event):
        if event is InputEventMouseButton:
            # Mouse click/unclick - start/stop drawing.
            drawing = not drawing
        if event is InputEventMouseMotion and drawing:
            # Calculate rect to center our drawn rectangle on mouse position
            # instead of mouse at top left.
            var rect = Rect2(event.position.x - 10, event.position.y - 10, 20, 20)
            texture.blit_rect(rect, null)

This should now draw black squares as you click and drag around the TextureRect.
For more natural drawing, we probably want to be drawing a circle shape, and
actually coloring it.

We can adjust what's being drawn by using a Texture to copy from, and the
modulate parameter. We will use this :download:`plain white circle texture <img/circle.svg>`,
which we load as the ``texture`` parameter in ``blit_rect()``,
and use a red color as the ``modulate`` parameter.

.. code-block:: gdscript

    if event is InputEventMouseMotion and drawing:
        # Calculate rect to center our drawn rectangle on mouse position
        # instead of mouse at top left.
        var rect = Rect2(event.position.x - 10, event.position.y - 10, 20, 20)
        texture.blit_rect(rect, preload("res://circle.svg"), Color.RED)

The drawing now looks much more natural and colorful. To further customize this,
you could connect a :ref:`class_ColorPickerButton` node to the script to store
the user's color choice for the ``modulate`` parameter of ``blit_rect()``. You
could also store a brush size variable, give the user a way to adjust it, and
incorporate it into the rectangle calculation so the user can draw larger or
smaller strokes.

.. code-block:: gdscript

    var drawing = false
    var my_color = Color.RED
    var my_size = 20.0

    func _on_gui_input(event):
        if event is InputEventMouseButton:
            # Mouse click/unclick - start/stop drawing.
            drawing = not drawing
        if event is InputEventMouseMotion and drawing:
            # Calculate rect to center our drawn rectangle on mouse position
            # instead of mouse at top left.
            var rect = Rect2(event.position.x - my_size / 2, event.position.y - my_size / 2, my_size, my_size)
            texture.blit_rect(rect, preload("res://circle.svg"), my_color)

    func _on_color_picker_button_color_changed(color):
        my_color = color

    func _on_h_slider_value_changed(value):
        my_size = value
