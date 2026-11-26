.. _doc_2d_gizmo_plugins:

2D gizmo plugins
================

Introduction
------------

If you've created custom CanvasItem nodes for your project, you might have noticed
that working with them in the editor can be a bit awkward. They appear as single
points in the viewport, making them hard to select. You can't see their boundaries,
and there's no quick way to adjust their properties visually. This is where 2D
gizmo plugins come in.

With 2D gizmo plugins, we can make our custom nodes work just like built-in ones
in the editor. We can add:

- **Outline rect control** - A boundary box with scaling handles
- **Collision shapes** - Make your nodes easier to click and select
- **Handles** - Draggable controls for properties like radius or width
- **Subgizmos** - Selectable and transformable sub-parts like polygon vertices or curve points

In this tutorial, we'll walk through each of these features step by step, starting
with the basics and working up to more advanced techniques.

.. note:: This tutorial assumes you already know how to make generic plugins. If
          you are new to making plugins, please check out the :ref:`doc_making_plugins` page.

Setting up the gizmo plugin
----------------------------
To create a 2D gizmo plugin, we'll need two things: a gizmo plugin class that
extends :ref:`EditorCanvasItemGizmoPlugin <class_EditorCanvasItemGizmoPlugin>`,
and our main editor plugin to register it.

Let's start with the gizmo plugin class. Create a new script:

::

    # circle_gizmo_plugin.gd
    @tool
    extends EditorCanvasItemGizmoPlugin


    func _has_gizmo(for_canvas_item: CanvasItem) -> bool:
        return for_canvas_item is Circle


    func _get_gizmo_name() -> String:
        return "Circle"
Let's look at these two methods:

- ``_has_gizmo()`` tells the editor which nodes this plugin supports. Return ``true``
  for nodes we want to add gizmos to. In this example, we're only supporting a custom
  ``Circle`` node.

- ``_get_gizmo_name()`` returns the name shown in the gizmo menu in the 2D editor.
  This lets users show and hide gizmos created by our plugin.

Now we need to register this gizmo plugin in our main editor plugin:

::

    # my_editor_plugin.gd
    @tool
    extends EditorPlugin


    const CircleGizmoPlugin = preload("res://addons/my_addon/circle_gizmo_plugin.gd")

    var gizmo_plugin = CircleGizmoPlugin.new()


    func _enter_tree():
        add_node_2d_gizmo_plugin(gizmo_plugin)


    func _exit_tree():
        remove_node_2d_gizmo_plugin(gizmo_plugin)

That's it for the basic setup! The gizmo plugin will now be active, though it doesn't
do anything yet. Let's add some features.

Outline rect control
--------------------

The outline rect control gives our node a visible boundary box and automatic scaling
handles, just like built-in nodes such as Sprite2D or ColorRect. This is useful when
our node has a definable size or bounds.

To enable outline rect control, implement three methods:

::

    func _edit_use_rect(_gizmo: EditorCanvasItemGizmo) -> bool:
        return true


    func _edit_get_rect(gizmo: EditorCanvasItemGizmo) -> Rect2:
        var circle: Circle = gizmo.get_canvas_item()
        var radius: float = circle.radius
        return Rect2(Vector2(-radius, -radius), Vector2(radius * 2, radius * 2))


    func _edit_set_rect(gizmo: EditorCanvasItemGizmo, boundary: Rect2) -> void:
        var old_boundary: Rect2 = _edit_get_rect(gizmo)
        var new_transform: Transform2D = boundary_change_to_transform(old_boundary, boundary)

        var circle: Circle = gizmo.get_canvas_item()
        circle.transform *= new_transform

Here's what each method does:

- ``_edit_use_rect()`` tells the editor whether to show the outline rect. Return ``true``
  to enable it, ``false`` to disable it.

- ``_edit_get_rect()`` returns the current boundary rectangle of your node. For our circle,
  we calculate a square that contains the entire circle based on its radius.

- ``_edit_set_rect()`` is called when the user modifies the boundary (by dragging the scaling
  handles). We need to apply these changes to our node.

The ``boundary_change_to_transform()`` helper is particularly useful. It calculates the
transform that represents the change from the old boundary to the new one. We can then
multiply this with our node's existing transform to get the new position and scale. The
editor automatically handles undo/redo for these changes.

.. note:: Not every node needs outline rect control. For example, if our node has a
          fixed structure that shouldn't be scaled (like our Flower example later),
          we can return ``false`` from ``_edit_use_rect()`` and skip the other methods.

Making your node pickable
-------------------------

By default, the Godot editor doesn't know what shape our custom node has, so it
treats it as a single point. This makes it very difficult to click and select in
the viewport. We can fix this by adding collision shapes to our gizmo.

Collision shapes are added in the ``_redraw()`` method, which is called whenever
the gizmo needs to update its visual representation:

::

    func _redraw(gizmo: EditorCanvasItemGizmo) -> void:
        var circle: Circle = gizmo.get_canvas_item()

        var circle_polygon: PackedVector2Array = []
        for i: int in 16:
            var angle: float = i * TAU / 16.0
            circle_polygon.append(Vector2(cos(angle), sin(angle)) * circle.radius)
        gizmo.add_collision_polygon(circle_polygon)

You have two options for collision shapes:

- ``add_collision_rect()`` - Use this for nodes with rectangular bounds. It's simple
  but might not be accurate for other shapes.

- ``add_collision_polygon()`` - Use this for more accurate picking. Provide an array
  of points that outline your node's shape.

For our circle, we use a 16-segment polygon approximation. This gives much better
picking accuracy than a rectangle would - users won't accidentally select the circle
by clicking in the corners where there's no circle.

.. tip:: We can add multiple collision shapes if our node has multiple distinct parts.
         Each call to ``add_collision_rect()`` or ``add_collision_polygon()`` adds
         another pickable area.

Adding custom handles
---------------------

Handles are draggable controls that let users modify our node's properties visually.
They're perfect for properties like radius, width, height, or control points. When we
drag a handle, we're directly manipulating a value on our node.

Adding handles
~~~~~~~~~~~~~~

First, add the handles in your ``_redraw()`` method:

::

    func _redraw(gizmo: EditorCanvasItemGizmo) -> void:
        var circle: Circle = gizmo.get_canvas_item()

        # ... collision shapes code ...

        # Add a handle for the radius
        var handle_pos: Vector2 = Vector2(sin(PI/4.0), cos(PI/4.0)) * circle.radius
        gizmo.add_handles([handle_pos])

The ``add_handles()`` method takes an array of positions (in the node's local coordinate
space). We position our radius handle at a 45-degree angle so it doesn't overlap with
the scaling handles from the outline rect.

Implementing handle callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To make handles functional, we need to implement four callback methods:

::

    func _get_handle_name(_gizmo: EditorCanvasItemGizmo, handle_id: int, _secondary: bool) -> String:
        if handle_id == 0:
            return "Radius"
        return "Unknown handle"


    func _get_handle_value(gizmo: EditorCanvasItemGizmo, handle_id: int, _secondary: bool) -> Variant:
        var circle: Circle = gizmo.get_canvas_item()
        if handle_id == 0:
            return circle.radius
        return null


    func _set_handle(gizmo: EditorCanvasItemGizmo, handle_id: int, _secondary: bool, position: Vector2) -> void:
        if handle_id != 0:
            return

        var circle: Circle = gizmo.get_canvas_item()
        var new_radius: float = position.length()
        circle.radius = new_radius


    func _commit_handle(gizmo: EditorCanvasItemGizmo, handle_id: int, _secondary: bool, restore: Variant, cancel: bool) -> void:
        if handle_id != 0:
            return

        var circle: Circle = gizmo.get_canvas_item()

        if cancel:
            circle.radius = restore
            return

        var undo_redo: EditorUndoRedoManager = EditorInterface.get_editor_undo_redo()
        undo_redo.create_action("Set radius")
        undo_redo.add_do_property(circle, "radius", circle.radius)
        undo_redo.add_undo_property(circle, "radius", restore)
        undo_redo.commit_action()

Each callback has a specific role:

- ``_get_handle_name()`` returns the name shown to the user when they hover over or drag
  the handle. The ``handle_id`` is the position in the array we passed to ``add_handles()``.

- ``_get_handle_value()`` returns the current value associated with the handle. This is
  used for showing the value to the user and for undo/redo. For our radius handle, we
  return the circle's radius property.

- ``_set_handle()`` is called repeatedly while the user drags the handle. The ``position``
  parameter is in the node's local coordinate space. We should apply this position to
  our node's properties. For the radius, we calculate the distance from the center.

- ``_commit_handle()`` is called when the user releases the handle or cancels the drag
  (by pressing Escape). If ``cancel`` is true, restore the original value from the
  ``restore`` parameter. Otherwise, create an undo/redo action so the user can undo
  the change.

.. important:: Unlike the outline rect control, the editor cannot automatically handle
               undo/redo for custom handles. We must implement this ourselves in
               ``_commit_handle()``.

Working with subgizmos
----------------------

Subgizmos are more advanced than handles. While handles can only be dragged to change
a value, subgizmos can be selected, moved, rotated, and scaled using the standard editor
transform tools. They're perfect for representing sub-parts of your node, like:

- Vertices of a polygon
- Points along a path or curve
- Sub-objects that are part of your node (like the petals of a flower)

Put simply: use handles when we just need to drag something to change a value, and use
subgizmos when we want to select and transform actual parts of our node.

Making subgizmos pickable
~~~~~~~~~~~~~~~~~~~~~~~~~~

To make subgizmos pickable, implement the intersection methods:

::

    func _subgizmos_intersect_point(gizmo: EditorCanvasItemGizmo, point: Vector2, _distance: float) -> int:
        var flower: Flower = gizmo.get_canvas_item()

        for i: int in flower._petals.size():
            var petal: Transform2D = flower._petals[i]
            var collision_polygon: PackedVector2Array = _calculate_collision_circle(flower.radius, petal)
            if Geometry2D.is_point_in_polygon(point, collision_polygon):
                return i

        return -1

The ``_subgizmos_intersect_point()`` method is called when the user clicks in the editor.
Return the ID of the subgizmo at that point, or ``-1`` if there isn't one. The ``point``
is in the node's local coordinate space.

For rectangle selection (when the user shift-drags to select multiple items), implement:

::

    func _subgizmos_intersect_rect(gizmo: EditorCanvasItemGizmo, rect: Rect2) -> PackedInt32Array:
        var flower: Flower = gizmo.get_canvas_item()
        var result: PackedInt32Array = []

        var global_transform: Transform2D = flower.global_transform

        # Create a polygon from the selection rectangle
        var rect_shape: PackedVector2Array = []
        rect_shape.append(rect.position)
        rect_shape.append(rect.position + Vector2(0, rect.size.y))
        rect_shape.append(rect.position + rect.size)
        rect_shape.append(rect.position + Vector2(rect.size.x, 0))

        for i in flower._petals.size():
            var petal_global: Transform2D = global_transform * flower._petals[i]
            var collision_polygon: PackedVector2Array = _calculate_collision_circle(flower.radius, petal_global)

            var overlap: Array[PackedVector2Array] = Geometry2D.intersect_polygons(rect_shape, collision_polygon)
            if not overlap.is_empty():
                result.append(i)

        return result

.. important:: The ``rect`` parameter in ``_subgizmos_intersect_rect()`` is in canvas
               (global) coordinates, not local coordinates! This is because it represents
               a screen-space selection rectangle. We'll need to use our node's
               ``global_transform`` to convert our subgizmo shapes to global space
               for comparison.

Managing subgizmo transforms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Subgizmos are all about transforms. We need to implement three methods to manage them:

::

    func _get_subgizmo_transform(gizmo: EditorCanvasItemGizmo, subgizmo_id: int) -> Transform2D:
        var flower: Flower = gizmo.get_canvas_item()
        return flower._petals[subgizmo_id]


    func _set_subgizmo_transform(gizmo: EditorCanvasItemGizmo, subgizmo_id: int, transform: Transform2D) -> void:
        var flower: Flower = gizmo.get_canvas_item()
        flower._petals[subgizmo_id] = transform
        flower._repaint()


    func _commit_subgizmos(gizmo: EditorCanvasItemGizmo, ids: PackedInt32Array, restores: Array[Transform2D], cancel: bool) -> void:
        var flower: Flower = gizmo.get_canvas_item()

        if cancel:
            for i: int in ids.size():
                var subgizmo_id: int = ids[i]
                var old_transform: Transform2D = restores[i]
                flower._petals[subgizmo_id] = old_transform
            flower._repaint()
            return

        # Build the undo array
        var undo_petals: Array[Transform2D] = flower._petals.duplicate()
        for i: int in ids.size():
            var subgizmo_id: int = ids[i]
            var old_transform: Transform2D = restores[i]
            undo_petals[subgizmo_id] = old_transform

        var undo_redo: EditorUndoRedoManager = EditorInterface.get_editor_undo_redo()
        undo_redo.create_action("Set petals")
        undo_redo.add_do_property(flower, "_petals", flower._petals)
        undo_redo.add_do_method(flower, "_repaint")
        undo_redo.add_undo_property(flower, "_petals", undo_petals)
        undo_redo.add_undo_method(flower, "_repaint")
        undo_redo.commit_action()

Each method has a specific purpose:

- ``_get_subgizmo_transform()`` returns the current transform of a subgizmo. This is
  similar to ``_get_handle_value()`` for handles.

- ``_set_subgizmo_transform()`` is called repeatedly while the user transforms the
  subgizmo. Apply the new transform to our data structure.

- ``_commit_subgizmos()`` is called when the user finishes or cancels the transformation.
  Note that it receives arrays of IDs and restores, because multiple subgizmos can be
  transformed at once. Like with handles, we need to implement undo/redo ourselves.

Visual feedback for selected subgizmos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's helpful to show users which subgizmos are currently selected. We can do this
in our ``_redraw()`` method:

::

    func _redraw(gizmo: EditorCanvasItemGizmo) -> void:
        var flower: Flower = gizmo.get_canvas_item()

        # ... add collision shapes ...

        for i: int in flower._petals.size():
            var petal: Transform2D = flower._petals[i]

            # Highlight selected petals
            if gizmo.is_subgizmo_selected(i):
                var polygon: PackedVector2Array = _calculate_collision_circle(flower.radius, petal)
                gizmo.add_polygon(polygon, Color(0.39, 0.58, 0.93, 0.8))

The ``is_subgizmo_selected()`` method tells us whether a specific subgizmo is currently
selected. We can then use ``add_polygon()`` to draw a colored overlay on it.

Visual customization
--------------------

.. note:: **TODO:** This section will be expanded with examples once the API is finalized.

We can customize the appearance of our gizmos beyond the default styles:

- **Shape overlays** - Draw colored polygons and lines for visual feedback (like the
  petal selection highlight shown above)
- **Handle icons** - Customize the appearance of our handles

These features allow us to create gizmos that match our node's visual style and
provide clear feedback to users.

Custom pivot points
-------------------

Pivot points define the center of rotation and scaling for a node. By default, CanvasItem
nodes use their position as the pivot point, but sometimes we want to allow users to
customize this - for example, a circle that can rotate around an off-center point, or a
sprite where the user can adjust the anchor point.

The 2D gizmo plugin API supports custom pivots through five methods that work together
to save, restore, and modify the pivot position.

Enabling pivot support
~~~~~~~~~~~~~~~~~~~~~~~

First, tell the editor that our node supports a custom pivot:

::

    func _has_pivot(_gizmo: EditorCanvasItemGizmo) -> bool:
        return true

This will make the editor show a pivot control (a small cross icon) that users can drag
to change the pivot position.

Getting and setting the pivot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We need to tell the editor where the pivot is currently located and how to update it:

::

    func _get_pivot(_gizmo: EditorCanvasItemGizmo) -> Vector2:
        # Since our circle implements the pivot by offsetting the drawing, the
        # pivot point is always at the node position, so we return Vector2.ZERO here.
        return Vector2.ZERO


    func _set_pivot(gizmo: EditorCanvasItemGizmo, pivot: Vector2) -> void:
        var circle: Circle = gizmo.get_canvas_item()
        # The new pivot we get here is relative to the node position. Since
        # we offset the circle drawing by the pivot, our pivot position is always
        # at the node position. This means that the pivot we get is relative to
        # our old pivot (which visually was at the node position). Therefore we add
        # it to the circle's pivot rather than overwriting it.
        circle.pivot = circle.pivot + pivot

Let's understand what's happening here:

- ``_get_pivot()`` returns where the pivot should be **drawn** in the editor, relative to
  the node's position. How you implement this depends on your pivot strategy. In our circle
  example, the pivot is implemented by offsetting the drawing, so the visual pivot is
  always at the node's position. Because of this, we return Vector2.ZERO (the node position
  in local coordinates).

- ``_set_pivot()`` receives a new pivot position relative to the node's current position.
  The implementation depends on how your node handles pivots internally. In our case, since
  we offset the drawing, we add the change to our existing pivot value. Note that the editor
  automatically handles undo/redo for pivot changes, so we don't need to manually create
  undo/redo actions here.

.. important:: The pivot value passed to ``_set_pivot()`` is a local position relative to the
               node's position (e.g. in the same local space as the value returned by ``_get_pivot()``).
               How you apply this depends on your node's internal pivot implementation.

Saving and restoring state
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When users drag the pivot, the editor constantly takes snapshots and restores them before
applying new pivot values. We need to implement state management:

::

    func _edit_get_state(gizmo: EditorCanvasItemGizmo) -> Dictionary:
        var circle: Circle = gizmo.get_canvas_item()
        # The base state (transform, etc.) is automatically saved from the
        # underlying node, so we only need to add what is custom to our node
        return {"pivot": circle.pivot}


    func _edit_set_state(gizmo: EditorCanvasItemGizmo, state: Dictionary) -> void:
        var circle: Circle = gizmo.get_canvas_item()
        # The underlying CanvasItem will restore the transform automatically,
        # so we only need to restore our custom pivot property
        circle.pivot = state.pivot

The state methods serve two purposes:

- They provide undo/redo support for pivot changes automatically
- They allow the editor to restore the previous state before applying incremental
  pivot changes during dragging

.. note:: The base transform is saved and restored automatically by the editor. We only
          need to save custom properties that affect our node's appearance or behavior.

Updating other methods for pivot support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When we add pivot support, we need to update other gizmo methods to account for the
pivot offset:

**Boundary rectangle**::

    func _edit_get_rect(gizmo: EditorCanvasItemGizmo) -> Rect2:
        var circle: Circle = gizmo.get_canvas_item()
        var radius: float = circle.radius
        # Offset the rectangle by the pivot
        return Rect2(Vector2(-radius, -radius) - circle.pivot, Vector2(radius * 2, radius * 2))

**Collision shapes**::

    func _redraw(gizmo: EditorCanvasItemGizmo) -> void:
        var circle: Circle = gizmo.get_canvas_item()

        var circle_polygon: PackedVector2Array = []
        for i: int in 16:
            var angle: float = i * TAU / 16.0
            circle_polygon.append(
                (Vector2(cos(angle), sin(angle)) * circle.radius)
                - circle.pivot  # Offset by pivot
            )
        gizmo.add_collision_polygon(circle_polygon)

**Handle positions**::

    func _redraw(gizmo: EditorCanvasItemGizmo) -> void:
        var circle: Circle = gizmo.get_canvas_item()
        # ... collision shapes ...

        # Offset handle by pivot
        var handle_pos: Vector2 = \
            Vector2(sin(PI/4.0), cos(PI/4.0)) * circle.radius \
            - circle.pivot
        gizmo.add_handles([handle_pos])

**Handle dragging**::

    func _set_handle(gizmo: EditorCanvasItemGizmo, handle_id: int, _secondary: bool, position: Vector2) -> void:
        if handle_id != 0:
            return

        var circle: Circle = gizmo.get_canvas_item()
        # The center is offset by the pivot
        var center := -circle.pivot
        var new_radius: float = (position - center).length()
        circle.radius = new_radius

.. tip:: Any visual element or calculation that uses the node's center needs to account
         for the pivot offset. Think of the pivot as shifting where the "center" of your
         node is located.

Where to go from here
---------------------

We've now learned the fundamentals of creating 2D gizmo plugins! We can:

- Add outline rect control for scalable nodes
- Make nodes easy to select with collision shapes
- Create draggable handles for visual property editing
- Build advanced subgizmo systems for sub-parts of our nodes
- Add custom pivot points for flexible rotation and scaling

For complete working examples, see the
`2D Gizmos demo project <https://github.com/godotengine/godot-demo-projects/tree/master/2d/gizmos>`__.
The demo project files include:

- ``circle_gizmo_plugin.gd`` - Demonstrates outline rect, collision shapes, handles, and custom pivots
- ``flower_gizmo_plugin.gd`` - Demonstrates subgizmos with full picking and transform support

Both files include plenty of inline comments explaining how everything works.

Tips and best practices
------------------------

As you build your own gizmo plugins, keep these tips in mind:

**Coordinate spaces**
  Pay attention to coordinate spaces. Handle positions, pivots, and ``_subgizmos_intersect_point()``
  use local coordinates, but ``_subgizmos_intersect_rect()`` uses canvas (global)
  coordinates.

**Undo/redo**
  Always implement proper undo/redo for handles and subgizmos. The editor can't do
  this automatically because it doesn't know what your handles and subgizmos represent.

**When to use what**
  - Use outline rect for nodes that should be scalable
  - Skip outline rect for fixed-structure nodes (return ``false`` from ``_edit_use_rect()``)
  - Use polygon collision for accurate picking on non-rectangular shapes
  - Use handles for simple draggable values (radius, width, angles)
  - Use subgizmos for selectable/transformable sub-parts (vertices, points, sub-objects)
  - Use custom pivots when users need to control the center of rotation/scaling

**Performance**
  Keep your ``_redraw()`` method efficient. It's called frequently, so avoid heavy
  calculations. Cache collision shapes if they don't change often.

Feel free to experiment with these features and see what works best for your custom
nodes.
