.. _doc_controller_features:

Controller features
===================

Godot supports controller-specific features that can further enhance the gameplay
experience. This page describes these features, how existing games have used them,
and how you can get started with them in Godot.

.. warning::

    These controller features are currently only supported on Windows, macOS, and Linux.


.. warning::

    Unless you specifically advertise your game as requiring specific controllers,
    remember that there is no guarantee that players will have a controller with
    any given features.

    As a result, we suggest using these features to enhance the gameplay experience
    for players whose controllers support them, without detracting from those who
    don't have controllers.


LED color
---------

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

Motion sensors (gyroscope and accelerometer)
--------------------------------------------

There are several controller brands that have implemented gyroscope and accelerometer sensors
into their modern controllers, the biggest two being PlayStation and Nintendo.

To check if a connected controller has motion sensors, we can use :ref:`Input.has_joy_motion_sensors()<class_Input_method_has_joy_motion_sensors>`.

To use the controller motion sensors, we first have to enable them, because they are disabled by default
so they don't drain the controller's battery faster in games that don't use those features.
We can enable them by calling :ref:`Input.set_joy_motion_sensors_enabled()<class_Input_method_set_joy_motion_sensors_enabled>`.

Gyroscope
~~~~~~~~~

Before we dive deeper into how motion sensors can be used in Godot games,
we first need to briefly explain how they work and what they do.

**Gyroscope** is a type of sensor that detects the device's rotation.
For example, it can be useful to make a gyroscope-based player camera
that detects the controller's rotation to precisely rotate the camera.

The following example rotates an object using a controller's gyroscope sensor.
You can also access this example by taking a look at the
:ref:`Input.start_joy_motion_sensors_calibration()<class_Input_method_start_joy_motion_sensors_calibration>` documentation.

.. code-block::
    
	const GYRO_SENSITIVITY = 10.0

	func _ready():
		# In this example we only use the first connected joypad (id 0).
		if 0 not in Input.get_connected_joypads():
			return

		if not Input.has_joy_motion_sensors(0):
			return

		# We must enable the motion sensors before using them.
		Input.set_joy_motion_sensors_enabled(0, true)

		# (Tell the users here that they need to put their joypads on a flat surface and wait for confirmation.)

		# Start the calibration process.
		calibrate_motion()

	func _process(delta):
		# Only move the object if the joypad motion sensors are calibrated.
		if Input.is_joy_motion_sensors_calibrated(0):
			move_object(delta)

	func calibrate_motion():
		Input.start_joy_motion_sensors_calibration(0)

		# Wait for some time.
		await get_tree().create_timer(1.0).timeout

		Input.stop_joy_motion_sensors_calibration(0)
		# The joypad is now calibrated.

	func move_object(delta):
		var object: Node3D = ... # Put your object here.

		var gyro := Input.get_joy_gyroscope(0)
		object.rotation.x -= -gyro.y * GYRO_SENSITIVITY * 0.5 * delta  # Use rotation around the Y axis (yaw) here.
		object.rotation.y += -gyro.x * GYRO_SENSITIVITY * delta  # Use rotation around the X axis (pitch) here.

Notice that we're using gyroscope calibration here by calling :ref:`Input.start_joy_motion_sensors_calibration()<class_Input_method_start_joy_motion_sensors_calibration>`
and :ref:`Input.stop_joy_motion_sensors_calibration()<class_Input_method_stop_joy_motion_sensors_calibration>`.
That's because modern gyroscopes often need calibration. This is like how a weighing scale can need calibration to tell it what "zero" is.
Like a weighing scale, only a correctly calibrated gyroscope will give an accurate reading.
If you're using the gyro input as a mouse, which is the simplest application of a controller's gyroscope,
you can find essential reading on `GyroWiki here <http://gyrowiki.jibbsmart.com/blog:good-gyro-controls-part-1:the-gyro-is-a-mouse>`__.
Calibration just means having the controller sit still and remembering the average reported angular velocity on each axis.
This is the gyroscope's "bias".

After the controller's gyroscope has been enabled and correctly calibrated,
you can read its reported values by using :ref:`Input.get_joy_gyroscope()<class_Input_method_get_joy_gyroscope>`.

Accelerometer
~~~~~~~~~~~~~

**Accelerometer** is a type of sensor that detects a device's acceleration in m/s².
In simpler terms, this means it can detect if the device (in our case, a controller) has been physically moved quickly.
For example, it can detect if the player quickly raises their controller, quickly moves it to the side,
or if the player is shaking the controller.
Note that, unfortunately, it does not **not** mean that the device will be able to detect precise movements that can be used to replicate a VR controller's movement (for example).

Now we can move on to using the controller's accelerometer sensor in games.
As mentioned earlier, an accelerometer is a type of sensor that detects a device's acceleration in m/s²,
but the reported values also include **the force of gravity**,
and to get just the acceleration we can subtract the gravity values from the accelerometer values
like this: ``Input.get_joy_accelerometer(device) - Input.get_joy_gravity(device)``.

Note that due to how accelerometers work physically, when it's being quickly moved to the left
the reported X value is **positive**, and it's **negative** when the controller is moved to the right.
The same is true for the other axes:
when you move the controller upwards, the acceleration's Y value becomes negative,
when you move the controller downwards, the acceleration's Y value becomes positive,
when you quickly move the controller towards you its Z value becomes negative,
and when you quickly move the controller away from you its Z value becomes positive.

And due to how accelerometers work physically, after reporting movement in one direction
they almost immediately report movement in the opposite direction.
We don't want this tutorial to become a physics lecture, so we'll just say that after you detect
movement in one direction you can make the code ignore the accelerometer readings for a small period of time
before reading them again to not read the reported opposite movement.

The following example prints the controller movement when it's being quickly moved by using its accelerometer.
If you feel like this code is too sensitive or not sensitive enough for your controller's physical movement,
you can also tweak the values used here however you feel like.

.. code-block::

    var detect_accelerometer = true

    func _ready():
        # In this example we only use the first connected joypad (id 0).
        if 0 not in Input.get_connected_joypads():
            return

        if not Input.has_joy_motion_sensors(0):
            return

        # We must enable the motion sensors before using them.
        Input.set_joy_motion_sensors_enabled(0, true)

    func _process(delta):
        if Input.has_joy_motion_sensors(0):
            accelerometer_example()

    func accelerometer_example():
        if not detect_accelerometer:
            return
            
        var acceleration = Input.get_joy_accelerometer(0) - Input.get_joy_gravity(0)
        if acceleration.length() > 10:
            if acceleration.x > 10:
                print("Moved left")
            elif acceleration.x < -10:
                print("Moved right") 
            if acceleration.y < -10:
                print("Moved up")
            elif acceleration.y > 10:
                print("Moved down")
            if acceleration.z < -10:
                print("Moved closer to the player")
            elif acceleration.z > 10:
                print("Moved away from the player")
                
            # After detecting movement in one direction, the accelerometer sensor
            # will briefly report movement in the opposite direction, even though the controller only moved once.
            # So we need to ignore these reported values for a short amount of time.
            detect_accelerometer = false
            await get_tree().create_timer(0.5, false).timeout
            detect_accelerometer = true
