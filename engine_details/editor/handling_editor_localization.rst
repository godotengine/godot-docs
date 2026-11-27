.. _doc_handling_editor_localization:

Handling editor localization
============================

The editor localization effort has two goals: every relevant string can be
translated, and the editor language can be switched without restarting the
editor. Achieving both requires more than wrapping strings in a translation
function, because the editor has to know which strings change at runtime.

Editor translations are extracted from the source code by RegEx-based scripts
(`godot-editor-l10n <https://github.com/godotengine/godot-editor-l10n/tree/main/scripts>`__),
so every translateable string has to be marked in some way.

Because the scripts run on raw source code, they parse strings anywhere they
appear, including inside comments. This can be used deliberately to extract
strings that don't exist verbatim in the code, for example a string that is
capitalized from a raw name. The scripts do not support concatenated strings:
``TTR("Hello " + "world")`` is not extracted correctly, and has to be split into
``TTR("Hello ") + TTR("world")``. Unquoted arguments such as ``TTR(variable)``
are not extracted, but using translation functions on them is still allowed and
may be relevant.

Relevant strings include almost anything displayed in the GUI. Strings shown
only in the console or the output log should not be translated, which mostly
applies to error messages.

Static strings
--------------

For most static strings, use the ``TTRC`` macro. It is a no-op macro that marks
a string for extraction, and it only supports static string literals, such as
``TTRC("Update")``. The string is extracted by the extraction script, and once
translations are synced and filled in on Weblate, the auto-translation system
shows the localized string automatically when a language is selected.

``TTRC`` applies when all of the following are true:

- The string is static, i.e. it is a singular string literal and not part of a
  larger compound string built with ``vformat()`` or concatenation.
- The displayed text has auto-translation enabled. This can be controlled by
  the ``auto_translate_mode`` property of :ref:`Node <class_Node>`, as well as
  granular auto-translation in various :ref:`Control <class_Control>` nodes
  such as :ref:`ItemList <class_ItemList>` items.
- The string is not a property name or a documentation string.

``TTRC`` is also usable in the first two cases. Its main purpose is to mark a
string as translateable without modifying it, so the raw string can be
translated later with ``TTR``. The following is acceptable:

.. code-block:: cpp

    String string1 = TTRC("Hello");
    String string2 = TTRC("world");
    label->set_text(TTR(string1) + " " + TTR(string2));

Such constructs are rarely needed, and they have to be refreshed manually like
dynamic strings.

Dynamic strings
---------------

For dynamic strings, use the ``TTR`` function. It translates the given string in
place, but the string is not subject to auto-translation and has to be
refreshed manually on ``NOTIFICATION_TRANSLATION_CHANGED``.

``TTR`` applies when:

- The string is constructed dynamically, e.g.
  ``vformat(TTR("%d pieces"), n_of_pieces)`` or
  ``TTR("Hello") + "\n" + TTR("world")``.
- The displayed text is not auto-translated, which includes nodes whose
  ``auto_translate_mode`` is disabled, and text drawn with ``draw_string()``.

The following should always use ``TTR`` even when ``TTRC`` could technically
apply, because these strings can be either static or dynamic but are displayed
by the same GUI element:

- Undo and redo action names.
- Editor toaster messages.

Refreshing dynamic strings
--------------------------

Dynamic strings have to be refreshed manually: whenever
``NOTIFICATION_TRANSLATION_CHANGED`` is received, the text has to be updated to
the new language. This is usually done by re-assigning all affected strings.

Because the notification is received automatically when the node enters the
tree, the string should not be assigned in the constructor as well, to avoid
duplication:

.. code-block:: cpp

    // Wrong: assigned twice.
    MyNode::MyNode() {
        button = memnew(Button);
        button->set_tooltip_text(TTR("Press to do stuff.") + "\n" + TTR("Shift+Press to do other stuff."));
    }

    void MyNode::_notification(int p_what) {
        if (p_what == NOTIFICATION_TRANSLATION_CHANGED) {
            button->set_tooltip_text(TTR("Press to do stuff.") + "\n" + TTR("Shift+Press to do other stuff."));
        }
    }

In this case the tooltip should only be assigned in the notification handler.

Some updates involve a more complex tree update that should not happen
immediately. Such updates can be guarded with ``is_ready()``:

.. code-block:: cpp

    void MyNode::_notification(int p_what) {
        if (p_what == NOTIFICATION_TRANSLATION_CHANGED) {
            if (is_ready()) {
                _update_tree();
            }
        }
    }

Transient messages are an exception to auto-refresh. Error dialogs, for
example, are exclusive, so the editor language cannot be changed while their
text is displayed and it usually does not matter whether the string is static or
dynamic. This only applies to dialogs that set their text right before showing,
most notably ``EditorNode::show_warning()``.

Plurals
-------

When a string includes a counter, consider using plural messages with ``TTRN``:

.. code-block:: cpp

    TTRN("%d step", "%d steps", step_count)

Such strings are dynamic and need to be refreshed manually.

For messages without a counter, e.g. "Node moved." versus "Nodes moved.", do not
use ``TTRN``. Either use the dedicated ``TPL`` macro, which is a ternary
operator:

.. code-block:: cpp

    text = TPL(nodes.size(), TTRC("Node moved."), TTRC("Nodes moved."));

or make the message "universal", such as ``TTRC("Node(s) moved.")``. The first
form is preferred, because universal messages are not viable for all languages.

Translation-friendly strings
----------------------------

A translateable string should only include the part that is relevant for
translation, together with the full context. For example:

- ``vformat(TTR("%s somethings"), sth_counter)`` is preferred over
  ``itos(sth_counter) + TTR(" somethings")``.
- ``TTR("First line.") + "\n" + TTR("Second line.")`` is preferred over
  ``TTRC("First line.\nSecond line.")``, especially when the separate lines are
  reused in other strings.
- Trailing whitespace should be removed, so ``TTR("Node list:") + " "`` is
  preferred over ``TTRC("Node list: ")``.

Note that in some cases a more friendly string means the string has to be
dynamic.

Auto-translate mode
-------------------

Most nodes that display text support auto-translation, and in many cases that
auto-translation is granular. For example the auto-translate mode of a
:ref:`Button <class_Button>` and of its tooltip can be set separately. This is
useful to make some strings static while another part of the same node is
dynamic or has auto-translation disabled. Typical cases include:

- A button whose text should not be translated but whose tooltip should be.
- A :ref:`Tree <class_Tree>` or :ref:`ItemList <class_ItemList>` that displays
  some items that should be translated and some that should not. In this case
  the node's own auto-translate mode applies to the majority of the items, while
  other items are set individually.

Auto-translate mode should be disabled in these cases:

- The text is a class name, e.g. "Node2D". This does not apply to text that
  includes a class name, e.g. "This is a Node2D.".
- The text displays custom strings such as group names or node names.
- The text is a proper name, e.g. "Godot".

Ideally a displayed dynamic string should also have auto-translate disabled.
Otherwise the engine translates the string twice, first for the dynamic string
and then for auto-translation, which will fail. This is harmless, so it is not
strictly followed.

Runtime strings
---------------

Some editor strings are included in runtime code, most notably configuration
warnings. For those, ``RTR`` and ``RTRN`` are the runtime equivalents of ``TTR``
and ``TTRN``.

The runtime equivalent of ``TTRC`` is ``ETR``, but it should only be used for
text displayed by the node itself, especially text that can also be displayed
outside the editor context, i.e. at runtime. :ref:`FileDialog <class_FileDialog>`
labels are an example. ``ETR`` strings are extracted into a separate translation
domain, which can be included in Template Generation for translations. There is
no dynamic equivalent of ``ETR``; use ``atr(ETR())`` for that.

Properties
----------

Most property names are extracted automatically from the registration methods of
``ClassDB``. Some dynamic properties are not registered, and should use
``PNAME``. This includes properties added with ``_get_property_list()``:

.. code-block:: cpp

    p_list->push_back(PropertyInfo(Variant::INT, vformat("%s/%d/%s", PNAME("args"), i, PNAME("type"))));

and properties registered with ``PropertyListHelper``:

.. code-block:: cpp

    base_property_helper.register_property(PropertyInfo(Variant::STRING, PNAME("name"), PROPERTY_HINT_NONE, "", PROPERTY_USAGE_NO_EDITOR), defaults.name, &MeshLibrary::set_item_name, &MeshLibrary::get_item_name);

.. note::

    This may change, based on how
    `godotengine/godot#123364 <https://github.com/godotengine/godot/pull/123364>`__
    is handled.

Strings displayed as a section in the inspector also need ``PNAME`` when the
string is part of a hint:

.. code-block:: cpp

    ADD_PROPERTY(PropertyInfo(Variant::INT, "input_port_count", PROPERTY_HINT_NONE, "", PROPERTY_USAGE_DEFAULT | PROPERTY_USAGE_ARRAY, String(PNAME("Input Ports")) + ",input_port_,swap_method=move_input_port,add_button_text=" + String(TTRC("Add Port"))), "set_input_port_count", "get_input_port_count");

While ``PNAME`` is like ``TTRC``, they are not interchangeable. ``PNAME``
strings are extracted into a separate translation domain, which is used when
localized properties and settings are enabled.

``GNAME`` extracts dynamic property groups:

.. code-block:: cpp

    p_list->push_back(PropertyInfo(Variant::NIL, GNAME("Terrains", ""), PROPERTY_HINT_NONE, "", PROPERTY_USAGE_GROUP));

Documentation strings
---------------------

Documentation has its own separate translation domain. Documentation strings are
marked and translated with ``DTR`` and ``DTRN``. This is only useful for text
that pulls from the documentation, such as tooltips, or strings that should be
extracted as part of the documentation.
