.. _doc_changing_applicationIcon_for_windows:

Changing applciation icon for windows
==========================================

By default, the exported game icon will be the godot icon, most likely you will like to change the icon for your game. There are two types of icon that can be changed, the file icon and the taskbar icon.


Changing the taskbar icon
----------------------------------
The taskbar icon is the icon that show on the taskbar when your game is running.

.. image:: img/icon_taskbar_icon.png

To change the taskbar icon, go to Project>Project Settings>Application>Config>Icon. Click on the folder icon and select your desired icon that will show up in the taskbar.

.. note:: This is also the icon you are viewing in the Godot project list.

.. image:: img/icon_project_settings.png

Changing the file icon
----------------------------------
The file icon is the icon that you click on to start the game.

.. image:: img/icon_file_icon.png

Before selecting it in the export options, you will need to install an extra tool called rcedit.
You can download it here:
https://github.com/electron/rcedit/releases

After downloading, you need to tell godot the path of rcedit on your computer. Go to Editor>Editor Settings>Export>Windows. Select the rcedit exectuable by clicking the folder icon in the rcedit entry.

.. note:: For linux users, you will also need to install wine in order to use rcedit. For more information, check https://www.winehq.org/

.. image:: img/icon_rcedit.png

Now you have everything ready for changing the file icon. To change the file icon, you will need to specify the icon when exporting. Go to Project>Export. Asumming you have a windows deskop preset ready, in the options, under Application, you will find Icon, select your desired image in ICO format as your file icon.

.. note::
Check the documentation for more info about exporting

.. image:: img/icon_export_settings.png


Testing the result
------------------------------
You can now export the game and see whether you have change the icons sucessfully or not.
If everything works fine, you will see this.

.. image:: img/icon_result.png

 
