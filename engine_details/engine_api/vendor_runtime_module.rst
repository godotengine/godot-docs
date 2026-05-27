.. _doc_vendor_runtime_module:

Vendor Runtime Module
=====================

A Vendor Runtime Module is a :ref:`Godot module <doc_custom_modules_in_cpp>`
which is only applicable at runtime in a running project.
It is created like a regular :ref:`custom C++ module <doc_custom_modules_in_cpp>`, but is
packaged using an :ref:`editor plugin <doc_making_plugins>` to make the functionality
it provides easily accessible and usable within a *stock* Godot project.

What for?
---------

Vendor runtime modules provide developers with access to vendor-specific optimizations, features,
and/or platforms for their running projects. 

This provides benefits to vendors who are able to expose their technologies to all developers,
and improve and refine them in a rapid, iterative, and frictionless manner.
This also provides benefits to developers and users who are able to access and use a diverse range of vendor 
technologies to improve their games.

Creating a vendor runtime module
--------------------------------

Generating export templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure to follow the :ref:`instructions for creating a custom C++ module <doc_creating_custom_modules_in_cpp>`.

Since this is a runtime module whose functionality is meant to only be accessed from the running project, you must
generate an export template for every platform you plan to support.
See the :ref:`Compiling <toc-devel-compiling>` pages for more information.

Creating the wrapper editor plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the export templates are generated, you must create an editor plugin to package them and make them easily
accessible to end users via the `Godot Asset Store <https://store.godotengine.org/>`_.

Follow :ref:`these instructions <doc_making_plugins_template>` to start creating the plugin. Your base plugin script should look like the following:

.. code-block:: gdscript

    @tool
    extends EditorPlugin


    func _enter_tree():
        # Initialization of the plugin goes here.
        pass


    func _exit_tree():
        # Clean-up of the plugin goes here.
        pass


The next step is to define and instantiate an :ref:`EditorExportPlugin<class_EditorExportPlugin>` instance. 
The :ref:`EditorExportPlugin<class_EditorExportPlugin>` instance is used to hook into the export flow and
replace the default export templates with the ones generated from the vendor runtime module.

Using our base editor plugin template code above, an example implementation looks like this:

.. code-block:: gdscript

    @tool
    extends EditorPlugin

    # A class member to hold the editor export plugin during its lifecycle.
    var export_plugin: VRMExportPlugin

    func _enter_tree():
        # Initialization of the plugin goes here.
        export_plugin = VRMExportPlugin.new()
        add_export_plugin(export_plugin)


    func _exit_tree():
        # Clean-up of the plugin goes here.
        remove_export_plugin(export_plugin)
        export_plugin = null


    class VRMExportPlugin extends EditorExportPlugin:
        var _path_to_debug_export_template = ""
        var _path_to_release_export_template = ""

        # Return true for all supported platforms.
        func _supports_platform(platform):
            return platform is EditorExportPlatformAndroid

        # Overrides the default export templates.
        func _get_export_options_overrides(platform):
            var overrides = {}
            if not _supports_platform(platform):
                return overrides
            
            # Overrides Android export preset's "custom_template" options.
            overrides["custom_template/debug"] = _path_to_debug_export_template
            overrides["custom_template/release"] = _path_to_release_export_template

            return overrides

        # Optional: specify additional export preset options to customize the export template.
        func _get_export_options(platform):
            pass
        
        func _get_name():
            return "VRM Plugin"


.. tip::

    This section covers the basics to wrap and expose a vendor runtime module via an editor plugin, but
    editor plugins have a lot more functionality that can be used to customize the editor further. 
    Feel free to :ref:`explore and leverage those functionalities <toc-tutorials-plugins>` to improve the
    user experience for your vendor runtime module.
