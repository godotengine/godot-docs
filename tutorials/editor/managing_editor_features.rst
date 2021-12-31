.. _doc_managing_editor_features:

Managing Editor Features
========================

Introduction
------------

In certain situations it may be desirable to limit what features can be used
in the Godot editor. For example, a UI designer on a team who doesn't need to
see 3D features, or an educator slowly introducing features to students. Godot
has a built in system called "feature profiles" to do this.

With feature profiles major features and nodes can be hidden from the editor.
As this is not removing features from the editor projects with hidden features
or nodes will not break. This also means feature profiles are not an
optimization technique. For information on how to optimize Godot see
:ref:`_doc_performance`.

Creating a profile
------------------

To manage editor features go to **Editor > Manage Editor Features**. This
will open the **Manage Editor Feature Profiles** window. By default there
will be no profile. Click on **Create Profile** and give it a name. Now
that there is a profile there will be a list of all the features in the Godot
editor.

..img:: img/configure_profile.png

The first section allows major editor features to be removed. Such as the 3D
editor or scripting editor. Below the main features is every class and node in
Godot, which can be disabled as well. Click on a node and all of its properties
and options will be listed in the **Extra Items** box, these can all be
individually disabled.

..img:: img/node_features.png

Sharing a profile
-----------------

To share profiles between editors click on the **Export** button. Save the custom
profile somewhere as a ``.profile`` file. To use this in another editor open that
editors **Manage Editor Feature Profiles** window and click import, then select the
``.profile`` file.

This process is potentially cumbersome however if a large amount of computers need
custom profiles. As an alternative self contained mode for Godot can be enabled,
the necessary profiles can be created, then the editor with those profiles can be put
on different computers.

To enabled self contained mode create a file called ._sc_ or _sc_ in the same directory
as the editor binary. This will make Godot write all user data to a directory named
editor_data/ in the same directory as the editor binary. This makes Godot a "portable"
application, which can then be placed on an USB drive and copied to other computers.
