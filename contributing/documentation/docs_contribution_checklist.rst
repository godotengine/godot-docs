.. _docs_contribution_checklist:

Documentation contribution checklist
====================================

This page is a summary of the guidelines to follow when contributing to the
documentation. Before you press that **Create pull request** button on GitHub,
read over this list to double check if you missed anything.

You don't need to read all the guidelines here in order to start contributing.
If you do miss something, it will be pointed out during review. However,
following the guidelines you are aware of as best you can will help speed up the
review process.

Writing style
-------------

:ref:`See here. <doc_docs_writing_guidelines_clear_english_rules>`

- Use the active voice.
- Use precise action verbs.
- Avoid verbs that end in -ing.
- Remove unnecessary adverbs and adjectives.
- Ban these 8 words: obvious, simple, basic, easy, actual, just, clear, and however.
- Use explicit references.
- Use 's to show possession.
- Use the Oxford comma.

Code examples
-------------

- Use dynamic typing. :ref:`See here. <doc_docs_writing_guidelines_dynamic_typing>`
- Use real, practical examples. Avoid ``foo`` / ``bar`` examples. :ref:`See here. <doc_docs_writing_guidelines_real_world_code_example>`

Manual style and formatting
---------------------------

- Use common vocabulary for the editor interface. :ref:`See here. <doc_docs_writing_guidelines_common_vocabulary>`
- Use ``:kbd:`` for keyboard shortcuts. :ref:`See here. <doc_docs_writing_guidelines_keyboard_shortcuts>`
- Literals use ``code style``. :ref:`See here. <doc_docs_writing_guidelines_literals>`
- Classes link to the class reference once, then use ``ClassName`` for the rest
  of the page.
  Methods and properties link to the class ref once, then use ``PropertyName``
  for the rest of the page. :ref:`See here. <doc_docs_writing_guidelines_class_properties_methods>`
- Editor UI, like menus, windows, and editor navigation paths, use
  ``Bold Style``. :ref:`See here. <doc_docs_writing_guidelines_editor_ui>`
- Link to project settings when referencing them. :ref:`See here. <doc_docs_writing_guidelines_project_settings>`
- Text is manually wrapped to 80-100 characters. :ref:`See here. <doc_docs_writing_guidelines_manually_wrapping_lines>`
- No trailing whitespace at the end of lines.
- Most of the time, avoid mentioning a specific Godot version. :ref:`See here. <doc_docs_writing_guidelines_specific_version>`

Images and videos
-----------------

- New (and updated) images are in WebP format. :ref:`See here. <doc_docs_image_guidelines_format_conversion>`
- Editor screenshots are cropped. :ref:`See here. <doc_docs_image_guidelines_cropping>`
- Images larger than 1080p or 300kb are scaled down. :ref:`See here. <doc_docs_image_guidelines_scaling_down>`
- Outlines in images use ``fffb44`` yellow. :ref:`See here. <doc_docs_image_guidelines_outlines>`
- Videos use the ``:autoplay:``, ``:loop:``, and ``:muted:`` tags. :ref:`See here. <doc_docs_image_guidelines_videos>`

GitHub
------

- The PR title starts with a word like ``Fix``, ``Add``, ``Update``,
  ``Clarify``, or ``Improve``.
- If the PR closes an issue, link to the issue with one of GitHub's 
  `keywords <https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests>`__:
  ``closes``, ``fixes``, or ``resolves``, in the text of the PR.
- Ideally, PR contains a single commit. However, multiple commits can be
  :ref:`squashed <doc_pr_workflow_rebase>` later.

