.. _doc_beziers_and_curves:

Beziers, Curves and Paths
==========================

Introduction
~~~~~~~~~~~~

Bezier curves are a mathematical approximation to natural shapes. Their goal is to represent a curve with
as little information as possible, and with a high level of flexibility.

Unlike other more abstract mathematical concepts, Bezier curves were created for industrial design and are
widely popular in the graphics software industry.

The way they work is very simple, but to understand it, let's start from the most minimal example.


Quadratic Bezier
----------------

Take three points (the minimum required):

.. image:: img/bezier_quadratic_points.png

To draw the curve between them, just interpolate the two segments that form between the three points, individually (using values 0 to 1). This will result in two points.

.. tabs::
 .. code-tab:: gdscript GDScript

    func _quadratic_bezier(p0 : Vector2,p1 : Vector2,p2 : Vector2 ,t : float):
        var q0 = p0.linear_interpolate(p1,t)
        var q1 = p1.linear_interpolate(p2,t)

This will reduce the points from 3 to 2. Do the same process with *q0* and *q1* to obtain a single point *r*.

.. tabs::
 .. code-tab:: gdscript GDScript

        var r = q0.linear_interpolate(q1,t)
        return r

Finally, this point fill follow the curve when t goes from 0 to 1. This type of curve is called *Quadratic Bezier*.

.. image:: img/bezier_quadratic_points2.gif

*(Image credit: Wikipedia)*

Cubic Bezier
----------------

Let's add one more point and make it four. 

.. image:: img/bezier_cubic_points.png

Then let's modify the function to take four points as an input, *p0, p1, p2* and *p3*:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _cubic_bezier(p0 : Vector2,p1 : Vector2,p2 : Vector2,p3 : Vector2 ,t : float):

Interpolate then into three points:

.. tabs::
 .. code-tab:: gdscript GDScript

        var q0 = p0.linear_interpolate(p1,t)
        var q1 = p1.linear_interpolate(p2,t)
        var q2 = p2.linear_interpolate(p3,t)

From there to two points:

.. tabs::
 .. code-tab:: gdscript GDScript

        var r0 = q0.linear_interpolate(q1,t)
        var r1 = q1.linear_interpolate(q2,t)

And to one:

.. tabs::
 .. code-tab:: gdscript GDScript

        var s = r0.linear_interpolate(r1,t)
        return s

The result will be a smooth curve interpolating between all four points:

.. image:: img/bezier_quadratic_points2.gif

*(Image credit: Wikipedia)*

.. note:: For 3D, it's exactly the same, just change Vector2 into Vector3.

Control point form
-------------------

Now, let's take these points and change the way we understand them. Instead of having p0, p1, p2 and p3, we will store them as:

* **POINT0** = **P0**: Is the first point, the source
* **CONTROL0** = **P1** - **P0**: Is a relative vector for the first control point
* **CONTROL1** = **P3** - **P2**: Is a relative vector for the second control point
* **POINT1** = **P3**: Is the second point, the destination

This way, we have two points and two control points (which are relative vectors to the respective points). If visualized, they will look a lot more familiar:

.. image:: img/bezier_cubic_handles.png

This is actually how graphics software presents Bezier curves to the users, and how Godot supports them.

Curve, Curve2D, Path and Path2D
-------------------------------

There are two objects that contain curves: :ref:`Curve <class_Curve>` and :ref:`Curve <class_Curve2D>` (for 3D and 2D respectively).

They can contain several points, allowing for longer paths. It is also possible to set them to nodes: :ref:`Path <class_Path>` and :ref:`Path2D <class_Path2D>` (also for 3D and 2D respectively):

.. image:: img/bezier_path_2d.png

Using them, however, may not be completely obvious, so following is a description of the most common use cases for Bezier curves.

Evaluating
-----------

Just evaluating them may be an option, but in most cases it's not very useful. The big drawback with Bezier curves is that if you traverse them at constant speed, from *t=0* to *t=1*, the actual interpolation will *not* move at constant speed. The speed is also an interpolation between the distances between points p0, p1, p2 and p3 and there is not a mathematically simple way to traverse the curve at constant speed.

Let's do a simple example with the following pseudocode:

.. tabs::
 .. code-tab:: gdscript GDScript

    var t = 0.0
    _process(delta):
        t+=delta
        position = _cubic_bezier(p0,p1,p2,p3,t)


.. image:: img/bezier_interpolation_speed.gif

As you can see, the speed (in pixels per second) of the circle varies, even though *t* is increased at constant speed. This makes beziers difficult to use for anything practical out of the box.

Drawing
-------

Drawing beziers (or objects based on the curve) is a very common use case, but it's also not easy. For pretty much any case, Bezier curves need to be converted to some sort of segments. This is normally difficult, however, without creating a very high amount of them.

The reason is that some sections of a curve (specifically, corners) may requiere considerably points, while other sections may not:

.. image:: img/bezier_point_amount.png

Additionally, if both control points were 0,0 (remember they are relative vectors), the Bezier curve would just be a straight line (so drawing a high amount of points would be wasteful).

Before drawing Bezier curves, *tesselation* is required. This is often done with a recursive or divide and conquer function that splits the curve until the curvature amount becomes less than a certain threshold.

The *Curve* classes provide this via the :ref:`Curve.tesselate()<class_Curve_method_tesselete>` function (which receives optional *stages* of recursion and angle *tolerance* arguments). This way, drawing something based on a curve is easier.

Traversal
---------

The last common use case for the curves is to traverse them. Because of what was mentioned before regarding constant speed, this is also difficult. 

To make this easier, the curves need to be *baked* into equidistant points. This way, they can be approximated with regular  interpolation (which can be improved further with a cubic option). To do this, just use the :ref:`Curve.interpolate_baked()<class_Curve_method_interpolate_baked>` method together with :ref:`Curve.get_baked_length()<class_Curve_method_get_baked_length>`. The first call to either of them will bake the curve internally.

Traversal at constant speed, then, can be done with the following pseudo-code:

.. tabs::
 .. code-tab:: gdscript GDScript

    var t = 0.0
    _process(delta):
        t+=delta	
        position = curve.interpolate_baked( t * curve.get_baked_length(), true)

And the output will, then, move at constant speed:

.. image:: img/bezier_interpolation_baked.gif


