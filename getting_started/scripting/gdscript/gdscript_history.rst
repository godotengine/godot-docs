GDScript History
================

In the early days, the Godot engine used the `Lua <http://www.lua.org>`__
scripting language. Lua is fast, but creating bindings to an object
oriented system (by using fallbacks) was complex and slow and took an
enormous amount of code. After some experiments with
`Python <https://www.python.org>`__, it also proved difficult to embed.

The last third party scripting language that was used for shipped games
was `Squirrel <http://squirrel-lang.org>`__, but it was dropped as well.
At that point, it became evident that a custom scripting language could
more optimally make use of Godot's particular architecture:

-  Godot embeds scripts in nodes. Most languages are not designed with
   this in mind.
-  Godot uses several built-in data types for 2D and 3D math. Script
   languages do not provide this, and binding them is inefficient.
-  Godot uses threads heavily for lifting and initializing data from the
   net or disk. Script interpreters for common languages are not
   friendly to this.
-  Godot already has a memory management model for resources, most
   script languages provide their own, which results in duplicate
   effort and bugs.
-  Binding code is always messy and results in several failure points,
   unexpected bugs and generally low maintainability.

The result of these considerations is *GDScript*. The language and
interpreter for GDScript ended up being smaller than the binding code itself
for Lua and Squirrel, while having equal functionality. With time, having a
built-in language has proven to be a huge advantage.
