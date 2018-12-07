.. _doc_autoloads_versus_internal_nodes:

Autoloads versus internal nodes
===============================

Other engines might encourage the use of creating "manager" classes that
organize lots of functionality into a globally accessible entity. Godot
thrives by supporting ways to cut down the size of such objects. Instead it
shifts content into individual nodes as much as possible.

For example, what if a developer is building a platformer and they want to
collect coins that play a sound effect? Well, there's a node for that:
the :ref:`AudioStreamPlayer <class_AudioStreamPlayer>`. But they notice during
their testing that if they "play" an AudioStreamPlayer while it is already playing
the sound, then the new sound interrupts the first sound, terminating it
before it can play.

Users tend to think the best solution is to make the whole system smarter by 
making a SoundManager autoload node. It generates a pool of AudioStreamPlayers
that cycle through as each new request for sound effects comes in. They then
make this SoundManager an autoload so that they can access it from anywhere with
`SFX.play("coin_pickup.ogg")`. Little do they know, they've invited a great
many complications into their code.

- **global state**: One object is now responsible for all objects' data. If
  SFX has errors or doesn't have an AudioStreamPlayer available, everything
  will break.

- **global access**: Now that any object can call `SFX.play(sound_path)`
  from anywhere, there's no longer an easy way to track where an SFX bug
  began.

- **global resource allocation**: If all objects' data and processing is
  centralized from the start, then one must either...

  1. risk under-allocating resources which might lead to faulty behavior.

     - Ex: Have too few AudioStreamPlayers in the object pool. Sound doesn't
       play or it interrupts another sound.

  2. over-allocate resources and use more memory/processing than it needs.

     - Ex: Have an arbitrarily large number of AudioStreamPlayers, with
       many of them idling away and not doing anything.

  3. have each object that needs an AudioStreamPlayer register exactly how
     many it needs and for which sounds. This defeats the purpose of
     using a 3rd party though; it is now coupled to each object, just
     as a child node would have been. One has added an unnecessary
     middleman to the equation.

Contrast this with each scene keeping as many AudioStreamPlayer nodes as it
needs within itself and all these problems go away.

- Each scene manages its own state information. If there is a problem with the
  data, it will only cause issues in that one scene.

- Each scene accesses only its own nodes. Now, if there is
  a bug, tracing which node is responsible (probably the root node of the
  scene), and where in the code it's making the problematic call (locate
  where the code references the given node) is going to be much easier.

- Each scene knows exactly how many resources it needs for the task it
  performs. No waste of memory or processing due to a lack of information.

The typical justifications for the Autoload include, "I have common Xs that
involve many nodes across many scenes, and I want each scene to have X."

If X is a function, then the solution is to create a new type of
:ref:`Node <class_Node>` that deals with providing that feature for an
individual scene or node subtree.

If X is data, then the solution is either 1) to create a new type of
:ref:`Resource <class_Resource>` to share the data, or 2) to store the data
in an object to which each node has access (nodes within a scene can use
`get_owner()` to fetch the scene root for example).

So when *should* one use an autoload?

- **Static Data**: if you need static data, i.e. data that should be
  associated with a class (so there is only ever one copy of the data), then
  autoloads are good opportunities for that. Static data doesn't exist in
  Godot's scripting API, so autoload singletons are the next best thing. If
  one creates a class as an autoload, and never creates another copy of that
  class within a scene, then it will function in place of a formal singleton
  API.

- **Convenience**: autoloaded nodes have a global variable for their name
  generated in GDScript. This can be very convenient for defining objects
  that should always exist, but which need object instance information.
  The alternative is to create a namespace script: a script that's purpose
  is only to load and create constants to access other Script or PackedScene
  resources, resulting in something like ``MyAutoload.MyNode.new()``.

  - Note that the introduction of script classes in Godot 3.1 questions
    the validity of this reason. With them, one can access scripts using an
    explicit name from GDScript. Using an autoload to get to a namespace
    script becomes unnecessary, e.g. ``MyScriptClass.MyPreloadedScript.new()``.

If the singleton is managing its own information and not invading the data of
other objects, then it's a great way to create a "system" class that handles
a broad-scoped task. For example a targeting system, quest system, or dialogue
system would be great use cases of singleton implementations.
