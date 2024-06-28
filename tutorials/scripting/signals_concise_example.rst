.. _doc_signals_concise_example:

Signals, concise example
========================

.. image:: img/signals_concise_example.webp

Goal: Rotate the **yellow gate** by sending a signal from the **red button**.

``red_button.gd``

.. tabs::
  .. code-tab:: gdscript GDScript

    extends Area3D
    signal trigger(degrees_sent : int, player_color_sent : Color)
  
    func _on_body_entered(body):
        if body == %Player
            trigger.emit(90, Color.GOLD)

  .. code-tab:: csharp

        // red_button.cs
        using Godot;

---------

``yellow_gate.gd``

.. tabs::
  .. code-tab:: gdscript GDScript

    extends StaticBody3D
    
    func _ready():
        %RedButtonArea3D.trigger.connect(_on_trigger_press)
    
    func _on_trigger_press(degrees_received, player_color_received):
        rotation.x = -deg_to_rad(degrees_received)
        %"Player/Mesh".mesh.material.albedo_color = player_color_received

  .. code-tab:: csharp

        // red_button.cs
        using Godot;

Just to reiterate:

* Signal *trigger* is **defined** in sender (red button)
* Signal *trigger* is **emitted** in sender (red button)
* Signal *trigger* is **connected** in receiver (yellow gate), but pointing to the sender object first
