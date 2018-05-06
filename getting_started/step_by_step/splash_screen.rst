.. _doc_splash_screen:

Splash screen
=============

Tutorial
--------

This is a simple tutorial to establish the basic idea of how the GUI
subsystem works. The goal is to create a simple, static
splash screen.

.. image:: img/robisplash_result.png

Following is a file with the assets that will be used. The extracted files can
be placed directly in your project folder and Godot will import them automatically.

:download:`robisplash_assets.zip <files/robisplash_assets.zip>`.

Setting up
----------

Set the display resolution to 800x450 in Project Settings, and set up a new scene like this:

.. image:: img/robisplash_scene.png

The nodes "background" and "logo" are of :ref:`TextureRect <class_TextureRect>`
type. To display an image, drag the corresponding asset to the texture property.

.. image:: img/robisplash_background_inspector.png

The node "start" is a :ref:`TextureButton <class_TextureButton>`.
It takes several images for different states, but only the normal and
pressed will be supplied in this example:

.. image:: img/robisplash_button_inspector.png

Finally, the node "copyright" is a :ref:`Label <class_Label>`.

Your final scene should look something like this.

.. image:: img/robisplash_editor.png

Go ahead and run the project.  If you're satisfied with the results, continue to
the next tutorial.
