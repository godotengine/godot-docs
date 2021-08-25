.. _doc_pr_review_guidelines:

Pull request review guidelines
==============================

.. note::

    This page is targeted at engine maintainers responsible for reviewing
    and approving pull requests. While not all tips and recommendations
    here are actionable if you are not a maintainer, this can still give
    you and insight into what goes into successfully merging a PR.

    Even if you are not a maintainer, you can always help by spotting
    issues in code or problems with the implementation overall, as well
    as by doing live testing of PRs on your machine and confirming that
    they work as intended.

If you are a designated Godot maintainer ("Member" on GitHub), you've
likely demonstrated skill, knowledge, and capacity for better judgement when
writing, reviewing, and improving Godot engine code and experience. You
are entrusted with keeping Godot moving forward, so feel free to exercise
your maintainer power to achieve that.

One part of that power is reviewing and merging pull requests, created
by your teammates and other contributors. You may not even realize it,
but you have full control of that green "Merge" button and are encouraged
to use it. But there are a few rules, checks, and recommendations that you
need to keep in mind before proceeding to do that.

Now, some of the things stated below may look obvious, but this is not
to insult your intelligence. We all can forget things, and we also come
from different backgrounds. It's to everyone's benefit that all important,
even if most obvious, steps are listed here.

Have a good reviewing experience, and feel free to contribute to this
guide if you think that anything is missing.

If you are a reviewer
---------------------

0. Make sure you haven't authored the PR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Even lead developers ask contributors to review their work. Nobody is
free from sin, and everyone can make a mistake. While it's tempting to
quickly merge a small fix you yourself just made, do not rush it and
seek approvals from your peers and leaders.

1. Confirm that the problem exists
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PRs need to solve problems, whether it is related to the engine functioning
properly or to the user experience using it. And problems need to be
documented. Make sure that the pull request links and closes or addresses
a bug or a proposal. If it doesn't, make sure that the opening message
of the PR is descriptive to explain the problem it aims to solve.

Ultimately, you need to be able to understand what the code is trying to
do to assess if it succeeds.

2. Build the PR branch and look for regressions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At the very least no PR should make the engine worse. Regardless of the
practicality of the solution, there should not be any immediate downgrades,
regressions, and unforeseen side-effects. It is very easy to become too
focused on solving a particular issue and accidentally breaking something
unrelated.

As such, a reviewer needs to establish that at a glance nothing outside
of the PR target area was affected (at least, affected negatively). It
should be enough to start the editor with a project, clicking a couple
of buttons, and running a scene.

3. Test the improved functionality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While the rest of the engine and the editor only need a cursory look,
the areas directly affected by PR need to be evaluated more carefully.
Before going after the code, it always makes sense to check if the
desired outcome is achieved in practice.

.. note::

    Some PRs can also aim to improve code that could theoretically cause a
    problem. Use your better judgement and experience there to assess the
    case, if it cannot be reproduced and tested in practice.

The precise approach would highly depend on the affected area of the
engine.

4. Do a code review
^^^^^^^^^^^^^^^^^^^

While code reviews can be quite boring and tedious, we cannot avoid
them. Thankfully, some PRs are short and sweet, and can probably be
approved just from the code review alone, skipping steps 1 through 3.
(Not recommended).

Remember, that a good code review is not only beneficial for the
codebase itself, but also for the reviewee and the reviewer too. You
make better contributors out of PR authors when you give them a good
thoughtful review, or even when you just offer small tips. And you
can learn something new yourself.

While a proper code review requires you to understand the nuance of the
affected engine area and is better left for your judgement, there is a
checklist of universal things to look for:

* **The PR follows** :ref:`doc_code_style_guidelines`.

  While ``clang-format`` and various CI checks can catch a lot of
  inconsistencies, they are far from perfect in that regard and are
  unable to detect some issues. For example, check that:

  * The style of header includes is respected.
  * Identifiers use ``snake_case`` and follow our naming conventions.
  * Method parameters start with ``p_*`` or ``r_*``.
  * Braces are used appropriately, even for one-liner conditionals.
  * Code is properly spaced (exactly one empty line between methods, no
    unnecessary empty lines inside of method bodies).

.. note::

    This list is not complete and doesn't aim to be complete. Refer to
    the linked style guide document for a complete set of rules. Keep
    in mind that ``clang-format`` may not catch things you hope it would,
    so pay attention and try to build a sense of what exactly it can and
    cannot detect.

* **Code only touches the areas announced in the PR (and the commit
  message).**

  It is always tempting to start fixing random things in code, as you
  see them. However, this can quickly become a hell to dig through in
  the commit history. Small touch-ups next to the related area are
  alright, but often bugs that you can find along the way are better
  left for their own PRs.

* **Code properly uses Godot's own APIs and patterns.**

  This is true for any reasonably sized project — consistency is very
  important, and a solution that already exists in the codebase
  is preferable to an ad-hoc solution.

* **Are core areas affected by the change?**

  Sometimes a PR that is supposed to solve a local problem can have a
  far-reaching effect, way outside of its scope. If you believe that
  is the case, make sure to get senior maintainers involved in the
  process, namely `reduz <https://github.com/reduz>`_ or
  `vnen <https://github.com/vnen>`_. Their input and approval would
  be required for changes to the engine's core systems and overall
  architecture, APIs that touch on all Objects or Nodes, and changes
  to GDScript and GDNative. If the pull request modifies the build
  system, you can contact `Akien <https://github.com/akien-mga>`_.

5. Iterate with the contributor and improve the PR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inevitably, a lot of pull requests would be initially undercooked.
At this point, you and the contributor should enter a feedback loop
where they iterate on your notes, recommendations, and requests, and
you make sure that they have indeed fixed the issues you've highlighted.

Try not to exhaust the contributor with style nitpicks, especially
if it's still up in the air whether their PR would be accepted at
all. Preferably, suggestions should come in order of importance:
firstly, address their overall code design and approach to solving the
problem, then make sure their code is complying with the engine's
best practices, and lastly, do the "pretty pass".

Some areas of the engine are more important than others. There is
a lot of ugly code in the editor and UI components, and while this
is not ideal, it's not the end of the world either. It's fine to
suggest improvements there as well, but don't insist too much if
the end result is achieved and the contribution leaves the code
reasonably maintainable.

And ultimately, don't feel pressured to deal with the PR all
alone. Feel free to ask for a helping hand on the `Godot
Contributors Chat <https://chat.godotengine.org>`_, in the appropriate
channel or in general. Other teams may already be tagged for review,
so you can also wait or ask for their assistance.

6. Approve the pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you find that everything is in order, that the PR is addressing
the problem, and that it does so in an acceptable way (it doesn't have
to be perfect, but it helps), then put your positive review on it.

If you are a merger
-------------------

A merger is just a reviewer in fancy pants. All recommendations
above still apply if you aim to merge a pull request, but you
can also completely rely on your fellow maintainers and their
judgement. Naturally, there is little point in doing a full review
yourself if you see your team members approving the changes.

But there are still more things that need to be checked before a
PR can be merged.

1. Get feedback from multiple people/teams
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Try not to merge things based on one review alone, especially
your own. Get a second opinion from your teammates, and make
sure all the teams have been reasonably represented by the
reviewers. For example, if a pull request adds to the documentation,
it's often useful to let the area maintainers check it for
factual correctness and let documentation maintainers check it
for formatting, style, and grammar.

Make sure that the reviews and approvals were left by people
competent in that specific engine area. It is possible that
even a long-standing member of the Godot organization left
a review without having the relevant expertise. As a merger
you can overrule their approving decision or their requests
for changes.

While you shouldn't approve your own PRs, you can still merge
them after receiving positive reviews from other maintainers.

2. Get feedback from the community
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Not all areas of the engine have a lot of maintainers, so
don't shy away from asking the involved users to help (namely,
the reporter of the bug or the submitter of the proposal).
Even if they cannot validate the code, they can still test the
changes with their projects and report back the results.

If you know of a contributor who has recently worked in the
area, you can also ask them to give it a look. Consider this
both help with the PR and an act of indoctrination into our
team.

3. Git checklist
^^^^^^^^^^^^^^^^

* **Make sure that the PR comes in one commit.**

  For some cases it may be okay to have it spread across
  several commits, but this is not the case for the majority
  of contributions. If the pull request consists of several
  commits, each commit must be as functional as if other
  commits didn't exist.

* **Fixes made during the review process must be squashed into
  the main commit.**

  For multi-commit PRs check that those fixes are amended in
  the relevant commits, and are not just applied on top of
  everything.

* **Make sure that the PR has no merge conflicts.**

  It must be a one click merge, and if it's not, the contributor
  needs to rebase their work from the current version of the
  target branch (e.g. ``master`` or ``3.x``).

* **Check for proper commit attribution.**

  This can primarily happen with new contributors, as they
  often don't provide a correct author signature in their
  commits (i.e. they don't use their actual email address, or
  the address they use isn't connected to their GitHub account).
  This can result in the PR being authored by seemingly one
  person, but submitted for review by another. Ultimately,
  it's up to them if they want to fix it, but such PRs won't
  count towards their contributions to the project and will
  keep them forever "New contributor" as far as GitHub is
  concerned.

* **Check for proper commit messages.**

  While we don't have a very strict ruleset for commit messages,
  we still require them to be short yet descriptive and use proper
  English. As a maintainer you've probably written them enough
  times to know how to make one, but for a general template
  think about *"Fix <issue> in <part of codebase>"*.

4. GitHub checklist
^^^^^^^^^^^^^^^^^^^

* **Validate the target branch of the PR.**

  Godot development happens around the ``master`` branch. Therefore
  most pull requests must be made against it, and can then be
  backported to other branches. Be wary of people making PRs
  on the version they are working on (e.g, ``3.3``) and guide
  them to make a change against a higher-order branch. If the
  change doesn't make sense for the ``master``, the initial PR can
  be made against the current maintenance branch, such as ``3.x``.
  It's okay for people to make multiple PRs for each target
  branch, especially if the changes cannot be easily backported.
  Cherry-picking is also an option, if possible. Use the appropriate
  labels if the PR can be cherrypicked (e.g. ``cherrypick:3.x``).

.. note::

    It is possible to change the target branch of the PR,
    that has already been submitted, but be aware of the
    consequences. As it cannot be synchronized with the push,
    the target branch change will inevitable tag the entire
    list of maintainers for review. It may also render the
    CI incapable of running properly. A push should help with
    that, but if nothing else, recommend opening a new, fresh PR.

* **Make sure that the appropriate milestone is assigned.**

  This will make it more obvious which version would include the
  submitted changes, should the pull request be merged now.
  Note, that the milestone is not a binding contract and does
  not guarantee that this version is definitely going to include
  the PR. If the pull request is not merged before the version
  is released, the milestone is moved (and the PR itself may
  require a target branch change).

* **Make sure that the opening message of the PR contains the
  magic words "Closes #..." or "Fixes #...".**

  These link the PR and the referenced issue together and allow
  to auto-close the latter when you merge the changes. Note, that
  this only works for the PRs that target the ``master`` branch.
  For others you need to pay attention and close the related
  issues manually. Do it with *"Fixed by #..."* or *"Resolved by #..."*
  comment to clearly indicate the act for future generations.

* **For the issues that get closed by the PR add the closest
  relevant milestone.**

  In other words, if the PR is targeting the ``master``, but is then
  also cherrypicked for ``3.x``, the next ``3.x`` release would be the
  appropriate milestone for the issue.

5. Don't be afraid
^^^^^^^^^^^^^^^^^^

That's the beauty of version control systems — you can always
revert, go back to a previous commit that was working. We use
Git, so you shouldn't be afraid to merge good pull requests
out of concerns that it may be a mistake. It can, but it's not
a problem and nobody is going to judge you for it.

If a PR you've merged gets reverted, you will be given feedback,
so you know what to improve in your approach, but don't let
it stop you completely in your tracks. Continue reviewing and
merging, work with your fellow contributors, and refer to this
guide, when in doubt.
