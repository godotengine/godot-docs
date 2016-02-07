Custom GUI Controls
===================

So Many Controls..
------------------

Yet there are never enough. Creating your own custom controls that act
just the way you want them is an obsession of almost every GUI
programmer. Godot provides plenty of them, but they may not work exactly
the way you want. Before contacting the developers with a pull-request
to support diagonal scrollbars, at least it will be good to know how to
create these controls easily from script.

Drawing
-------

For drawing, it is recommended to check the [[Custom Draw 2D]] tutorial.
The same applies. Some functions are worth mentioning due to their
usefulness when drawing, so they will be detailed next:

Checking Control Size
~~~~~~~~~~~~~~~~~~~~~

Unlike 2D nodes, "size" is very important with controls, as it helps to
organize them in proper layouts. For this, the
`Control.get\_size() <https://github.com/okamstudio/godot/wiki/class_control#get_size>`__
method is provided. Checking it during \_draw() is vital to ensure
everything is kept in-bounds.

Checking Focus
~~~~~~~~~~~~~~

Some controls (such as buttons or text editors) might provide input
focus for keyboard or joypad input. Examples of this are entering text
or pressing a button. This is controlled with the
`Control.set\_focus\_mode() <https://github.com/okamstudio/godot/wiki/class_control#set_focus_mode>`__
function. When drawing, and if the control supports input focus, it is
always desired to show some sort of indicator (highight, box, etc) to
indicate that this is the currently focused control. To check for this
status, the
`Control.has\_focus() <https://github.com/okamstudio/godot/wiki/class_control#has_focus>`__
exists. Example

::

    func _draw():
        if (has_focus()):
             draw_selected()
        else:
             draw_normal()

Sizing
------

As mentioned before, size is very important to controls. This allows
them to lay out properly, when set into grids, containers, or anchored.
Controls most of the time provide a *minimum size* to help to properly
lay them out. For example, if controls are placed vertically on top of
each other using a
`VBoxContainer <https://github.com/okamstudio/godot/wiki/class_vboxcontainer>`__,
the minimum size will make sure your custom control is not squished by
the other controls in the container.

To provide this callback, just override
`Control.get\_minimum\_size() <https://github.com/okamstudio/godot/wiki/class_control#get_minimum_size>`__,
for example:

::

    func get_minimum_size(): 
        return Vector2(30,30)

Or alternatively, set it via function:

::

    func _ready():
        set_custom_minimum_size( Vector2(30,30) )

Input
-----

Controls provide a few helpers to make managing input events much esier
than regular nodes.

Input Events
~~~~~~~~~~~~

There are a few tutorials about input before this one, but it's worth
mentioning that controls have a special input method that only works
when:

-  The mouse pointer is over the control.
-  The left button was pressed over this control (control always
   captures input until button si released)
-  Control provides keyboard/joypad focus via
   `Control.set\_focus\_mode <https://github.com/okamstudio/godot/wiki/class_control#set_focus_mode>`__.

This function is
`Control.\_input\_event(event) <https://github.com/okamstudio/godot/wiki/class_control#_input_event>`__.
Simply override it in your control. No processing needs to be set.

::

    extends Control

    func _input_event(ev):
       if (ev.type==InputEvent.MOUSE_BUTTON and ev.button_index==BUTTON_LEFT and ev.pressed):
           print("Left mouse button was pressed!")

For more information about events themselves, check the [[Input Events]]
tutorial.

Notifications
~~~~~~~~~~~~~

Controls also have many useful notifications for which no callback
exists, but can be checked with the \_notification callback:

::

    func _notification(what):

       if (what==NOTIFICATION_MOUSE_ENTER):
          pass # mouse entered the area of this control
       elif (what==NOTIFICATION_MOUSE_EXIT):
          pass # mouse exited the area of this control
       elif (what==NOTIFICATION_FOCUS_ENTER):
          pass # control gained focus
       elif (what==NOTIFICATION_FOCUS_EXIT):
          pass # control lost focus
       elif (what==NOTIFICATION_THEME_CHANGED):
          pass # theme used to draw the control changed
          # update and redraw is recommended if using a theme
       elif (what==NOTIFICATION_VISIBILITY_CHANGED):
          pass # control became visible/invisible
          # check new status with is_visible()
       elif (what==NOTIFICATION_THEME_CHANGED):
          pass # theme used to draw the control changed
          # update and redraw is recommended if using a theme
       elif (what==NOTIFICATION_RESIZED):
          pass # control changed size, check new size
          # with get_size()
       elif (what==NOTIFICATION_MODAL_CLOSED):
          pass # for modal popups, notification
          # that the popup was closed

