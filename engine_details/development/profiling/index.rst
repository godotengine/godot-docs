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

.. note::

    Perfetto is the default tracing system for Android, so pre-built export templates
    with Perfetto built-in and enabled are provided from 
    the `GitHub Releases page <https://github.com/godotengine/godot-builds/releases>`__.

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

Microbenchmarks
---------------

While not technically profiling, microbenchmarks are a related concept: after you've identified
your hotspot, you'll want a simple and isolatable way to test whether what you're doing has an impact.
While re-profiling can be an option, sometimes a microbenchmark can be simpler.

You can see example benchmark setups in the subsections below. Between C++ and GDScript, GDScript
benchmarks are usually the more appropriate choice. Because they involve the GDScript language and
its overhead, GDScript benchmarks are truthful to how most people will experience your changes.
C++ benchmarks are more versatile and can measure smaller performance differences. However, they
are also more difficult to get right.
In practice, it can often be good to benchmark both.

.. note::

    To benchmark effectively can be difficult. Benchmarks can easily lead you astray, for example
    by not representing the situation faithfully, by failing to account for compiler optimizations
    and other nuances, or by measuring in an unreliable way such that you record noise instead of
    an actual performance change. Before you start benchmarking, please read up on benchmarking
    guides and best practices. A good place to start is Gregg's `"Active Benchmarking" <https://www.brendangregg.com/activebenchmarking.html>`__,
    which provides a high level overview and quick checklist for benchmarking.

GDScript benchmarks
~~~~~~~~~~~~~~~~~~~

To run a GDScript benchmark, start by creating a ``benchmark.gd`` file with the following
contents:

.. code-block:: gdscript

    extends SceneTree

    func _init():
        const N = 1_000_000

        var t0 := Time.get_ticks_usec()
        for i in N:
            pass  # Do the thing you want to benchmark here.
        var t1 := Time.get_ticks_usec()

        var ns_per_op := (t1 - t0) * 1000.0 / N
        print("Benchmark result: %.1f ns/op" % ns_per_op)
        quit()

Edit the file to add your benchmark.
You can run the benchmark using ``godot --headless -s benchmark.gd``.

.. note::

    At the time of writing, GDScript performs few code optimization. Dead code elimination,
    for example, is generally not performed. Therefore, it is easier to write a decently
    representative benchmark in GDScript than in C++. This might change in the future.

C++ benchmarks
~~~~~~~~~~~~~~

To run a C++ benchmark, create the file ``tests/core/test_user_bench.cpp`` with the following contents:

.. code-block:: cpp

    #include "tests/test_macros.h"

    TEST_FORCE_LINK(test_user_bench)

    #include <chrono>
    #include <cstdio>

    static void user_bench() {
        const int N = 1'000'000;
        static uintptr_t sink = 0; // Defeats dead-code elimination.

        auto t0 = std::chrono::steady_clock::now();
        for (int i = 0; i < N; i++) {
            // Do the thing you want to benchmark here.
            // sink += (uintptr_t)something; // Update the sink from the result somehow.
        }
        auto t1 = std::chrono::steady_clock::now();

        double ns_per_op = std::chrono::duration<double, std::nano>(t1 - t0).count() / N;
        printf("Benchmark result: %.1f ns/op (sink %zu)\n", ns_per_op, (size_t)sink);
    }

    REGISTER_TEST_COMMAND("user-bench", &user_bench)

Edit the file to add your benchmark.
Compile Godot with ``tests=yes``, and run the benchmark using ``godot --test user-bench``.

.. note::

    C++ benchmarks can be fickle and can easily lead you astray unless you have a strong
    foundation of knowledge about C++ and compilers. Before you start benchmarking, read
    up on guides and best practices about how to benchmark C++.  You
    can find free in-depth guides in Bakhvalov's `"Performance Analysis and Tuning on Modern CPUs" <https://github.com/dendibakh/perf-book>`__,
    and Agner Fog's `"Software Optimization Resources" <https://www.agner.org/optimize/>`__.
