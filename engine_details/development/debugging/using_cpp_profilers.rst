.. _doc_using_cpp_profilers:

Using C++ profilers
===================

To optimize Godot's performance, you need to know what to optimize first.
To this end, profilers are useful tools.

.. note::

    There is a :ref:`built-in GDScript profiler <doc_the_profiler>` in the editor,
    but using C++ profiler may be useful in cases where the GDScript profiler
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

.. toctree::
   :maxdepth: 1
   :name: toc-devel-using-cpp-profilers

   profiling/sampling_profilers
   profiling/tracing_profilers
