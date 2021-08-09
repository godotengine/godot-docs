.. _doc_gui_skinning:

GUI skinning
============

Themes
------

All control nodes are skinned through the :ref:`Theme <class_Theme>`
resource. Theme contains all the information required to change the
entire visual styling of all controls. 

A Theme can be applied to any control node in the scene. As a result,
all children and grand-children controls will use that same theme, too
(unless another theme is specified further down the tree). If a value is
not found in a theme, it will be searched in themes higher up in the
hierarchy, towards the root. If nothing was found, the default theme is
used. This system allows for flexible overriding of themes in complex
user interfaces.

.. attention::
   
   Don't use the custom theme option in the Project Settings, as there
   are known bugs with theme propagation. Instead, apply your theme to the
   root Control node's Theme property. It will propagate to instanced scenes
   automatically. To get correct theming in the editor for instanced scenes,
   you can apply the theme resource to the instanced scene's root node as well.

Creating a theme
----------------

Themes can be created from any control node. Select a control node in the scene
hierarchy, then in the inspector go to the theme property. From there you can
select **New Theme**.

.. image:: img/new_theme.png

This will create an empty theme and open up the theme editor.

.. image:: img/theme_editor.png

In the theme editor you can customize everything about a theme except for
the default font the theme uses. That can only be customized in the inspector under
the selected theme.

.. image:: img/default_font.png

Theme items
-----------

In the theme editor, next to the default preview window, is where you make changes
to your theme. Clicking the plus button opens the **Add item Type** menu.

.. image:: img/add_item_type.png

From here select the control node you want your theme to modify and click **Ok**. You
should now see theme items for that node in the theme editor. Theme items are what defines
the look of a theme, each kind of item in a theme can be:

-  **Color**: A single color, with or without transparency. Colors are
   usually applied to fonts and icons.
-  **Constant**: A single numerical constant. Generally used
   to define spacing between components or alignment.
-  **Font**: Every control that uses text can be assigned the fonts
   used to draw strings.
-  **Icon**: A single image. Textures are not often used, but when
   they are, they represent handles to pick or icons in a complex control
   (such as a file dialog).
-  **StyleBox**: Stylebox is a resource that defines how to draw a
   panel in varying sizes (more information on them later).

Every item is associated with:

-  A name (the name of the item)
-  A Control (the name of the control)

To customize a theme item click on the plus sign next to it. Your theme
will now override the default theme for that item. To modify it click on **Empty**,
then select the new theme item you want to create. Click on it again and you can
now modify it in the inspector.

.. image:: img/theme_item_inspector.png

You can also add custom theme items to a control node under the built in theme items.

In the theme editor, above the theme items, is the **Show Default** toggle. It will hide
or show any theme items that are using the default theme settings. Next to it is the
**Override Defaults** button, which will override the default theme for all theme items
of the currently selected control node.

Manage theme Items
------------------

Clicking the **Manage Items** button brings up the Manage theme items menu. In
the edit items tab you can view all the theme items for your theme, add a custom
theme item, or a custom control node type.

.. image:: img/manage_items.png

You can also mass delete theme items from here. **Remove Class Items** will remove
all built in theme items you have customized for the control node. **Remove Custom
Items** will remove all the custom theme items for the selected node. And **Remove
All Items** will remove everything. 

From the **Import Items** tab you can import theme items from other themes. You can
import items from the default Godot theme, the Godot editor theme, or another custom
theme. You can import all of the theme items for a control node or only one. You need
to select **Data** when importing to actually import the theme item. Otherwise your
theme will just have a blank override for that theme option.

.. image:: img/import_items.png

Preview
-------

The **Default Preview** tab of the theme editor shows you how every control node in
Godot will look with your theme settings applied. If you haven't applied a setting
then the default theme setting will be used.

.. image:: img/default_preview.png

You can also preview how other scenes will look by clicking the **Add Preview** button
and selecting a tscn file that has a control node as the root node.

.. image:: img/scene_preview.png

Theme overrides
---------------

If only a few controls need to be skinned, it is often not necessary to
create a new theme. Controls offer their theme items as special kinds
of properties. If checked, overriding will take place:

.. image:: img/themecheck.png

As can be seen in the image above, theme items have little check boxes.
If checked, they can be used to override the value of the theme just for
that control.

Changing themes with code
-------------------------

In addition to the theme editor it is possible to change theme items with
code, here is an example:

.. tabs::
 .. code-tab:: gdscript GDScript

    var theme = Theme.new()
    theme.set_color("font_color", "Label", Color.red)

    var label = Label.new()
    label.theme = theme

 .. code-tab:: csharp

    var theme = new Theme();
    theme.SetColor("fontColor", "Label", new Color(1.0f, 0.0f, 0.0f));

    var label = new Label();
    label.Theme = theme;

In the example above, a new theme is created. The "font_color" option
is changed and then applied to a label. Therefore, the label's text (and all
children and grandchildren labels) will be red.

It is possible to override those options without using the theme
directly, and only for a specific control, by using the override API in
:ref:`Control.add_color_override() <class_Control_method_add_color_override>`:

.. tabs::
 .. code-tab:: gdscript GDScript

    var label = Label.new()
    label.add_color_override("font_color", Color.red)

 .. code-tab:: csharp

    var label = new Label();
    label.AddColorOverride("fontColor", new Color(1.0f, 0.0f, 0.0f));

In the inline help of Godot (in the Script tab), you can check which theme items
are overridable, or check the :ref:`Control <class_Control>` class reference.
