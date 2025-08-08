.. _doc_scripting_development:

Scripting development
=====================

GDScript
--------

Annotation guidelines
~~~~~~~~~~~~~~~~~~~~~

..
    This description intentionally avoids mention of implementation and
    compilation details because these are often inconsistent between annotations

Create annotations for modifiers that act on the script or its code.
Additionally, create annotations for behavior that is specific to the Godot
engine and editor; if the primary purpose is to affect the way that the engine
or editor treats or interacts with the script, implement the token as an
annotation.

Do not create annotations for general programming language features.

::

    # Affects how the editor treats this script.
    @icon("res://path/to/class/icon.svg")
    
    # Affects how the engine interacts with this script.
    @onready var character_name = $Label

    # static is a general programming language feature.
    static var num_players = 2

For historical reasons, some existing annotations and keywords do not strictly
follow these guidelines. Choosing between implementing a feature as an
annotation or as a language keyword is a nuanced decision that should be made
through discussion with other GDScript developers.
