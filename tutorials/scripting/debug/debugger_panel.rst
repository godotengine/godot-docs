.. _doc_debugger_panel:

Debugger panel
==============

Many of Godot's debugging tools, including the debugger, can be found in the
debugger panel at the bottom of the screen. Click on **Debugger** to open it.

.. image:: img/overview_debugger.png

The debugger panel is split into several tabs, each focusing on a specific task.

Debugger
++++++++

The Debugger tab opens automatically when the GDScript compiler reaches
a breakpoint in your code.

It gives you a `stack trace <https://en.wikipedia.org/wiki/Stack_trace>`__,
information about the state of the object, and buttons to control
the program's execution.

You can use the buttons in the top-right corner to:

- Skip all breakpoints. That way, you can save breakpoints for future
  debugging sessions.
- Copy the current error message.
- **Step Into** the code. This button takes you to the next line of code,
  and if it's a function, it steps line-by-line through the function.
- **Step Over** the code. This button goes to the next line of code,
  but it doesn't step line-by-line through functions.
- **Break**. This button pauses the game's execution.
- **Continue**. This button resumes the game after a breakpoint or pause.

.. warning::

    Breakpoints won't break on code if it's
    :ref:`running in a thread <doc_using_multiple_threads>`.
    This is a current limitation of the GDScript debugger.

Errors
++++++

This is where error and warning messages are printed while running the game.

You can disable specific warnings in **Project Settings > Debug > GDScript**.

Profiler
++++++++

The profiler is used to see what code is running while your project is in use,
and how that effects performance. A detailed explanation of how to use it can
be found :ref:`here <doc_the_profiler>`.

Network Profiler
++++++++++++++++

The Network Profiler contains a list of all the nodes that communicate over the
multiplayer API and, for each one, some counters on the amount of incoming and
outgoing network interactions. It also features a bandwidth meter that displays
the total bandwidth usage at any given moment.

Monitors
++++++++

The monitors are graphs of several aspects of the game while its running such as
FPS, memory usage, how many nodes are in a scene and more. All monitors keep
track of stats automatically, so even if one monitor isn't open while the game
is running, you can open it later and see how the values changed.

Video RAM
+++++++++

The **Video RAM** tab shows the video RAM usage of the game while it is running.
It provides a list of every resource using video RAM by resource path, the type
of resource it is, what format it is in, and how much Video RAM that resource is
using. There is also a total video RAM usage number at the top right of the panel.

.. image:: img/video_ram.png

Misc
++++

The **Misc** tab contains tools to identify the control nodes you are clicking
at runtime:

- **Clicked Control** tells you where the clicked node is in the scene tree.
- **Clicked Control Type** tells you the type of the node you clicked is.
