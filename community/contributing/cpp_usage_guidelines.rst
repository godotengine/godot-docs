.. _doc_cpp_usage_guidelines:

C++ usage guidelines
====================

Rationale
---------

Since Godot 4.0, the C++ standard used throughout the codebase is a subset of
**C++17**. While modern C++ brings a lot of opportunities to write faster, more
readable code, we chose to restrict our usage of C++ to a subset for a few
reasons:

- It makes it easier to review code in online editors. This is because engine
  contributors don't always have access to a full-featured IDE while reviewing
  code.
- It makes the code easier to grasp for beginner contributors (who may not be
  professional C++ programmers). Godot's codebase is known to be easy to learn
  from, and we'd like to keep it that way.

To get your pull request merged, it needs to follow the C++ usage guidelines
outlined here. Of course, you can use features not allowed here in your own C++
modules or GDNative scripts.

.. note::

    Prior to Godot 4.0, the C++ standard used throughout the codebase was C++03,
    with a handful of C++11 extensions.

    The guidelines below don't apply to third-party dependencies, although we
    generally favor small libraries instead of larger solutions. See also
    :ref:`doc_best_practices_for_engine_contributors`.

.. seealso::

    See :ref:`doc_code_style_guidelines` for formatting guidelines.

Disallowed features
-------------------

**Any feature not listed below is allowed.** Using features like ``constexpr``
variables and ``nullptr`` is encouraged when possible. Still, try to keep your
use of modern C++ features conservative. Their use needs to serve a real
purpose, such as improving code readability or performance.

Standard Template Library
^^^^^^^^^^^^^^^^^^^^^^^^^

We don't allow using the `STL <https://en.wikipedia.org/wiki/Standard_Template_Library>`__
as Godot provides its own data types (among other things).
See :ref:`doc_faq_why_not_stl` for more information.

This means that pull requests should **not** use ``std::string``,
``std::vector`` and the like. Instead, use Godot's datatypes as described below:

- Use ``String`` instead of ``std::string``.
- Use ``Vector`` instead of ``std::vector``. In some cases, ``List`` or
  ``LocalVector`` can be used as an alternative (ask core developers first).
- Use ``Array`` instead of ``std::array``.

``auto`` keyword
^^^^^^^^^^^^^^^^

Please don't use the ``auto`` keyword for type inference. While it can avoid
repetition, it can also lead to confusing code:

.. code-block:: cpp

    // Not so confusing...
    auto button = memnew(Button);

    // ...but what about this?
    auto result = EditorNode::get_singleton()->get_complex_result();

Keep in mind hover documentation often isn't readily available for pull request
reviewers. Most of the time, reviewers will use GitHub's online viewer to review
pull requests.

We chose to forbid ``auto`` instead of allowing it on a case-by-case basis to
avoid having to decide on difficult edge cases. Thank you for your understanding.

``for`` range loop
^^^^^^^^^^^^^^^^^^

Don't use the ``for`` range loop syntax (``for (String string : some_array)``).
Use traditional ``for`` loops instead as they're more explicit.

Lambdas
^^^^^^^

Lambdas should be used conservatively when they make code effectively faster or
simpler, and do not impede readability. Please ask before using lambdas in a
pull request.

``#pragma once``
^^^^^^^^^^^^^^^^

To follow the existing style, please use standard ``#ifdef``-based include
guards instead of ``#pragma once`` in new files.

.. seealso::

    See :ref:`doc_code_style_guidelines_header_includes` for guidelines on sorting
    includes in C++ and Objective-C files.
