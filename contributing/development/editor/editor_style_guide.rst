.. _doc_editor_style_guide:

Editor style guide
==================

Introduction
------------

Thanks for your interest in contributing to the Godot editor!

This page describes the grammar and writing style used throughout the Godot
editor. Following this style guide will help your contribution get merged faster
since there will be fewer review steps required.

Writing style
-------------

- **Write messages (errors, warnings, ...) as full sentences.** They should start
  with an uppercase letter and end with a period.
- **Try to keep sentences short.** This makes it more likely that their translations
  will be short as well, which is a good thing to avoid UI bugs.
- **Use contractions.** For example, use "isn't" instead of "is not". An exception
  to this rule can be made when you specifically want to emphasize one of the
  contraction's words.
- **Use double quotes in messages** (``""``) instead of single quotes (``''``).
  Double quotes should be used to quote user input, file paths and possibly
  other things depending on the context.

.. seealso::

    Try to follow the :ref:`doc_docs_writing_guidelines` in addition to the
    guidelines outlined above.

Button and menu texts
---------------------

Capitalize text in buttons and menu actions:

- **Good:** *Open Editor Data Folder*
- **Bad:** *Open editor data folder*

If a menu action opens a modal dialog, suffix it with an ellipsis (``...``).

- **Good:** *Editor Settings...*
- **Bad:** *Editor Settings*

Inspector sections
------------------

In general, don't create sections that contain less than 3 items. Sections that
contain few items make it difficult to navigate the inspector, while missing the
benefits of using sections such as folding.

There are some valid exceptions for this, such as material features in
:ref:`class_StandardMaterial3D`.

This advice also applies to the Project Settings and Editor Settings.

Inspector performance hints
---------------------------

Enum properties that noticeably impact performance should have a performance
hint associated. The hint should refer to the *absolute* performance impact,
rather than being relative to the other options provided in the enum. Here are
some examples taken from the Godot editor:

- **Screen-space antialiasing:** *Disabled (Fastest), FXAA (Fast)*
- **MSAA quality:** *Disabled (Fastest), 2x (Fast), 4x (Average), 8x (Slow), 16x
  (Slower)*
- **DirectionalLight mode:** *Orthogonal (Fast), PSSM 2 Splits
  (Average), PSSM 4 Splits (Slow)*

For consistency, try to stick to the terms below (from fastest to slowest):

- *Fastest, Faster, Fast, Average, Slow, Slower, Slowest*

Their usage doesn't have to be contiguous. For example, you can use only "Fast"
and "Slow" from the list above.

If you're adding a new enum, its values should be ordered from the fastest
option to the slowest option.

Tooltips
--------

Consider adding tooltips whenever the action performed by a button or menu
action isn't obvious. You can also provide additional context or highlight
caveats in the tooltip.

You can do this by calling ``set_tooltip(TTR("Text here."))`` on the
Control-based node in question. If the tooltip is particularly long (more than
~80 characters), wrap it over several lines by adding line breaks using ``\n``.

Tooltips should follow the writing style described above. In addition to this,
use indicative mood instead of imperative mood:

- **Good:** *Computes global illumination for the selected GIProbe.*
- **Bad:** *Compute global illumination for the selected GIProbe.*
