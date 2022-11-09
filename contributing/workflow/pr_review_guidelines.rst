.. _doc_pr_review_guidelines:

Pull request review process
===========================

.. note::

    This page is intended to provide insight into the pull request (PR) review
    process that we aspire to. As such, it is primarily targeted at engine
    maintainers who are responsible for reviewing and approving pull requests.
    That being said, much of the content is useful for prospective contributors
    wanting to know how to ensure that their PR is merged.

From a high level, the ideal life cycle of a pull request looks like the
following: 

  1. A contributor opens a PR that fixes a specific problem (optimally closing
     a GitHub `issue <https://github.com/godotengine/godot>`_ or implementing
     a `proposal <https://github.com/godotengine/godot-proposals>`_).

  2. Other contributors provide feedback on the PR (including reviewing and/or
     approving the PR, as appropriate).

  3. An engine maintainer reviews the code and provides feedback, requests
     changes, or approves the pull request, as appropriate.

  4. Another maintainer reviews the code with a focus on code style/clarity and
     approves it once satisfied.

  5. A team leader or a member of the `production team
     <https://godotengine.org/teams#production>`_ merges the pull request if
     satisfied that it has been sufficiently reviewed.

This document will explain steps 2, 3, 4, and 5 in more detail. For a more
detailed explanation of the pull request workflow please see the :ref:`pull
request workflow document <doc_pr_workflow>`. 

.. note:: 
  In practice these steps may blend together. Oftentimes maintainers will
  provide comments on code style and code quality at the same time and will
  approve a pull request for both.

Typically the first interaction on a pull request will be an engine maintainer
assigning tags to the pull request and flagging it for review by someone
familiar with that area of code.

Engine maintainers are folks who are "members" of the Godot project repository
on GitHub and/or are listed on the `Teams page <https://godotengine.org/teams>`_
on the Godot website. Maintainers are responsible for a given area of the
engine. Typically this means they are the people who are given more trust to
approve and recommend pull requests for merging.

Even if you are not a maintainer, you can still help by reviewing code,
providing feedback on PRs and testing PRs locally on your machine to confirm
that they work as intended. Many of the currently active maintainers started out
doing this before they became maintainers.

Code review and testing
-----------------------

The following is a list of things that contributors and engine maintainers can
do to conduct a substantive code review of a pull request.

.. note::
  If you want to conduct a code review, but can't do everything on this list,
  say that in your review comment. For example, it is still very helpful to
  provide comments on code, even if you can't build the pull request locally to
  test the pull request (or vice versa). Feel free to review the code, just
  remember to make a note at the end of your review that you have reviewed the
  code only and have not tested the changes locally.

1. Confirm that the problem exists
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PRs need to solve problems and problems need to be documented. Make sure that
the pull request links and closes (or at least addresses) a bug or a proposal.
If it doesn't, consider asking the contributor to update the opening message of
the PR to explain the problem that the PR aims to solve in more detail.

.. note::
  It should be clear _why_ a pull request is needed before it is merged. This
  assists reviewers in determining whether a PR does what it says it does and it
  helps contributors in the future understand why the code is the way it is.

2. Test the PR and look for regressions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While strict code review and CI help to ensure that all pull requests work as
intended, mistakes happen and sometimes contributors push code that creates a
problem in addition to solving a problem. Maintainers will avoid merging code
that contains a regression even if it solves the problem as intended.

When reviewing a pull request, ensure that the PR does what it says it does
(i.e. fixes the linked bug or implements the new feature) and nothing outside of
the PR target area is broken by the change. You can do this by running the
editor and trying out some common functions of the editor (adding objects to a
scene, running GDScript, opening and closing menus etc.). Also, while reviewing
the code, look for suspicious changes in other parts of the engine. Sometimes
during rebasing changes slip through that contributors are not aware of.

3. Do a code review
^^^^^^^^^^^^^^^^^^^

Code reviews are usually done by people who are already experienced in a given
area. They may be able to provide ideas to make code faster, more organized, or
more idiomatic. But, even if you are not very experienced, you may want to
conduct a code review to provide feedback within the scope of what you are
comfortable reviewing. Doing so is valuable for the area maintainer (as a second
set of eyes on a problem is always helpful) and it is also helpful for you as it
will help you get more familiar with that area of code and will expose you to
how other people solve problems. In fact, reviewing the code of experienced
engine maintainers is a great way to get to know the codebase.

Here are some things to think about and look out for as you review the code:

* **Code only touches the areas announced in the PR (and the commit
  message).**

  It can be tempting to fix random things in the code, as you see them. However,
  this can quickly make a pull request difficult to review and can make it hard
  to dig through in the commit history. Small touch-ups next to the related area
  are alright, but often bugs that you can find along the way are better fixed
  in their own PRs.

* **Code properly uses Godot's own APIs and patterns.**

  Consistency is very important, and a solution that already exists in the
  codebase is preferable to an ad-hoc solution.

* **Are core areas affected by the change?**

  Sometimes a PR that is supposed to solve a local problem can have a
  far-reaching effect way outside of its scope. Usually it is best to keep code
  changes local to where the problem arises. If you think that the solution
  requires changes outside the scope of the problem, it is usually best to seek
  the opinion of a team leader who may have another idea for how to solve the
  problem.

4. Iterate with the contributor and improve the PR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Maintainers should provide feedback and suggestions for improvement if they spot
things in the code that they would like changed. Preferably, suggestions should
come in order of importance: first, address overall code design and the approach
to solving the problem, then make sure the code is complying with the engine's
best practices, and lastly, do the :ref:`code style review <doc_code_style_review>`.

.. note::

    **Communicate barriers to merging early in the review process.**

    If the PR has clear blockers or will likely not get merged for whatever other
    reason, that fact should be communicated as early and clearly as possible. We
    want to avoid stringing people along because it feels bad to say "sorry, no".

As you review pull requests, keep the Godot `Code of Conduct
<https://godotengine.org/code-of-conduct>`_ in mind. Especially the following:

* Politeness is expected at all times. Be kind and courteous.

* Always assume positive intent from others.

* Feedback is always welcome but keep your criticism constructive.

Here are some things to avoid as you iterate on a pull request with a
contributor:

* **Needless double reviews.**

  In other words, review the full PR at once and avoid coming back endless times
  to point out issues that you could have noted in the first review. Of course,
  this can't always be avoided, but we should try to catch everything at once.

* **Being overly nitpicky.**

  Code quality can be flexible depending on the area of the engine you are
  working in. In general, our standard for code quality is much higher in core
  areas and in performance-sensitive areas than it is in editor code for
  example.

* **Expanding the scope of a pull request.** 

  Providing context or related/similar issues or proposals that may be fixed
  similarly can be helpful, but adding a "may as well fix that thing over there
  as well while at it" or "could we add to this as well?" isn't always fair to
  the contributor. Use your judgement when deciding whether additional fixes are
  within scope, but try to keep the scope as close to the original pull request
  as possible.

And ultimately, don't feel pressured to deal with the PR all alone. Feel free to
ask for a helping hand on the `Godot Contributors Chat
<https://chat.godotengine.org>`_, in the appropriate channel or in #general.
Other teams may already be tagged for review, so you can also wait or ask for
their assistance.

5. Approve the pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^

After reviewing the code, if you think that the code is ready to be merged into
the engine, then go ahead and "approve" it. Make sure to also comment and
specify the nature of your review (i.e. say whether you ran the code locally,
whether you reviewed for style as well as correctness, etc.). Even if you are
not an engine maintainer, approving a pull request signals to others that the
code is good and likely solves the problem the PR says it does. Approving a pull
request as a non-engine maintainer does not guarantee that the code will be
merged, other people will still review it, so don't be shy.

.. _doc_code_style_review:

Code style review
-----------------

Generally speaking, we aim to conduct a code review before a style/clarity
review as contributors typically want to know if their general approach is
acceptable before putting in the effort to make nitpicky changes to style. In
other words, maintainers shouldn't ask contributors to change the style of code
that may need to be rewritten in subsequent reviews. Similarly, maintainers
should avoid asking for contributors to rebase PRs if the PR has not been
reviewed.

That being said, not everyone feels confident enough to provide a review on code
correctness, in that case, providing comments on code style and clarity ahead of
a more substantive code review is totally appropriate and more than welcome.

In practice the code style review can be done as part of the substantive code
review. The important thing is that both the substantive code and the code style
need to be reviewed and considered before a pull request is merged.

When reviewing code style pay particular attention to ensuring that the pull
request follows the :ref:`doc_code_style_guidelines`. While ``clang-format`` and
various CI checks can catch a lot of inconsistencies, they are far from perfect
and are unable to detect some issues. For example, you should check that:

  * The style of header includes is respected.
  * Identifiers use ``snake_case`` and follow our naming conventions.
  * Method parameters start with ``p_*`` or ``r_*`` (if they are used to return
    a value).
  * Braces are used appropriately, even for one-liner conditionals.
  * Code is properly spaced (exactly one empty line between methods, no
    unnecessary empty lines inside of method bodies).

.. note::

    This list is not complete and doesn't aim to be complete. Refer to
    the linked style guide document for a complete set of rules. Keep
    in mind that ``clang-format`` may not catch things you hope it would,
    so pay attention and try to build a sense of what exactly it can and
    cannot detect.

Merging pull requests
---------------------

In general, pull requests should only be merged by members of the production
team or team leaders for pull requests in their area of the engine. For example,
the networking team leader could merge a networking pull request that doesn't
substantially change non-networking sections of code. 

In practice it is best to wait for a member of the production team to merge the
pull request as they keep a close eye on the entire codebase and will likely
have a better sense of what other recent/upcoming changes this pull request may
conflict with (or any other reason that it may make sense to delay the pull
request). Feel free to leave a comment saying that the PR should be ready to
merge.

The following are the steps to take before merging a pull request. The degree to
which you adhere to these steps can be flexible for simple/straightforward pull
requests, but they should be carefully taken for complex or risky pull requests.

As a contributor you can help move a pull request forward by doing some of these
steps yourself.

1. Get feedback from the right people/teams
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Production team members should ensure that the right people look at a pull
request before it is merged. In some cases this may require multiple people to
weigh in. In other cases, only one substantive approval is needed before the
code can be merged. 

In general, try not to merge things based on one review alone, especially if it
is your own. Get a second opinion from another maintainer, and make sure all the
teams that may be impacted have been reasonably represented by the reviewers.
For example, if a pull request adds to the documentation, it's often useful to
let the area maintainers check it for factual correctness and let documentation
maintainers check it for formatting, style, and grammar.

A good rule of thumb is that at least one subject matter expert should have
approved the pull request for correctness, and at least one other maintainer
should have approved the pull request for code style. Either of those people
could be the person merging the pull request.

Make sure that the reviews and approvals were left by people competent in that
specific engine area. It is possible that even a long-standing member of the
Godot organization left a review without having the relevant expertise.

.. note::

    An easy way to find PRs that may be ready for merging is filtering by
    approved PRs and sorting by recently updated. For example, in the main Godot
    repository, you can use `this link
    <https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+review%3Aapproved+sort%3Aupdated-desc>`_.

2. Get feedback from the community
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If a pull request is having trouble attracting reviewers, you may need to reach
out more broadly to ask for help reviewing. Consider asking:

* the person who reported the bug if the pull request fixes the bug for them,
* contributors who have recently edited that file if they could take a look, or
* a more experienced maintainer from another area if they could provide feedback.

3. Git checklist
^^^^^^^^^^^^^^^^

* **Make sure that the PR comes in one commit.**

  When each commit is self-contained and could be used to build a clean and
  working version of the engine, it may be okay to merge a pull request with
  multiple commits, but in general, we require that all pull requests only have
  one commit. This helps us keep the Git history clean.

* **Fixes made during the review process must be squashed into
  the main commit.**

  For multi-commit PRs check that those fixes are amended in the relevant
  commits, and are not just applied on top of everything.

* **Make sure that the PR has no merge conflicts.**

  Contributors may need to rebase their changes on top of the relevant branch
  (e.g. ``master`` or ``3.x``) and manually fix merge conflicts. Even if there
  are no merge conflicts, contributors may need to rebase especially old PRs as
  the GitHub conflict checker may not catch all conflicts, or the CI may have
  changed since it was originally run.

* **Check for proper commit attribution.**

  If a contributor uses an author signature that is not listed in their GitHub
  account, GitHub won't link the merged pull request to their account. This
  keeps them from getting proper credit in the GitHub history and makes them
  appear like a new contributor on the GitHub UI even after several
  contributions.

  Ultimately, it's up to the user if they want to fix it, but they can do so by
  authoring the Git commit with the same email they use for their GitHub
  account, or by adding the email they used for the Git commit to their GitHub
  profile.

* **Check for proper commit messages.**

  While we don't have a very strict ruleset for commit messages, we still
  require them to be short yet descriptive and use proper English. As a
  maintainer you've probably written them enough times to know how to make one,
  but for a general template think about *"Fix <issue> in <part of codebase>"*.
  For a more detailed recommendation see the `contributing.md
  <https://github.com/godotengine/godot/blob/master/CONTRIBUTING.md#format-your-commit-messages-with-readability-in-mind>`_
  page in the main Godot repository.

4. GitHub checklist
^^^^^^^^^^^^^^^^^^^

* **Validate the target branch of the PR.**

  Most Godot development happens around in the ``master`` branch. Therefore most
  pull requests must be made against it. From there pull requests can then be
  backported to other branches. Be wary of people making PRs on the version they
  are using (e.g, ``3.3``) and guide them to make a change against a
  higher-order branch (e.g. ``3.x``). If the change is not applicable for the
  ``master`` branch, the initial PR can be made against the current maintenance
  branch, such as ``3.x``. It's okay for people to make multiple PRs for each
  target branch, especially if the changes cannot be easily backported.
  Cherry-picking is also an option, if possible. Use the appropriate labels if
  the PR can be cherrypicked (e.g. ``cherrypick:3.x``).

.. note::

    It is possible to change the target branch of the PR, that has already been
    submitted, but be aware of the consequences. As it cannot be synchronized
    with the push, the target branch change will inevitable tag the entire list
    of maintainers for review. It may also render the CI incapable of running
    properly. A push should help with that, but if nothing else, recommend
    opening a new, fresh PR.

* **Make sure that the appropriate milestone is assigned.**

  This will make it more obvious which version would include the submitted
  changes, should the pull request be merged now. Note, that the milestone is
  not a binding contract and does not guarantee that this version is definitely
  going to include the PR. If the pull request is not merged before the version
  is released, the milestone will be moved (and the PR itself may require a
  target branch change).

  Similarly, when merging a PR with a higher milestone than the current version,
  or a "wildcard" milestone (e.g. "4.x"), ensure to update the milestone to the
  current version.

* **Make sure that the opening message of the PR contains the
  magic words "Closes #..." or "Fixes #...".**

  These link the PR and the referenced issue together and allow GitHub to
  auto-close the latter when you merge the changes. Note, that this only works
  for the PRs that target the ``master`` branch. For others you need to pay
  attention and close the related issues manually. Do it with *"Fixed by #..."*
  or *"Resolved by #..."* comment to clearly indicate the act for future
  contributors.

* **For the issues that get closed by the PR add the closest
  relevant milestone.**

  In other words, if the PR is targeting the ``master`` branch, but is then also
  cherrypicked for ``3.x``, the next ``3.x`` release would be the appropriate
  milestone for the closed issue.

5. Merge the pull request
^^^^^^^^^^^^^^^^^^^^^^^^^

If it is appropriate for you to be merging a pull request (i.e. you are on the
production team or you are the team leader for that area), you are confident
that the pull request has been sufficiently reviewed, and once you carry out
these steps you can go ahead and merge the pull request.
