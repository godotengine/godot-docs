.. _doc_design_interfaces_with_the_control_nodes:

Design interfaces with the Control nodes
========================================

Computer displays, mobile phones, and TV screens come in all shapes and
sizes. To ship a game, you'll need to support different screen ratios
and resolutions. It can be hard to build responsive interfaces that
adapt to all platforms. Thankfully, Godot comes with robust tools to
design and manage a responsive User Interface.

.. figure:: img/godot_editor_ui.png

   Godot's editor is made with the engine's UI framework

This guide will get you started with UI design. You will learn:

-  The five most useful control nodes to build your games' interface
-  How to work with the anchor of UI elements
-  How to efficiently place and arrange your user interface using
   containers
-  The five most common containers (you can learn more about containers in
   the :ref:`GUI Containers <doc_gui_containers>` documentation page).

To learn how to control the interface and connect it to other scripts,
read :ref:`Build your first game UI in Godot <doc_ui_game_user_interface>`.

To design your UI, you'll use the Control nodes. These are the nodes with green icons in the
editor. There are dozens of them, for creating anything from life bars to
complex applications. Godot's editor itself is built using Control nodes.

Control nodes have unique properties that allow them to work well with one another.
Other visual nodes, like Node2D and Sprite don't have these capabilities. So to
make your life easier use Control nodes wherever possible when building your UIs.

All control nodes share the same main properties:

1. Anchor
2. Bounding rectangle
3. Focus and focus neighbor
4. Size flags
5. Margin
6. The optional UI theme

Once you understand the basics of the Control node, it will take you less time to learn all the
nodes that derive from it.


The 5 most common UI elements
-----------------------------

Godot ships with dozens of Control nodes. A lot of them are here to help
you build editor plugins and applications.

For most games, you'll only need five types of UI elements, and a few
Containers. These five Control nodes are:

1. Label: for displaying text
2. TextureRect: used mostly for backgrounds, or everything that should
   be a static image
3. TextureProgress: for lifebars, loading bars, horizontal, vertical or
   radial
4. NinePatchRect: for scalable panels
5. TextureButton: to create buttons

.. figure:: img/five_most_common_nodes.png

   The 5 most common Control nodes for UI design

TextureRect
~~~~~~~~~~~

**TextureRect** displays a texture or image inside a UI.
It seems similar to the Sprite node, but it offers multiple scaling modes.
Set the Stretch Mode property to change its behavior:

- ``Scale On Expand (compat)`` scales the texture to fit the node's bounding rectangle,
  only if ``expand`` property is ``true``; otherwise, it behaves like ``Keep`` mode.
  Default mode for backwards compatibility.
- ``Scale`` scales the texture to fit the node's bounding rectangle.
- ``Tile`` makes the texture repeat, but it won't scale.
-  ``Keep`` and ``Keep Centered`` force the texture to remain at its
   original size, in the top left corner or the center of the frame
   respectively.
- ``Keep Aspect`` and ``Keep Aspect Centered`` scales the texture but force it to remain
  its original aspect ratio, in the top left corner or the center of the frame respectively.
- ``Keep Aspect Covered`` works just like ``Keep Aspect Centered`` but the shorter side
  fits the bounding rectangle and the other one clips to the node's limits.

As with Sprite nodes, you can modulate the TextureRect's color. Click
the ``Modulate`` property and use the color picker.

.. figure:: img/five_common_nodes_textureframe.png

   TextureRect modulated with a red color

TextureButton
~~~~~~~~~~~~~

**TextureButton** is like TextureRect, except it has 5 texture slots:
one for each of the button's states. Most of the time, you'll use the
Normal, Pressed, and Hover textures. Focused is useful if your interface
listens to the keyboard's input. The sixth image slot, the Click Mask,
lets you define the clickable area using a 1-bit, pure black and white
image.

In the Base Button section, you'll find a few checkboxes that change how
the button behaves. When ``Toggle Mode`` is on, the button will toggle
between active and normal states when you press it. ``Disabled`` makes it
disabled by default, in which case it will use the ``Disabled`` texture.
TextureButton shares a few properties with the texture frame: it has a
``modulate`` property, to change its color, and ``Resize`` and ``Stretch`` modes to
change its scale behavior.

.. figure:: img/five_common_nodes_texturebutton.png

   TextureButton and its 5 texture slots

TextureProgress
~~~~~~~~~~~~~~~

**TextureProgress** layers up to 3 sprites to create a progress bar. The
Under and Over textures sandwich the Progress one, which displays the
bar's value.

The ``Mode`` property controls the direction in which the bar grows:
horizontally, vertically, or radially. If you set it to radial, the
``Initial Angle`` and ``Fill Degrees`` properties let you limit the range of the
gauge.

To animate the bar, you'll want to look at the Range section. Set the
``Min`` and ``Max`` properties to define the range of the gauge. For instance,
to represent a character's life, you'll want to set ``Min`` to ``0,`` and ``Max`` to
the character's maximum life. Change the ``Value`` property to update the
bar. If you leave the ``Min`` and ``Max`` values to the default of ``0`` and ``100,``
and set the ``Value`` property to ``40``, 40% of the ``Progress`` texture will show
up, and 60% of it will stay hidden.

.. figure:: img/five_common_nodes_textureprogress.png

   TextureProgress bar, two thirds filled

Label
~~~~~

**Label** prints text to the screen. You'll find all its properties in
the Label section, in the Inspector. Write the text in the ``Text``
property, and check Autowrap if you want it to respect the textbox's
size. If Autowrap is off, you won't be able to scale the node. You can
align the text horizontally and vertically with Align and Valign,
respectively.

.. figure:: img/five_common_nodes_label.png

   Picture of a Label

NinePatchRect
~~~~~~~~~~~~~

**NinePatchRect** takes a texture split in 3 rows and 3 columns. The
center and the sides tile when you scale the texture, but it never
scales the corners. It is useful to build panels, dialog boxes
and scalable backgrounds for your UI.

.. figure:: img/five_common_nodes_ninepatchrect.png

   NinePatchRect scaled with the min\_size property

There are two workflows to build responsive UIs
-----------------------------------------------

There are two workflows to build scalable and flexible interfaces in Godot:

1. You have many container nodes at your disposal that scale and place UI elements for you. They take control over their children.
2. On the other side, you have the layout menu. It helps you to anchor, place and resize a UI element within its parent.

The two approaches are not always compatible. Because a container controls its children, you cannot use the layout menu on them. Each container has a specific effect, so you may need to nest several of them to get a working interface. With the layout approach you work from the bottom up, on the children. As you don't insert extra containers in the scene it can make for cleaner hierarchies, but it's harder to arrange items in a row, column, grid, etc.

As you create UIs for your games and tools, you'll develop a sense for what fits best in each situation.


Place UI elements precisely with anchors
----------------------------------------

Control nodes have a position and size, but they also have anchors and
margins. Anchors define the origin, or the reference point, for the
Left, Top, Right and Bottom edges of the node. Change any of the 4
anchors to change the reference point of the margins.

.. figure:: img/anchor_property.png

   The anchor property

How to change the anchor
~~~~~~~~~~~~~~~~~~~~~~~~

Like any properties, you can edit the 4 anchor points in the Inspector,
but this is not the most convenient way. When you select a control node,
the layout menu appears above the viewport, in the toolbar. It gives you
a list of icons to set all 4 anchors with a single click, instead of
using the inspector's 4 properties. The layout menu will only show up
when you select a control node.

.. figure:: img/layout_menu.png

   The layout menu in the viewport

Anchors are relative to the parent container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each anchor is a value between 0 and 1. For the left and top anchors, a
value of 0 means that without any margin, the node's edges will align
with the left and top edges of its parent. For the right and bottom
edges, a value of 1 means they'll align with the parent container's
right and bottom edges. On the other hand, margins represent a distance
to the anchor position in pixels, while anchors are relative to the
parent container's size.

.. figure:: ./img/ui_anchor_and_margins.png

   Margins are relative to the anchor position, which is relative to the
   anchors. In practice, you'll often let the container update margins
   for you

Margins change with the anchor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Margins update automatically when you move or resize a control node.
They represent the distance from the control node's edges to its anchor,
which is relative to the parent control node or container. That's why
your control nodes should always be inside a container, as we'll see in
a moment. If there's no parent, the margins will be relative to the
node's own bounding Rectangle, set in the Rect section, in the
inspector.

.. figure:: img/control_node_margin.png

   Margins on a CenterContainer set to the "Full Rect" anchor

Try to change the anchors or nest your Control nodes inside Containers:
the margins will update. You'll rarely need to edit the margins
manually. Always try to find a container to help you first; Godot comes
with nodes to solve all the common cases for you. Need to add space
between a lifebar and the border of the screen? Use the MarginContainer.
Want to build a vertical menu? Use the VBoxContainer. More on these
below.

Use size tags to change how UI elements fill the available space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every control node has Size Flags. They tell containers how the UI
elements should scale. If you add the "Fill" flag to the Horizontal or
Vertical property, the node's bounding box will take all the space it
can, but it'll respect its siblings and retain its size. If there are 3
TextureRect nodes in an HBoxContainer, with the "Fill" flags on both
axes, they'll each take up to a third of the available space, but no
more. The container will take over the node and resize it automatically.

.. figure:: img/textureframe_in_box_container_fill.png

   3 UI elements in an HBoxContainer, they align horizontally

The "Expand" flag lets the UI element take all the space it can, and
push against its siblings. Its bounding rectangle will grow against the
edges of its parent, or until it's blocked by another UI node.

.. figure:: img/textureframe_in_box_container_expand.png

   The same example as above, but the center node has the "Expand" size
   flag

You'll need some practice to understand the size tags, as their effect
can change quite a bit depending on how you set up your interface.

Arrange control nodes automatically with containers
---------------------------------------------------

Containers automatically arrange all children Control nodes including
other containers in rows, columns, and more. Use them to add padding
around your interface or center nodes in their bounding rectangles. All
built-in containers update in the editor, so you can see the effect
instantly.

Containers have a few special properties to control how they arrange UI
elements. To change them, navigate down to the Custom Constants section
in the Inspector.

The 5 most useful containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you build tools, you might need all of the containers. But for most
games, a handful will be enough:

-  MarginContainer, to add margins around part of the UI
-  CenterContainer, to center its children in its bounding box
-  VboxContainer and HboxContainer, to arrange UI elements in rows or
   columns
-  GridContainer, to arrange Controls nodes in a grid-like pattern

CenterContainer centers all its children inside of its bounding
rectangle. It's one you typically use for title screens, if you want the
options to stay in the center of the viewport. As it centers everything,
you'll often want a single container nested inside it. If you use
textures and buttons instead, they'll stack up.

.. figure:: img/five_containers_centercontainer.png

   CenterContainer in action. The life bar centers inside its parent
   container.

The MarginContainer adds a margin on any side of the child nodes. Add a
MarginContainer that encompasses the entire viewport to add a separation
between the edge of the window and the UI. You can set a margin on the
top, left, right, or bottom side of the container. No need to tick the
checkbox: click the corresponding value box and type any number. It will
activate automatically.

.. figure:: img/five_containers_margincontainer.png

   The MarginContainer adds a 40px margin around the Game User Interface

There are two BoxContainers: VBoxContainer and HBoxContainer. You cannot
add the BoxContainer node itself, as it is a helper class, but you can
use vertical and horizontal box containers. They arrange nodes either in
rows or columns. Use them to line up items in a shop, or to build
complex grids with rows and columns of different sizes, as you can nest
them to your heart's content.

.. figure:: img/five_containers_boxcontainer.png

   The HBoxContainer horizontally aligns UI elements

VBoxContainer automatically arranges its children into a column. It puts
them one after the other. If you use the separation parameter, it will
leave a gap between its children. HBoxContainer arranges UI elements in
a row. It's similar to the VBoxContainer, with an extra ``add_spacer``
method to add a spacer control node before its first child or after its
last child, from a script.

The GridContainer lets you arrange UI elements in a grid-like pattern.
You can only control the number of columns it has, and it will set the
number of rows by itself, based on its children's count. If you have
nine children and three columns, you will have 9÷3 = 3 rows. Add three
more children and you'll have four rows. In other words, it will create
new rows as you add more textures and buttons. Like the box containers,
it has two properties to set the vertical and horizontal separation
between the rows and columns respectively.

.. figure:: img/five_containers_gridcontainer.png

   A GridContainer with 2 columns. It sizes each column automatically.

Godot's UI system is complex, and has a lot more to offer. To learn how
to design more advanced interfaces, head to the :ref:`GUI section <toc-learn-features-gui>` of the docs.
