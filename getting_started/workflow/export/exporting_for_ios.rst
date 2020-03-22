.. _doc_exporting_for_ios:

Exporting for iOS
=================

These are the steps to load a Godot project in Xcode. This allows you to
build and deploy to an iOS device, build a release for the App Store, and
do everything else you can normally do with Xcode.

Requirements
------------

-  You must export for iOS from a computer running macOS with Xcode installed.
-  Download the Godot export templates. Use the Godot menu: Editor > Manage Export Templates

Export a Godot project to Xcode
-------------------------------

In the Godot editor, open the **Export** window from the **Project** menu. When the
Export window opens, click **Add..** and select **iOS**.

The following export options are required. Leaving any blank will cause the
exporter to throw an error:

  * In the **Application** category
    * **App Store Team ID** and (Bundle) **Identifier**
  * Everything in the **Required Icons** category
  * Everything in the **Landscape Launch Screens** category
  * Everything in the **Portrait Launch Screens** category

After you click **Export Project**, there are still two important options left:

  * **Path** is an empty folder that will contain the exported Xcode project files.
  * **File** will be the name of the Xcode project and several project specific files and directories.

.. image:: img/ios_export_file.png

.. note:: This tutorial uses **exported_xcode_project_name**, but you will use your
          project's name. When you see **exported_xcode_project_name**
          in the following steps, replace it with the name you used instead.

.. note:: Avoid using spaces when you choose your **exported_xcode_project_name** as
          this can lead to corruption in your XCode project file.

When the export completes, the output folder should look like this:

.. image:: img/ios_export_output.png

Opening **exported_xcode_project_name.xcodeproj** lets you build and deploy
like any other iOS app.

Active development considerations
---------------------------------

The above method creates an exported project that you can build for
release, but you have to re-export every time you make a change in Godot.

While developing, you can speed this process up by linking your
Godot project files directly into your app.

In the following example:

  * **exported_xcode_project_name** is the name of the exported iOS application (as above).
  * **godot_project_to_export** is the name of the Godot project.

Steps to link a Godot project folder to Xcode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Start from an exported iOS project (follow the steps above).
2. In Finder, drag the Godot project folder into the Xcode file browser.

.. image:: img/ios_export_add_dir.png

3. In the dialog, make sure **Create folder references** is selected. This means
you will be able to continue to edit your Godot project in its current location.

.. image:: img/ios_export_file_ref.png

4. See the **godot_project_to_export** folder in the Xcode file browser.
5. Delete **exported_xcode_project_name.pck** from the Xcode project.

.. image:: img/ios_export_delete_pck.png

6. Open **exported_xcode_project_name-Info.plist** and add a string property named
**godot_path** (this is the real key name) with a value **godot_project_to_export**
(this is the name of your project)

.. image:: img/ios_export_set_path.png

That's it! You can now edit your project in the Godot editor and build it
in Xcode when you want to run it on a device.

Services for iOS
----------------

Special iOS services can be used in Godot. Check out the
:ref:`doc_services_for_ios` page.
