.. _doc_bbcode_in_richtextlabel:

BBCode in RichTextLabel
=======================

Introduction
------------

:ref:`class_RichTextLabel` allows to display complex text markup in a control.
It has a built-in API for generating the markup, but can also parse a BBCode.

Note that the BBCode tags can also be used to some extent in the
:ref:`XML source of the class reference <doc_updating_the_class_reference>`.

Setting up
----------

For RichTextLabel to work properly, it must be set up. This means loading
the intended fonts in the relevant properties:

.. image:: /img/rtl_setup.png

Reference
---------

+-----------------+--------------------------------------------+--------------------------------------------------------------+
| Command         | Tag                                        | Description                                                  |
+-----------------+--------------------------------------------+--------------------------------------------------------------+
| **bold**        | ``[b]{text}[/b]``                          | Makes {text} bold.                                           |
+-----------------+--------------------------------------------+--------------------------------------------------------------+
| **italics**     | ``[i]{text}[/i]``                          | Makes {text} italics.                                        |
+-----------------+--------------------------------------------+--------------------------------------------------------------+
| **underline**   | ``[u]{text}[/u]``                          | Makes {text} underline.                                      |
+-----------------+--------------------------------------------+--------------------------------------------------------------+
| **code**        | ``[code]{text}[/code]``                    | Makes {text} monospace.                                      |
+-----------------+--------------------------------------------+--------------------------------------------------------------+
| **center**      | ``[center]{text}[/center]``                | Makes {text} centered.                                       |
+-----------------+--------------------------------------------+--------------------------------------------------------------+
| **right**       | ``[right]{text}[/right]``                  | Makes {text} right-aligned.                                  |
+-----------------+--------------------------------------------+--------------------------------------------------------------+
| **fill**        | ``[fill]{text}[/fill]``                    | Makes {text} fill width.                                     |
+-----------------+--------------------------------------------+--------------------------------------------------------------+
| **indent**      | ``[indent]{text}[/indent]``                | Increase indent level of {text}.                              |
+-----------------+--------------------------------------------+--------------------------------------------------------------+
| **url**         | ``[url]{url}[/url]``                       | Show {url} as such.                                          |
+-----------------+--------------------------------------------+--------------------------------------------------------------+
| **url (ref)**   | ``[url=<url>]{text}[/url]``                | Makes {text} reference <url>.                                |
+-----------------+--------------------------------------------+--------------------------------------------------------------+
| **image**       | ``[img=<path>][/img]``                     | Insert image at resource <path>.                             |
+-----------------+--------------------------------------------+--------------------------------------------------------------+
| **font**        | ``[font=<path>]{text}[/font]``             | Use custom font at <path> for {text}.                        |
+-----------------+--------------------------------------------+--------------------------------------------------------------+
| **color**       | ``[color=<code/name>]{text}[/color]``      | Change {text} color, use # format such as #ff00ff or name.   |
+-----------------+--------------------------------------------+--------------------------------------------------------------+

Built-in color names
~~~~~~~~~~~~~~~~~~~~

List of valid color names for the [color=<name>] tag:

-  aqua
-  black
-  blue
-  fuchsia
-  gray
-  green
-  lime
-  maroon
-  navy
-  purple
-  red
-  silver
-  teal
-  white
-  yellow

Hexadecimal color codes
~~~~~~~~~~~~~~~~~~~~
 
Any valid 6 digit hexadecimal code is supported. e.g: [color=#ffffff]white[/color]
