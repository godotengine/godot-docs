.. _doc_overview_of_debugging_tools:

Overview of debugging tools
===========================

Introduction
------------

When developing your game, you want to test your game and debug when problems occurr. Godot provides several debugging options and
tools which aid your debugging process. There are the debug dropdown options, Script editor debug options, debug project settings,
and the debugger.

Debug dropdown options
----------------------

There are a few options that you can enable when running your game in the editor which can help you in debugging your game.
These options are located in ``DEBUG`` in the main menus.

.. image:: img/overview_debug.png

Here are the descriptions of the options:

Deploy with Remote Debug
++++++++++++++++++++++++

When exporting and deploying, the resulting executable will attempt to connect to the IP of your computer, in order to be debugged.

Small Deploy with Network FS
++++++++++++++++++++++++++++

Export or deploy will produce minimal executable. The filesystem will be provided from the project by the editor over the network.
On Android, deploy will use the USB cable for faster performance. This option speeds up testing for games with a large footprint.

Visible Collision Shapes
++++++++++++++++++++++++

Collision shapes and raycast nodes(for 2D and 3D) will be visible on the running game.

Visible Navigation
++++++++++++++++++

Navigation meshes and polygons will be visible on the running game.

Sync Scene Changes
++++++++++++++++++

Any changes made to the scene in the editor will be replicated in the running game.
When used remotely on a device, this is more efficient with network filesystem.

Sync Script Changes
+++++++++++++++++++

Any script that is saved will be reloaded on the running game.
When used remotely on a device, this is more efficient with network filesystem.

Script Editor Debug Tools and Options
-------------------------------------

The script editor has its own set of debug tools for use with breakpoints, and two
options. The breakpoint tools can also be found in the debugger tab of the debugger.

..image:: img/overview_script_editor.png

The ``Break`` Button causes a break in the script like a breakpoint would. ``Continue``
makes the game continue after pausing at a breakpoint. ``Step Over`` goes to the next
line of code, and ``Step Into`` goes into a function if it can, if it can't it does the
same thing as ``Step Over``

The ``Keep Debugger Open`` Option keeps the debugger open after a scene has been closed.
And the ``Debug with External Editor`` option lets you debug your game with an external
editor.

Debug project settings
----------------------

In the project settings there is a debug category with three sub categories which
control different things.

Settings
++++++++

These are some general settings such as printing the current FPS to the Output panel, the
maximum ammount of functions when profiling and others

GDScript
++++++++

These settings allow you to turn specific GDScript warnings, such as an unused variable, on
or off. You can also turn off warnings completely.

Shapes
++++++

Shapes is where you can adjust the color of shapes that only appear for debugging pruposes,
such as collisions and navigation.

Debugging tools
---------------

The ``Debugger`` can be found in Godot's bottom panel. Click on it and the panel expands
to show all the debugging tools.

.. image:: img/overview_debugger.png

There are multiple parts of the debugger, each is for a specific task.

Debugger
++++++++

The debugger tab is for working with breakpoints in the script. When a script reaches a breakpoint
this panel gives you information on it.

The buttons in the top right can be used to turn off breakpoints completely, copy an error, Step
Into goes into a function if possible and if it can't it acts like step over, step over goes to
the next line of code, you can cause a break in the game topause it like a breakpoint would, and
you can stop the break and continue the game.

Errors
++++++

This is where errors and warning messages are printed while running the game.

Profiler
++++++++

Profiles the performance of any function call in the running game.

Network Profiler
++++++++++++++++

The Network Profiler contains a list of all the nodes that communicate over the multiplayer API
and, for each one, some counters on the amount of incoming and outgoing network interactions.
It also features a bandwidth meter that displays the total bandwidth usage at any given moment 

Monitors
++++++++

The monitors are graphs of several aspects of the game while its running such as FPS, memory usage,
how many nodes are in a scene and more. All monitors keep track of stats automatically, so even if one
monitor isn't open while the game is running, you can open it later and see how the values changed.

Video Mem
+++++++++

Video Lists the video memory usage of the running game and which resource is using it.

Misc
++++

Miscellaneous options for debug.

Remote in Scene dock
--------------------

When running a game in the editor two options appear at the top of the ``Scene`` dock,
``Remote`` and ``Local``. While using ``Remote`` you can inspect or change the nodes' parameters
in the running game.

.. image:: img/overview_remote.png

.. note:: Some editor settings related to debugging can be found inside the ``Editor Settings``, under Network>Debug and Debugger sections.
