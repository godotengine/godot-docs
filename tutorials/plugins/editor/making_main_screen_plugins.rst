:article_outdated: True

.. _doc_making_main_screen_plugins:

Making main screen plugins
==========================

What this tutorial covers
-------------------------

Main screen plugins allow you to create
new UIs in the central part of the editor, which appear next to the
"2D", "3D", "Script", and "AssetLib" buttons. Such editor plugins are
referred as "Main screen plugins".

This tutorial leads you through the creation of a basic main screen plugin.
For the sake of simplicity, our main screen plugin will contain a single
button that prints text to the console.

Initializing the plugin
-----------------------

First create a new plugin from the Plugins menu. For this tutorial, we'll put
it in a folder called ``main_screen``, but you can use any name you'd like.

The plugin script will come with ``_enter_tree()`` and ``_exit_tree()``
methods, but for a main screen plugin we need to add a few extra methods.
Add five extra methods such that the script looks like this:

.. tabs::
 .. code-tab:: gdscript GDScript

    @tool
    extends EditorPlugin


    func _enter_tree():
        pass


    func _exit_tree():
        pass


    func _has_main_screen():
        return true


    func _make_visible(visible):
        pass


    func _get_plugin_name():
        return "Main Screen Plugin"


    func _get_plugin_icon():
        return EditorInterface.get_editor_theme().get_icon("Node", "EditorIcons")

 .. code-tab:: csharp

    #if TOOLS
    using Godot;

    [Tool]
    public partial class MainScreenPlugin : EditorPlugin
    {
        public override void _EnterTree()
        {

        }

        public override void _ExitTree()
        {

        }

        public override bool _HasMainScreen()
        {
            return true;
        }

        public override void _MakeVisible(bool visible)
        {

        }

        public override string _GetPluginName()
        {
            return "Main Screen Plugin";
        }

        public override Texture2D _GetPluginIcon()
        {
            return EditorInterface.GetEditorTheme().GetIcon("Node", "EditorIcons");
        }
    }
    #endif

The important part in this script is the ``_has_main_screen()`` function,
which is overloaded so it returns ``true``. This function is automatically
called by the editor on plugin activation, to tell it that this plugin
adds a new center view to the editor. For now, we'll leave this script
as-is and we'll come back to it later.

Main screen scene
-----------------

Create a new scene with a root node derived from ``Control`` (for this
example plugin, we'll make the root node a ``CenterContainer``).
Select this root node, and in the viewport, click the ``Layout`` menu
and select ``Full Rect``. You also need to enable the ``Expand``
vertical size flag in the inspector.
The panel now uses all the space available in the main viewport.

Next, let's add a button to our example main screen plugin.
Add a ``Button`` node, and set the text to "Print Hello" or similar.
Add a script to the button like this:

.. tabs::
 .. code-tab:: gdscript GDScript

    @tool
    extends Button


    func _on_print_hello_pressed():
        print("Hello from the main screen plugin!")

 .. code-tab:: csharp

    using Godot;

    [Tool]
    public partial class PrintHello : Button
    {
        private void OnPrintHelloPressed()
        {
            GD.Print("Hello from the main screen plugin!");
        }
    }


Then connect the "pressed" signal to itself. If you need help with signals,
see the :ref:`doc_signals` article.

We are done with the main screen panel. Save the scene as ``main_panel.tscn``.

Update the plugin script
------------------------

We need to update the ``main_screen_plugin.gd`` script so the plugin
instances our main panel scene and places it where it needs to be.
Here is the full plugin script:

.. tabs::
 .. code-tab:: gdscript GDScript

    @tool
    extends EditorPlugin


    const MainPanel = preload("res://addons/main_screen/main_panel.tscn")

    var main_panel_instance


    func _enter_tree():
        main_panel_instance = MainPanel.instantiate()
        # Add the main panel to the editor's main viewport.
        EditorInterface.get_editor_main_screen().add_child(main_panel_instance)
        # Hide the main panel. Very much required.
        _make_visible(false)


    func _exit_tree():
        if main_panel_instance:
            main_panel_instance.queue_free()


    func _has_main_screen():
        return true


    func _make_visible(visible):
        if main_panel_instance:
            main_panel_instance.visible = visible


    func _get_plugin_name():
        return "Main Screen Plugin"


    func _get_plugin_icon():
        # Must return some kind of Texture for the icon.
        return EditorInterface.get_editor_theme().get_icon("Node", "EditorIcons")

 .. code-tab:: csharp

    #if TOOLS
    using Godot;

    [Tool]
    public partial class MainScreenPlugin : EditorPlugin
    {
        PackedScene MainPanel = ResourceLoader.Load<PackedScene>("res://addons/main_screen/main_panel.tscn");
        Control MainPanelInstance;

        public override void _EnterTree()
        {
            MainPanelInstance = (Control)MainPanel.Instantiate();
            // Add the main panel to the editor's main viewport.
            EditorInterface.GetEditorMainScreen().AddChild(MainPanelInstance);
            // Hide the main panel. Very much required.
            _MakeVisible(false);
        }

        public override void _ExitTree()
        {
            if (MainPanelInstance != null)
            {
                MainPanelInstance.QueueFree();
            }
        }

        public override bool _HasMainScreen()
        {
            return true;
        }

        public override void _MakeVisible(bool visible)
        {
            if (MainPanelInstance != null)
            {
                MainPanelInstance.Visible = visible;
            }
        }

        public override string _GetPluginName()
        {
            return "Main Screen Plugin";
        }

        public override Texture2D _GetPluginIcon()
        {
            // Must return some kind of Texture for the icon.
            return EditorInterface.GetEditorTheme().GetIcon("Node", "EditorIcons");
        }
    }
    #endif

A couple of specific lines were added. ``MainPanel`` is a constant that holds
a reference to the scene, and we instance it into `main_panel_instance`.

The ``_enter_tree()`` function is called before ``_ready()``. This is where
we instance the main panel scene, and add them as children of specific parts
of the editor. We use ``EditorInterface.get_editor_main_screen()`` to
obtain the main editor screen and add our main panel instance as a child to it.
We call the ``_make_visible(false)`` function to hide the main panel so
it doesn't compete for space when first activating the plugin.

The ``_exit_tree()`` function is called when the plugin is deactivated.
If the main screen still exists, we call ``queue_free()`` to free the
instance and remove it from memory.

The ``_make_visible()`` function is overridden to hide or show the main
panel as needed. This function is automatically called by the editor when the
user clicks on the main viewport buttons at the top of the editor.

The ``_get_plugin_name()`` and ``_get_plugin_icon()`` functions control
the displayed name and icon for the plugin's main viewport button.

Another function you can add is the ``handles()`` function, which
allows you to handle a node type, automatically focusing the main
screen when the type is selected. This is similar to how clicking
on a 3D node will automatically switch to the 3D viewport.

Try the plugin
--------------

Activate the plugin in the Project Settings. You'll observe a new button next
to 2D, 3D, Script above the main viewport. Clicking it will take you to your
new main screen plugin, and the button in the middle will print text.

If you would like to try a finished version of this plugin,
check out the plugin demos here:
https://github.com/godotengine/godot-demo-projects/tree/master/plugins

If you would like to see a more complete example of what main screen plugins
are capable of, check out the 2.5D demo projects here:
https://github.com/godotengine/godot-demo-projects/tree/master/misc/2.5d
