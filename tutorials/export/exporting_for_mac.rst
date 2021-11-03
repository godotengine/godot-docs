.. _doc_exporting_for_mac:

Exporting for macOS
===================

macOS apps are exported as an ``.app`` bundle, a folder with a specific structure which stores the executable, libraries and all the project files.
This bundle is packed in a ZIP archive or DMG disk image (only supported when exporting for macOS).

Requirements
------------

-  To enable code signing and notarization, you must export from a computer running macOS with Xcode command line tools installed.
-  Download the Godot export templates. Use the Godot menu: ``Editor > Manage Export Templates``.

.. warning::

    Projects exported without code signing and notarization will be blocked by Gatekeeper if they are downloaded from unknown sources, see the :ref:`Running Godot apps on macOS <doc_running_on_mac>` page for more info.

Code signing and notarization
-----------------------------

By default, macOS will run only applications that are signed and notarized, if you use any other signing configuration see :ref:`Running Godot apps on macOS <doc_running_on_mac>` for workarounds.

To notarize an app you mast have a valid `Apple Developer ID Certificate <https://developer.apple.com/>`__.

If you have an Apple Developer ID Certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Enable ``Code Signing``, ``Notarization``, ``Hardened Runtime`` and ``Timestamp`` and disable the ``Debug`` entitlement.
- Provide valid Apple ID credentials and certificate identity.

If ``Notarization`` is enabled, Godot will automatically upload the exported project for notarization.

You can use the ``xcrun notarytool history`` command to check notarization status and use the ``xcrun notarytool log {ID}`` command to download the notarization log.

If you encounter notarization issues, see `Resolving common notarization issues <https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution/resolving_common_notarization_issues>`__ for more info.

After notarization is completed, `staple the ticket <https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution/customizing_the_notarization_workflow>`__ to the exported project.

If you do not have an Apple Developer ID Certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Keep ``Code Signing`` enabled and leave the ``Identity`` option empty, in this case Godot will use a ad-hoc signature, which will make running an exported app easier for the end users.

Signing Options
~~~~~~~~~~~~~~~

+------------------------------+---------------------------------------------------------------------------------------------------+
| Option                       | Description                                                                                       |
+==============================+===================================================================================================+
| Enable                       | Enables code signing.                                                                             |
+------------------------------+---------------------------------------------------------------------------------------------------+
| Identity                     | The "Full Name" or "Common Name" of the signing identity, store in the macOS key chain. [1]_      |
+------------------------------+---------------------------------------------------------------------------------------------------+
| Timestamp                    | Requests a timestamp server to authenticate the time of signing. Required for notarization.       |
+------------------------------+---------------------------------------------------------------------------------------------------+
| Hardened Runtime             | Enables "Hardened Runtime". Required for notarization.                                            |
+------------------------------+---------------------------------------------------------------------------------------------------+
| Replace Existing Signature   | Replaces existing signatures of the GDNative libraries and embedded helper executables.           |
+------------------------------+---------------------------------------------------------------------------------------------------+

.. note::

    To notarize an app, you must enable the ``Hardened Runtime`` and ``Timestamp``.

.. [1] Leave ``Identity`` option empty to use ad-hoc signature.

Notarization Options
~~~~~~~~~~~~~~~~~~~~

+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option             | Description                                                                                                                                                                  |
+====================+==============================================================================================================================================================================+
| Enable             | Enables automatic upload for notarization.                                                                                                                                   |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Apple ID Name      | Apple ID account name (email address)                                                                                                                                        |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Apple ID Password  | Apple ID app-specific password. See `Using app-specific passwords <https://support.apple.com/en-us/HT204397>`__ to enable two-factor authentication and create app password. |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Apple Team ID      | Team ID if your Apple ID belongs to multiple teams                                                                                                                           |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

See `Notarizing macOS Software Before Distribution <https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution?language=objc>`__ for more info.

Entitlements
------------

Hardened Runtime Entitlements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hardened Runtime entitlements manage security options and resource access policy.
See `Hardened Runtime <https://developer.apple.com/documentation/security/hardened_runtime?language=objc>`__ for more info.

+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Entitlement                           | Description                                                                                                                                                                                      |
+=======================================+==================================================================================================================================================================================================+
| Allow JIT Code Execution [2]_         | Allows creating writable and executable memory for JIT code. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation.             |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Allow Unsigned Executable Memory [2]_ | Allows creating writable and executable memory without JIT restrictions. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation. |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Allow DYLD Environment Variables [2]_ | Allows app to uss dynamic linker environment variables to inject code.  f you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation.   |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Disable Library Validation            | Allows app to load arbitrary libraries and frameworks. Enabled it if you are using GDNative add-ons and ad-hoc signature, or want to support user-provided external add-ons.                     |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Audio Input                           | Enable if you need to use the microphone or other audio input sources, if it's enabled you should also provide usage message in the `privacy/microphone_usage_description` option.               |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Camera                                | Enable if you need to use the camera, if it's enabled you should also provide usage message in the `privacy/camera_usage_description` option.                                                    |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Location                              | Enable if you need to use location information from Location Services, if it's enabled you should also provide usage message in the `privacy/location_usage_description` option.                 |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Address Book                          | [3]_ Enable to allow access contacts in the user's address book, if it's enabled you should also provide usage message in the `privacy/address_book_usage_description` option.                   |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Calendars                             | [3]_ Enable to allow access to the user's calendar, if it's enabled you should also provide usage message in the `privacy/calendar_usage_description` option.                                    |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Photo Library                         | [3]_ Enable to allow access to the user's Photos library, if it's enabled you should also provide usage message in the `privacy/photos_library_usage_description` option.                        |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Apple Events                          | [3]_ Enable to allow app to send Apple events to other apps.                                                                                                                                     |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Debugging                             | [4]_ You can temporarily enable this entitlement to use native debugger (GDB, LLDB) with the exported app. This entitlement should be disabled for production export.                            |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. [2] The ``Allow JIT Code Execution``, ``Allow Unsigned Executable Memory`` and ``Allow DYLD Environment Variables`` entitlements are always enabled for the Godot Mono exports, and are not visible in the export options.
.. [3] These features aren't supported by Godot out of the box, enable them only if you are using add-ons which require them.
.. [4] To notarize an app, you must disable the ``Debugging`` entitlement.

App Sandbox Entitlement
~~~~~~~~~~~~~~~~~~~~~~~

The App Sandbox restricts access to user data, networking and devices.
Sandboxed apps can't access most of the file system, can't use custom file dialogs and execute binaries (using ``OS.execute`` and ``OS.create_process``) outside the ``.app`` bundle.
See `App Sandbox <https://developer.apple.com/documentation/security/app_sandbox?language=objc>`__ for more info.

.. note::

    To distribute an app through the App Store, you must enable the App Sandbox.

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Entitlement                       | Description                                                                                                                          |
+===================================+======================================================================================================================================+
| Enabled                           | Enables App Sandbox.                                                                                                                 |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Network Server                    | Enable to allow app to listen for incoming network connections.                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Network Client                    | Enable to allow app to establish outgoing network connections.                                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Device USB                        | Enable to allow app to interact with USB devices. This entitlement is required to use wired controllers.                             |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Device Bluetooth                  | Enable to allow app to interact with Bluetooth devices. This entitlement is required to use wireless controllers.                    |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Files Downloads [5]_              | Allows read or write access to the user's "Downloads" folder.                                                                        |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Files Pictures [5]_               | Allows read or write access to the user's "Pictures" folder.                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Files Music [5]_                  | Allows read or write access to the user's "Music" folder.                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Files Movies [5]_                 | Allows read or write access to the user's "Movies" folder.                                                                           |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Files User Selected [5]_          | Allows read or write access to arbitrary folder. To gain access, a folder must be selected from the native file dialog by the user.  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Helper Executable                 | List of helper executables to embedded to the app bundle. Sandboxed app are limited to execute only these executable.                |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+

.. [5] You can optionally provide usage messages for various folders in the `privacy/*_folder_usage_description` options.

You can override default entitlements by selecting custom entitlements file, in this case all other entitlement are ignored.
