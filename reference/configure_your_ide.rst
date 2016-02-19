.. _doc_configure_your_ide:

Configure an IDE
================

Eclipse
-------

TODO.

QtCreator
---------

Importing the project
^^^^^^^^^^^^^^^^^^^^^

* Choose *New Project* -> *Import Project* -> *Import Existing Project*.
* Set the path to your Godot root directory and enter the project name.
* Here you can choose which folders and files will be visible to the project. C/C++ files
  are added automatically. Potentially useful additions: *.py for buildsystem files, *.java for Android development,
  *.mm for OSX. Click "Next".
* Click *Finish*.

Build and run
^^^^^^^^^^^^^
Build configuration:

* Click on *Projects* and open the *Build* tab.
* Delete the pre-defined **make** build step.
* Click *Add Build Step* -> *Custom Process Step*.
* Type **scons** in the *Command* field.
* Fill the *Arguments* field with your compilation options. (e.g.: ``p=x11 target=debug -j 4``)

Run configuration:

* Open the *Run* tab.
* Point the *Executable* to your compiled Godot binary.
* If you want to run a specific game or project, point *Working directory* to the game directory.
* If you want to run the editor, add **-e** to the *Command line arguments* field.

Other editors (vim, emacs, Atom...)
-----------------------------------

TODO.
