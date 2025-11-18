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
which records which functions are running. The profiler can aggregate this data to
produce a graph which shows which functions the program spent the most time in.

Tracing profilers work by recording application-specific events over a short
period of time (usually only a few seconds), producing a log called a "trace".
The profiler can use the trace to produce a graph showing a high-level timeline of
what happened, when and how long it took.

While a sampling profiler doesn't require any code changes (only a build with
debug symbols), in order to use a tracing profiler, there needs to be additional
logging code added.

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
