.. _doc_introduction_to_godot_development:

Introduction to Godot development
=================================

This page is meant to introduce the global organization of Godot Engine's
source code, and give useful tips for extending/fixing the engine on the
C++ side.

Architecture diagram
--------------------

The following diagram describes the architecture used by Godot, from the
core components down to the abstracted drivers, via the scene
structure and the servers.

.. image:: img/architecture_diagram.jpg
