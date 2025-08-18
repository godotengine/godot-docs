.. _doc_scripting_development:

Scripting development
=====================

GDScript
--------

Annotation guidelines
~~~~~~~~~~~~~~~~~~~~~

In Godot 3 we had a lot of keywords (including ``tool``, ``export``, ``onready``).
This had the following disadvantages:

- Overcomplication of the language grammar.
- Possible conflicts with user identifiers.
- Need to touch the parser in a major way to add a new keyword.

So in Godot 4 we introduced the concept of annotations. An annotation is a modifier
(an attribute, a marker) that can be applied to an entire script, a declaration,
a statement, or a location in the source code. Annotations can optionally take
additional arguments, listed in parentheses. Annotation arguments must be constant
expressions or string literals (in a few special cases where the argument value
must be resolved in the parser rather than in the analyzer).

Currently, an annotation target can be a combination of the following
``GDScriptParser::AnnotationInfo::TargetKind`` flags:

+-----------------+----------------------------------------------+-----------------------------+
| **Target Kind** | **Description**                              | **Example**                 |
+=================+==============================================+=============================+
| ``SCRIPT``      | The entire script.                           | ``@tool``                   |
+-----------------+----------------------------------------------+-----------------------------+
| ``CLASS``       | A class (both the outermost and inner ones). | ``@abstract``               |
+-----------------+----------------------------------------------+-----------------------------+
| | ``VARIABLE``  | Other types of class members.                | ``@export``                 |
| | ``CONSTANT``  |                                              |                             |
| | ``SIGNAL``    |                                              |                             |
| | ``FUNCTION``  |                                              |                             |
+-----------------+----------------------------------------------+-----------------------------+
| ``STATEMENT``   | Statements inside a function.                | ``@warning_ignore``         |
+-----------------+----------------------------------------------+-----------------------------+
| ``STANDALONE``  | Some place inside a class or a line          | | ``@export_category``      |
|                 | in the source code.                          | | ``@warning_ignore_start`` |
|                 |                                              |                             |
|                 | 1. Class pseudo-members.                     |                             |
|                 | 2. Markers for the start and end             |                             |
|                 |    of a warning-ignoring region.             |                             |
+-----------------+----------------------------------------------+-----------------------------+

**When to use a keyword and when an annotation to implement a new feature?**

- **General rule:** Do not use keywords unless they are required by the language grammar
  and the parser. Do not use annotations for independent syntactic units.
- Use keywords for class member declarators (``var``, ``const``, ``func``).
- Use annotations for class member modifiers (``@export``, ``@onready``, ``@abstract``).
- Use keywords for operators within expressions (``and``), for delimiters in statements
  (``in``, ``when``), and declarations (``extends``).

.. note::

    For historical reasons, some existing annotations and keywords do not strictly
    follow these guidelines. Choosing between implementing a feature as an annotation
    or as a language keyword is a nuanced decision that should be made through discussion
    with other GDScript developers.
