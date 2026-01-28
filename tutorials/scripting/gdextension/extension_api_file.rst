.. _doc_gdextension_api_file:

The GDExtension API file
========================

The ``extension_api.json`` is a file that contains information about all the high level
APIs that are exposed from Godot for use in programming languages like GDScript or C++.

You can use the Godot executable to dump the file by using the following command:

.. code-block:: shell

    godot --dump-extension-api

This file is intended to be used by GDExtension language bindings to generate code for
using this API in whatever form makes the most sense for that language.

.. note::

    This is not to be confused with the ``gdextension_interface.json`` file, which
    is also used by GDExtension language bindings. ``gdextension_interface.json``
    is more low level, and is used to establish communication between Godot and a
    GDExtension, while ``gdextension_interface.json`` contains high level APIs.

The goal of this page is to explain the JSON format for the GDExtension language bindings that
would like to do their own code generation from the JSON.

Overall structure
-----------------

TBD
