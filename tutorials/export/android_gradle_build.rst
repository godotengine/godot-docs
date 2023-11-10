.. _doc_android_gradle_build:

Gradle builds for Android
=========================

Godot provides the option to build using the gradle buildsystem. Instead of
using the already pre-built template that ships with Godot, an Android
Java project gets installed into your project folder. Godot will then build it
and use it as an export template every time you export the project.

There are some reasons why you may want to do this:

* Modify the project before it's built.
* Add external SDKs that build with your project.

Configuring the gradle build is a fairly straightforward process. But first
you need to follow the steps in :ref:`exporting for android<doc_exporting_for_android>`
up to **Setting it up in Godot**. After doing that, follow the steps below.

Set up the gradle build environment
-----------------------------------

Go to the Project menu, and install the *Gradle Build* template:

.. image:: img/gradle_build_install_template.webp

Make sure export templates are downloaded. If not, this menu will help you
download them.

A Gradle-based Android project will be created under ``res://android/build``.
Editing these files is not needed unless you really need to modify the project.


Enabling the gradle build and exporting
---------------------------------------

When setting up the Android project in the **Project > Export** dialog,
**Gradle Build** needs to be enabled:

.. image:: img/gradle_build_enable.webp

From now on, attempting to export the project or one-click deploy will call the
`Gradle <https://gradle.org/>`__ build system to generate fresh templates (this
window will appear every time):

.. image:: img/gradle_build_gradle.webp

The templates built will be used automatically afterwards, so no further
configuration is needed.

.. note::

    When using the gradle Android build system, assets that are placed within a
    folder whose name begins with an underscore will not be included in the
    generated APK. This does not apply to assets whose *file* name begins with
    an underscore.

    For example, ``_example/image.png`` will **not** be included as an asset,
    but ``_image.png`` will.
