.. _doc_configure_your_ide:

Configure an IDE
================
We assume you've already `cloned <https://github.com/godotengine/godot>`_ and `compiled <_compiling.rst>`_ Godot.

Kdevelop
--------
Is a free, open source IDE (Integrated Development Environment) for Linux, Solaris, FreeBSD, Mac OS X and other Unix flavors.

You can find a video tutorial `here <https://www.youtube.com/watch?v=yNVoWQi9TJA>`_. or you may follow this text version tutorial.

Okay so start by openning Kdevelop and choosing open project.

.. image:: /img/kdevelop_newproject.png

Choose the directory where you cloned Godot.

.. image:: /img/kdevelop_openproject.png

For the build system, choose custom build system.

.. image:: /img/kdevelop_custombuild.png

Now that the project has been imported, open the project configuration.

.. image:: /img/kdevelop_openconfig.png

Add the following includes/imports:

* . (a dot to indicate the root of the Godot project)
* core/
* core/os/
* core/math/
* tools/
* drivers/
* platform/x11/ (Make that platform/osx/ is you're using OS X)

.. image:: /img/kdevelop_addincludes.png

Apply the changes then switch to the Custom Buildsystem tab. Leave the build directory blank. Enable build tools and add 'scons' as the executable and add 'platform=x11 target=debug' ('platform=osx' if you're on OS X)

.. image:: /img/kdevelop_buildconfig.png

Next we need to tell kdevelop where to find the binary. so from the run menu choose Configure Launches.

.. image:: /img/kdevelop_configlaunches.png

Add new if you none exists. And then add the path to your executable in the executable section. Your executable should be located in the bin/ sub-directory and should be named something like: 'godot.x11.tools.64' (the name could be different depending on your platform and depending on your build options).

.. image:: /img/kdevelop_configlaunches2.png

That's it! Now you should be good to go :)


Eclipse
-------

TODO.

QtCreator
---------

TODO.

Other editors (vim, emacs, Atom...)
-----------------------------------

TODO.
