Handling Quit Request
=====================

Quitting
--------

Most platforms have the option to request the application to quit. On
desktops, this is usually done with the "x" icon on the window titlebar.
On Android, the back button is used to quit when on the main screen (and
to go back otherwise).

Handling the Notification
-------------------------

The
`MainLoop <https://github.com/okamstudio/godot/wiki/class_mainloop>`__
has a special notification that is sent to all nodes when quit is
requested: MainLoop.NOTIFICATION\_WM\_QUIT.

Handling it is done as follows (on any node):

::

    func _notification(what):
        if (what==MainLoop.NOTIFICATION_WM_QUIT_REQUEST):
            get_tree().quit() #default behavior

When developing mobile apps, quitting is not desired unless the user is
on the main screen, so the behavior can be changed.

It is important to note that by default, Godot apps have the built-in
behavior to quit when quit is requested, this can be changed:

::

    get_tree().set_auto_accept_quit(false)

*Juan Linietsky, Ariel Manzur, Distributed under the terms of the `CC
By <https://creativecommons.org/licenses/by/3.0/legalcode>`__ license.*
