.. _docs_contribution_checklist:

Contribution checklist
======================

This page is a list of things to check as you are contributing to the documentation.
Before you hit that ``Create pull request`` button, read over this list at least
once to see if you missed anything.

**Writing style**

:ref:`See here. <doc_docs_writing_guidelines_clear_english_rules>`

- Use the active voice.
- Use precise action verbs.
- Avoid verbs that end in -ing.
- Remove unnecessary adverbs and adjectives.
- Ban these 8 words: obvious, simple, basic, easy, actual, just, clear, and however.
- Use explicit references.
- Use 's to show possession.
- Use the Oxford comma.

**Code examples**

- Use dynamic typing. :ref:`See here. <doc_docs_writing_guidelines_dynamic_typing>`
- Use real, practical examples. Do not use ``foo`` / ``bar`` examples. :ref:`See here. <doc_docs_writing_guidelines_real_world_code_example>`

**Writing formatting**

- Common vocabulary for the editor interface is used. :ref:`See here. <doc_docs_writing_guidelines_common_vocabulary>`
- Use :kbd: for keyboard shortcuts. :ref:`See here. <doc_docs_writing_guidelines_keyboard_shortcuts>`

- Literals use ``code style``.
- Classes link to the class reference once, then use ``ClassName``.
- Methods and properties link to the class ref once, then use ``PropertyName``.
- Menus, windows, and editor navigation paths use ``Bold Style``.
- Project settings are linked to.
- Avoid mentioning a specific Godot version. :ref:`See here. <doc_docs_writing_guidelines_specific_version>`

- Text is wrapped to 80-100 characters.
- No trailing whitespace at the end of lines.

**Images and videos**

- New images are in ``webp`` format. :ref:`See here. <doc_docs_image_guidelines_format_conversion>`
- Editor screenshots are cropped. :ref:`See here. <doc_docs_image_guidelines_cropping>`
- Images larger than 1080p or 300kb are scaled down. :ref:`See here. <doc_docs_image_guidelines_scaling_down>`
- Outlines in images use ``fffb44`` yellow. :ref:`See here. <doc_docs_image_guidelines_outlines>`
- Videos use the ``:autoplay:``, ``:loop:``, and ``:muted:`` tags. :ref:`See here. <doc_docs_image_guidelines_videos>`

**Github**

- The PR title starts with a word like ``Fix``, ``Add``, ``Update``, ``Clarify``, ``Improve``.
- If the PR closes an issue, link to the issue with one of GitHub's 
  `keywords <https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests>`_
  : ``closes``, ``fixes``, or ``resolves``.
- Ideally, PR contains a single commit. However, multiple commits can be :ref:`squashed <doc_pr_workflow_rebase>` later.
