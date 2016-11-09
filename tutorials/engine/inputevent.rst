.. _doc_inputevent:

InputEvent
==========

What is it?
-----------

Managing input is usually complex, no matter the OS or platform. To ease
this a little, a special built-in type is provided, :ref:`InputEvent <class_InputEvent>`.
This datatype can be configured to contain several types of input
events. Input Events travel through the engine and can be received in
multiple locations, depending on the purpose.

How does it work?
-----------------

Every input event is originated from the user/player (though it's
possible to generate an InputEvent and feed them back to the engine,
which is useful for gestures). The OS object for each platform will read
events from the device, then feed them to MainLoop. As :ref:`SceneTree <class_SceneTree>`
is the default MainLoop implementation, events are fed to it. Godot
provides a function to get the current SceneTree object :
**get_tree()**.

But SceneTree does not know what to do with the event, so it will give
it to the viewports, starting by the "root" :ref:`Viewport <class_Viewport>` (the first
node of the scene tree). Viewport does quite a lot of stuff with the
received input, in order:

.. image:: /img/input_event_flow.png

1. First of all, the standard _input function
   will be called in any node with input processing enabled (enable with
   :ref:`Node.set_process_input() <class_Node_set_process_input>` and override
   :ref:`Node._input() <class_Node__input>`). If any function consumes the event, it can
   call :ref:`SceneTree.set_input_as_handled() <class_SceneTree_set_input_as_handled>`, and the event will
   not spread any more. This ensures that you can filter all events of interest, even before the GUI. 
   For gameplay input, the _unhandled_input() is generally a better fit, because it allows the GUI to intercept the events.
2. Second, it will try to feed the input to the GUI, and see if any
   control can receive it. If so, the :ref:`Control <class_Control>` will be called via the
   virtual function :ref:`Control._input_event() <class_Control__input_event>` and the signal
   "input_event" will be emitted (this function is re-implementable by
   script by inheriting from it). If the control wants to "consume" the
   event, it will call :ref:`Control.accept_event() <class_Control_accept_event>` and the event will
   not spread any more.
3. If so far no one consumed the event, the unhandled input callback
   will be called (enable with
   :ref:`Node.set_process_unhandled_input() <class_Node_set_process_unhandled_input>` and override
   :ref:`Node._unhandled_input() <class_Node__unhandled_input>`). If any function consumes the
   event, it can call :ref:`SceneTree.set_input_as_handled() <class_SceneTree_set_input_as_handled>`, and the
   event will not spread any more. The unhandled input callback is ideal for full-screen gameplay events, so they are not received when a GUI is active.
4. If no one wanted the event so far, and a :ref:`Camera <class_Camera>` is assigned
   to the Viewport, a ray to the physics world (in the ray direction from
   the click) will be cast. If this ray hits an object, it will call the
   :ref:`CollisionObject._input_event() <class_CollisionObject__input_event>` function in the relevant
   physics object (bodies receive this callback by default, but areas do
   not. This can be configured through :ref:`Area <class_Area>` properties).
5. Finally, if the event was unhandled, it will be passed to the next
   Viewport in the tree, otherwise it will be ignored.

Anatomy of an InputEvent
------------------------

:ref:`InputEvent <class_InputEvent>` is just a base built-in type, it does not represent
anything and only contains some basic information, such as event ID
(which is increased for each event), device index, etc.

InputEvent has a "type" member. By assigning it, it can become
different types of input event. Every type of InputEvent has different
properties, according to its role.

Example of changing event type.

::

    # create event
    var ev = InputEvent()
    # set type index
    ev.type = InputEvent.MOUSE_BUTTON
    # button_index is only available for the above type
    ev.button_index = BUTTON_LEFT

There are several types of InputEvent, described in the table below:

+-------------------------------------------------------------------+--------------------+-----------------------------------------+
| Event                                                             | Type Index         | Description                             |
+-------------------------------------------------------------------+--------------------+-----------------------------------------+
| :ref:`InputEvent <class_InputEvent>`                              | NONE               | Empty Input Event.                      |
+-------------------------------------------------------------------+--------------------+-----------------------------------------+
| :ref:`InputEventKey <class_InputEventKey>`                        | KEY                | Contains a scancode and unicode value,  |
|                                                                   |                    | as well as modifiers.                   |
+-------------------------------------------------------------------+--------------------+-----------------------------------------+
| :ref:`InputEventMouseButton <class_InputEventMouseButton>`        | MOUSE_BUTTON       | Contains click information, such as     |
|                                                                   |                    | button, modifiers, etc.                 |
+-------------------------------------------------------------------+--------------------+-----------------------------------------+
| :ref:`InputEventMouseMotion <class_InputEventMouseMotion>`        | MOUSE_MOTION       | Contains motion information, such as    |
|                                                                   |                    | relative, absolute positions and speed. |
+-------------------------------------------------------------------+--------------------+-----------------------------------------+
| :ref:`InputEventJoystickMotion <class_InputEventJoystickMotion>`  | JOYSTICK_MOTION    | Contains Joystick/Joypad analog axis    |
|                                                                   |                    | information.                            |
+-------------------------------------------------------------------+--------------------+-----------------------------------------+
| :ref:`InputEventJoystickButton <class_InputEventJoystickButton>`  | JOYSTICK_BUTTON    | Contains Joystick/Joypad button         |
|                                                                   |                    | information.                            |
+-------------------------------------------------------------------+--------------------+-----------------------------------------+
| :ref:`InputEventScreenTouch <class_InputEventScreenTouch>`        | SCREEN_TOUCH       | Contains multi-touch press/release      |
|                                                                   |                    | information. (only available on mobile  |
|                                                                   |                    | devices)                                |
+-------------------------------------------------------------------+--------------------+-----------------------------------------+
| :ref:`InputEventScreenDrag <class_InputEventScreenDrag>`          | SCREEN_DRAG        | Contains multi-touch drag information.  | 
|                                                                   |                    | (only available on mobile devices)      |
+-------------------------------------------------------------------+--------------------+-----------------------------------------+
| :ref:`InputEventAction <class_InputEventAction>`                  | SCREEN_ACTION      | Contains a generic action. These events |
|                                                                   |                    | are often generated by the programmer   |
|                                                                   |                    | as feedback. (more on this below)       |
+-------------------------------------------------------------------+--------------------+-----------------------------------------+

Actions
-------

An InputEvent may or may not represent a pre-defined action. Actions are
useful because they abstract the input device when programming the game
logic. This allows for:

-  The same code to work on different devices with different inputs (e.g.,
   keyboard on PC, Joypad on console).
-  Input to be reconfigured at run-time.

Actions can be created from the Project Settings menu in the Actions
tab. Read :ref:`doc_simple_2d_game-input_actions_setup` for an
explanation on how the action editor works.

Any event has the methods :ref:`InputEvent.is_action() <class_InputEvent_is_action>`,
:ref:`InputEvent.is_pressed() <class_InputEvent_is_pressed>` and :ref:`InputEvent <class_InputEvent>`.

Alternatively, it may be desired to supply the game back with an action
from the game code (a good example of this is detecting gestures).
SceneTree (derived from MainLoop) has a method for this:
:ref:`MainLoop.input_event() <class_MainLoop_input_event>`. You would normally use it like this:

::

    var ev = InputEvent()
    ev.type = InputEvent.ACTION
    # set as move_left, pressed
    ev.set_as_action("move_left", true) 
    # feedback
    get_tree().input_event(ev)

InputMap
--------

Customizing and re-mapping input from code is often desired. If your
whole workflow depends on actions, the :ref:`InputMap <class_InputMap>` singleton is
ideal for reassigning or creating different actions at run-time. This
singleton is not saved (must be modified manually) and its state is run
from the project settings (engine.cfg). So any dynamic system of this
type needs to store settings in the way the programmer best sees fit.
