.. _class_RegEx:

RegEx
=====

Inherits: :ref:`Reference<class_reference>`
-------------------------------------------

Category: Core
--------------

Brief Description
-----------------

Simple regular expression matcher.

Member Functions
----------------

+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                  | :ref:`compile<class_RegEx_compile>`  **(** :ref:`String<class_string>` pattern, :ref:`int<class_int>` capture=9  **)**                          |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                  | :ref:`find<class_RegEx_find>`  **(** :ref:`String<class_string>` text, :ref:`int<class_int>` start=0, :ref:`int<class_int>` end=-1  **)** const |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`clear<class_RegEx_clear>`  **(** **)**                                                                                                    |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`is_valid<class_RegEx_is_valid>`  **(** **)** const                                                                                        |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                  | :ref:`get_capture_count<class_RegEx_get_capture_count>`  **(** **)** const                                                                      |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`            | :ref:`get_capture<class_RegEx_get_capture>`  **(** :ref:`int<class_int>` capture  **)** const                                                   |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`StringArray<class_stringarray>`  | :ref:`get_captures<class_RegEx_get_captures>`  **(** **)** const                                                                                |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

Class for finding text patterns in a string using regular expressions. Regular expressions are a way to define patterns of text to be searched.

This class only finds patterns in a string. It can not perform replacements.

Usage of regular expressions is too long to be explained here, but Internet is full of tutorials and detailed explanations.

Currently supported features:

Capturing :ref:`code<class_code>`():ref:`/code<class_/code>` and non-capturing :ref:`code<class_code>`(?:):ref:`/code<class_/code>` groups

Any character :ref:`code<class_code>`.:ref:`/code<class_/code>`

Shorthand caracter classes :ref:`code<class_code>`\w \W \s \S \d \D:ref:`/code<class_/code>`

User-defined character classes such as :ref:`code<class_code>`:ref:`A-Za-z<class_a-za-z>`:ref:`/code<class_/code>`

Simple quantifiers :ref:`code<class_code>`?:ref:`/code<class_/code>`, :ref:`code<class_code>`*:ref:`/code<class_/code>` and :ref:`code<class_code>`+:ref:`/code<class_/code>`

Range quantifiers :ref:`code<class_code>`{x,y}:ref:`/code<class_/code>`

Lazy (non-greedy) quantifiers :ref:`code<class_code>`*?:ref:`/code<class_/code>`

Begining :ref:`code<class_code>`^:ref:`/code<class_/code>` and end :ref:`code<class_code>`$:ref:`/code<class_/code>` anchors

Alternation :ref:`code<class_code>`|:ref:`/code<class_/code>`

Backreferences :ref:`code<class_code>`\1:ref:`/code<class_/code>` and :ref:`code<class_code>`\g{1}:ref:`/code<class_/code>`

POSIX character classes :ref:`code<class_code>`:ref:`[:alnum:<class_[:alnum:>`]:ref:`/code<class_/code>`

Lookahead :ref:`code<class_code>`(?=):ref:`/code<class_/code>`, :ref:`code<class_code>`(?!):ref:`/code<class_/code>` and lookbehind :ref:`code<class_code>`(?<=):ref:`/code<class_/code>`, :ref:`code<class_code>`(?<!):ref:`/code<class_/code>`

ASCII :ref:`code<class_code>`\xFF:ref:`/code<class_/code>` and Unicode :ref:`code<class_code>`\uFFFF:ref:`/code<class_/code>` code points (in a style similar to Python)

Word boundaries :ref:`code<class_code>`\b:ref:`/code<class_/code>`, :ref:`code<class_code>`\B:ref:`/code<class_/code>`

Member Function Description
---------------------------

.. _class_RegEx_compile:

- :ref:`int<class_int>`  **compile**  **(** :ref:`String<class_string>` pattern, :ref:`int<class_int>` capture=9  **)**

Compiles and assign the regular expression pattern to use. The limit on the number of capturing groups can be specified or made unlimited if negative.

.. _class_RegEx_find:

- :ref:`int<class_int>`  **find**  **(** :ref:`String<class_string>` text, :ref:`int<class_int>` start=0, :ref:`int<class_int>` end=-1  **)** const

This method tries to find the pattern within the string, and returns the position where it was found. It also stores any capturing group (see :ref:`get_capture<RegEx_get_capture>`) for further retrieval.

.. _class_RegEx_clear:

- void  **clear**  **(** **)**

This method resets the state of the object, as it was freshly created. Namely, it unassigns the regular expression of this object, and forgets all captures made by the last :ref:`find<RegEx_find>`.

.. _class_RegEx_is_valid:

- :ref:`bool<class_bool>`  **is_valid**  **(** **)** const

Returns whether this object has a valid regular expression assigned.

.. _class_RegEx_get_capture_count:

- :ref:`int<class_int>`  **get_capture_count**  **(** **)** const

Returns the number of capturing groups. A captured group is the part of a string that matches a part of the pattern delimited by parentheses (unless they are non-capturing parentheses *(?:)*).

.. _class_RegEx_get_capture:

- :ref:`String<class_string>`  **get_capture**  **(** :ref:`int<class_int>` capture  **)** const

Returns a captured group. A captured group is the part of a string that matches a part of the pattern delimited by parentheses (unless they are non-capturing parentheses *(?:)*).

.. _class_RegEx_get_captures:

- :ref:`StringArray<class_stringarray>`  **get_captures**  **(** **)** const

Return a list of all the captures made by the regular expression.


