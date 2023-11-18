.. _doc_bug_triage_guidelines:

Bug triage guidelines
=====================

This page describes the typical workflow of the bug triage team aka
bugsquad when handling issues and pull requests on Godot's
`GitHub repository <https://github.com/godotengine/godot>`__.
It is bound to evolve together with the bugsquad, so do not
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

For the time being, we do not use the project dashboard feature either.

As far as possible, we try to assign labels (and milestones, when relevant)
to both issues and pull requests.

Labels
~~~~~~

The following labels are currently defined in the Godot repository:

**Categories:**

-  *Archived*: either a duplicate of another issue, or invalid. Such an
   issue would also be closed.
-  *Breaks compat*: describes something that can only be fixed by breaking
   compatibility with existing projects.
-  *Bug*: describes something that is not working properly.
-  *Cherrypick*: describes something that can be backported to a stable branch
   after being merged in the ``master`` branch.
-  *Confirmed*: has been confirmed by at least one other contributor
   than the bug reporter (typically for *Bug* reports).
   The purpose of this label is to let developers know which issues are
   still reproducible when they want to select what to work on. It is
   therefore a good practice to add in a comment on what platform and
   what version or commit of Godot the issue could be reproduced; if a
   developer looks at the issue one year later, the *Confirmed* label
   may not be relevant anymore.
-  *Crash:* describes a bug that causes the engine to crash.
   This label is only used for "hard" crashes, not freezes.
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
   implemented. Note that the main Godot repository no longer accepts
   feature requests. Please use
   `godot-proposals <https://github.com/godotengine/godot-proposals>`__ instead.
-  *For PR meeting*: the issue needs to be discussed in a pull request meeting.
   These meetings are public and are held on the `Godot Contributors Chat <https://chat.godotengine.org/>`_.
-  *Good first issue*: the issue is *assumed* to be an easy one to fix, which makes
   it a great fit for new contributors who want to become familiar with
   the code base. It should be removed while an active PR is available, that
   resolves this issue.
-  *High priority:* the issue is particularly important as it can
   prevent people from releasing their projects or cause data loss.
-  *Needs testing*: the issue/pull request could not be completely tested
   and thus need further testing. This can mean that it needs to be tested
   on different hardware/software configurations or even that the steps to
   reproduce are not certain.
-  *Needs work*: the pull request needs additional work before it can be merged.
-  *Performance*: issues that directly impact engine or editor performance.
   Can also be used for pull requests that improve performance or add low-end-friendly options.
   Should not be coupled with *Usability*.
-  *Production*: Relates to the production team.
-  *Regression*: the bug appeared after a stable release not exhibiting
   the bug was released.
-  *Salvageable*: the pull request can't be merged due to design issues or
   merge conflicts and its author is not active anymore. However, it can still
   be picked up by an external contributor to bring it to a mergeable state.
   To do so, you need to open a new pull request based on the original pull request.
-  *Tracker*: issue used to track other issues (like all issues related to
   the plugin system).
-  *Usability*: issues that directly impact user usability. Should not be coupled with *Performance*.

The categories are used for general triage of the issues. They can be
combined in some way when relevant, e.g. an issue can be labelled
*Enhancement* and *Usability* at the same time if it's an issue to improve
usability. Or *Feature proposal* and *Discussion* if it's a non-consensual
feature request, or one that is not precise enough to be worked on.
At least one of the categories *Bug*, *Enhancement* or *Discussion* is used to
describe an issue or pull request.

**Topics:**

-  *2D*: relates to 2D-specific issues. Should be coupled with one of the labels below, and should not be coupled with *3D*.
-  *3D*: relates to 3D-specific issues. Should be coupled with one of the labels below, and should not be coupled with *2D*.
-  *Animation*: relates to the Animation system, editors and importers.
-  *Assetlib*: relates to issues with the asset library.
-  *Audio*: relates to the audio features (low and high level).
-  *Buildsystem*: relates to building issues, either linked to the SCons
   buildsystem or to compiler peculiarities.
-  *Codestyle*: relates to the programming style used within the codebase.
-  *Core*: anything related to the core engine. Specific topics are split off separately as they crop up.
-  *Dotnet*: relates to the C# / Dotnet bindings.
-  *Editor*: relates to issues in the editor (mainly UI).
-  *Export*: relates to the export system and templates.
-  *GDExtension*: relates to the GDExtension system for native extensions.
-  *GDScript*: relates to GDScript.
-  *GUI*: relates to GUI (Control) nodes or to Nodes that compose user interfaces.
-  *Import*: relates to the resource import system.
-  *Input*: relates to the input system.
-  *Multiplayer*: relates to multiplayer (high-level networking) systems.
-  *Navigation*: relates to the navigation system (including A* and navmeshes).
-  *Network*: relates to (lot-level) networking.
-  *Particles*: particles, particle systems and their editors.
-  *Physics*: relates to the physics engine (2D/3D).
-  *Plugin*: relates to problems encountered while writing plugins.
-  *Porting*: relates to some specific platforms or exporting projects.
-  *Rendering*: relates to the 2D and 3D rendering engines.
-  *Shaders*: relates to the Godot shader language or visual shaders.
-  *Tests*: relates to unit tests.
-  *Thirdparty*: relates to third-party libraries used in Godot.
-  *XR*: relates to Augmented Reality or Virtual Reality.

Issues would typically correspond to only one topic, though it's not
unthinkable to see issues that fit two bills. The general idea is that
there will be specialized contributors teams behind all topics, so they
can focus on the issues labelled with their team's topic.

**Platforms:**

*Android*, *iOS*, *Linux*, *macOS*, *Web*, *Windows*

By default, it is assumed that a given issue applies to all platforms.
If one of the platform labels is used, it is then exclusive and the
previous assumption doesn't stand anymore (so if it's a bug on e.g.
Android and Linux exclusively, select those two platforms).

Documentation labels
~~~~~~~~~~~~~~~~~~~~

In the `documentation repository <https://github.com/godotengine/godot-docs>`__, we
use the following labels:

-  *Archived*: either a duplicate of another issue, or invalid. Such an
   issue would also be closed.
-  *Bug*: Incorrect information in an existing page. Not to be used for
   *missing* information.
-  *Cherrypick*: describes something that can be backported to a stable branch
   after being merged in the ``master`` branch.
-  *Dependencies*: describes pull requests that update a dependency file.
-  *Discussion*: the issue is not consensual and needs further
   discussion to define what exactly should be done to address the
   topic.
-  *Enhancememnt*: new information to be added in an existing page.
-  *Good first issue*: the issue is *assumed* to be an easy one to fix, which makes
   it a great fit for new contributors who want to become familiar with
   the code base. It should be removed while an active PR is available, that
   resolves this issue.
-  *Needs work*: the pull request needs additional work before it can be merged.
-  *Python*: Pull requests that update Python code.
-  *Salvageable*: the pull request can't be merged due to design issues or
   merge conflicts and its author is not active anymore. However, it can still
   be picked up by an external contributor to bring it to a mergeable state.
   To do so, you need to open a new pull request based on the original pull request.
-  *Tracker*: issue used to track other issues (like all issues related to
   the plugin system).

**Area:**

-  *About*: Issues and PRs related to the About section of the documentation and other general articles.
-  *Class reference*: the issue is about the class reference, not a documentation page.
-  *Community*: Issues and PRs related to the Community section of the documentation.
-  *Contributing*: Issues and PRs related to the Contributing/Development section of the documentation.
-  *Getting started*: Issues and PRs related to the Getting Started section of the documentation.
-  *Manual*: Issues and PRs related to the Manual/Tutorials section of the documentation.

**Content:**

-  *Images*: Issues and PRs involving outdated or incorrect images in articles.
-  *New page*: Issues and PRs related to creation of new documentation pages for new or undocumented features.
-  *Organization*: Issues and PRs related to reorganizing the content.
-  *Proofreading*: Issues and PRs related to proofreading the documentation.
-  *Redirect*: Issues and PRs involving moving content and adding a redirect rule on the backend.
-  *Website*: Issues related to adding website features and fixing bugs, whether on the front or back-end,

**Topic:**

The available topics describe the same content as the topics in the main
repository.

Milestones
~~~~~~~~~~

`Milestones <https://github.com/godotengine/godot/milestones>`_ correspond to
planned future versions of Godot for which there is an existing roadmap. Issues
that fit in the said roadmap should be filed under the corresponding milestone;
if they don't correspond to any current roadmap, they should be left without
milestone. As a rule of thumb, an issue corresponds to a given milestone if it
concerns a feature that is new in the milestone, or a critical bug that can't be
accepted in any future stable release, or anything that Juan wants to work on
right now. :)

Contributors are free to pick issues regardless of their assigned milestone;
if a fix is proposed for a bug that was not deemed urgent and thus without
milestone, it would likely still be very welcome.
