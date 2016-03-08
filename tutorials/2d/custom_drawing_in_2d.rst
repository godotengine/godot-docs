.. _doc_custom_drawing_in_2d:

Custom drawing in 2D
====================

Why?
----

Godot has nodes to draw sprites, polygons, particles, and all sort of
stuff. For most cases this is enough, but not always. If something
desired is not supported, and before crying in fear, angst and range
because a node to draw that-specific-something does not exist.. it would
be good to know that it is possible to easily make any 2D node (be it
:ref:`Control <class_Control>` or :ref:`Node2D <class_Node2D>`
based) draw custom commands. It is *really* easy to do it too.

But...
------

Custom drawing manually in a node is *really* useful. Here are some
examples why:

-  Drawing shapes or logic that is not handled by nodes (example: making
   a node that draws a circle, an image with trails, a special kind of
   animated polygon, etc).
-  Visualizations that are not that compatible with nodes: (example: a
   tetris board). The tetris example uses a custom draw function to draw
   the blocks.
-  Managing drawing logic of a large amount of simple objects (in the
   hundreds of thousands). Using a thousand nodes is probably not nearly
   as efficient as drawing, but a thousand of draw calls are cheap.
   Check the "Shower of Bullets" demo as example.
-  Making a custom UI control. There are plenty of controls available,
   but it's easy to run into the need to make a new, custom one.

OK, how?
--------

Add a script to any :ref:`CanvasItem <class_CanvasItem>`
derived node, like :ref:`Control <class_Control>` or
:ref:`Node2D <class_Node2D>`. Override the _draw() function.

::

    extends Node2D

    func _draw():
        #your draw commands here
        pass

Draw commands are described in the :ref:`CanvasItem <class_CanvasItem>`
class reference. There are plenty of them.

Updating
--------

The _draw() function is only called once, and then the draw commands
are cached and remembered, so further calls are unnecessary.

If re-drawing is required because a state or something else changed,
simply call :ref:`CanvasItem.update() <class_CanvasItem_update>`
in that same node and a new _draw() call will happen.

Here is a little more complex example. A texture variable that will be
redrawn if modified:

::

    extends Node2D

    var texture setget _set_texture

    func _set_texture(value):
        #if the texture variable is modified externally,
        #this callback is called.
        texture=value #texture was changed
        update() #update the node

    func _draw():
        draw_texture(texture,Vector2())

In some cases, it may be desired to draw every frame. For this, just
call update() from the _process() callback, like this:

::

    extends Node2D

    func _draw():
        #your draw commands here
        pass

    func _process(delta):
        update()

    func _ready():
        set_process(true)

OK! This is basically it! Enjoy drawing your own nodes!

Tools
-----

Drawing your own nodes might also be desired while running them in the
editor, to use as preview or visualization of some feature or
behavior.

Remember to just use the "tool" keyword at the top of the script
(check the :ref:`doc_gdscript` reference if you forgot what this does).
