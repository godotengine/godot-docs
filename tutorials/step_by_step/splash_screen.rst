:: _doc_splash_screen:

Splash screen
=============

Tutorial
--------

This will be a simple tutorial to cement the basic idea of how the GUI
subsystem works. The goal will be to create a really simple, static,
splash screen.

Following is a file with the assets that will be used:

attachment:robisplash\_assets.zip

Setting Up
----------

Create a scene with screen resolution 800x450, and set it up like this:

.. image:: /img/robisplashscene.png

.. image:: /img/robisplashpreview.png

The nodes 'background" and "logo" are of
`TextureFrame <https://github.com/okamstudio/godot/wiki/class_textureframe>`__
type. These have a special property for setting the texture to be
displayed, just load the corresponding file.

.. image:: /img/texframe.png

The node "start" is a
`TextureButton <https://github.com/okamstudio/godot/wiki/class_texturebutton>`__,
it takes several images for different states, but only the normal and
pressed will be supplied in this example:

.. image:: /img/texbutton.png

Finally, the node "copyright" is a
`Label <https://github.com/okamstudio/godot/wiki/class_label>`__. Labels
can be set a custom font by editing the following property:

.. image:: /img/label.png

As a side note, the font was imported from a TTF, there is a [[Importing
Fonts]] for importing fonts.



