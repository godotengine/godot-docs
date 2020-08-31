.. _doc_bullet_and_godotphysics_differences:

Bullet and GodotPhysics Differences
===================================

Godot includes two different physics engines for 3D physics, Bullet, which
is the default, and GodotPhysics. There are several important differences
in how the physics engines function. They will **not** always produce
identical or even similar results.

RigidBody3D
-----------

In Bullet physics, the center of mass for RigidBody3D nodes is the center
of the node. In GodotPhysics, the center of mass is the average of the
collision shape centers.

Linear and angular damping behave very differently in Bullet compared to
GodotPhysics. Values over 1 do not make a difference in Bullet, but do make
a difference in GodoyPhysics. Additionally, in Bullet the effect at 1 is
significantly stronger compared to GodotPhysics. Conversely, a value of -1
is significantly less strong in Bullet compared to GodotPhysics.
