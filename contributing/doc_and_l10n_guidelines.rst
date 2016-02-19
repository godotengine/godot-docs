.. _doc_doc_and_l10n_guidelines:

Documentation and localisation guidelines
=========================================

This page describes the rules to follow if you want to contribute Godot
Engine by writing documentation or translating existing documentation.

What is a good documentation?
-----------------------------

A good documentation is well written in plain English and well-formed
sentences. It is clear and objective.

A documentation page is not a tutorial page. We differentiate these
concepts by these definitions :

-  tutorial : a page aiming at explaining how to use one or more
   concepts in Godot Editor in order to achieve a specific goal with a
   learning purpose (ie. "make a simple 2d Pong game", "apply forces to
   an object"...)
-  documentation : a page describing precisely one and only one concept
   at the time, if possible exhaustively (ie. the list of methods of the
   Sprite class for example).

You are free to write the kind of documentation you wish, as long as you
respect the following rules.

Create a new wiki page
----------------------

**TODO: Needs review for Sphinx doc**

Creating a new documentation page or tutorial page is easy. The
following rules must be respected:

-  Choose a short and explicit title
-  Respect the grammar and orthography
-  Make use of the :ref:`doc_wiki_syntax`

Try to structure your page in order to enable users to include a page
directly in another page or even forum posts using the include wiki
syntax. For example, the syntax to include the page you are reading is
:

::

    :ref:`the cool documentation guidelines <doc_doc_and_l10n_guidelines>`

Titles
~~~~~~

Please always begin pages with their title and a reference based on the
file name (which should ideally be the same as the page title):

::

    .. _insert_your_title_here:

    Insert your title here
    ======================

Also, avoid American CamelCase titles: titles' first word should begin
with a capitalized letter, and every following word should not. Thus,
this is a good example:

-  Insert your title here
   And this is a bad example:
-  Insert Your Title Here

Only project names (and people names) should have capitalized first
letter. This is good:

-  Starting up with Godot Engine
   and this is bad:
-  Starting up with godot engine

Note for non-English authors
----------------------------

For the moment, we will not pull contributed pages that have no English counterpart.
We aim at providing a tool helping translators and writers to determine whether certain languages have pages that do not exist in other languages, but this is not done yet. When it is done, we will open the documentation to new contributions.

Please be patient, we are working on it ;) .

..
   If you intend to create a new page in your language, you are asked to
   firstly create the corresponding English page if it doesn't already
   exist. **Do it even if you will not write it yourself, just leave it
   blank.** Only then, create the corresponding page in your own
   language. Maybe later, another contributor will translate your new
   page to English.
   
   **Remember** : even if Godot aims at being accessible to everyone,
   English is the most frequent language for documentation.

Translating existing pages
--------------------------

**New guidelines will come soon !**

..
   **TODO: Needs review for Sphinx doc**
   
   You are very welcome to translate existing pages from English to your
   language, or from your language to English. If these guidelines were
   respected, an English page already exists for every page of this wiki,
   even if it is empty. To translate an existing page, please follow these
   few rules :
   
   -  Respect the grammar and orthography
   -  Make use of the :ref:`doc_wiki_syntax`
   -  Re-use images
   -  Always keep the structure of the English page (if it is written yet,
      follow the structure of the original language page you are
      translating from).
   
   To translate an existing page, simply copy its original content. Then,
   create the new page in the section of your language, copy the English
   content in it and start translating.
   
   Please add a line at the very beginning of your translation, linking
   to the English base page you translate from:
   
   Traduction de ![[Godot Engine:Creating 2D Games]]
   
   The previous link is of the form ![[<project name>:<project page>]] which
   enables you to add a link to a page located in an other project. Here,
   "Godot Engine" is the English project.

Important changes and discussions
---------------------------------

You are welcome to correct mistakes or styles to respect these
guidelines. However, in case of important changes, please do not start a
discussion on this page: use the forum, create a new topic with a link
to the incriminated page and start discussing there about your remarks.

Licence
-------

This wiki and every page it contains is published under the terms of the
Creative Commons BY 3.0 license.
