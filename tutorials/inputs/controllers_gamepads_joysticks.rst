.. _doc_controllers_gamepads_joysticks:

Controllers, gamepads, and joysticks
====================================

Godot supports hundreds of controller models out of the box.
Controllers are supported on Windows, macOS, Linux, Android, iOS, and Web.

.. note::

    Since Godot 4.5, the engine relies on `SDL 3 <https://www.libsdl.org/index.php>`__
    for controller support on Windows, macOS, and Linux. This means the list of
    supported controllers and their behavior should closely match what is available
    in other games and engines using SDL 3. Note that SDL is only used for input,
    not for windowing or sound.

    Prior to Godot 4.5, the engine used its own controller support code.
    This can cause certain controllers to behave incorrectly.
    This custom code is still used to support controllers on Android, iOS,
    and Web, so it may result in issues appearing only on those platforms.

Note that more specialized devices such as steering wheels, rudder pedals and
`HOTAS <https://en.wikipedia.org/wiki/HOTAS>`__ are less tested and may not
always work as expected. Overriding force feedback for those devices is also not
implemented yet. If you have access to one of those devices, don't hesitate to
`report bugs on GitHub
<https://github.com/godotengine/godot/blob/master/CONTRIBUTING.md#reporting-bugs>`__.

In this guide, you will learn:

- **How to write your input logic to support both keyboard and controller inputs.**
- **How controllers can behave differently from keyboard/mouse input.**
- **Troubleshooting issues with controllers in Godot.**

Supporting universal input
--------------------------

Thanks to Godot's input action system, Godot makes it possible to support both
keyboard and controller input without having to write separate code paths.
Instead of hardcoding keys or controller buttons in your scripts, you should
create *input actions* in the Project Settings which will then refer to
specified key and controller inputs.

Input actions are explained in detail on the :ref:`doc_inputevent` page.

.. note::

    Unlike keyboard input, supporting both mouse and controller input for an
    action (such as looking around in a first-person game) will require
    different code paths since these have to be handled separately.

Which Input singleton method should I use?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are 3 ways to get input in an analog-aware way:

- When you have two axes (such as joystick or WASD movement) and want both
  axes to behave as a single input, use ``Input.get_vector()``:

.. tabs::
 .. code-tab:: gdscript GDScript

    # `velocity` will be a Vector2 between `Vector2(-1.0, -1.0)` and `Vector2(1.0, 1.0)`.
    # This handles deadzone in a correct way for most use cases.
    # The resulting deadzone will have a circular shape as it generally should.
    var velocity = Input.get_vector("move_left", "move_right", "move_forward", "move_back")

    # The line below is similar to `get_vector()`, except that it handles
    # the deadzone in a less optimal way. The resulting deadzone will have
    # a square-ish shape when it should ideally have a circular shape.
    var velocity = Vector2(
            Input.get_action_strength("move_right") - Input.get_action_strength("move_left"),
            Input.get_action_strength("move_back") - Input.get_action_strength("move_forward")
    ).limit_length(1.0)

 .. code-tab:: csharp

    // `velocity` will be a Vector2 between `Vector2(-1.0, -1.0)` and `Vector2(1.0, 1.0)`.
    // This handles deadzone in a correct way for most use cases.
    // The resulting deadzone will have a circular shape as it generally should.
    Vector2 velocity = Input.GetVector("move_left", "move_right", "move_forward", "move_back");

    // The line below is similar to `get_vector()`, except that it handles
    // the deadzone in a less optimal way. The resulting deadzone will have
    // a square-ish shape when it should ideally have a circular shape.
    Vector2 velocity = new Vector2(
            Input.GetActionStrength("move_right") - Input.GetActionStrength("move_left"),
            Input.GetActionStrength("move_back") - Input.GetActionStrength("move_forward")
    ).LimitLength(1.0);

- When you have one axis that can go both ways (such as a throttle on a
  flight stick), or when you want to handle separate axes individually,
  use ``Input.get_axis()``:

.. tabs::
 .. code-tab:: gdscript GDScript

    # `walk` will be a floating-point number between `-1.0` and `1.0`.
    var walk = Input.get_axis("move_left", "move_right")

    # The line above is a shorter form of:
    var walk = Input.get_action_strength("move_right") - Input.get_action_strength("move_left")

 .. code-tab:: csharp

    // `walk` will be a floating-point number between `-1.0` and `1.0`.
    float walk = Input.GetAxis("move_left", "move_right");

    // The line above is a shorter form of:
    float walk = Input.GetActionStrength("move_right") - Input.GetActionStrength("move_left");

- For other types of analog input, such as handling a trigger or handling
  one direction at a time, use ``Input.get_action_strength()``:

.. tabs::
 .. code-tab:: gdscript GDScript

    # `strength` will be a floating-point number between `0.0` and `1.0`.
    var strength = Input.get_action_strength("accelerate")

 .. code-tab:: csharp

    // `strength` will be a floating-point number between `0.0` and `1.0`.
    float strength = Input.GetActionStrength("accelerate");

For non-analog digital/boolean input (only "pressed" or "not pressed" values),
such as controller buttons, mouse buttons or keyboard keys,
use ``Input.is_action_pressed()``:

.. tabs::
 .. code-tab:: gdscript GDScript

    # `jumping` will be a boolean with a value of `true` or `false`.
    var jumping = Input.is_action_pressed("jump")

 .. code-tab:: csharp

    // `jumping` will be a boolean with a value of `true` or `false`.
    bool jumping = Input.IsActionPressed("jump");

.. note::

    If you need to know whether an input was *just* pressed in the previous
    frame, use ``Input.is_action_just_pressed()`` instead of
    ``Input.is_action_pressed()``. Unlike ``Input.is_action_pressed()`` which
    returns ``true`` as long as the input is
    held, ``Input.is_action_just_pressed()`` will only return ``true`` for one
    frame after the button has been pressed.

Vibration
---------

Vibration (also called *haptic feedback*) can be used to enhance the feel of a
game. For instance, in a racing game, you can convey the surface the car is
currently driving on through vibration, or create a sudden vibration on a crash.

Use the Input singleton's
:ref:`start_joy_vibration<class_Input_method_start_joy_vibration>` method to
start vibrating a gamepad. Use
:ref:`stop_joy_vibration<class_Input_method_stop_joy_vibration>` to stop
vibration early (useful if no duration was specified when starting).

On mobile devices, you can also use
:ref:`vibrate_handheld<class_Input_method_vibrate_handheld>` to vibrate the
device itself (independently from the gamepad). On Android, this requires the
``VIBRATE`` permission to be enabled in the Android export preset before
exporting the project.

.. note::

   Vibration can be uncomfortable for certain players. Make sure to provide an
   in-game slider to disable vibration or reduce its intensity.

Differences between keyboard/mouse and controller input
-------------------------------------------------------

If you're used to handling keyboard and mouse input, you may be surprised by how
controllers handle specific situations.

Dead zone
~~~~~~~~~

Unlike keyboards and mice, controllers offer axes with *analog* inputs. The
upside of analog inputs is that they offer additional flexibility for actions.
Unlike digital inputs which can only provide strengths of ``0.0`` and ``1.0``,
an analog input can provide *any* strength between ``0.0`` and ``1.0``. The
downside is that without a deadzone system, an analog axis' strength will never
be equal to ``0.0`` due to how the controller is physically built. Instead, it
will linger at a low value such as ``0.062``. This phenomenon is known as
*drifting* and can be more noticeable on old or faulty controllers.

Let's take a racing game as a real-world example. Thanks to analog inputs, we
can steer the car slowly in one direction or another. However, without a
deadzone system, the car would slowly steer by itself even if the player isn't
touching the joystick. This is because the directional axis strength won't be
equal to ``0.0`` when we expect it to. Since we don't want our car to steer by
itself in this case, we define a "dead zone" value of ``0.2`` which will ignore
all input whose strength is lower than ``0.2``. An ideal dead zone value is high
enough to ignore the input caused by joystick drifting, but is low enough to not
ignore actual input from the player.

Godot features a built-in deadzone system to tackle this problem. The default
value is ``0.5``, but you can adjust it on a per-action basis in the Project
Settings' Input Map tab. For ``Input.get_vector()``, the deadzone can be
specified as an optional 5th parameter. If not specified, it will calculate the
average deadzone value from all of the actions in the vector.

"Echo" events
~~~~~~~~~~~~~

Unlike keyboard input, holding down a controller button such as a D-pad
direction will **not** generate repeated input events at fixed intervals (also
known as "echo" events). This is because the operating system never sends "echo"
events for controller input in the first place.

If you want controller buttons to send echo events, you will have to generate
:ref:`class_InputEvent` objects by code and parse them using
:ref:`Input.parse_input_event() <class_Input_method_parse_input_event>`
at regular intervals. This can be accomplished
with the help of a :ref:`class_Timer` node.

Window focus
~~~~~~~~~~~~

Unlike keyboard input, controller inputs can be seen by **all** windows on the
operating system, including unfocused windows.

While this is useful for
`third-party split screen functionality <https://nucleus-coop.github.io/>`__,
it can also have adverse effects. Players may accidentally send controller inputs
to the running project while interacting with another window.

If you wish to ignore events when the project window isn't focused, you will
need to create an :ref:`autoload <doc_singletons_autoload>` called ``Focus``
with the following script and use it to check all your inputs:

::

    # Focus.gd
    extends Node

    var focused := true

    func _notification(what: int) -> void:
        match what:
            NOTIFICATION_APPLICATION_FOCUS_OUT:
                focused = false
            NOTIFICATION_APPLICATION_FOCUS_IN:
                focused = true


    func input_is_action_pressed(action: StringName) -> bool:
        if focused:
            return Input.is_action_pressed(action)

        return false


    func event_is_action_pressed(event: InputEvent, action: StringName) -> bool:
        if focused:
            return event.is_action_pressed(action)

        return false

Then, instead of using ``Input.is_action_pressed(action)``, use
``Focus.input_is_action_pressed(action)`` where ``action`` is the name of
the input action. Also, instead of using ``event.is_action_pressed(action)``,
use ``Focus.event_is_action_pressed(event, action)`` where ``event`` is an
InputEvent reference and ``action`` is the name of the input action.

Power saving prevention
~~~~~~~~~~~~~~~~~~~~~~~

Unlike keyboard and mouse input, controller inputs do **not** inhibit sleep and
power saving measures (such as turning off the screen after a certain amount of
time has passed).

To combat this, Godot enables power saving prevention by default when a project
is running. If you notice the system is turning off its display when playing
with a gamepad, check the value of **Display > Window > Energy Saving > Keep Screen On**
in the Project Settings.

On Linux, power saving prevention requires the engine to be able to use D-Bus.
Check whether D-Bus is installed and reachable if running the project within a
Flatpak, as sandboxing restrictions may make this impossible by default.

Troubleshooting
---------------

.. seealso::

    You can view a list of
    `known issues with controller support <https://github.com/godotengine/godot/issues?q=is%3Aopen+is%3Aissue+label%3Atopic%3Ainput+gamepad>`__
    on GitHub.

My controller isn't recognized by Godot.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, check that your controller is recognized by other applications. You can
use the `Gamepad Tester <https://hardwaretester.com/gamepad>`__ website to confirm
that your controller is recognized.

On Windows Godot only supports up to 4 controllers at a time. This is
because Godot uses the XInput API, which is limited to supporting 4 controllers
at once. Additional controllers above this limit are ignored by Godot.

My controller has incorrectly mapped buttons or axes.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, if your controller provides some kind of firmware update utility,
make sure to run it to get the latest fixes from the manufacturer. For instance,
Xbox One and Xbox Series controllers can have their firmware updated using the
`Xbox Accessories app <https://www.microsoft.com/en-us/p/xbox-accessories/9nblggh30xj3>`__.
(This application only runs on Windows, so you have to use a Windows machine
or a Windows virtual machine with USB support to update the controller's firmware.)
After updating the controller's firmware, unpair the controller and pair it again
with your PC if you are using the controller in wireless mode.

If buttons are incorrectly mapped, this may be due to an erroneous mapping from
the SDL game controller database used by Godot or the
`Godot game controller database <https://github.com/godotengine/godot/blob/master/core/input/godotcontrollerdb.txt>`__.
In this case, you will need to create a custom mapping for your controller.

There are many ways to create mappings. One option is to use the mapping wizard
in the `official Joypads demo <https://godotengine.org/asset-library/asset/2785>`__.
Once you have a working mapping for your controller, you can test it by defining
the ``SDL_GAMECONTROLLERCONFIG`` environment variable before running Godot:

.. tabs::
 .. code-tab:: bash Linux/macOS

    export SDL_GAMECONTROLLERCONFIG="your:mapping:here"
    ./path/to/godot.x86_64

 .. code-tab:: bat Windows (cmd)

    set SDL_GAMECONTROLLERCONFIG=your:mapping:here
    path\to\godot.exe

 .. code-tab:: powershell Windows (PowerShell)

    $env:SDL_GAMECONTROLLERCONFIG="your:mapping:here"
    path\to\godot.exe

To test mappings on non-desktop platforms or to distribute your project with
additional controller mappings, you can add them by calling
:ref:`Input.add_joy_mapping() <class_Input_method_add_joy_mapping>`
as early as possible in a script's ``_ready()`` function.

Once you are satisfied with the custom mapping, you can contribute it for
the next Godot version by opening a pull request on the
`Godot game controller database <https://github.com/godotengine/godot/blob/master/core/input/godotcontrollerdb.txt>`__.

My controller works on a given platform, but not on another platform.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Linux
^^^^^

If you're using a self-compiled engine binary, make sure it was compiled with
udev support. This is enabled by default, but it is possible to disable udev
support by specifying ``udev=no`` on the SCons command line. If you're using an
engine binary supplied by a Linux distribution, double-check whether it was
compiled with udev support.

Controllers can still work without udev support, but it is less reliable as
regular polling must be used to check for controllers being connected or
disconnected during gameplay (hotplugging).

Android/iOS
^^^^^^^^^^^

As described at the top of the page, controller support on mobile platforms relies
on a custom implementation instead of using SDL for input. This means controller
support may be less reliable than on desktop platforms.

Support for SDL-based controller input on mobile platforms is
`planned <https://github.com/godotengine/godot/pull/109645>`__
in a future release.

Web
^^^

Web controller support is often less reliable compared to "native" platforms.
The quality of controller support tends to vary wildly across browsers. As a
result, you may have to instruct your players to use a different browser if they
can't get their controller to work.

Like for mobile platforms, support for SDL-based controller input on the web platform
is `planned <https://github.com/godotengine/godot/pull/109645>`__ in a future release.
