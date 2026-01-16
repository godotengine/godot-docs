.. _doc_drawable_textures:

DrawableTextures
====================

DrawableTextures are a type of Texture2D with additional functions for modifying the texture via the GPU.

Basic Blit_Rect
---------------

The most basic operation on a drawable texture is blit_rect()  - 
Blitting (copying) the whole of one texture into the given rectangle on the ``DrawableTexture``. 

.. code-block:: gdscript

    texture.blit_rect(Rect2(20, 50, 60, 60), load("res://circle.svg"))
    texture.blit_rect(Rect2(20, 50, 60, 60), load("res://circle.svg"), Color.WHITE, 0)

The code above blits the circle texture into the rectangle (20, 50, 60, 60) on the ``DrawableTexture``. 
(20,50) is the top left corner of the rectangle being drawn to, and (60, 60) is its size. 
If you wanted to draw over the whole texture, simply match the Rect parameter to the ``DrawableTexture``'s size.

The next parameter in blit_rect() is an optional parameter, Modulate. 
This is a color that the output is multiplied by (in the default behavior). 
This can be used to recolor, or even mask the drawn output of blit_rect(). 
Using a modulate of Color(0, 0, 1, 0) for example, will only draw to and update the Blue values of each pixel on the DrawableTexture.

blit_rect()'s 4th parameter, Mipmap, can specify a mipmap level to draw to. 
You only need to use this if you want very fine control over each mipmap layer. 
Keep in mind, you do not need to adjust the rectangle size - it is converted to a portion of the textures whole size. 
If you just want to update all the mipmap layers, you should draw to the texture, and then call generate_mipmaps() on it

Blend Modes & TextureBlit Shaders
---------------------------------

The drawing process for blit_rect() and DrawableTextures is governed by a TextureBlit GDShader. 
Even when the user does not supply one, the engine has a default TextureBlit shader it uses.

.. code-block:: glsl

    // Default Texture Blit shader.

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

The Blend_mode defines the how the output color value 
is blended with the current color of the pixel on the ``DrawableTexture``.
While the engine defaults to Blend_Mix, these shaders also support 
blend_disabled, blend_sub, blend_add, and blend_mul.

If you just want to use a different blend_mode than the default, 
you can instantiate and pass in a new ``BlitMaterial`` in the GDScript code.

.. code-block:: gdscript

    var myMat = BlitMaterial.new()
    myMat.blend_mode = BlitMaterial.BLEND_MODE_DISABLED
    texture.blit_rect(Rect2(0, 0, 200, 200), load("res://icon.svg"), Color.WHITE, 0, myMat)

If you want more complicated behavior, then you can write your own TextureBlit Shader!
Create a new TextureBlit GDShader, write your Shader code, and load it into a material
to pass to the function. The Material is passed as a function parameter rather than bound
to the resource to make it easier to perform multiple different types of Draws to the same texture.

Blit_Rect Multi
---------------

DrawableTextures also have a Blit_Rect multi function, 
to allow for up to 4 inputs and outputs in the same step.

.. code-block:: gdscript

	texture.blit_rect_multi(Rect2(0, 0, 200, 200), [load("res://icon.svg"), load("res://circle.svg")], [otherDrawTex])

The default behavior of this is to just match each input and output in order
which can be useful for, say, drawing to an Albedo, Normal, and Depth texture simultaneously.

Of course, this behavior too can be customized via the TextureBlit shader.
In the GDShader, the extra outputs are written to via COLOR1, COLOR2, and COLOR3
And the extra inputs can be read as uniforms with hint_blit_source1, hint_blit_source2, and hint_blit_source3

.. _doc_drawable_textures_example_1:

Example 1: Simple Painting
--------------------------
One of the most intuitive uses for DrawableTextures is for, well, drawing! 
Its easier than ever to set up a canvas the user can paint. 
For this example, were going to start a new project, and create 
a new UI Scene with a Control Node at its root. 
Next, you'll want to create a TextureRect Node which is going to be our user's canvas. 
Size it appropriately for your screen, and then attach a new GDScript to it.
The start of this script should initialize the TextureRect's texture to a new DrawableTexture.

.. code-block:: gdscript

    extends TextureRect

    func _ready():
        texture = DrawableTexture2D.new()
        # Be Careful - if the dimensions of the Node != the setup size here
        # our draw call later will seem to happen at the wrong spot
        texture.setup(500, 500, DrawableTexture2D.DRAWABLE_FORMAT_RGBA8, false)

Next, we just need the TextureRect to respond to the player clicking and dragging as if they are painting! 
To do this, we can connect the _on_gui_input() Signal from the TextureRect to our script, 
and parse InputMouseButton and InputMouseMotion events

.. code-block:: gdscript

    var drawing: bool = false

    func _on_gui_input(event: InputEvent) -> void:
        if event is InputEventMouseButton:
            # Mouse click/unclick - start/stop drawing
            drawing = !drawing
        if event is InputEventMouseMotion and drawing:
            # Calculate rect to center our drawn rectangle on mouse position
            # instead of mouse at top left
            var p = event.position
            var rect: Rect2 = Rect2(p.x - 10, p.y - 10, 20, 20)
            texture.blit_rect(rect, null)

This should now draw black squares as you click and drag around the TextureRect. 
For more natural drawing, we probably want to be drawing a circle shape, and actually coloring it! 
We can adjust whats being drawn by using a Texture to copy from, and the modulate parameter. 
I downloaded a plain white circle texture, which I load as the Texture parameter in Blit_Rect, 
and use Red as my Modulate parameter.

.. code-block:: gdscript

    if event is InputEventMouseMotion and drawing:
        # Calculate rect to center our drawn rectangle on mouse position
        # instead of mouse at top left
        var p = event.position
        var rect: Rect2 = Rect2(p.x - 10, p.y - 10, 20, 20)
        texture.blit_rect(rect, load("res://circle.svg"), Color.RED)

Now the drawing looks much more natural and colorful! 
To further customize this, you could connect a ColorPickerButton Node to the script 
to store a users Color choice for the Modulate Parameter of Blit_Rect. 
You could also store a Brush Size variable, give the user a way to adjust it, 
and incorporate it into the Rectangle calculation so the user can draw bigger or smaller strokes.

.. code-block:: gdscript

    var drawing: bool = false
    var myColor: Color = Color.RED
    var mySize: float = 20.0

    func _on_gui_input(event: InputEvent) -> void:
        if event is InputEventMouseButton:
            # Mouse click/unclick - start/stop drawing
            drawing = !drawing
        if event is InputEventMouseMotion and drawing:
            # Calculate rect to center our drawn rectangle on mouse position
            # instead of mouse at top left
            var p = event.position
            var rect: Rect2 = Rect2(p.x - mySize/2, p.y - mySize/2, mySize, mySize)
            texture.blit_rect(rect, load("res://circle.svg"), myColor)

    func _on_color_picker_button_color_changed(color: Color) -> void:
        myColor = color

    func _on_h_slider_value_changed(value: float) -> void:
        mySize = value