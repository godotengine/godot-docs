.. _doc_exporting_for_windows:

Exporting for Windows
=====================

The simplest way to distribute a game for PC is to copy the executable
(``godot.exe``), compress the folder and send it to someone else. However, this
is often not desired.

Godot offers a more elegant approach for PC distribution when using the export
system. When exporting for Windows, the exporter takes all the project files and
creates a ``data.pck`` file. This file is bundled with a specially optimized
binary that is smaller, faster and does not contain the editor and debugger.

Requirements
------------

-  To enable code signing, you must have the ``Windows 10 SDK`` (on Windows) or `osslsigncode <https://github.com/mtrojnar/osslsigncode>`__ (on any other OS) installed.
-  Download the Godot export templates. Use the Godot menu: ``Editor > Manage Export Templates``.

.. warning::

    If you export for Windows with embedded PCK files, you will not be able to
    sign the program as it will break.

    On Windows, PCK embedding is also known to cause false positives in
    antivirus programs. Therefore, it's recommended to avoid using it unless
    you're distributing your project via Steam as it bypasses code signing and
    antivirus checks.
