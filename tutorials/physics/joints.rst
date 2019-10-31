.. _docs_joints:

Joints
======

Introduction
------------

Joints are used to bind together two physics bodies. Joints can be acted as constraints or motor of the system of physics bodies to limit or drive the translation or rotation of the system.

Degree of Freedom
-----------------

Degree of Freedom (DOF) is the number that defines the configuration of a mechanical system. It can include the translation along any of the 3 axes (XYZ) and the rotation around any of the 3 axes. For a physics body, the maximum of DOF is 6.

2D Joints
---------

2D joints connects two physics bodies together in two dimensional spaces. Godot has 3 kinds of 2D joints: Pin joints, Groove Joint and Damped Spring Joint.



Pin Joint 2D
++++++++++++

Pin Joint for 2D Rigid Bodies. It pins two bodies (rigid or static) together.

Groove Joint 2D
+++++++++++++++

Groove constraint for 2D physics. This is useful for making a body “slide” through a segment placed in another.

Damped Spring Joint 2D
++++++++++++++++++++++

Damped spring constraint for 2D physics. This resembles a spring joint that always wants to go back to a given length.

3D Joints
---------

3D joints connects two physics bodies together in three dimensional spaces. Godot has 3 kinds of 2D joints: Pin joints, Groove Joint and Damped Spring Joint.


Pin Joint
+++++++++

Pin Joint for 3D Rigid Bodies. It pins 2 bodies (rigid or static) together.

Hinge Joint
+++++++++++

A hinge between two 3D bodies.

Slider joint
++++++++++++

Piston kind of slider between two bodies in 3D.

Cone Twist Joint
++++++++++++++++

Ball socket joint with spin

Generic 6DOF Joint
++++++++++++++++++

The generic 6 degrees of freedom joint can implement a variety of joint-types by locking certain axes’ rotation or translation.
