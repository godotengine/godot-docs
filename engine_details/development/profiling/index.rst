.. _doc_using_cpp_profilers:

Using C++ profilers
===================

To optimize Godot's performance, you need to know what to optimize first.
To this end, profilers are useful tools.

.. note::

    There is a :ref:`built-in GDScript profiler <doc_the_profiler>` in the editor,
    but using a C++ profiler may be useful in cases where the GDScript profiler
    is not accurate enough or is missing information due to bugs in the profiler.

There are two main types of profilers: sampling profilers and tracing profilers.

Sampling profilers periodically interrupt the running program and take a "sample",
which records which functions are running. Using this information, the profiler
estimates which functions the program spent the most time in.

Tracing profilers work by recording application-specific events (such as the
start and end of a single frame), producing a log called a "trace". The profiler
can use the trace to produce a graph showing an accurate high-level timeline of
what happened. However, any code that is not explicitly instrumented will not
appear in a tracing profiler's timeline!

Godot supports both sampling profilers and tracing profilers, and already
includes the logging code for common Godot events for use with a tracing profiler!

Different problems may be easier to debug with one kind of profiler over the other,
but it's difficult to provide a set of rules for which to use. Give both a try,
and see what you can learn from them!

.. _doc_sampling_profilers:

Sampling profilers
------------------

We recommend the following sampling profilers:

- :ref:`VerySleepy <doc_profiler_very_sleepy>` (Windows only)
- :ref:`Hotspot <doc_profiler_hotspot>` (Linux only)
- :ref:`Instruments <doc_profiler_instruments>` (Apple only)

These profilers may not be the most powerful or flexible options, but their
standalone operation and limited feature set tends to make them easier to use.

Setting up Godot
~~~~~~~~~~~~~~~~

To get useful profiling information, it is **absolutely required** to use a Godot
build that includes debugging symbols. Official binaries do not include debugging
symbols, since these would make the download size significantly larger.

To get profiling data that best matches the production environment (but with debugging symbols),
you should compile binaries with the ``production=yes debug_symbols=yes`` SCons options.

It is possible to run a profiler on less optimized builds (e.g. ``target=template_debug`` without LTO),
but results will naturally be less representative of real world conditions.

.. warning::

    Do *not* strip debugging symbols on the binaries using the ``strip`` command
    after compiling the binaries. Otherwise, you will no longer get useful
    profiling information when running a profiler.

Benchmarking startup/shutdown times
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're looking into optimizing Godot's startup/shutdown performance,
you can tell the profiler to use the ``--quit`` command line option on the Godot binary.
This will exit Godot just after it's done starting.
The ``--quit`` option works with ``--editor``, ``--project-manager``, and
``--path <path to project directory>`` (which runs a project directly).

.. seealso::

    See :ref:`doc_command_line_tutorial` for more command line arguments
    supported by Godot.

.. _doc_tracing_profilers:

Tracing profilers
-----------------

Godot currently supports three tracing profilers:

- :ref:`Tracy <doc_profiler_tracy>`
- :ref:`Perfetto <doc_profiler_perfetto>`
- :ref:`Instruments <doc_profiler_instruments>` (Apple only)

In order to use either of them, you'll need to build the engine from source.
If you've never done this before, please read
:ref:`these docs <doc_compiling_index>` for the platform you want to profile on.
You'll need to perform the same steps here, but with some additional arguments
for ``scons``.

All recommended profilers
-------------------------

.. toctree::
   :maxdepth: 1
   :name: toc-devel-using-cpp-profilers

   hotspot
   instruments
   perfetto
   tracy
   very_sleepy
