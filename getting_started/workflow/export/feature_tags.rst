.. _doc_feature_tags:

Feature Tags
============

Introduction
------------

Godot has a special system to tag availability of features. Each *feature* is represented
as a string, and it can refer to many of the following:

* Platform name.
* Platform bits (64/32).
* Platform type (desktop/mobile).
* Supported texture compression in platform.
* Whether a build is debug or release.
* Many more things.

Features can be queried in run-time to the singleton API by calling:

::

	OS.has_feature(name)


Default features
----------------

Here is a list of most feature tags in Godot. Keep in mind they are *case sensitive*:

+-----------------+--------------------------------------------------------+
| **Feature Tag** | **Description**                                        |
+=================+========================================================+
| **Android**     | Running on Android                                     |
+-----------------+--------------------------------------------------------+
| **JavaScript**  | Running on JavaScript (HTML5)                          |
+-----------------+--------------------------------------------------------+
| **OSX**         | Running on macOS                                       |
+-----------------+--------------------------------------------------------+
| **iOS**         | Running on iOS                                         |
+-----------------+--------------------------------------------------------+
| **UWP**         | Running on UWB                                         |
+-----------------+--------------------------------------------------------+
| **Windows**     | Running on Windows                                     |
+-----------------+--------------------------------------------------------+
| **X11**         | Running on X11                                         |
+-----------------+--------------------------------------------------------+
| **debug**       | Running on debug build                                 |
+-----------------+--------------------------------------------------------+
| **release**     | Running on release build                               |
+-----------------+--------------------------------------------------------+
| **32**          | Running on 32-bit build                                |
+-----------------+--------------------------------------------------------+
| **64**          | Running on 64-bit build                                |
+-----------------+--------------------------------------------------------+
| **mobile**      | Host OS is a mobile platform                           |
+-----------------+--------------------------------------------------------+
| **pc**          | Host OS is a PC platform (desktop/laptop)              |
+-----------------+--------------------------------------------------------+
| **web**         | Hot OS is a Web browser                                |
+-----------------+--------------------------------------------------------+
| **etc**         | Textures using ETC1 compression are supported          |
+-----------------+--------------------------------------------------------+
| **etc2**        | Textures using ETC2 compression are supported          |
+-----------------+--------------------------------------------------------+
| **s3tc**        | Textures using S3TC (DXT/BC) compression are supported |
+-----------------+--------------------------------------------------------+
| **pvrtc**       | Textures using PVRTC compression are supported         |
+-----------------+--------------------------------------------------------+

Custom features
---------------

It is possible to add custom features to a build, just use the relevant
field in the *export preset** used to generate it:

.. image:: img/feature_tags1.png

Overriding project settings
---------------------------

Features can be used to override specific configuration values in the *Project Settings*.
This allows to better customize any configuration when doing a build.

In the following example, a different icon is added for the demo build of the game (which was
customized in a special export preset which, in turn, includes only demo levels).

.. image:: img/feature_tags2.png

After overriding, a new field is added for this specific configuration:

.. image:: img/feature_tags3.png

Default overrides
-----------------

There are already a lot of settings that come with overrides by default, they can be found
in many sections of the project settings.

.. image:: img/feature_tags4.png

Customizing Build
------------------

Feature tags can be used to customize a build process too, by writing a custom **ExportPlugin**.
They also are used to specify which shared library is loaded and exported in **GDNative**.
