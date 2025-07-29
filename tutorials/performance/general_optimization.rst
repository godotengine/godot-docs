.. _doc_general_optimization:

General optimization tips
=========================

Introduction
------------

In an ideal world, computers would run at infinite speed. The only limit to
what we could achieve would be our imagination. However, in the real world, it's
all too easy to produce software that will bring even the fastest computer to
its knees.

Thus, designing games and other software is a compromise between what we would
like to be possible, and what we can realistically achieve while maintaining
good performance.

To achieve the best results, we have two approaches:

- Work faster.
- Work smarter.

And preferably, we will use a blend of the two.

Smoke and mirrors
~~~~~~~~~~~~~~~~~

Part of working smarter is recognizing that, in games, we can often get the
player to believe they're in a world that is far more complex, interactive, and
graphically exciting than it really is. A good programmer is a magician, and
should strive to learn the tricks of the trade while trying to invent new ones.

The nature of slowness
~~~~~~~~~~~~~~~~~~~~~~

To the outside observer, performance problems are often lumped together.
But in reality, there are several different kinds of performance problems:

- A slow process that occurs every frame, leading to a continuously low frame
  rate.
- An intermittent process that causes "spikes" of slowness, leading to
  stalls.
- A slow process that occurs outside of normal gameplay, for instance,
  when loading a level.

Each of these are annoying to the user, but in different ways.

Measuring performance
---------------------

Probably the most important tool for optimization is the ability to measure
performance - to identify where bottlenecks are, and to measure the success of
our attempts to speed them up.

There are several methods of measuring performance, including:

- Putting a start/stop timer around code of interest.
- Using the :ref:`Godot profiler <doc_the_profiler>`.
- Using :ref:`external CPU profilers <doc_using_cpp_profilers>`.
- Using external GPU profilers/debuggers such as
  `NVIDIA Nsight Graphics <https://developer.nvidia.com/nsight-graphics>`__,
  `Radeon GPU Profiler <https://gpuopen.com/rgp/>`__,
  `PIX <https://devblogs.microsoft.com/pix/download/>`__ (Direct3D 12 only),
  `Xcode <https://developer.apple.com/documentation/xcode/optimizing-gpu-performance>`__ (Metal only), or
  `Arm Performance Studio <https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio>`__.
- Checking the frame rate (with V-Sync disabled). Third-party utilities such as
  `RivaTuner Statistics Server <https://www.guru3d.com/files-details/rtss-rivatuner-statistics-server-download.html>`__ (Windows),
  `Special K <https://www.special-k.info/>`__ (Windows),
  or `MangoHud <https://github.com/flightlessmango/MangoHud>`__
  (Linux) can also be useful here.
- Using an unofficial `debug menu add-on <https://github.com/godot-extended-libraries/godot-debug-menu>`__.

Be very aware that the relative performance of different areas can vary on
different hardware. It's often a good idea to measure timings on more than one
device. This is especially the case if you're targeting mobile devices.

Limitations
~~~~~~~~~~~

CPU profilers are often the go-to method for measuring performance. However,
they don't always tell the whole story.

- Bottlenecks are often on the GPU, "as a result" of instructions given by the
  CPU.
- Spikes can occur in the operating system processes (outside of Godot) "as a
  result" of instructions used in Godot (for example, dynamic memory allocation).
- You may not always be able to profile specific devices like a mobile phone
  due to the initial setup required.
- You may have to solve performance problems that occur on hardware you don't
  have access to.

As a result of these limitations, you often need to use detective work to find
out where bottlenecks are.

Detective work
--------------

Detective work is a crucial skill for developers (both in terms of performance,
and also in terms of bug fixing). This can include hypothesis testing, and
binary search.

Hypothesis testing
~~~~~~~~~~~~~~~~~~

Say, for example, that you believe sprites are slowing down your game.
You can test this hypothesis by:

- Measuring the performance when you add more sprites, or take some away.

This may lead to a further hypothesis: does the size of the sprite determine
the performance drop?

- You can test this by keeping everything the same, but changing the sprite
  size, and measuring performance.

Binary search
~~~~~~~~~~~~~

If you know that frames are taking much longer than they should, but you're
not sure where the bottleneck lies. You could begin by commenting out
approximately half the routines that occur on a normal frame. Has the
performance improved more or less than expected?

Once you know which of the two halves contains the bottleneck, you can
repeat this process until you've pinned down the problematic area.

Profilers
---------

Profilers allow you to time your program while running it. Profilers then
provide results telling you what percentage of time was spent in different
functions and areas, and how often functions were called.

This can be very useful both to identify bottlenecks and to measure the results
of your improvements. Sometimes, attempts to improve performance can backfire
and lead to slower performance.
**Always use profiling and timing to guide your efforts.**

For more info about using Godot's built-in profiler, see :ref:`doc_the_profiler`.

Principles
----------

`Donald Knuth <https://en.wikipedia.org/wiki/Donald_Knuth>`__ said:

    *Programmers waste enormous amounts of time thinking about, or worrying
    about, the speed of noncritical parts of their programs, and these attempts
    at efficiency actually have a strong negative impact when debugging and
    maintenance are considered. We should forget about small efficiencies, say
    about 97% of the time: premature optimization is the root of all evil. Yet
    we should not pass up our opportunities in that critical 3%.*

The messages are very important:

- Developer time is limited. Instead of blindly trying to speed up
  all aspects of a program, we should concentrate our efforts on the aspects
  that really matter.
- Efforts at optimization often end up with code that is harder to read and
  debug than non-optimized code. It is in our interests to limit this to areas
  that will really benefit.

Just because we *can* optimize a particular bit of code, it doesn't necessarily
mean that we *should*. Knowing when and when not to optimize is a great skill to
develop.

One misleading aspect of the quote is that people tend to focus on the subquote
*"premature optimization is the root of all evil"*. While *premature*
optimization is (by definition) undesirable, performant software is the result
of performant design.

Performant design
~~~~~~~~~~~~~~~~~

The danger with encouraging people to ignore optimization until necessary, is
that it conveniently ignores that the most important time to consider
performance is at the design stage, before a key has even hit a keyboard. If the
design or algorithms of a program are inefficient, then no amount of polishing
the details later will make it run fast. It may run *faster*, but it will never
run as fast as a program designed for performance.

This tends to be far more important in game or graphics programming than in
general programming. A performant design, even without low-level optimization,
will often run many times faster than a mediocre design with low-level
optimization.

Incremental design
~~~~~~~~~~~~~~~~~~

Of course, in practice, unless you have prior knowledge, you are unlikely to
come up with the best design the first time. Instead, you'll often make a series
of versions of a particular area of code, each taking a different approach to
the problem, until you come to a satisfactory solution. It's important not to
spend too much time on the details at this stage until you have finalized the
overall design. Otherwise, much of your work will be thrown out.

It's difficult to give general guidelines for performant design because this is
so dependent on the problem. One point worth mentioning though, on the CPU side,
is that modern CPUs are nearly always limited by memory bandwidth. This has led
to a resurgence in data-oriented design, which involves designing data
structures and algorithms for *cache locality* of data and linear access, rather
than jumping around in memory.

The optimization process
~~~~~~~~~~~~~~~~~~~~~~~~

Assuming we have a reasonable design, and taking our lessons from Knuth, our
first step in optimization should be to identify the biggest bottlenecks - the
slowest functions, the low-hanging fruit.

Once we've successfully improved the speed of the slowest area, it may no
longer be the bottleneck. So we should test/profile again and find the next
bottleneck on which to focus.

The process is thus:

1. Profile / Identify bottleneck.
2. Optimize bottleneck.
3. Return to step 1.

Optimizing bottlenecks
~~~~~~~~~~~~~~~~~~~~~~

Some profilers will even tell you which part of a function (which data accesses,
calculations) are slowing things down.

As with design, you should concentrate your efforts first on making sure the
algorithms and data structures are the best they can be. Data access should be
local (to make best use of CPU cache), and it can often be better to use compact
storage of data (again, always profile to test results). Often, you precalculate
heavy computations ahead of time. This can be done by performing the computation
when loading a level, by loading a file containing precalculated data, or
by storing the results of complex calculations into a script constant and
reading its value.

Once algorithms and data are good, you can often make small changes in routines
which improve performance. For instance, you can move some calculations outside
of loops or transform nested ``for`` loops into non-nested loops.
(This should be feasible if you know a 2D array's width or height in advance.)

Always retest your timing/bottlenecks after making each change. Some changes
will increase speed, others may have a negative effect. Sometimes, a small
positive effect will be outweighed by the negatives of more complex code, and
you may choose to leave out that optimization.

Appendix
--------

Bottleneck math
~~~~~~~~~~~~~~~

The proverb *"a chain is only as strong as its weakest link"* applies directly to
performance optimization. If your project is spending 90% of the time in
function ``A``, then optimizing ``A`` can have a massive effect on performance.

.. code-block:: none

    A: 9 ms
    Everything else: 1 ms
    Total frame time: 10 ms

.. code-block:: none

    A: 1 ms
    Everything else: 1ms
    Total frame time: 2 ms

In this example, improving this bottleneck ``A`` by a factor of 9× decreases
overall frame time by 5× while increasing frames per second by 5×.

However, if something else is running slowly and also bottlenecking your
project, then the same improvement can lead to less dramatic gains:

.. code-block:: none

    A: 9 ms
    Everything else: 50 ms
    Total frame time: 59 ms

.. code-block:: none

    A: 1 ms
    Everything else: 50 ms
    Total frame time: 51 ms

In this example, even though we have hugely optimized function ``A``,
the actual gain in terms of frame rate is quite small.

In games, things become even more complicated because the CPU and GPU run
independently of one another. Your total frame time is determined by the slower
of the two.

.. code-block:: none

    CPU: 9 ms
    GPU: 50 ms
    Total frame time: 50 ms

.. code-block:: none

    CPU: 1 ms
    GPU: 50 ms
    Total frame time: 50 ms

In this example, we optimized the CPU hugely again, but the frame time didn't
improve because we are GPU-bottlenecked.
