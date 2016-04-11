
Area Input
==========

Objectives of the demo
----------------------


Bullet Lists
------------

====




Bullet lists:

- This is item 1
- This is item 2

- Bullets are "-", "*" or "+".
  Continuing text must be aligned
  after the bullet and whitespace.

* bullet
+ different bullet.
  
Note that a blank line is required
before the first item and after the
last, but is optional between items. 

Enumerated Lists
----------------

Enumerated lists:

3. This is the first item
4. This is the second item
5. Enumerators are arabic numbers,
   single letters, or roman numerals
6. List items should be sequentially
   numbered, but need not start at 1
   (although not all formatters will
   honour the first index).
#. This item is auto-enumerated 

Field Lists
-----------

:Authors:
    Tony J. (Tibs) Ibbs,
    David Goodger

    (and sundry other good-natured folks)

:Version: 1.0 of 2001/08/08
:Dedication: To my father. 

Line Blocks
-----------

| Line blocks are useful for addresses,
| verse, and adornment-free lists.
|
| Each new line begins with a
| vertical bar ("|").
|     Line breaks and initial indents
|     are preserved.
| Continuation lines are wrapped
  portions of long lines; they begin
  with spaces in place of vertical bars.
|


Tables
------

Grid table:

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

Simple table:

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

Transitions
-----------

 A transition marker is a horizontal line
of 4 or more repeated punctuation
characters.

------------

A transition should not begin or end a
section or document, nor should two
transitions be immediately adjacent. 

===============
Explicit Markup
===============

Hyperlink Targets
-----------------

External hyperlinks, like Python_.

.. _Python: http://www.python.org/ 

External hyperlinks, like `Python
<http://www.python.org/>`_.

Internal crossreferences, like example_.

.. _example:

This is an example crossreference target. 

Python_ is `my favourite
programming language`__.

.. _Python: http://www.python.org/

__ Python_ 


Directives
----------

For instance:

.. image:: images/ball1.gif 

.. code:: python

 def my_function():
     "just a test"
     print 8/2

.. |date| date::
.. |time| date:: %H:%M

Today's date is |date|.

This document was generated on |date| at |time|.

end of file...