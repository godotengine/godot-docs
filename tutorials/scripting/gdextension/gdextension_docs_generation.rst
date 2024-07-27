.. _doc_gdextension_docs_generation:

Adding documentation to your GDExtension
========================================

.. note::
    Adding documentation for GDExtensions is only possible for 4.3 and later.

Similarly to how the engine works with built-in documentation inside the editor is how the
generation of the GDExtension documentation works.

Inside the Godot project directory of your GDExtension directory you run the following terminal command:

.. code-block:: none

    godot --doctool ../ --gdextension-docs

This command calls upon the Godot editor binary to generate documentation via the ``--doctool``
and ``--gdextension-docs`` commands. The ``../`` addition is to let Godot know where the GDExtension
SConstruct file is located. By calling this command Godot generates a ``doc_classes`` directory inside the
project directory in which it generates ``xml`` files for the GDExtension classes. Those files
can then be edited to add information about member variables, methods, signals, and more.

To add the now edited documentation to the GDExtension and let the editor load it you need to
add the following lines to your SConstruct file:

.. note::
    We are assuming you are using the SConstruct file supplied in the :ref:`GDExtension C++ Example <doc_gdextension_cpp_example>`.

.. code-block:: py

    if env["target"] in ["editor", "template_debug"]:
    try:
        doc_data = env.GodotCPPDocData("src/gen/doc_data.gen.cpp", source=Glob("doc_classes/*.xml"))
        sources.append(doc_data)
    except AttributeError:
        print("Not including class reference as we're targeting a pre-4.3 baseline.")

The if-statement checks if we are compiling the GDExtension library with the ``editor`` and ``template_debug``
flags. SCons then tries to load all the ``xml`` files inside the ``doc_classes`` directory and appends them
to the ``sources`` variable which already includes all the source files of your extension. If it fails
it means we are currently trying to compile the library when the ``godot_cpp`` is set to a version before 4.3.

After loading the extension in a 4.3 Godot editor or later and open the documentation of your extension class
either by :kbd:`Ctrl + Click` in the script editor or the Editor help dialog you will see something like this:

.. image:: img/gdextension_docs_generation.webp
