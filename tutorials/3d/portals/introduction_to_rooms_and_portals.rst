.. _doc_portals_introduction:

Introduction to Rooms and Portals
=================================

The rooms and portals system is an optional component of Godot that allows you to partition your 3D game levels into a series of :ref:`Room<class_Room>` s (*aka cells*), and :ref:`Portal<class_Portal>` s. Portals are openings between the rooms that the :ref:`Camera<class_Camera>` (and lights) can see through.
 
This allows several features:

- **Portal occlusion culling**, which can increase performance by reducing the number of objects that are drawn, both to cameras and to shadow maps.

- **Gameplay callbacks**, which allow turning off activity outside the gameplay area - AI, physics, animation, processing etc.

The trade off for these features is that we have to manually partition our level into rooms, and add portals between them.

.. note:: Godot portals should not be confused with those in the `game of the same name <https://en.wikipedia.org/wiki/Portal_(video_game)>`__. They do not warp space, they simply represent a window that the camera (or lights) can see through.

Minimizing manual labour
^^^^^^^^^^^^^^^^^^^^^^^^

Although the effort involved in creating rooms for a large level may seem daunting, there are several factors which can make this much easier:

- If you are "kit bashing" and reusing rooms or areas already, this is an ideal way to save effort. Your level tiles can be rooms, with portals already placed.
- If you are creating procedural levels, you can create rooms and portals as part of the procedural generation algorithm you're writing.
- Finally, if you are manually creating freeform levels, bear in mind there are absolutely no rules as to how far you go with portalling. Even if you separate a large game level into only two rooms, with a single portal between them, this can still result in relatively large performance gains.

The performance benefits (especially in terms of occlusion) follow an L-shaped curve, with the lion's share occurring when you have created just a few rooms. So do not be afraid to be lazy - **\*work smart\***.

In general, when it comes to medium and large-sized levels, it is better to do a little portalling than none at all.

Some caveats
^^^^^^^^^^^^

.. note:: The portal system should be considered an **advanced feature** of Godot. You should not attempt to use rooms and portals until you are familiar with the Godot editor, and have successfully made at least a couple of test games.

It gives you great power as a game designer, but the trade off is that it requires a very technical approach to level design. It is aimed at producing professional-grade results, and assumes the user is prepared to put in the work for this. It is not intended to be used for all 3D games. Not all games will significantly benefit from portals, and it may require more time than a short game jam allows.
