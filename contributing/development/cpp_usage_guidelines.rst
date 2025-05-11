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
modules or GDExtensions.

.. note::

    Prior to Godot 4.0, the C++ standard used throughout the codebase was C++03,
    with a handful of C++14 extensions. If you are contributing a pull request
    to the `3.x` branch rather than `master`, your code can't use C++17 features.
    Instead, your code must be able to be built with a C++14 compiler.

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

.. _doc_cpp_godot_types:

Standard Template Library
~~~~~~~~~~~~~~~~~~~~~~~~~

We don't allow using the `STL <https://en.wikipedia.org/wiki/Standard_Template_Library>`__
as Godot provides its own data types (among other things).
See :ref:`doc_faq_why_not_stl` for more information.

This means that pull requests should **not** use ``std::string``,
``std::vector`` and the like. Instead, use Godot's datatypes as described below.
A 📜 icon denotes the type is part of :ref:`Variant <doc_variant_class>`. This
means it can be used as a parameter or return value of a method exposed to the
scripting API.

+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| Godot datatype         | Closest C++ STL datatype | Comment                                                                               |
+========================+==========================+=======================================================================================+
| ``String`` 📜          | ``std::string``          | **Use this as the "default" string type.** ``String`` uses UTF-32 encoding            |
|                        |                          | to improve performance thanks to its fixed character size.                            |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``StringName`` 📜      | ``std::string``          | Uses string interning for fast comparisons. Use this for static strings that are      |
|                        |                          | referenced frequently and used in multiple locations in the engine.                   |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``Vector``             | ``std::vector``          | **Use this as the "default" vector type.** Uses copy-on-write (COW) semantics.        |
|                        |                          | This means it's generally slower but can be copied around almost for free.            |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``LocalVector``        | ``std::vector``          | Closer to ``std::vector`` in semantics. In most situations, ``Vector`` should be      |
|                        |                          | preferred.                                                                            |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``Array`` 📜           | ``std::vector``          | Values can be of any Variant type. No static typing is imposed.                       |
|                        |                          | Uses shared reference counting, similar to ``std::shared_ptr``.                       |
|                        |                          | Uses Vector<Variant> internally.                                                      |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``TypedArray`` 📜      | ``std::vector``          | Subclass of ``Array`` but with static typing for its elements.                        |
|                        |                          | Not to be confused with ``Packed*Array``, which is internally a ``Vector``.           |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``Packed*Array`` 📜    | ``std::vector``          | Alias of ``Vector``, e.g. ``PackedColorArray = Vector<Color>``.                       |
|                        |                          | Only a limited list of packed array types are available                               |
|                        |                          | (use ``TypedArray`` otherwise).                                                       |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``List``               | ``std::list``            | Linked list type. Generally slower than other array/vector types. Prefer using        |
|                        |                          | other types in new code, unless using ``List`` avoids the need for type conversions.  |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``FixedVector``        | ``std::array``           | Vector with a fixed capacity (more similar to ``boost::container::static_vector``).   |
|                        |                          | This container type is more efficient than other vector-like types because it makes   |
|                        |                          | no heap allocations.                                                                  |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``Span``               | ``std::span``            | Represents read-only access to a contiguous array without needing to copy any data.   |
|                        |                          | See `pull request description <https://github.com/godotengine/godot/pull/100293>`__   |
|                        |                          | for details.                                                                          |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``HashSet``            | ``std::unordered_set``   | **Use this as the "default" set type.**                                               |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``RBSet``              | ``std::set``             | Uses a `red-black tree <https://en.wikipedia.org/wiki/Red-black_tree>`__              |
|                        |                          | for faster access.                                                                    |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``VSet``               | ``std::flat_set``        | Uses copy-on-write (COW) semantics.                                                   |
|                        |                          | This means it's generally slower but can be copied around almost for free.            |
|                        |                          | The performance benefits of ``VSet`` aren't established, so prefer using other types. |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``HashMap``            | ``std::unordered_map``   | **Use this as the "default" map type.** Preserves insertion order.                    |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``AHashMap``           | ``std::unordered_map``   | Array-based implementation of a hash map. Does not preserve insertion order.          |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``OAHashMap``          | ``std::unordered_map``   | Does not preserve insertion order.                                                    |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``RBMap``              | ``std::map``             | Uses a `red-black tree <https://en.wikipedia.org/wiki/Red-black_tree>`__              |
|                        |                          | for faster access.                                                                    |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``VMap``               | ``std::flat_map``        | Uses copy-on-write (COW) semantics.                                                   |
|                        |                          | This means it's generally slower but can be copied around almost for free.            |
|                        |                          | The performance benefits of ``VMap`` aren't established, so prefer using other types. |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``Dictionary`` 📜      | ``std::unordered_map``   | Keys and values can be of any Variant type. No static typing is imposed.              |
|                        |                          | Uses shared reference counting, similar to ``std::shared_ptr``.                       |
|                        |                          | Preserves insertion order. Uses ``HashMap<Variant>`` internally.                      |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``TypedDictionary`` 📜 | ``std::unordered_map``   | Subclass of ``Dictionary`` but with static typing for its keys and values.            |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+
| ``Pair``               | ``std::pair``            | Stores a single key-value pair.                                                       |
+------------------------+--------------------------+---------------------------------------------------------------------------------------+

``auto`` keyword
~~~~~~~~~~~~~~~~

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

The ``auto`` keyword can be used in some special cases, like C++ lambda or Objective-C block
definitions and C++ templates. Please ask before using templates with ``auto`` in a pull request.

.. code-block:: cpp

    // Full type definitions.
    void (*mult64to128)(uint64_t, uint64_t, uint64_t &, uint64_t &) = [](uint64_t u, uint64_t v, uint64_t &h, uint64_t &l) { ... }
    void (^JOYSTICK_LEFT)(GCControllerDirectionPad *__strong, float, float) = ^(GCControllerDirectionPad *dpad, float xValue, float yValue) { ... }

    // Less clutter with auto.
    auto mult64to128 = [](uint64_t u, uint64_t v, uint64_t &h, uint64_t &l) { ... }
    auto JOYSTICK_LEFT = ^(GCControllerDirectionPad *dpad, float xValue, float yValue) { ... }

    // Compare function for different types.
    template <typename T1, typename T2>
    constexpr auto MIN(const T1 m_a, const T2 m_b) {
        return m_a < m_b ? m_a : m_b;
    }

We chose to forbid ``auto`` in all other cases. Thank you for your understanding.

Lambdas
~~~~~~~

Lambdas should be used conservatively when they make code effectively faster or
simpler, and do not impede readability. Please ask before using lambdas in a
pull request.

``#ifdef``-based include guards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting with 4.5, all files now use the ``#pragma once`` directive, as they
improve readability and declutter macros. Use of ``#ifdef``-based include
guards are now actively discouraged.

``try``-``catch`` blocks
~~~~~~~~~~~~~~~~~~~~~~~~

C++ style exception handling using ``try`` and ``catch`` blocks is forbidden.
This restriction is in place for several reasons, including performance, binary
size and code complexity.
Use :ref:`doc_common_engine_methods_and_macros_error_macros` instead.


.. seealso::

    See :ref:`doc_code_style_guidelines_header_includes` for guidelines on sorting
    includes in C++ and Objective-C files.
