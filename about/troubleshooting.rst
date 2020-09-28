.. _doc_troubleshooting:

Troubleshooting
===============

This page lists common issues encountered when using Godot and possible solutions.

Everything I do in the editor or project manager appears delayed by one frame.
------------------------------------------------------------------------------

This is a `known bug <https://github.com/godotengine/godot/issues/23069>`__ on
Intel graphics drivers on Windows. Updating to the latest graphics driver
version *provided by Intel* should fix the issue.

You should use the graphics driver provided by Intel rather than the one
provided by your desktop or laptop's manufacturer because their version is often
outdated.

The grid disappears and meshes turn black when I rotate the 3D camera in the editor.
------------------------------------------------------------------------------------

This is a `known bug <https://github.com/godotengine/godot/issues/30330>`__ on
Intel graphics drivers on Windows.

The only workaround, for now, is to switch to the GLES2 renderer. You can switch
the renderer in the top-right corner of the editor or the Project Settings.

If you use a computer allowing you to switch your graphics card, like NVIDIA
Optimus, you can use the dedicated graphics card to run Godot.

The editor or project takes a very long time to start.
------------------------------------------------------

This is a `known bug <https://github.com/godotengine/godot/issues/20566>`__ on
Windows when you have specific USB peripherals connected. In particular,
Corsair's iCUE software seems to cause the bug. Try updating your USB
peripherals' drivers to their latest version. If the bug persists, you need to
disconnect the faulty peripherals before opening the editor. You can then
connect the peripheral again.

The Godot editor appears frozen after clicking the system console.
------------------------------------------------------------------

When running Godot on Windows with the system console enabled, you can
accidentally enable *selection mode* by clicking inside the command window. This
Windows-specific behavior pauses the application to let you select text inside
the system console. Godot cannot override this system-specific behavior.

To solve this, select the system console window and press Enter to leave
selection mode.

The project window appears blurry, unlike the editor.
-----------------------------------------------------

Unlike the editor, the project isn't marked as DPI-aware by default. This is
done to improve performance, especially on integrated graphics, where rendering
3D scenes in hiDPI is slow.

To resolve this, open **Project > Project Settings** and enable **Display >
Window > Dpi > Allow Hidpi**. On top of that, make sure your project is
configured to support :ref:`multiple resolutions <doc_multiple_resolutions>`.

The project window doesn't appear centered when I run the project.
------------------------------------------------------------------

This is a `known bug <https://github.com/godotengine/godot/issues/13017>`__. To
resolve this, open **Project > Project Settings** and enable **Display > Window
> Dpi > Allow Hidpi**. On top of that, make sure your project is configured to
support :ref:`multiple resolutions <doc_multiple_resolutions>`.

The project works when run from the editor, but fails to load some files when running from an exported copy.
------------------------------------------------------------------------------------------------------------

This is usually caused by forgetting to specify a filter for non-resource files
in the Export dialog. By default, Godot will only include actual *resources*
into the PCK file. Some files commonly used, such as JSON files, are not
considered resources. For example, if you load ``test.json`` in the exported
project, you need to specify ``*.json`` in the non-resource export filter. See
:ref:`doc_exporting_projects_export_mode` for more information.

On Windows, this can also be due to :ref:`case sensitivity
<doc_project_organization_case_sensitivity>` issues. If you reference a resource
in your script with a different case than on the filesystem, loading will fail
once you export the project. This is because the virtual PCK filesystem is
case-sensitive, while Windows's filesystem is case-insensitive by default.
