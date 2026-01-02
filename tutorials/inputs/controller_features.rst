.. _doc_controller_features:

Controller features
===================

Godot supports controller-specific features that can further enhance the gameplay
experience. This page describes these features, how existing games have used them,
and how you can get started with them in Godot.

.. warning::

    Unless you specifically advertise your game as requiring specific controllers,
    remember that there is no guarantee that players will have a controller with
    given features.

    As a result, we suggest using these features to enhance the gameplay experience
    for players whose controllers support them, without detracting from those who
    don't have controllers.


LED color
---------
.. https://github.com/godotengine/godot/pull/111681

Games can use the LED lights on certain controllers to subtly complement the on-screen gameplay by
providing some matching visuals in the player's hands. Here are some notable examples:

- In *Hades*, the color of the light matches the god you're receiving a boon from.
- In *Resident Evil 2*, the color of the light indicates your health (green for full, yellow for medium, red for low).
- In *Star Wars Jedi: Fallen Order*, the color of the light matches your lightsaber's color.

Use the method :ref:`Input.set_joy_light()<class_Input_method_set_joy_light>` to set the color
of a given controller's LEDs.

To determine if a given controller supports setting LED lights, use the :ref:`Input.has_joy_light()<class_Input_method_has_joy_light>`
method. The PlayStation DualShock and DualSense controllers are known to support LED lights.

The following ``_process()`` method sets the LED color according to the currently pressed button,
and turns it off if no button is being pressed:

.. code-block::

    func _process(_delta):
        var color := Color.BLACK
        
        if Input.is_joy_button_pressed(0, JOY_BUTTON_A):
            color = Color.BLUE
        elif Input.is_joy_button_pressed(0, JOY_BUTTON_X):
            color = Color.MAGENTA
        elif Input.is_joy_button_pressed(0, JOY_BUTTON_B):
            color = Color.RED
        elif Input.is_joy_button_pressed(0, JOY_BUTTON_Y):
            color = Color.GREEN
            
        Input.set_joy_light(0, color)


The following example smoothly fades the LED through hues in a loop:

.. code-block::

    var hue = 0.0

    func _process(delta):
        var col = Color.from_hsv(hue, 1.0, 1.0)
        Input.set_joy_light(0, col)
        hue += delta * 0.1

The following example makes the LED blink red three times when the south button (Cross/X on PlayStation controllers) is pressed:

.. code-block::

    var blink_tween: Tween = null

    func _process(_delta):
        var ready_to_blink = not blink_tween or not blink_tween.is_running()
        if Input.is_joy_button_pressed(0, JOY_BUTTON_A) and ready_to_blink:
            do_blink()

    func do_blink():
        if blink_tween:
            blink_tween.kill()

        blink_tween = create_tween()
        blink_tween.tween_callback(func(): Input.set_joy_light(0, Color.RED))
        blink_tween.tween_interval(0.2)
        blink_tween.tween_callback(func(): Input.set_joy_light(0, Color.BLACK))
        blink_tween.tween_interval(0.2)
        blink_tween.set_loops(3)

