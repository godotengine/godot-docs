.. _doc_external_editor:

Using an external text editor
==============================

Godot can be used with an external text editor, such as Sublime Text or Visual Studio Code. To select an external text editor via the Godot editor menu:
``Editor -> Editor Settings -> Text Editor -> External``

.. image:: img/editor_settings.png

There are two fields: the executable path and command line flags. The flags
allow you to better integrate the editor with Godot. Godot will replace the
following inside the flags parameter:

+---------------------+-----------------------------------------------------+
| Field in Exec Flags | Is replaced with                                    |
+=====================+=====================================================+
| {project}           | The absolute path to the project directory          |
+---------------------+-----------------------------------------------------+
| {file}              | The absolute path to the file                       |
+---------------------+-----------------------------------------------------+
| {col}               | The column number of the error                      |
+---------------------+-----------------------------------------------------+
| {line}              | The line number of the error                        |
+---------------------+-----------------------------------------------------+

Some example Exec Flags for various editors include:

+---------------------+-----------------------------------------------------+
| Editor              | Exec Flags                                          |
+=====================+=====================================================+
| Geany/Kate          | {file} -\-line {line} -\-column {col}               |
+---------------------+-----------------------------------------------------+
| Atom/Sublime Text   | {file}:{line}                                       |
+---------------------+-----------------------------------------------------+
| JetBrains Rider     | -\-line {line} {file}                               |
+---------------------+-----------------------------------------------------+
| Visual Studio Code  | {project} -\-goto {file}:{line}:{col}               |
+---------------------+-----------------------------------------------------+

.. note:: For Visual Studio Code you will have to point to the "code.cmd" file.
