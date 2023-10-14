.. _doc_visibility_ranges:

Visibility ranges (HLOD)
========================

Along with :ref:`doc_mesh_lod` and :ref:`doc_occlusion_culling`,
visibility ranges are another tool to improve performance in large,
complex 3D scenes.

On this page, you'll learn:

- What visibility ranges can do and which scenarios they are useful in.
- How to set up visibility ranges (manual LOD) in Godot.
- How to tune visibility ranges for best performance and quality.

.. seealso::

    If you only need meshes to become less detailed over distance but don't have
    manually authored LOD meshes, consider relying on automatic
    :ref:`doc_mesh_lod` instead.

    Note that automatic mesh LOD and visibility ranges can be used at the same
    time, even on the same mesh.

How it works
------------

Visibility ranges can be used with any node that inherits from GeometryInstance3D.
This means they can be used not only with MeshInstance3D and MultiMeshInstance3D
for artist-controlled :abbr:`HLOD (Hierarchical Level of Detail)`, but also
GPUParticles3D, CPUParticles3D, Label3D, Sprite3D, AnimatedSprite3D and CSGShape3D.

Since visibility ranges are configured on a per-node basis, this makes it possible
to use different node types as part of a :abbr:`LOD (Level of Detail)` system.
For example, you could display a MeshInstance3D representing a tree when up close,
and replace it with a Sprite3D impostor in the distance to improve performance.

The benefit of :abbr:`HLOD (Hierarchical Level of Detail)` over a traditional
:abbr:`LOD (Level of Detail)` system is its hierarchical nature. A single larger
mesh can replace several smaller meshes, so that the number of draw calls can be
reduced at a distance, but culling opportunities can be preserved when up close.
For example, you can have a group of houses that uses individual MeshInstance3D
nodes (one for each house) when up close, but turns into a single MeshInstance3D
that represents a less detailed group of houses (or use a MultiMeshInstance3D).

Lastly, visibility ranges can also be used to fade certain objects entirely when
the camera gets too close or too far. This can be used for gameplay purposes,
but also to reduce visual clutter. For example, Label3D nodes can be faded using
visibility ranges when they're too far away to be readable or relevant to the
player.

Setting up visibility range
---------------------------

This is a quick-start guide for configuring a basic LOD system. After following
this guide, this LOD system will display a SphereMesh when up close and a
BoxMesh when the camera is far away enough. A small hysteresis margin is also
configured via the **Begin Margin** and **End Margin** properties. This prevents
LODs from popping back and forth too quickly when the camera is moving at the
"edge" of the LOD transition.

The visibility range properties can be found in the **Visibility Range** section
of the GeometryInstance3D inspector after selecting the MeshInstance3D Node.

- Add a Node3D node that will be used to group the two MeshInstance3D nodes
  together.
- Add a first MeshInstance3D node as a child of the Node3D. Assign a new
  SphereMesh to its Mesh property.
- Set the first MeshInstance3D's visibility range **End** to ``10.0`` and **End
  Margin** to ``1.0``.
- Add a second MeshInstance3D node as a child of the Node3D. Assign a new
  BoxMesh to its Mesh property.
- Set the second MeshInstance3D's visibility range **Begin** to ``10.0`` and
  **Begin Margin** to ``1.0``.
- Move the camera away and back towards the object. Notice how the object will
  transition from a sphere to a box as the camera moves away.

Visibility range properties
---------------------------

In the inspector of any node that inherits from GeometryInstance3D, you can adjust
the following properties in the GeometryInstance3D's **Visibility Range** section:

- **Begin:** The instance will be hidden when the camera is closer to the
  instance's *origin* than this value (in 3D units).
- **Begin Margin:** The hysteresis or alpha fade transition distance to use for
  the close-up transition (in 3D units). The behavior of this property depends
  on **Fade Mode**.
- **End:** The instance will be hidden when the camera is further away from the
  instance's *origin* than this value (in 3D units).
- **End Margin:** The hysteresis or alpha fade transition distance to use for
  the far-away transition (in 3D units). The behavior of this property depends
  on **Fade Mode**.
- **Fade Mode:** Controls how the transition between LOD levels should be performed.
  See below for details.

.. _doc_visibility_ranges_fade_mode:

Fade mode
^^^^^^^^^

.. note::

    The fade mode chosen only has a visible impact if either
    **Visibility Range > Begin Margin** or **Visibility Range > End Margin** is
    greater than ``0.0``.

In the inspector's **Visibility Range** section, there are 3 fade modes to
choose from:

- **Disabled:** Uses hysteresis to switch between LOD levels instantly. This
  prevents situations where LOD levels are switched back and forth quickly when
  the player moves forward and then backward at the LOD transition point. The
  hystereis distance is determined by **Visibility Range > Begin Margin** and
  **Visibility Range > End Margin**. This mode provides the best performance as
  it doesn't force rendering to become transparent during the fade transition.
- **Self:** Uses alpha blending to smoothly fade between LOD levels. The node
  will fade-out itself when reaching the limits of its own visibility range. The
  fade transition distance is determined by **Visibility Range > Begin Margin**
  and **Visibility Range > End Margin**. This mode forces transparent rendering
  on the object during its fade transition, so it has a performance impact.
- **Dependencies:** Uses alpha blending to smoothly fade between LOD levels. The
  node will fade-in its dependencies when reaching the limits of its own
  visibility range. The fade transition distance is determined by **Visibility
  Range > Begin Margin** and **Visibility Range > End Margin**. This mode forces
  transparent rendering on the object during its fade transition, so it has a
  performance impact. This mode is intended for hierarchical LOD systems using
  :ref:`Visibility parent <doc_visibility_ranges_visibility_parent>`. It acts
  the same as **Self** if visibility ranges are used to perform non-hierarchical
  LOD.

.. _doc_visibility_ranges_visibility_parent:

Visibility parent
^^^^^^^^^^^^^^^^^

The **Visibility Parent** property makes it easier to set up
:abbr:`HLOD (Hierarchical Level of Detail)`. It allows automatically hiding
child nodes if its parent is visible given its current visibility range properties.

.. note::

    The target of **Visibility Parent** *must* inherit from
    :ref:`class_GeometryInstance3D`.

    Despite its name, the **Visibility Parent** property *can* point to a node
    that is not a parent of the node in the scene tree. However, it is
    impossible to point **Visibility Parent** towards a child node, as this
    creates a dependency cycle which is not supported. You will get an error
    message in the Output panel if a dependency cycle occurs.

Given the following scene tree (where all nodes inherit from GeometryInstance3D):

::

    ┖╴BatchOfHouses
        ┠╴House1
        ┠╴House2
        ┠╴House3
        ┖╴House4

In this example, *BatchOfHouses* is a large mesh designed to represent all child
nodes when viewed at a distance. *House1* to *House4* are smaller
MeshInstance3Ds representing individual houses. To configure HLOD in this
example, we only need to configure two things:

- Set **Visibility Range Begin** to a number greater than `0.0` so that
  *BatchOfHouses* only appears when far away enough from the camera. Below this
  distance, we want *House1* to *House4* to be displayed instead.
- On *House1* to *House4*, assign the **Visibility Parent** property to *BatchOfHouses*.

This makes it easier to perform further adjustments, as you don't need to adjust
the **Visibility Range Begin** of *BatchOfHouses* and **Visibility Range End**
of *House1* to *House4*.

Fade mode is automatically handled by the **Visibility Parent** property, so
that the child nodes only become hidden once the parent node is fully faded out.
This is done to minimize visible pop-in. Depending on your :abbr:`HLOD
(Hierarchical Level of Detail)` setup, you may want to try both the **Self** and
**Dependencies** :ref:`fade modes <doc_visibility_ranges_fade_mode>`.

.. note::

    Nodes hidden via the **Visible** property are essentially removed from the
    visibility dependency tree, so dependent instances will not take the hidden
    node or its ancestors into account.

    In practice, this means that if the target of the **Visibility Parent** node
    is hidden by setting its **Visible** property to ``false``, the node will
    not be hidden according to the **Visibility Range Begin** value specified in
    the visibility parent.

Configuration tips
------------------

Use simpler materials at a distance to improve performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One way to further improve performance is to use simpler materials for distant
LOD meshes. While using LOD meshes will reduce the number of vertices that need
to be rendered, the per-pixel shading load for materials remains identical.
However, per-pixel shading load is regularly a bottleneck on the GPU in complex
3D scenes. One way to reduce this shading load on the GPU is to use simpler
materials when they don't make much of a visual difference.

Performance gains when doing so should be carefully measured, as
increasing the number of *unique* materials in a scene has a performance cost on
its own. Still, using simpler materials for distant LOD meshes can still result
in a net performance gain as a result of the fewer per-pixel calculations
required.

For example, on the materials used by distant LOD meshes, you can disable
expensive material features such as:

- Normal Map (especially on mobile platforms)
- Rim
- Clearcoat
- Anisotropy
- Height
- Subsurface Scattering
- Back Lighting
- Refraction
- Proximity Fade

Use dithering for LOD transitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Godot currently only supports alpha-based fading for visibility ranges. You can
however use dithering instead by using several different materials for different
LOD levels.

There are two advantages to using dithering over alpha blending for LOD transitions:

- Higher performance, as dithering transparency is faster to render compared to
  alpha blending.
- No visual glitches due to
  :ref:`transparency sorting issues <doc_3d_rendering_limitations_transparency_sorting>`
  during LOD transitions.

The downside of dithering is that a "noisy" pattern is visible during LOD fade
transitions. This may not be as noticeable at higher viewport resolutions or
when temporal antialiasing is enabled.

Also, as distance fade in BaseMaterial3D only supports fading up close *or*
fading when far away, this setup is best used with only two LODs as part of the
setup.

- Ensure **Begin Margin** and **End Margin** is set to ``0.0`` on both
  MeshInstance3D nodes, as hysteresis or alpha fade are not desired here.
- On both MeshInstance3D nodes, *decrease* **Begin** by the desired fade transition
  distance and *increase* **End** by the same distance. This is required for the
  dithering transition to actually be visible.
- On the MeshInstance3D that is displayed up close, edit its material in the inspector.
  Set its **Distance Fade** mode to **Object Dither**. Set **Min Distance** to
  the same value as the visibility range **End**. Set **Max Distance** to the
  same value *minus* the fade transition distance.
- On the MeshInstance3D that is displayed far away, edit its material in the inspector.
  Set its **Distance Fade** mode to **Object Dither**. Set **Min Distance** to
  the same value as the visibility range **Begin**. Set **Max Distance** to the
  same value *plus* the fade transition distance.
