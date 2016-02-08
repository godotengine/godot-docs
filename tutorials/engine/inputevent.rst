.. _doc_inputevent:

InputEvent
==========

What is it?
-----------

Managing input is usually complex, no matter the OS or platform. To ease
this a little, a special built-in type is provided, [[API:InputEvent]].
This datatype can be configured to contain several types of input
events. Input Events travel through the engine and can be received in
multiple locations, depending on the purpose.

How does it work?
-----------------

Every input event is originated from the user/player (though it's
possible to generate an InputEvent and feed then back to the engine,
which is useful for gestures). The OS object for each platform will read
events from the device, then feed the to MainLoop. As [[API::SceneTree]]
is the default MainLoop implementation, events are fed to it. Godot
provides a function to get the current SceneTree object :
**get\_tree()**.

But SceneTree does not know what to do with the event, so it will give
it to the viewports, starting by the "root" [[API:Viewport]] (the first
node of the scene tree). Viewport does quite a lot of stuff with the
received input, in order:

.. image:: /img/input_event_flow.png

1. First, it will try to feed the input to the GUI, and see if any
control can receive it. If so, the [[API:Control]] will be called the
virtual function [[API:Control.\_input\_event()]] and the signal
"input\_event" will be emitted (this function is re-implementable by
script by inheriting from it). If the control wants to "consume" the
event, it will call [[API:Control.accept\_event()]] and the event will
not spread any more.
2. If the GUI does not want the event, the standard \_input function
will be called in any node with input processing enabled (enable with
[[API:Node.set\_process\_input()]]) and override
[[API:Node.\_input()]]). If any function consumes the event, it can
call [[API:SceneTree.set\_input\_as\_handled()]], and the event will
not spread any more.
3. If so far no one consumed the event, the unhandled input callback
will be called (enable with
[[API:Node.set\_process\_unhandled\_input()]]) and override
[[API:Node.\_unhandled\_input()]]). If any function consumes the
event, it can call [[SceneTree.set\_input\_as\_handled()]], and the
event will not spread any more.
4. If no one wanted the event so far, and a [[API:Camera]] is assigned
to the Viewport, a ray to the physics world (in the ray direction from
the click) will be casted. If this ray hits an object, it will call the
[[API:CollisionObject.\_input\_event()]] function in the relevant
physics object (bodies receive this callback by default, but areas do
not. This can be configured through [[API:Area]] properties).
5. Finally, if the event was unhandled, it will be passed to the next
Viewport in the tree, or it will be ignored.

Anatomy of an InputEvent
------------------------

[[API:InputEvent]] is just a base built-in type, it does not represent
anything and only contains some basic information, such as event ID
(which is increased for each event), device index, etc.

InputEvent has a "type" member. By assigning it, it can become
different types of input event. Every type of InputEvent has different
properties, according to it's role.

Example of changing event type.

::

    # create event
    var ev = InputEvent()
    # set type index
    ev.type=InputEvent.MOUSE_BUTTON
    # button_index is only available for the above type
    ev.button_index=BUTTON_LEFT

There are several types of InputEvent, described in the table below:

+------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------------------+
| Event                              | Type Index         | Description                                                                                                       |
+------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------------------+
| [[API:InputEvent]]                 | NONE               | Empty Input Event                                                                                                 |
+------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------------------+
| [[API:InputEventKey]]              | KEY                | Contains a scancode and unicode value, as well as modifiers                                                       |
+------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------------------+
| [[API:InputEventMouseButton]]      | MOUSE\_BUTTON      | Contains click information, such as button, modifiers, etc.                                                       |
+------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------------------+
| [[API:InputEventMouseMotion]]      | MOUSE\_MOTION      | Contains motion information, such as relative, absolute positions and speed.                                      |
+------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------------------+
| [[API:InputEventJoystickMotion]]   | JOYSTICK\_MOTION   | Contains Joystick/Joypad analog axis information.                                                                 |
+------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------------------+
| [[API:InputEventJoystickButton]]   | JOYSTICK\_BUTTON   | Contains Joystick/Joypad button information.                                                                      |
+------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------------------+
| [[API:InputEventScreenTouch]]      | SCREEN\_TOUCH      | Contains multi-touch press/release information. (only available on mobile devices)                                |
+------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------------------+
| [[API:InputEventScreenDrag]]       | SCREEN\_DRAG       | Contains multi-touch drag information. (only available on mobile devices)                                         |
+------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------------------+
| [[API:InputEventAction]]           | SCREEN\_ACTION     | Contains a generic action. These events are often generated by the programmer as feedback. (more on this below)   |
+------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------------------+

Actions
-------

An InputEvent may or may not represent a pre-defined action. Actions are
useful because they abstract the input device when programming the game
logic. This allows for:

-  The same code to work on different devices with different inputs (ie:
   keyboard on PC, Joypad on console)
-  Input to be reconfigured at run-time.

Actions can be created from the Project Settings menu in the Actions
tab. If you read the :ref:`doc_simple_2d_game`, there is an explanation on how
does the action editor work.

Any event has the methods [[API:InputEvent.is\_action()]],
[[API:InputEvent.is\_pressed()]] and [[API:InputEvent.is\_echo()]].

Alternatively, it may be desired to supply the game back with an action
from the game code (a good example of this is detecting gestures).
SceneTree (derived from MainLoop) has a method for this:
[[API:MainLoop.input\_event(ev)]]. You would normally use it like this:

::

    var ev = InputEvent()
    ev.type=InputEvent.ACTION
    # set as move_left, pressed
    ev.set_as_action("move_left",true) 
    # feedback
    get_tree().input_event(ev)

InputMap
--------

Customizing and re-mapping input from code is often desired. If your
whole workflow depends on actions, the [[API:InputMap]] singleton is
ideal for reassigning or creating different actions at run-time. This
singleton is not saved (must be modified manually) and it's state is run
from the project settings (engine.cfg). So any dynamic system of this
type needs to store settings in the way the programmer sees best fit.



