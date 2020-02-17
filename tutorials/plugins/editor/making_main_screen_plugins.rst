.. _doc_making_main_screen_plugins:

Making main screen plugins
==========================

What this tutorial covers
-------------------------

As seen in the :ref:`doc_making_plugins` page, making a basic plugin that
extends the editor is fairly easy. This plugin mechanism also allows you to
create new UIs in the central part of the editor, similarly to the basic 2D, 3D,
Script and AssetLib views. Such editor plugins are referred as "Main screen
plugins".

This tutorial leads you through the creation of a basic main screen plugin. With 
this plugin example, we want to demonstrate:

- Creating a main screen plugin
- Linking the main screen to another plugin GUI element (such as a Tab panel,
  similar to the Inspector tab)

For the sake of simplicity, the two GUI elements of our main screen plugin will
both consist in a Label and a Button. Pressing one element's button will display
some text on the other's label node.

Initializing the plugin
-----------------------

The plugin itself is a Godot project. It is best to set its contents in an
``addons/my_plugin_name/`` structure. The only files that lie in the root folder
are the project.godot file, and the project icon.

In the ``addons/my_plugin_name/`` folder, we create the ``plugin.cfg`` file as
described in the :ref:`doc_making_plugins` page.

::

    [plugin]
    name="Main screen plugin demo"
    description="A plugin that adds a main screen panel and a side-panel which communicate with each other."
    author="Your Name Here"
    version="1.0.0"
    script="main_screen_plugin.gd"

We also initialize the file targeted by the ``script=`` property of the ``.cfg``
file. In our example, ``main_screen_plugin.gd``.

::

    tool
    extends EditorPlugin

    func _enter_tree():
       pass

    func _exit_tree():
       pass

    func has_main_screen():
       return true

    func make_visible(visible):
       pass

    func get_plugin_name():
       return "Main Screen Plugin"

The important part in this script is the ``has_main_screen()`` function, which is
overloaded so it returns ``true``. This function is automatically called by the
editor on plugin activation, to tell it that this plugin adds a new center view to
the editor. For now, we'll leave this script as-is and we'll come back to it
later.

Scenes
------

The ``main_screen_plugin.gd`` file will be responsible for each of our plugin's
UI element instantiation, and it will also manage the communication between them.

As a matter of fact, we wish to design each UI element in their own scene.
Different scenes are not aware of each other unless they are both children of a
parent scene, yet they will then require ``get_node("../sibling")`` accessors.
Such practice is more likely to produce errors at runtime, especially if these
scenes do not share the same parent node. This is why, they should only be
allowed to access their children.

So, in order to communicate information to another scene, the best design is to
define signals. If a user action in a UI scene #1 has to trigger something in
another UI scene #2, then this user action has to emit a signal from scene #1,
and scene #2 will be connected to that signal. Since all of our UI scenes will
be instanced by ``main_screen_plugin.gd`` script, this one script will also
connect each of them to the required signals.

.. note:: If the ``main_screen_plugin.gd`` instantiates the UI scenes, won't
          they be sibling nodes then?

Not necessarily: this script may add all UI scenes as children of the same node
of the editor's scene tree - but maybe it won't. And the ``main_screen_plugin.gd``
script will *not* be the parent node of any instantiated scene because it is a
script, not a node! This script will only hold references to instantiated
scenes.

Main screen scene
-----------------

Create a new scene with a ``Panel`` root node. Select this root node,
and in the viewport, click the ``Layout`` menu and select ``Full Rect``.
You also need to enable the ``Expand`` vertical size flag in the inspector.
The panel now uses all the space available in the viewport.
Now, let's add a new script on the root node. Name it ``main_panel.gd``.

We then add 2 children to this Panel node: first a ``Button`` node. Place it
anywhere on the Panel. Then add a ``Label`` node.

Now we need to define a behaviour when this button is pressed. This is covered
by the :ref:`Handling a signal <doc_scripting_handling_a_signal>` page, so this
part will not be described in details in this tutorial.
Select the Button node and click the ``Node`` side dock.
Select the ``pressed()`` signal and click the ``Connect`` button (you can also
double-click the ``pressed()`` signal instead). In the window that opened,
select the Panel node (we will centralize all behaviors in its attached
script). Keep the default function name, make sure that the ``Make function``
toggle is ON and hit ``Connect``. This creates an ``_on_Button_pressed()``
function in the ``main_panel.gd`` script, that will be called every time the
button is pressed.

As the button gets pressed, we want the side-panel's ``Label`` node to show a
specific text. As explained above, we cannot directly access the target scene,
so we'll emit a signal instead. The ``main_screen_plugin.gd`` script will then
connect this signal to the target scene. Let's continue in the ``main_panel.gd``
script:

::

    tool
    extends Panel

    signal main_button_pressed(value)

    func _on_Button_pressed():
       emit_signal("main_button_pressed", "Hello from main screen!")

In the same way, this main scene's Label node has to show a value when it
receives a specific signal. Let's create a new
``_on_side_button_pressed(text_to_show)`` function for this purpose:

::

    func _on_side_button_pressed(text_to_show):
       $Label.text = text_to_show

We are done for the main screen panel. Save the scene as ``main_panel.tscn``.

Tabbed panel scene
------------------

The tabbed panel scene is almost identical to the main panel scene. You can
either duplicate the ``main_panel.tscn`` file and name the new file
``side_panel.tscn``, or re-create it from a new scene by following the previous
section again. However, you will have to create a new script and attach it to
the Panel root node. Save it as ``side_panel.gd``. Its content is slightly
different, as the signal emitted and the target function have different names.
Here is the script's full content:

::

    tool
    extends Panel

    signal side_button_pressed(value)

    func _on_Button_pressed():
       emit_signal("side_button_pressed", "Hello from side panel!")

    func _on_main_button_pressed(text_to_show):
       $Label.text = text_to_show

Connecting the two scenes in the plugin script
----------------------------------------------

We now need to update the ``main_screen_plugin.gd`` script so the plugin
instances our 2 GUI scenes and places them at the right places in the editor.
Here is the full ``main.gd``:

::

    tool
    extends EditorPlugin

    const MainPanel = preload("res://addons/my_plugin_name/main_panel.tscn")
    const SidePanel = preload("res://addons/my_plugin_name/side_panel.tscn")

    var main_panel_instance
    var side_panel_instance

    func _enter_tree():
       main_panel_instance = MainPanel.instance()
       side_panel_instance = SidePanel.instance()

       # Add the main panel to the editor's main viewport.
       get_editor_interface().get_editor_viewport().add_child(main_panel_instance)

       # Add the side panel to the Upper Left (UL) dock slot of the left part of the editor.
       # The editor has 4 dock slots (UL, UR, BL, BR) on each side (left/right) of the main screen.
       add_control_to_dock(DOCK_SLOT_LEFT_UL, side_panel_instance)

       # Hide the main panel
       make_visible(false)

    func _exit_tree():
       main_panel_instance.queue_free()
       side_panel_instance.queue_free()

    func _ready():
       main_panel_instance.connect("main_button_pressed", side_panel_instance, "_on_main_button_pressed")
       side_panel_instance.connect("side_button_pressed", main_panel_instance, "_on_side_button_pressed")

    func has_main_screen():
       return true

    func make_visible(visible):
       if visible:
          main_panel_instance.show()
       else:
          main_panel_instance.hide()

    func get_plugin_name():
       return "Main Screen Plugin"

A couple of specific lines were added. First, we defined the constants that
contain our 2 GUI packed scenes (``MainPanel`` and ``SidePanel``). We will use
these resources to instance both scenes.

The ``_enter_tree()`` function is called before ``_ready()``. This is where we
actually instance the 2 GUI scenes, and add them as children of specific parts
of the editor. The side panel case is similar to the example shown in
:ref:`doc_making_plugins` page: we add the scene in an editor dock. We specified
it will be placed in the left-side dock, upper-left tab.

``EditorPlugin`` class does not provide any function to add an element in the
main viewport. We thus have to use the
``get_editor_interface().get_editor_viewport()`` to obtain this viewport and add
our main panel instance as a child to it. We call the ``make_visible(false)``
function to hide the main panel so it is not directly shown when first
activating the plugin.

The ``_exit_tree()`` is pretty straightforward. It is automatically called when
the plugin is deactivated. It is then important to ``queue_free()`` the elements
previously instanced to preserve memory. If you don't, the elements will
effectively be invisible in the editor, but they will remain present in the
memory. Multiple de-activations/re-activations will then increase memory usage
without any way to free it, which is not good.

Finally the ``make_visible()`` function is overridden to hide or show the main
panel as needed. This function is automatically called by the editor when the
user clicks on another main viewport button such as 2D, 3D or Script.

Try the plugin
--------------

Activate the plugin in the Project Settings. You'll observe a new button next to
2D, 3D, Script above the main viewport. You'll also notice a new tab in the left
dock. Try to click the buttons in both side and main panels: events are emitted
and caught by the corresponding target scene to change the Label caption inside it.
