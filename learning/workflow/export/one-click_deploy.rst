.. _doc_one-click_deploy:

One-click deploy
================

Sounds good, what is it?
------------------------

This feature will pop up automatically once a platform is properly
configured and a supported device is connected to the computer. Since
things can go wrong at many levels (platform may not be configured
correctly, SDK may incorrectly installed, device may be improperly
configured, kitty ate the USB cable, etc.), it's good to let the user
know that it exists.

Some platforms (at the time of this writing, only Android and Blackberry
10) can detect when a USB device is connected to the computer, and offer
the user to automatically export, install and run the project (in debug
mode) on the device. This feature is called, in industry buzz-words,
"One Click Deploy" (though, it's technically two clicks...).

Steps for one-click deploy
--------------------------

#. Configure target platform.
#. Configure device (make sure it's in developer mode, likes the
   computer, usb is recognized, usb cable is plugged, etc.).
#. Connect the device..
#. And voila!

.. image:: /img/oneclick.png

Click once.. and deploy!
