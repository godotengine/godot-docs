.. _doc_changing_application_icon_for_windows:

Changing application icon for windows
=====================================

By default, the exported game icon will be the Godot icon. Most likely you will want to change that for your game. There are two types of icons that can be changed: the file icon and the taskbar icon.

Changing the taskbar icon
-------------------------

The taskbar icon is the icon that shows up on the taskbar when your game is running.

.. image:: img/icon_taskbar_icon.png

To change the taskbar icon, go to Project>Project Settings>Application>Config>Icon. Click on the folder icon and select your desired icon.

.. note:: This is also the icon that gets displayed in the Godot project list.

.. image:: img/icon_project_settings.png

Changing the file icon
----------------------

The file icon is the icon of the executable that you click on to start the game.

.. image:: img/icon_file_icon.png

Before selecting it in the export options, you will need to install an extra tool called **rcedit**.
You can download it here:
https://github.com/electron/rcedit/releases

After downloading, you need to tell Godot the path to the **rcedit** executable on your computer. Go to Editor>Editor Settings>Export>Windows. Click on the folder icon for the **rcedit** entry. Navigate to and select the **rcedit** exectuable.

.. note:: For Linux users, you will also need to install wine in order to use rcedit. For more information, check https://www.winehq.org/

.. image:: img/icon_rcedit.png

Now you have everything ready for changing the file icon. To do that, you will need to specify the icon when exporting. Go to Project>Export. Assuming you have a windows deskop preset ready, in the options, under Application, you will find Icon, select your desired image in ICO format as your file icon.

.. note:: To export an ICO image, you can use GIMP. For more details, please refer to this tutorial: http://skyboygames.com/easily-create-a-windows-app-icon-with-gimp/

.. seealso:: Check the documentation for more info about exporting.

.. image:: img/icon_export_settings.png


Testing the result
------------------

You can now export the game and see whether you have change the icons successfully or not.
If everything works fine, you will see this.

.. image:: img/icon_result.png

Icon (ICO) file requirements
----------------------------

Regardless of which program you use to create your ICO file, there are some requirements to ensure the icon (and your executable) works on Windows.

This is a bit tricky, as can be seen in the following StackOverflow threads: `one <https://stackoverflow.com/questions/3236115/which-icon-sizes-should-my-windows-applications-icon-include>`__, `two <https://stackoverflow.com/questions/40749785/windows-10-all-icon-resolutions-on-all-dpi-settings-format-pixel-art-as-icon>`__.

Your ICO file should at least contain icons in the following resolutions: 16x16, 48x48 and 256x256.
They should also be uncompressed. The 256x256 icon *can* be compressed, but this breaks backwards compatibility with Windows XP.

If you want to fully support high-DPI screens, this is the full list of supported icon sizes on Windows 10:
16, 20, 24, 28, 30, 31, 32, 40, 42, 47, 48, 56, 60, 63, 84 and one larger than 255px. (I.e. 256 or 512 or 1024)

Note that for high-DPI compression may be used, also they should be using 24bpp mode in contrast to the lower resolutions.
