.. _doc_bug_triage_guidelines:

Bug triage guidelines
=====================

This page describes the typical workflow of the bug triage team aka
bugsquad when handling issues and pull requests on Godot's `GitHub <https://github.com/godotengine/godot>`_
repository. It is bound to evolve together with the bugsquad, so do not
hesitate to propose modifications to the following guidelines.

Issues management
-----------------

GitHub proposes various features to manage issues:

-  Set one or several labels from a predefined list
-  Set one milestone from a predefined list
-  Keep track of the issue in the project dashboard
-  Define one contributor as "assignee" among the Godot engine
   organization members

As the Godot engine organization on GitHub currently has a restricted
number of contributors, we do not use assignees extensively for now. All
contributors are welcome to take on any issue, if relevant after mentioning
it on the issue ticket and/or discussing the best way to resolve it with
other developers.

For the time being we do not use the project dashboard feature either.

As far as possible, we try to assign labels (and milestones, when relevant)
to both issues and pull requests.

Labels
~~~~~~

The following labels are currently defined in the Godot repository:

**Categories:**

-  *Archived*: either a duplicate of another issue, or invalid. Such an
   issue would also be closed.
-  *Bug*: describes something that is not working properly.
-  *Confirmed*: has been confirmed by at least one other contributor
   than the bug reporter (typically for *Bug* reports).
   The purpose of this label is to let developers know which issues are
   still reproducible when they want to select what to work on. It is
   therefore a good practice to add in a comment on what platform and
   what version or commit of Godot the issue could be reproduced; if a
   developer looks at the issue one year later, the *Confirmed* label
   may not be relevant anymore.
-  *Discussion*: the issue is not consensual and needs further
   discussion to define what exactly should be done to address the
   topic.
-  *Documentation*: issue related to the documentation. Mainly to request
   enhancements in the API documentation. Issues related to the ReadTheDocs
   documentation should be filed on the
   `godot-docs <https://github.com/godotengine/godot-docs>`_ repository.
-  *Enhancement*: describes a proposed enhancement to an existing
   functionality.
-  *Feature proposal*: describes a wish for a new feature to be
   implemented.
-  *Junior job*: the issue is *assumed* to be an easy one to fix, which makes
   it a great fit for junior contributors who need to become familiar with
   the code base.
-  *Needs rebase*: the issue need a Git rebase to be merged.
-  *Needs testing*: the issue/pull request could not be completely tested
   and thus need further testing. This can mean that it needs to be tested
   on different hardware/software configurations or even that the steps to
   reproduce are not certain.
-  *PR welcome / hero wanted!*: Contributions for issues with these labels are especially welcome.
   Note that this **doesn't** mean you can't work on issues without
   these labels.
-  *Tracker*: issue used to track other issues (like all issues related to
   the plugin system).
-  *Usability*: issues that directly impact user usability.

The categories are used for general triage of the issues. They can be
combined in some way when relevant, e.g. an issue can be labelled
*Enhancement* and *Usability* at the same time if it's an issue to improve
usability. Or *Feature proposal* and *Discussion* if it's a non-consensual
feature request, or one that is not precise enough to be worked on.

**Topics:**

-  *Assetlib*: relates to issues with the asset library.
-  *Audio*: relates to the audio features (low and high level).
-  *Buildsystem*: relates to building issues, either linked to the SCons
   buildsystem or to compiler peculiarities.
-  *Core*: anything related to the core engine. It might be further
   split later on as it's a pretty big topic.
-  *Drivers*: relates to issues with the drivers used by the engine.
-  *Editor*: relates to issues in the editor (mainly UI).
-  *GDNative*: relates to the GDNative module.
-  *GDScript*: relates to GDScript.
-  *Mono*: relates to the C# / Mono bindings.
-  *Network*: relates to networking.
-  *Physics*: relates to the physics engine (2D/3D).
-  *Plugin*: relates to problems encountered while writing plugins.
-  *Porting*: relates to some specific platforms.
-  *Rendering*: relates to the 2D and 3D rendering engines.
-  *VisualScript*: relates to issues with the visual scripting language.

Issues would typically correspond to only one topic, though it's not
unthinkable to see issues that fit two bills. The general idea is that
there will be specialized contributors teams behind all topics, so they
can focus on the issues labelled with their team's topic.

**Platforms:**

*Android*, *HTML5*, *iOS*, *Linux*, *macOS*, *Windows*, *UWP*

By default, it is assumed that a given issue applies to all platforms.
If one of the platform labels is used, it is then exclusive and the
previous assumption doesn't stand anymore (so if it's a bug on e.g.
Android and Linux exclusively, select those two platforms).

Milestones
~~~~~~~~~~

`Milestones <https://github.com/godotengine/godot/milestones>`_ correspond to planned future versions of Godot for which
there is an existing roadmap. Issues that fit in the said roadmap should
be filed under the corresponding milestone; if they don't correspond to
any current roadmap, they should be left without milestone. As a rule of
thumb, an issue corresponds to a given milestone if it concerns a feature
that is new in the milestone, or a critical bug that can't be accepted in any
future stable release, or anything that Juan wants to work on right now.
:)

Contributors are free to pick issues regardless of their assigned milestone;
if a fix is proposed for a bug that was not deemed urgent and thus without
milestone, it would likely still be very welcome.
