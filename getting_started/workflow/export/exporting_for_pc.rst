.. _doc_exporting_for_pc:

Exporting for PC
================

The simplest way to distribute a game for PC is to copy the executables
(``godot.exe`` on Windows, ``godot`` on the rest), compress the folder
and send it to someone else. However, this is often not desired.

Godot offers a more elegant approach for PC distribution when using the
export system. When exporting for PC (Linux, Windows, macOS), the exporter
takes all the project files and creates a ``data.pck`` file. This file is
bundled with a specially optimized binary that is smaller, faster and
does not contain the editor and debugger.
