.. _doc_gdextension_file:

The .gdextension file
=====================

Introduction
------------

The ``.gdextension`` file in your project contains the instructions for how to load
the GDExtension. The instructions are separated into specific sections. This page
should give you a quick overview of the different options available to you. For an introduction
how to get started with C++ (godot-cpp), take a look at the :ref:`GDExtension C++ Example <doc_godot_cpp_getting_started>`.

Configuration section
---------------------

+-------------------------------+------------+------------------------------------------------------------------------------------------------------+
| Property                      | Type       | Description                                                                                          |
+===============================+============+======================================================================================================+
| **entry_symbol**              | String     | Name of the entry function for initializing the GDExtension. This function should be defined in      |
|                               |            | the ``register_types.cpp`` file when using godot-cpp. Adding this is necessary for the extension to  |
|                               |            | work.                                                                                                |
+-------------------------------+------------+------------------------------------------------------------------------------------------------------+
| **compatibility_minimum**     | String     | Minimum compatible version. This prevents older versions of Godot from loading extensions that       |
|                               |            | depend on features from newer versions of Godot. **Only supported in Godot 4.1 or later**            |
+-------------------------------+------------+------------------------------------------------------------------------------------------------------+
| **compatibility_maximum**     | String     | Maximum compatible version. This prevents newer versions of Godot from loading the extension.        |
|                               |            | **Only supported in Godot 4.3 or later**                                                             |
+-------------------------------+------------+------------------------------------------------------------------------------------------------------+
| **reloadable**                | Boolean    | Reloads the extension upon recompilation. Reloading is supported for the godot-cpp binding in        |
|                               |            | Godot 4.2 or later. Other language bindings may or may not support it as well. This flag should be   |
|                               |            | mainly used for developing or debugging an extension.                                                |
+-------------------------------+------------+------------------------------------------------------------------------------------------------------+
| **android_aar_plugin**        | Boolean    | The GDExtension is part of a :ref:`v2 Android plugin <doc_android_plugin>`. During export this flag  |
|                               |            | will indicate to the editor that the GDExtension native shared libraries are exported by the Android |
|                               |            | plugin AAR binaries.                                                                                 |
+-------------------------------+------------+------------------------------------------------------------------------------------------------------+

Libraries section
-----------------

In this section you can set the paths to the compiled binaries of your GDExtension libraries.
By specifying feature flags you can filter which version should be loaded and exported with your
game depending on which feature flags are active. Every feature flag must match to Godot's
feature flags or your custom export flags to be loaded in an exported game. For instance ``macos.debug``
means that it will be loaded if Godot has both the ``macos`` and ``debug`` flag active. Each
line of the section is evaluated from top to bottom.

Here is an example of what that can look like:

.. code-block:: none

    [libraries]

    macos.debug = "res://bin/libgdexample.macos.template_debug.framework"
    macos.release = "res://bin/libgdexample.macos.template_release.framework"
    windows.debug.x86_32 = "res://bin/libgdexample.windows.template_debug.x86_32.dll"
    windows.release.x86_32 = "res://bin/libgdexample.windows.template_release.x86_32.dll"
    windows.debug.x86_64 = "res://bin/libgdexample.windows.template_debug.x86_64.dll"
    windows.release.x86_64 = "res://bin/libgdexample.windows.template_release.x86_64.dll"
    linux.debug.x86_64 = "res://bin/libgdexample.linux.template_debug.x86_64.so"
    linux.release.x86_64 = "res://bin/libgdexample.linux.template_release.x86_64.so"
    linux.debug.arm64 = "res://bin/libgdexample.linux.template_debug.arm64.so"
    linux.release.arm64 = "res://bin/libgdexample.linux.template_release.arm64.so"
    linux.debug.rv64 = "res://bin/libgdexample.linux.template_debug.rv64.so"
    linux.release.rv64 = "res://bin/libgdexample.linux.template_release.rv64.so"


Entries are matched in order, so if two sets of feature tags could match
the same system, be sure to put the more specific ones first:

.. code-block:: none

    [libraries]

    linux.release.editor.x86_64 = "res://bin/libgdexample.linux.template_release.x86_64.so"
    linux.release.x86_64 = "res://bin/libgdexample.linux.noeditor.template_release.x86_64.so"

Here are lists of some of the available built-in options (for more look at the :ref:`feature tags <doc_feature_tags>`):

Running system
~~~~~~~~~~~~~~

+-------------------------------+------------------------------------------------------------------------------------------------------+
| Flag                          | Description                                                                                          |
+===============================+======================================================================================================+
| **windows**                   | Windows operating system                                                                             |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **macos**                     | Mac operating system                                                                                 |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **linux**                     | Linux operating system                                                                               |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **bsd**                       | BSD operating system                                                                                 |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **linuxbsd**                  | Linux or BSD operating system                                                                        |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **android**                   | Android operating system                                                                             |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **ios**                       | iOS operating system                                                                                 |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **web**                       | Web browser                                                                                          |
+-------------------------------+------------------------------------------------------------------------------------------------------+

Build
~~~~~

+-------------------------------+------------------------------------------------------------------------------------------------------+
| Flag                          | Description                                                                                          |
+===============================+======================================================================================================+
| **debug**                     | Build with debug symbols                                                                             |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **release**                   | Optimized build without debug symbols                                                                |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **editor**                    | Editor build                                                                                         |
+-------------------------------+------------------------------------------------------------------------------------------------------+

Architecture
~~~~~~~~~~~~

+-------------------------------+------------------------------------------------------------------------------------------------------+
| Flag                          | Description                                                                                          |
+===============================+======================================================================================================+
| **double**                    | double-precision build                                                                               |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **single**                    | single-precision build                                                                               |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **x86_64**                    | 64-bit x86 build                                                                                     |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **arm64**                     | 64-bit ARM build                                                                                     |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **rv64**                      | 64-bit RISC-V build                                                                                  |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **riscv**                     | RISC-V build (any bitness)                                                                           |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **wasm32**                    | 32-bit WebAssembly build                                                                             |
+-------------------------------+------------------------------------------------------------------------------------------------------+

Icons section
-------------

By default, Godot uses the Node icon in the scene dock for GDExtension nodes. A custom icon can be
set by reference to its name and resource path of an SVG file.

For example:

.. code-block:: none

    [icons]

    GDExample = "res://icons/gd_example.svg"

The path should point to a 16 by 16 pixel SVG image. Read the guide for :ref:`creating icons <doc_editor_icons>`
for more information.

Dependencies section
--------------------

In this section you set the paths of the GDExtension dependencies. This is used internally to export the dependencies
when exporting your game executable. You are able to set which dependency is loaded depending on the feature flags
of the exported executable. In addition, you are able to set an optional subdirectory to move your dependencies into.
If no path is supplied Godot will move the libraries into the same directory as your game executable.

.. warning::
    In MacOS it is necessary to have shared libraries inside a folder called ``Frameworks`` with a directory structure
    like this: ``Game.app/Contents/Frameworks``.

.. code-block:: none

    [dependencies]

    macos.debug = {
        "res://bin/libdependency.macos.template_debug.framework" : "Contents/Frameworks"
    }
    macos.release = {
        "res://bin/libdependency.macos.template_release.framework" : "Contents/Frameworks"
    }
    windows.debug = {
        "res://bin/libdependency.windows.template_debug.x86_64.dll" : "",
        "res://bin/libdependency.windows.template_debug.x86_32.dll" : ""
    }
    windows.release = {
        "res://bin/libdependency.windows.template_release.x86_64.dll" : "",
        "res://bin/libdependency.windows.template_release.x86_32.dll" : ""
    }
    linux.debug = {
        "res://bin/libdependency.linux.template_debug.x86_64.so" : "",
        "res://bin/libdependency.linux.template_debug.arm64.so" : "",
        "res://bin/libdependency.linux.template_debug.rv64.so" : ""
    }
    linux.release = {
        "res://bin/libdependency.linux.template_release.x86_64.so" : "",
        "res://bin/libdependency.linux.template_release.arm64.so" : "",
        "res://bin/libdependency.linux.template_release.rv64.so" : ""
    }
