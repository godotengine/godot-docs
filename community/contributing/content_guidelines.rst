.. _doc_content_guidelines:

Content guidelines
==================

This document outlines what should be included in the official documentation.
Below, you will find a couple of principles and recommendations for writing
accessible content.

We want to achieve two goals:

1. **Empathize with our users.** We should write in a way that makes it easy for
   them to learn from the docs.
2. **Write a complete reference manual**. Our goal here is not to teach
   programming fundamentals. Instead, our goal is to provide a reference for how
   Godot's features work.

Guidelines and principles
-------------------------

Below are the guidelines we should strive to follow. They are not hard rules,
though: sometimes, a topic will require breaking one or more of them.
Still, we should strive to achieve the two goals listed above.

Writing complete and accessible documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**A feature doesn't exist unless it is documented**. If a user can't find
information about a feature and how it works, it doesn't exist to them. We
should ensure that we cover everything Godot does.

.. note::

    When adding or updating an engine feature, the documentation team needs to
    know about it. Contributors should open an issue on the `godot-docs` repository
    when their work gets merged and requires documentation.

Do your best to keep documents **under 1000 words in length**. If a page goes
past that threshold, consider splitting it into two parts. Limiting page size
forces us to write concisely and to break up large documents so that each page
focuses on a particular problem.

Each page or section of a page should clearly state what **problem** it tackles
and what it will teach the user. Users need to know if they're reading the
correct guide for solving the problems they're encountering. For example,
instead of writing the heading "Signals", consider writing "Reacting to changes
with signals". The second title makes it clear what the purpose of signals is.

.. note::

    Long section titles lead to long entries in the side menu, which can make
    navigation cumbersome. Try to keep headings five words long or less.

If the page assumes specific knowledge of other Godot features, mention it and
link to the corresponding documentation. For instance, a page about physics
may use signals, in which case you could note that the signals tutorial is a
prerequisite. You may also link to other websites for prerequisites beyond the
documentation's scope. For example, you could link to an introduction to
programming in the getting started guide, or a website that teaches math theory
in the math section.

Limiting cognitive load
~~~~~~~~~~~~~~~~~~~~~~~

Limit the cognitive load required to read the documentation. The simpler and
more explicit language we use, the more efficient it becomes for people to
learn. You can do so by:

1. Introducing only one new concept at a time whenever possible.
2. Using simple English, as we recommend in our writing guidelines.
3. Including one or more **concrete usage examples**. Prefer a real-world example
   to one that uses names like ``foo``, ``bar``, or ``baz``.

While many people may understand more complex language and abstract examples,
you will lose others. Understandable writing and practical examples benefit
everyone.

Always make an effort to **put yourself in the user's shoes**. When we
understand something thoroughly, it becomes obvious to us. We may fail to think
about details relevant to a newcomer, but **good documentation meets users where
they are**. We should explain each feature's capabilities or intended uses with
the most straightforward language possible.

Try to remember what you first needed to know when learning about the feature or
concept. What new terms did you need to learn? What confused you? What was the
hardest to grasp? You will want users to review your work, and we recommend you
practice explaining the feature before writing about it.

.. note::

    Programming fundamentals are a prerequisite for using a complex engine like
    Godot. Talking about variables, functions, or classes is acceptable. But we
    should favor plain language over specific terminology like
    "metaprogramming". If you need to use precise terms, be sure to define them.
