.. _doc_handling_quit_requests:

Handling quit requests
======================

Quitting
--------

Most platforms have the option to request the application to quit. On
desktops, this is usually done with the "x" icon on the window titlebar.
On Android, the back button is used to quit when on the main screen (and
to go back otherwise).

Handling the notification
-------------------------

The :ref:`MainLoop <class_MainLoop>`
has a special notification that is sent to all nodes when quit is
requested: MainLoop.NOTIFICATION_WM_QUIT.

Handling it is done as follows (on any node):

.. tabs::
 .. code-tab:: gdscript GDScript

    func _notification(what):
        if what == MainLoop.NOTIFICATION_WM_QUIT_REQUEST:
            get_tree().quit() # default behavior

 .. code-tab:: csharp

    public override void _Notification(int what)
    {
        if (what == MainLoop.NotificationWmQuitRequest)
            GetTree().Quit(); // default behavior
    }

When developing mobile apps, quitting is not desired unless the user is
on the main screen, so the behavior can be changed.

It is important to note that by default, Godot apps have the built-in
behavior to quit when quit is requested, this can be changed:

.. tabs::
 .. code-tab:: gdscript GDScript

    get_tree().set_auto_accept_quit(false)

 .. code-tab:: csharp

    GetTree().SetAutoAcceptQuit(false);
