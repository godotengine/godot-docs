.. _doc_bug_triage_guidelines:

Bug triage guidelines
=====================

This page describes the typical workflow of the bug triage team aka
bugsquad when handling issues and pull requests on Godot's GitHub
repository. It is bound to evolve together with the bugsquad, so do not
hesitate to propose modifications to the following guidelines.

Issues management
-----------------

GitHub proposes three features to manage issues:

-  Set one or several labels from a predefined list
-  Set one milestone from a predefined list
-  Define one contributor as "assignee" among the Godot engine
   organization members

As the Godot engine organization on GitHub currently has a restricted
number of contributors and we are not sure yet to what extent we will
use it or OpenProject instead, we will not use assignees extensively for
the time being.

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
-  *Enhancement*: describes a proposed enhancement to an existing
   functionality.
-  *Feature request*: describes a wish for a new feature to be
   implemented.
-  *High priority*: the issue should be treated in priority (typically
   critical bugs).
-  *Needs discussion*: the issue is not consensual and needs further
   discussion to define what exactly should be done to address the
   topic.

The categories are used for general triage of the issues. They can be
combined in some way when relevant, e.g. an issue can be labelled *Bug*,
*Confirmed* and *High priority* at the same time if it's a critical bug
that was confirmed by several users, or *Feature request* and *Needs
discussion* if it's a non-consensual feature request, or one that is not
precise enough to be worked on.

**Topics:**

-  *Buildsystem*: relates to building issues, either linked to the SCons
   buildsystem or to compiler peculiarities.
-  *Core*: anything related to the core engine. It might be further
   split later on as it's a pretty big topic.
-  *Demos*: relates to the official demos.
-  *GDScript*: relates to GDScript.
-  *Porting*: relates to some specific platforms.
-  *Rendering engine*: relates to the 2D and 3D rendering engines.
-  *User interface*: relates to the UI design.

Issues would typically correspond to only one topic, though it's not
unthinkable to see issues that fit two bills. The general idea is that
there will be specialized contributors teams behind all topics, so they
can focus on the issues labelled with their team topic.

Bug reports concerning the website or the documentation should not be
filed in GitHub but in the appropriate tool in OpenProject, therefore
such issues should be closed and archived once they have been moved to
their rightful platform.

**Platforms:** *Android*, *HTML5*, *iOS*, *Linux*, *OS X*, *Windows*

By default, it is assumed that a given issue applies to all platforms. 
If one of the platform labels is used, it is the exclusive and the
previous assumption doesn't stand anymore (so if it's a bug on e.g.
Android and Linux exclusively, select those two platforms).

Milestones
~~~~~~~~~~

Milestones correspond to planned future versions of Godot for which
there is an existing roadmap. Issues that fit in the said roadmap should
be filed under the corresponding milestone; if they don't correspond to
any current roadmap, they should be set to *Later*. As a rule of thumb,
an issue corresponds to a given milestone if it concerns a feature that
is new in the milestone, or a critical bug that can't be accepted in any
future stable release, or anything that Juan wants to work on right now
:)
