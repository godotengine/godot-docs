.. meta::
    :keywords: FAQ

.. _doc_faq:

Frequently asked questions
==========================

What can I do with Godot? How much does it cost? What are the license terms?
----------------------------------------------------------------------------

Godot is `Free and Open-Source Software <https://en.wikipedia.org/wiki/Free_and_open-source_software>`_ available under the `OSI-approved <https://opensource.org/licenses/MIT>`_ MIT license. This means it is free as in "free speech" as well as in "free beer."

In short:

* You are free to download and use Godot for any purpose, personal, non-profit, commercial, or otherwise.
* You are free to modify, distribute, redistribute, and remix Godot to your heart's content, for any reason, both non-commercially and commercially.

All the contents of this accompanying documentation are published under
the permissive Creative Commons Attribution 3.0 (`CC-BY 3.0 <https://creativecommons.org/licenses/by/3.0/>`_) license, with attribution
to "Juan Linietsky, Ariel Manzur and the Godot Engine community."

Logos and icons are generally under the same Creative Commons license. Note
that some third-party libraries included with Godot's source code may have
different licenses.

For full details, look at the `COPYRIGHT.txt <https://github.com/godotengine/godot/blob/master/COPYRIGHT.txt>`_ as well
as the `LICENSE.txt <https://github.com/godotengine/godot/blob/master/LICENSE.txt>`_ and `LOGO_LICENSE.txt <https://github.com/godotengine/godot/blob/master/LOGO_LICENSE.md>`_ files
in the Godot repository.

Also, see `the license page on the Godot website <https://godotengine.org/license>`_.

Which platforms are supported by Godot?
---------------------------------------

**For the editor:**

* Windows
* macOS
* X11 (Linux, \*BSD)

**For exporting your games:**

* Windows (and UWP)
* macOS
* X11 (Linux, \*BSD)
* Android
* iOS
* Web

Both 32- and 64-bit binaries are supported where it makes sense, with 64
being the default.

Some users also report building and using Godot successfully on ARM-based
systems with Linux, like the Raspberry Pi.

Additionally, there is some unofficial third-party work being done on building
for some consoles. However, none of this is included in the default build
scripts or export templates at this time.

For more on this, see the sections on :ref:`exporting <toc-learn-workflow-export>`
and :ref:`compiling Godot yourself <toc-devel-compiling>`.

Which programming languages are supported in Godot?
---------------------------------------------------

The officially supported languages for Godot are GDScript, Visual Scripting,
C#, and C++. See the subcategories for each language in the
:ref:`scripting <toc-learn-scripting>` section.

If you are just starting out with either Godot or game development in general,
GDScript is the recommended language to learn and use since it is native to Godot.
While scripting languages tend to be less performant than lower-level languages in
the long run, for prototyping, developing Minimum Viable Products (MVPs), and
focusing on Time-To-Market (TTM), GDScript will provide a fast, friendly, and capable
way of developing your games.

Note that C# support is still relatively new, and as such, you may encounter some
issues along the way. Our friendly and hard-working development community is always
ready to tackle new problems as they arise, but since this is an open-source project,
we recommend that you first do some due diligence yourself. Searching through
discussions on `open issues <https://github.com/godotengine/godot/issues>`_ is a
great way to start your troubleshooting.

As for new languages, support is possible via third parties using the GDNative /
NativeScript / PluginScript facilities. (See the question about plugins below.)
Work is currently underway, for example, on unofficial bindings for Godot
to `Python <https://github.com/touilleMan/godot-python>`_ and `Nim <https://github.com/pragmagic/godot-nim>`_.

.. _doc_faq_what_is_gdscript:

What is GDScript and why should I use it?
-----------------------------------------

GDScript is Godot's integrated scripting language. It was built from the ground
up to maximize Godot's potential in the least amount of code, affording both novice
and expert developers alike to capitalize on Godot's strengths as fast as possible.
If you've ever written anything in a language like Python before then you'll feel
right at home. For examples, history, and a complete overview of the power GDScript
offers you, check out the :ref:`GDScript scripting guide <doc_gdscript>`.

There are several reasons to use GDScript--especially when you are prototyping, in
alpha/beta stages of your project, or are not creating the next AAA title--but the
most salient reason is the overall **reduction of complexity.**

The original intent of creating a tightly integrated, custom scripting language for
Godot was two-fold: first, it reduces the amount of time necessary to get up and running
with Godot, giving developers a rapid way of exposing themselves to the engine with a
focus on productivity; second, it reduces the overall burden of maintenance, attenuates
the dimensionality of issues, and allows the developers of the engine to focus on squashing
bugs and improving features related to the engine core--rather than spending a lot of time
trying to get a small set of incremental features working across a large set of languages.

Since Godot is an open-source project, it was imperative from the start to prioritize a
more integrated and seamless experience over attracting additional users by supporting
more familiar programming languages--especially when supporting those more familiar
languages would result in a worse experience. We understand if you would rather use
another language in Godot (see the list of supported options above). That being said, if
you haven't given GDScript a try, try it for **three days**. Just like Godot,
once you see how powerful it is and rapid your development becomes, we think GDScript
will grow on you.

More information about getting comfortable with GDScript or dynamically typed
languages can be found in the :ref:`doc_gdscript_more_efficiently` tutorial.

What were the motivations behind creating GDScript?
---------------------------------------------------

In the early days, the engine used the `Lua <https://www.lua.org>`__
scripting language. Lua is fast, but creating bindings to an object
oriented system (by using fallbacks) was complex and slow and took an
enormous amount of code. After some experiments with
`Python <https://www.python.org>`__, it also proved difficult to embed.

The main reasons for creating a custom scripting language for Godot were:

1. Poor threading support in most script VMs, and Godot uses threads
   (Lua, Python, Squirrel, JavaScript, ActionScript, etc.).
2. Poor class-extending support in most script VMs, and adapting to
   the way Godot works is highly inefficient (Lua, Python, JavaScript).
3. Many existing languages have horrible interfaces for binding to C++, resulting in large amount of
   code, bugs, bottlenecks, and general inefficiency (Lua, Python,
   Squirrel, JavaScript, etc.) We wanted to focus on a great engine, not a great amount of integrations.
4. No native vector types (vector3, matrix4, etc.), resulting in highly
   reduced performance when using custom types (Lua, Python, Squirrel,
   JavaScript, ActionScript, etc.).
5. Garbage collector results in stalls or unnecessarily large memory
   usage (Lua, Python, JavaScript, ActionScript, etc.).
6. Difficulty to integrate with the code editor for providing code
   completion, live editing, etc. (all of them). This is well-supported
   by GDScript.

GDScript was designed to curtail the issues above, and more.

What type of 3D model formats does Godot support?
-------------------------------------------------

Godot supports Collada via the `OpenCollada <https://github.com/KhronosGroup/OpenCOLLADA/wiki/OpenCOLLADA-Tools>`_ exporter (Maya, 3DSMax).
If you are using Blender, take a look at our own `Better Collada Exporter <https://godotengine.org/download>`_.

As of Godot 3.0, glTF is supported.

FBX is supported via the Open Asset Import library. However, FBX is proprietary
so we recommend using other formats listed above, if suitable for your workflow.

Will [insert closed SDK such as FMOD, GameWorks, etc.] be supported in Godot?
-----------------------------------------------------------------------------

The aim of Godot is to create a free and open-source MIT-licensed engine that
is modular and extendable. There are no plans for the core engine development
community to support any third-party, closed-source/proprietary SDKs, as integrating
with these would go against Godot's ethos.

That said, because Godot is open-source and modular, nothing prevents you or
anyone else interested in adding those libraries as a module and shipping your
game with them--as either open- or closed-source.

To see how support for your SDK of choice could still be provided, look at the
Plugins question below.

If you know of a third-party SDK that is not supported by Godot but that offers
free and open-source integration, consider starting the integration work yourself.
Godot is not owned by one person; it belongs to the community, and it grows along
with ambitious community contributors like you.

How should assets be created to handle multiple resolutions and aspect ratios?
------------------------------------------------------------------------------

This question pops up often and it's probably thanks to the misunderstanding
created by Apple when they originally doubled the resolution of their devices.
It made people think that having the same assets in different resolutions was a
good idea, so many continued towards that path. That originally worked to a
point and only for Apple devices, but then several Android and Apple devices
with different resolutions and aspect ratios were created, with a very wide
range of sizes and DPIs.

The most common and proper way to achieve this is to, instead, use a single
base resolution for the game and only handle different screen aspect ratios.
This is mostly needed for 2D, as in 3D it's just a matter of Camera XFov or YFov.

1. Choose a single base resolution for your game. Even if there are
   devices that go up to 2K and devices that go down to 400p, regular
   hardware scaling in your device will take care of this at little or
   no performance cost. Most common choices are either near 1080p
   (1920x1080) or 720p (1280x720). Keep in mind the higher the
   resolution, the larger your assets, the more memory they will take
   and the longer the time it will take for loading.

2. Use the stretch options in Godot; 2D stretching while keeping aspect
   ratios works best. Check the :ref:`doc_multiple_resolutions` tutorial
   on how to achieve this.

3. Determine a minimum resolution and then decide if you want your game
   to stretch vertically or horizontally for different aspect ratios, or
   if there is one aspect ratio and you want black bars to appear
   instead. This is also explained in :ref:`doc_multiple_resolutions`.

4. For user interfaces, use the :ref:`anchoring <doc_size_and_anchors>`
   to determine where controls should stay and move. If UIs are more
   complex, consider learning about Containers.

And that's it! Your game should work in multiple resolutions.

If there is a desire to make your game also work on ancient
devices with tiny screens (fewer than 300 pixels in width), you can use
the export option to shrink images, and set that build to be used for
certain screen sizes in the App Store or Google Play.

How can I extend Godot?
-----------------------

For extending Godot, like creating Godot Editor plugins or adding support
for additional languages, take a look at :ref:`EditorPlugins <doc_making_plugins>`
and tool scripts.

Also, see the official blog posts on these topics:

* `A look at the GDNative architecture <https://godotengine.org/article/look-gdnative-architecture>`_
* `GDNative is here! <https://godotengine.org/article/dlscript-here>`_

You can also take a look at the GDScript implementation, the Godot modules,
as well as the `unofficial Python support <https://github.com/touilleMan/godot-python>`_ for Godot.
This would be a good starting point to see how another third-party library
integrates with Godot.

I would like to contribute! How can I get started?
--------------------------------------------------

Awesome! As an open-source project, Godot thrives off of the innovation and
ambition of developers like you.

The first place to get started is in the `issues <https://github.com/godotengine/godot/issues>`_.
Find an issue that resonates with you, then proceed to the `How to Contribute <https://github.com/godotengine/godot/blob/master/CONTRIBUTING.md#contributing-pull-requests>`_
guide to learn how to fork, modify, and submit a Pull Request (PR) with your changes.

I have a great idea for Godot. How can I share it?
--------------------------------------------------

It might be tempting to want to bring ideas to Godot, like ones that
result in massive core changes, some sort of mimicry of what another
game engine does, or alternative workflows that you'd like built into
the editor. These are great, and we are thankful to have such motivated
people want to contribute, but Godot's focus is and always will be the
core functionality as outlined in the `Roadmap <https://github.com/godotengine/godot-roadmap/blob/master/ROADMAP.md>`_,
`squashing bugs and addressing issues <https://github.com/godotengine/godot/issues>`_,
and conversations between Godot community members.

Most developers in the Godot community will be more interested to learn
about things like:

-  Your experience using the software and the problems you have (we
   care about this much more than ideas on how to improve it).
-  The features you would like to see implemented because you need them
   for your project.
-  The concepts that were difficult to understand while learning the software.
-  The parts of your workflow you would like to see optimized.
-  Parts where you missed clear tutorials or where the documentation wasn't clear.

Please don't feel like your ideas for Godot are unwelcome. Instead,
try to reformulate them as a problem first, so developers and the community
have a functional foundation to ground your ideas on.

A good way to approach sharing your ideas and problems with the community
is as a set of user stories. Explain what you are trying to do, what behavior
you expect to happen, and then what behavior actually happened. Framing problems
and ideas this way will help the whole community stay focused on improving
developer experiences as a whole.

Bonus points for bringing screenshots, concrete numbers, test cases, or example
projects (if applicable).


Why does Godot not use STL (Standard Template Library)
------------------------------------------------------

Like many other libraries (Qt as an example), Godot does not make use of
STL. We believe STL is a great general purpose library, but we had special
requirements for Godot.

* STL templates create very large symbols, which results in huge debug binaries. We use few templates with very short names instead.
* Most of our containers cater to special needs, like Vector, which uses copy on write and we use to pass data around, or the RID system, which requires O(1) access time for performance. Likewise, our hash map implementations are designed to integrate seamlessly with internal engine types.
* Our containers have memory tracking built-in, which helps better track memory usage.
* For large arrays, we use pooled memory, which can be mapped to either a preallocated buffer or virtual memory.
* We use our custom String type, as the one provided by STL is too basic and lacks proper internationalization support.

Why does Godot not use exceptions?
----------------------------------

We believe games should not crash, no matter what. If an unexpected
situation happens, Godot will print an error (which can be traced even to
script), but then it will try to recover as gracefully as possible and keep
going.

Additionally, exceptions significantly increase binary size for the
executable.

Why does Godot not enforce RTTI?
--------------------------------

Godot provides its own type-casting system, which can optionally use RTTI
internally. Disabling RTTI in Godot means considerably smaller binary sizes can
be achieved, at a little performance cost.

Why does Godot not force users to implement DoD (Data oriented Design)?
-----------------------------------------------------------------------

While Godot internally for a lot of the heavy performance tasks attempts
to use cache coherency as well as possible, we believe most users don't
really need to be forced to use DoD practices.

DoD is mostly a cache coherency optimization that can only gain you
significant performance improvements when dealing with dozens of
thousands of objects (which are processed every frame with little
modification). As in, if you are moving a few hundred sprites or enemies
per frame, DoD won't help you, and you should consider a different approach
to optimization.

The vast majority of games do not need this and Godot provides handy helpers
to do the job for most cases when you do.

If a game that really needs to process such large amount of objects is
needed, our recommendation is to use C++ and GDNative for the high
performance parts and GDScript (or C#) for the rest of the game.

How can I support Godot development or contribute?
--------------------------------------------------

See :ref:`doc_ways_to_contribute`.

Who is working on Godot? How can I contact you?
-----------------------------------------------

See the corresponding page on the `Godot website <https://godotengine.org/contact>`_.
