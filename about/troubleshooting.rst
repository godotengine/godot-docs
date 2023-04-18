.. _doc_troubleshooting:

Troubleshooting
===============

This page lists common issues encountered when using Godot and possible solutions.

.. seealso::

    See :ref:`doc_using_the_web_editor` for caveats specific to the Web version
    of the Godot editor.

The editor runs slowly and uses all my CPU and GPU resources, making my computer noisy
--------------------------------------------------------------------------------------

This is a known issue, especially on macOS since most Macs have Retina displays.
Due to Retina displays' higher pixel density, everything has to be rendered at a
higher resolution. This increases the load on the GPU and decreases perceived
performance.

There are several ways to improve performance and battery life:

- In 3D, click the **Perspective** button in the top left corner and enable
  **Half Resolution**. The 3D viewport will now be rendered at half resolution,
  which can be up to 4 times faster.
- Open the Editor Settings and increase the value of **Low Processor Mode Sleep (µsec)**
  to ``33000`` (30 FPS). This value determines the amount of *microseconds*
  between frames to render. Higher values will make the editor feel less reactive
  but will help decrease CPU and GPU usage significantly.
- If you have a node that causes the editor to redraw continuously (such as
  particles), hide it and show it using a script in the ``_ready()`` method.
  This way, it will be hidden in the editor but will still be visible in the
  running project.

The editor stutters and flickers on my variable refresh rate monitor (G-Sync/FreeSync)
--------------------------------------------------------------------------------------

This is a `known issue <https://github.com/godotengine/godot/issues/38219>`__.
Variable refresh rate monitors need to adjust their gamma curves continuously to
emit a consistent amount of light over time. This can cause flicker to appear in
dark areas of the image when the refresh rate varies a lot, which occurs as
the Godot editor only redraws when necessary.

There are several workarounds for this:

- Enable **Interface > Editor > Update Continuously** in the Editor Settings. Keep in mind
  this will increase power usage and heat/noise emissions since the editor will
  now be rendering constantly, even if nothing has changed on screen. To
  alleviate this, you can increase **Low Processor Mode Sleep (µsec)** to
  ``33000`` (30 FPS) in the Editor Settings. This value determines the amount of
  *microseconds* between frames to render. Higher values will make the editor
  feel less reactive but will help decrease CPU and GPU usage significantly.
- Alternatively, disable variable refresh rate on your monitor or in the graphics driver.
- VRR flicker can be reduced on some displays using the **VRR Control** or
  **Fine Tune Dark Areas** options in your monitor's OSD. These options may
  increase input lag or result in crushed blacks.
- If using an OLED display, use the **Black (OLED)** editor theme preset in the
  Editor Settings. This hides VRR flicker thanks to OLED's perfect black levels.

The editor or project takes a very long time to start
-----------------------------------------------------

When using one of the Vulkan-based renderers (Forward+ or Forward Mobile),
the first startup is expected to be relatively long. This is because shaders
need to be compiled before they can be cached. Shaders also need to be cached
again after updating Godot, after updating graphics drivers or after switching
graphics cards.

If the issue persists after the first startup, this is a
`known bug <https://github.com/godotengine/godot/issues/20566>`__ on
Windows when you have specific USB peripherals connected. In particular,
Corsair's iCUE software seems to cause this bug. Try updating your USB
peripherals' drivers to their latest version. If the bug persists, you need to
disconnect the specific peripheral before opening the editor. You can then
connect the peripheral again.

The Godot editor appears frozen after clicking the system console
-----------------------------------------------------------------

When running Godot on Windows with the system console enabled, you can
accidentally enable *selection mode* by clicking inside the command window. This
Windows-specific behavior pauses the application to let you select text inside
the system console. Godot cannot override this system-specific behavior.

To solve this, select the system console window and press Enter to leave
selection mode.

Some text such as "NO DC" appears in the top-left corner of the Project Manager and editor window
-------------------------------------------------------------------------------------------------

This is caused by the NVIDIA graphics driver injecting an overlay to display information.

To disable this overlay on Windows, restore your graphics driver settings to the
default values in the NVIDIA Control Panel.

To disable this overlay on Linux, open ``nvidia-settings``, go to **X Screen 0 >
OpenGL Settings** then uncheck **Enable Graphics API Visual Indicator**.

The project works when run from the editor, but fails to load some files when running from an exported copy
-----------------------------------------------------------------------------------------------------------

This is usually caused by forgetting to specify a filter for non-resource files
in the Export dialog. By default, Godot will only include actual *resources*
into the PCK file. Some files commonly used, such as JSON files, are not
considered resources. For example, if you load ``test.json`` in the exported
project, you need to specify ``*.json`` in the non-resource export filter. See
:ref:`doc_exporting_projects_export_mode` for more information.

Also, note that files and folders whose names begin with a period will never be
included in the exported project. This is done to prevent version control
folders like ``.git`` from being included in the exported PCK file.

On Windows, this can also be due to :ref:`case sensitivity
<doc_project_organization_case_sensitivity>` issues. If you reference a resource
in your script with a different case than on the filesystem, loading will fail
once you export the project. This is because the virtual PCK filesystem is
case-sensitive, while Windows's filesystem is case-insensitive by default.
