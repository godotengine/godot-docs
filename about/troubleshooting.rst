.. _doc_troubleshooting:

Troubleshooting
===============

This page lists common issues encountered when using Godot and possible solutions.

.. seealso::

    See :ref:`doc_using_the_web_editor` for caveats specific to the HTML5 version
    of the Godot editor.

Everything I do in the editor or project manager appears delayed by one frame
-----------------------------------------------------------------------------

This is a `known bug <https://github.com/godotengine/godot/issues/23069>`__ on
Intel graphics drivers on Windows. Updating to the latest graphics driver
version *provided by Intel* should fix the issue.

You should use the graphics driver provided by Intel rather than the one
provided by your desktop or laptop's manufacturer because their version is often
outdated.

The grid disappears and meshes turn black when I rotate the 3D camera in the editor
-----------------------------------------------------------------------------------

This is a `known bug <https://github.com/godotengine/godot/issues/30330>`__ on
Intel graphics drivers on Windows.

The only workaround, for now, is to switch to the GLES2 renderer. You can switch
the renderer in the top-right corner of the editor or the Project Settings.

If you use a computer allowing you to switch your graphics card, like NVIDIA
Optimus, you can use the dedicated graphics card to run Godot.

The editor or project takes a very long time to start
-----------------------------------------------------

This is a `known bug <https://github.com/godotengine/godot/issues/20566>`__ on
Windows when you have specific USB peripherals connected. In particular,
Corsair's iCUE software seems to cause the bug. Try updating your USB
peripherals' drivers to their latest version. If the bug persists, you need to
disconnect the faulty peripherals before opening the editor. You can then
connect the peripheral again.

Editor tooltips in the Inspector and Node docks blink when they're displayed
----------------------------------------------------------------------------

This is a `known issue <https://github.com/godotengine/godot/issues/32990>`__
caused by the third-party Stardock Fences application on Windows.
The only known workaround is to disable Stardock Fences while using Godot.

The Godot editor appears frozen after clicking the system console
-----------------------------------------------------------------

When running Godot on Windows with the system console enabled, you can
accidentally enable *selection mode* by clicking inside the command window. This
Windows-specific behavior pauses the application to let you select text inside
the system console. Godot cannot override this system-specific behavior.

To solve this, select the system console window and press Enter to leave
selection mode.

Some text such as "NO DC" appears in the top-left corner of the project manager and editor window
-------------------------------------------------------------------------------------------------

This is caused by the NVIDIA graphics driver injecting an overlay to display information.

To disable this overlay on Windows, restore your graphics driver settings to the
default values in the NVIDIA Control Panel.

To disable this overlay on Linux, open ``nvidia-settings``, go to **X Screen 0 >
OpenGL Settings** then uncheck **Enable Graphics API Visual Indicator**.

The project window appears blurry, unlike the editor
----------------------------------------------------

Unlike the editor, the project isn't marked as DPI-aware by default. This is
done to improve performance, especially on integrated graphics, where rendering
3D scenes in hiDPI is slow.

To resolve this, open **Project > Project Settings** and enable **Display >
Window > Dpi > Allow Hidpi**. On top of that, make sure your project is
configured to support :ref:`multiple resolutions <doc_multiple_resolutions>`.

The project window doesn't appear centered when I run the project
-----------------------------------------------------------------

This is a `known bug <https://github.com/godotengine/godot/issues/13017>`__. To
resolve this, open **Project > Project Settings** and enable **Display > Window
> Dpi > Allow Hidpi**. On top of that, make sure your project is configured to
support :ref:`multiple resolutions <doc_multiple_resolutions>`.

The editor or project appears to have washed out colors
-------------------------------------------------------

On Windows, this is usually caused by incorrect OS or monitor settings, as Godot
currently does not support :abbr:`HDR (High Dynamic Range)` *output*
(even though it may internally render in HDR).

As `most displays are not designed to display SDR content in HDR mode <https://tftcentral.co.uk/articles/heres-why-you-should-only-enable-hdr-mode-on-your-pc-when-you-are-viewing-hdr-content>`__,
it is recommended to disable HDR in the Windows settings when not running applications
that use HDR output. On Windows 11, this can be done by pressing
:kbd:`Windows + Alt + B` (this shortcut is part of the Xbox Game Bar app).
To toggle HDR automatically based on applications currently running, you can use
`AutoActions <https://github.com/Codectory/AutoActions>`__.

If you insist on leaving HDR enabled, it is possible to somewhat improve the
result by ensuring the display is configured to use :abbr:`HGIG (HDR Gaming Interest Group)`
tonemapping (as opposed to :abbr:`DTM (Dynamic Tone Mapping)`), then
`using the Windows HDR calibration app <https://support.microsoft.com/en-us/windows/calibrate-your-hdr-display-using-the-windows-hdr-calibration-app-f30f4809-3369-43e4-9b02-9eabebd23f19>`__.
It is also strongly recommended to use Windows 11 instead of Windows 10 when using HDR.
The end result will still likely be inferior to disabling HDR on the display, though.

Support for HDR *output* is planned in a future release.

The editor/project freezes or displays glitched visuals after resuming the PC from suspend
------------------------------------------------------------------------------------------

This is a known issue on Linux with NVIDIA graphics when using the proprietary
driver. There is no definitive fix yet, as suspend on Linux + NVIDIA is often
buggy when OpenGL is involved.

The NVIDIA driver offers an *experimental*
`option to preserve video memory after suspend <https://wiki.archlinux.org/title/NVIDIA/Tips_and_tricks#Preserve_video_memory_after_suspend>`__
which may resolve this issue. This option has been reported to work better with
more recent NVIDIA driver versions.

To avoid losing work, save scenes in the editor before putting the PC to sleep.

The project works when run from the editor, but fails to load some files when running from an exported copy
-----------------------------------------------------------------------------------------------------------

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
