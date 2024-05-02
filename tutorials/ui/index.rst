:allow_comments: False

.. _doc_user_interface:

User interface (UI)
===================

In this section of the tutorial we explain the basics of creating a graphical
user interface (GUI) in Godot.

UI building blocks
------------------

Like everything else in Godot the user interface is built using nodes, specifically
:ref:`Control <class_Control>` nodes. There are many different types of controls
which are useful for creating specific types of GUIs. For simplicity we can
separate them into two groups: content and layout.

Typical content controls include:

* :ref:`Buttons <class_Button>`
* :ref:`Labels <class_Label>`
* :ref:`LineEdits <class_LineEdit>` and :ref:`TextEdits <class_TextEdit>`

Typical layout controls include:

* :ref:`BoxContainers <class_BoxContainer>`
* :ref:`MarginContainers <class_MarginContainer>`
* :ref:`ScrollContainers <class_ScrollContainer>`
* :ref:`TabContainers <class_TabContainer>`
* :ref:`Popups <class_Popup>`

The following pages explain the basics of using such controls.

.. toctree::
   :maxdepth: 1
   :name: toc-gui-basics

   size_and_anchors
   gui_containers
   custom_gui_controls
   gui_navigation
   control_node_gallery

GUI skinning and themes
-----------------------

Godot features an in-depth skinning/theming system for control nodes. The pages in this section
explain the benefits of that system and how to set it up in your projects.

.. toctree::
   :maxdepth: 1
   :name: toc-gui-skinning

   gui_skinning
   gui_using_theme_editor
   gui_theme_type_variations
   gui_using_fonts

Control node tutorials
----------------------

The following articles cover specific details of using particular control nodes.

.. toctree::
   :maxdepth: 1
   :name: toc-control-nodes-tutorials

   bbcode_in_richtextlabel
