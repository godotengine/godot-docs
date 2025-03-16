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

For issue management, we use the following GitHub processes:

- Each issue and pull request (PR) is categorized with a set of *labels*,
  sometimes called "tags".
- Each PR is assigned to a *milestone*. Some issues can also be assigned to a
  *milestone* (see below).
- Issues can have an *assignee*, who is a contributor among Godot maintainers.
- Issues can be put in one or more *projects*.
- PRs can be *linked* to one or more issues which they "fix" or "close".

We don't yet extensively use or rely on some other GitHub processes:

- Issue close reasons (completed, not planned, duplicate). While we use these,
  it is not consistent, and older issues are all closed as "completed", so the
  issue close reason should not be relied on.
- Issue *types* (Bug, Feature, Task).
- Issue *relationships*.

We only use the assignees feature for Godot maintainers who are members of the
Godot Engine GitHub organization, and even then not in all cases. For other
issues, we track who is working on an issue by comments on the issue and linked
pull requests. Most issues are available for any contributor to take on, after
discussing it with other contributors. If you would like to work on an issue,
first check that no one else is working on it, by looking for a linked pull
request, a comment "claiming" the issue, or an assignee. If no one else is
working on the issue, leave a comment on the issue to "claim" it and start
working on it.

Labels
~~~~~~

The following `labels <https://github.com/godotengine/godot/labels>`__ are
currently defined in the Godot repository:

Categories:
^^^^^^^^^^^

-  *Archived*: used to filter issues closed with a resolution other than "fixed".

   - For issues, added to all issues that are not resolved by engine or
     documentation changes. This includes duplicate issues, user error, or
     reports in the wrong repository.
     Since we don't rely on GitHub's issue close reasons (``completed``, ``not
     planned``, and ``duplicate``), it is possible for an issue to be closed as
     ``completed`` with the *Archived* label.
   - For PRs, added to all closed PRs that are not merged. This includes superseded
     or duplicate PRs, Git or GitHub mistakes, and valid PRs that end up not merged. 
   
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
-  *Documentation*: related to the documentation. PRs with this label improve the
   class reference. Issues with this label are either for wrong documentation, or
   are user-reported "bugs" that are actually limitations to be further documented.
   Often paired with *Discussion*. Issues related to the ReadTheDocs documentation
   should be filed on the `godot-docs <https://github.com/godotengine/godot-docs>`_ repository.
-  *Enhancement*: describes a proposed enhancement to an existing
   functionality.
-  *Feature proposal*: used for PRs adding new features which do not have a
   corresponding proposal use this label. The label is removed when a feature
   proposal is created and linked. The main Godot repository no longer accepts
   feature requests as issues. Please use the `godot-proposals
   <https://github.com/godotengine/godot-proposals>`__ repository instead.
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
   Also for issues that are very incomplete, such as missing reproduction steps.
-  *Performance*: issues that directly impact engine or editor performance.
   Can also be used for pull requests that improve performance or add low-end-friendly options.
   Should not be coupled with *Usability*.
-  *Regression*: the bug appeared after a stable release not exhibiting
   the bug was released.
-  *Salvageable*: the pull request can't be merged due to design issues or
   merge conflicts and its author is not active anymore. However, it can still
   be picked up by another contributor to bring it to a mergeable state.
   To do so, you need to open a new pull request based on the original pull request.
-  *Spam*: intentional spam issues, and extremely low-effort PRs. Used
   sparingly, since we give contributors and users the benefit of the doubt. In
   most cases, *Needs work* or *Archived* is more appropriate.
-  *Tracker*: issue used to track other issues (like all issues related to
   the plugin system).
-  *Usability*: issues that directly impact user usability. Should not be coupled with *Performance*.

The categories are used for general triage of the issues. They can be combined
in some way when relevant, e.g. an issue can be labeled *Bug* and *Usability*
at the same time if it's a bug that affects usability. Or *Enhancement* and
*Discussion* if it's an improvement that requires discussion of the best
approach. At least one of the categories *Bug*, *Enhancement*, or *Discussion*
are used to describe an issue or pull request.

Topics:
^^^^^^^

-  *2D*: relates to 2D nodes. Should be coupled with one of the labels
   below, and should not be coupled with *3D*.
-  *3D*: relates to 3D nodes. Should be coupled with one of the labels
   below, and should not be coupled with *2D*.
-  *Animation*: relates to the Animation system, editors and importers.
-  *Assetlib*: relates to issues with the asset library.
-  *Audio*: relates to the audio features (low- and high-level).
-  *Buildsystem*: relates to building issues, either linked to the SCons
   buildsystem or to compiler peculiarities.
-  *Codestyle*: relates to the programming style used within the codebase.
-  *Core*: anything related to the core engine. Specific topics are split off separately as they crop up.
-  *Dotnet*: relates to the C# / .NET bindings.
-  *Editor*: relates to issues in the editor (mainly UI).
-  *Export*: relates to the export system and templates.
-  *GDExtension*: relates to the GDExtension system for native extensions.
-  *GDScript*: relates to GDScript.
-  *GUI*: relates to GUI (Control) nodes or to Nodes that compose user interfaces.
-  *Import*: relates to the resource import system.
-  *Input*: relates to the input system.
-  *I18n*: relates to internationalization.
-  *Multiplayer*: relates to multiplayer (high-level networking) systems.
-  *Navigation*: relates to the navigation system (including A* and navmeshes).
-  *Network*: relates to (low-level) networking.
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

Platforms:
^^^^^^^^^^

*Android*, *iOS*, *LinuxBSD*, *macOS*, *Web*, *Windows*

By default, it is assumed that a given issue applies to all platforms.
If one of the platform labels is used, it is then exclusive and the
previous assumption doesn't stand anymore (so if it's a bug on e.g.
Android and Linux exclusively, select those two platforms).

Documentation labels
~~~~~~~~~~~~~~~~~~~~

In the `documentation repository <https://github.com/godotengine/godot-docs>`__, we
use the following `labels <https://github.com/godotengine/godot-docs/labels>`__:

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
-  *Enhancement*: new information to be added in an existing page.
-  *Good first issue*: the issue is *assumed* to be an easy one to fix, which makes
   it a great fit for new contributors who want to become familiar with
   the code base. It should be removed while an active PR is available, that
   resolves this issue.
-  *Linked demo PR*: the PR has a corresponding PR to the
   `Godot Demo Projects <https://github.com/godotengine/godot-demo-projects>`__
   repository which must be merged at the same time. Any changes to code in
   tutorials that have a corresponding demo, such as :ref:`doc_your_first_2d_game`,
   need to update both repositories so that the tutorial code stays in sync with
   the completed demo.
-  *Needs work*: the pull request needs additional work before it can be merged.
-  *Python*: Pull requests that update Python code.
-  *Salvageable*: the pull request can't be merged due to design issues or
   merge conflicts and its author is not active anymore. However, it can still
   be picked up by an external contributor to bring it to a mergeable state.
   To do so, you need to open a new pull request based on the original pull request.
-  *Tracker*: issue used to track other issues (like all issues related to
   the plugin system).
-  *Waiting on PR merge*: the PR documents an engine PR that has not been merged
   yet.

Area:
^^^^^

-  *About*: Issues and PRs related to the About section of the documentation and other general articles.
-  *Class reference*: the issue is about the class reference, not a documentation page.
-  *Community*: Issues and PRs related to the Community section of the documentation.
-  *Contributing*: Issues and PRs related to the Contributing/Development section of the documentation.
-  *Getting started*: Issues and PRs related to the Getting Started section of the documentation.
-  *Manual*: Issues and PRs related to the Manual/Tutorials section of the documentation.

Content:
^^^^^^^^

-  *Images*: Issues and PRs involving outdated or incorrect images in articles.
-  *Example code*: Issues and PRs involving writing or updating code examples.
-  *New page*: Issues and PRs related to creation of new documentation pages for new or undocumented features.
-  *Organization*: Issues and PRs related to reorganizing the content.
-  *Proofreading*: Issues and PRs related to proofreading the documentation.
-  *Redirect*: Issues and PRs involving moving content and adding a redirect rule on the backend.
-  *Website*: Issues related to adding website features and fixing bugs, whether on the front or back-end,

Topic:
^^^^^^

The available topics describe the same content as the topics in the main
repository.

Milestones
~~~~~~~~~~

`Milestones <https://github.com/godotengine/godot/milestones>`_ are used for
some issues and all PRs.

We have milestones for specific minor engine versions, like ``4.5`` and ``4.6``,
as well as general milestones for major engine versions, like ``3.x`` and
``4.x``. In the ``godot-proposals`` repo, we also have a ``5.0`` milestone for
compatibility-breaking changes that will be considered for Godot 5.0, in many
years.

Issues are assigned to the current development milestone, such as ``4.5``, if
they are related to features introduced in that engine version, or are bugs
(regressions) in that version. Additionally, all issues completed during the
development of that engine version are added to the milestone, so that users can
see at a glance in which minor version an issue was first fixed. We don't always
use the ``4.x`` milestone for issues, since by default all issues are related to
Godot 4.x. However, we do use the ``3.x`` milestone to mark issues that are
specific to Godot 3.x.

All pull requests are assigned to a milestone. By default, enhancement and
feature PRs are assigned to the ``4.x`` milestone, and bugs are assigned to the
current development milestone, such as ``4.5``. Towards the end of the minor
version's development, PRs currently in that milestone are reassessed. If
a PR is no longer being considered for that version, it is reassigned to either the
major version milestone (``4.x``), or the next minor version milestone (such as
``4.6``).

Pull requests in the ``4.x`` milestone are reassigned to the current minor
engine version, such as ``4.5``, when the review process is complete, and the
production team decides that the PR is ready to be merged soon. Note that
this usually requires more than one approving review.

The milestone assigned to a PR is a goal, not a guarantee. New features and
enhancements are merged when they are ready. While reviewers and maintainers do
their best to review PRs in time for the current version, at some point we reach
the beta, feature freeze, and then release; and existing PRs are reassigned to
the next minor version, or to ``4.x``. As a rule, we assign new features to the
``4.x`` milestone initially to avoid continually reassigning a PR from version
to version. However, a PR being in ``4.x`` does not mean it won't be merged;
it's just the default for new features.