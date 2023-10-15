.. _doc_one-click_deploy:

One-click deploy
================

What is one-click deploy?
-------------------------

One-click deploy is a feature that is available once a platform is properly
configured and a supported device is connected to the computer. Since things can
go wrong at many levels (platform may not be configured correctly, SDK may be
incorrectly installed, device may be improperly configured, etc.), it's good to
let the user know that it exists.

After adding an Android export preset marked as Runnable, Godot can detect when
a USB device is connected to the computer and offer the user to automatically
export, install and run the project (in debug mode) on the device. This feature
is called *one-click deploy*.

.. note::

   One-click deploy is only available once you've added an export template
   marked as **Runnable** in the Export dialog. You can mark several export
   presets as runnable, but only one preset per platform may be marked as
   runnable. If you mark a second preset in a given platform as runnable, the
   other preset will no longer be marked as runnable.

Supported platforms
-------------------

- **Android:** Exports the project with debugging enabled and runs it on the
  connected device.

   - Make sure to follow the steps described in :ref:`doc_exporting_for_android`.
     Otherwise, the one-click deploy button won't appear.

   - If you have more than one device connected, Godot will ask you which device
     the project should be exported to.

- **HTML5:** Starts a local web server and runs the exported project by opening
  the default web browser.

Support for more platforms such as iOS is planned.

Using one-click deploy
----------------------

- If deploying to Android, enable developer mode on your mobile device
  then enable USB debugging in the device's settings.
- After enabling USB debugging, connect the device to your PC using an USB cable.

   - For advanced users, it should also be possible to use wireless ADB.

- Make sure there is an export preset marked as **Runnable** for the target
  platform (Android or HTML5).
- If everything is configured correctly and with no errors, platform-specific
  icons will appear in the top-right corner of the editor.
- Click the button to export to the desired platform in one click.

.. image:: img/remote_debug.webp

.. _doc_one-click_deploy_troubleshooting:

Troubleshooting
---------------

Android
^^^^^^^

If you can't see the device in the list of devices when running the
``adb devices`` command in a terminal, it will not be visible by Godot either.
To resolve this:

- Check if USB debugging is enabled *and authorized on the device*.
  Try unlocking your device and accepting the authorization prompt if you see any.
  If you can't see this prompt, running ``adb devices`` on your PC should make
  the authorization prompt appear on the device.
- Try `revoking the debugging authorization <https://stackoverflow.com/questions/23081263/adb-android-device-unauthorized>`__
  in the device's developer settings, then follow the steps again.
- Try using USB debugging instead of wireless debugging or vice versa.
  Sometimes, one of those can work better than the other.
- On Linux, you may be missing the required
  `udev rules <https://github.com/M0Rf30/android-udev-rules>`__
  for your device to be recognized.
