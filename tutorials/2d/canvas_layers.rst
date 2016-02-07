Canvas Layers
=============

Viewport and Canvas Items
-------------------------

Regular 2D nodes, such as
`Node2D <https://github.com/okamstudio/godot/wiki/class_node2d>`__ or
`Control <https://github.com/okamstudio/godot/wiki/class_control>`__
both inherit from
`CanvasItem <https://github.com/okamstudio/godot/wiki/class_canvasitem>`__,
which is the base for all 2D nodes. CanvasItems can be arranged in trees
and they will inherit their transform. This means that, moving the
parent, the children will be moved too.

| These nodes are placed as direct or indirect children to a
  `Viewport <https://github.com/okamstudio/godot/wiki/class_viewport>`__,
  and will be displayed through it.
| Viewport has a property "canvas\_transform"
  (`Viewport.set\_canvas\_transform() <https://github.com/okamstudio/godot/wiki/class_viewport#set_canvas_transform)>`__,
  which allows to transform all the CanvasItem hierarchy by a custom
  `Matrix32 <https://github.com/okamstudio/godot/wiki/class_matrix32>`__
  transform. Nodes such as
  `Camera2D <https://github.com/okamstudio/godot/wiki/class_camera2d>`__,
  work by changing that transform.

Changing the canvas transform is useful because it is a lot more
efficient than moving the root canvas item (and hence the whole scene).
Canvas transform is a simple matrix that offsets the whole 2D drawing,
so it's the most efficient way to do scrolling.

Not Enough..
------------

But this is not enough. There are often situations where the game or
application may not want *everything* transformed by the canvas
transform. Examples of this are:

-  **Parallax Backgrounds**: Backgrounds that move slower than the rest
   of the stage.
-  **HUD**: Head's up display, or user interface. If the world moves,
   the life counter, points, etc must stay static.
-  **Transitions**: Effects used for transitions (fades, blends) may
   also want it to remain at a fixed location.

How can these problems be solved in a single scene tree?

CanvasLayers
------------

The answer is
`CanvasLayer <https://github.com/okamstudio/godot/wiki/class_canvaslayer>`__,
which is a node that adds a separate 2D rendering layer for all it's
children and grand-children. Viewport children will draw by default at
layer "0", while a CanvasLayer will draw at any numeric layer. Layers
with a greater number will be drawn above those with a smaller number.
CanvasLayers also have their own transform, and do not depend of the
transform of other layers. This allows the UI to be fixed in-place,
while the word moves.

An example of this is creating a parallax background. This can be done
with a CanvasLayer at layer "-1". The screen with the points, life
counter and pause button can also be created at layer "1".

Here's a diagram of how it looks:

.. image:: /img/canvaslayers.png

CanvasLayers are independent of tree order, and they only depend on
their layer number, so they can be instantiated when needed.

Performance
-----------

Even though there shouldn't be any performance limitation, it is not
advised to use excessive amount of layers to arrange drawing order of
nodes. The most optimal way will always be arranging them by tree order.
In the future, nodes will also have a priority or sub-layer index which
should aid for this.



