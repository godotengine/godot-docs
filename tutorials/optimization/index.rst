Optimization
=============

Introduction
------------

Godot follows a balanced performance philosophy. In the performance world, there
are always trade-offs, which consist of trading speed for usability and
flexibility. Some practical examples of this are:

-  Rendering objects efficiently in high amounts is easy, but when a
   large scene must be rendered, it can become inefficient. To solve this,
   visibility computation must be added to the rendering, which makes rendering
   less efficient, but, at the same time, fewer objects are rendered, so
   efficiency overall improves.

-  Configuring the properties of every material for every object that
   needs to be rendered is also slow. To solve this, objects are sorted by
   material to reduce the costs, but at the same time sorting has a cost.

-  In 3D physics a similar situation happens. The best algorithms to
   handle large amounts of physics objects (such as SAP) are slow at
   insertion/removal of objects and ray-casting. Algorithms that allow faster
   insertion and removal, as well as ray-casting, will not be able to handle as
   many active objects.

And there are many more examples of this! Game engines strive to be general
purpose in nature, so balanced algorithms are always favored over algorithms
that might be fast in some situations and slow in others or algorithms that are
fast but make usability more difficult.

Godot is not an exception and, while it is designed to have backends swappable
for different algorithms, the default ones prioritize balance and flexibility
over performance.

With this clear, the aim of this tutorial section is to explain how to get the
maximum performance out of Godot. While the tutorials can be read in any order,
it is a good idea to start from :ref:`doc_general_optimization`.

Common
------

.. toctree::
   :maxdepth: 1
   :name: toc-learn-features-general-optimization

   general_optimization
   using_servers

CPU
---

.. toctree::
   :maxdepth: 1
   :name: toc-learn-features-cpu-optimization

   cpu_optimization

GPU
---

.. toctree::
   :maxdepth: 1
   :name: toc-learn-features-gpu-optimization

   gpu_optimization
   using_multimesh

2D
--

.. toctree::
   :maxdepth: 1
   :name: toc-learn-features-2d-optimization

   batching

3D
--

.. toctree::
   :maxdepth: 1
   :name: toc-learn-features-3d-optimization

   optimizing_3d_performance
