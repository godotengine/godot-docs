.. _doc_wayland_x11:

Wayland/X11
===========

Overview
--------

One of the important components of any operating system is its display server.
Windows and MacOS only provide one option, Linux however has two, X11 and Wayland.

X11 is an older standard and is currently being gradually phased out by the majority
of linux distributions in favor of supporting Wayland, which has been developed as a
replacement. Applications running on X11 can still work when a distribution is
using Wayland thanks to a compatibility layer known as Xwayland.

Godot's support is still a work in progress, so for now X11 remains the default
setting for game projects, that will likely change in a future version.

When to use Wayland
-------------------

If you're an engine developer who wants to help improve support, or if you think
Xwayland might be causing visual glitches in your exported project for whatever
reason, then we would recommend using Wayland. But outside of that it's recommended
to stick with X11 for now. It's important to note that while X11 applications can
run on Wayland, the reverse is not true.

As of January 2026 most popular distributions are using Wayland by default,
including, but not limited to, the following:

- SteamOS
- Bazzite
- CachyOS
- Fedora
- Fedora Silverblue
- Ubuntu
- OpenSuse

Keep in mind that for some distributions, like Ubuntu, users may have
changed the display server to X11 manually themselves.

Changing the setting
--------------------

To change your display server to Wayland click on :menu:`Project > project settings`,
from here, go to :button:`Display Server` and change the :button:`driver.linuxbsd`
option to ``wayland``.

Disabling Libdecor loading
--------------------------

Libdecor loading on Wayland has some quirks and it may be useful to disable it
depending on your situation. To do that you need to set the ``GODOT_WAYLAND_DISABLE_LIBDECOR``
environment variable to ``1`` like this:

.. tabs::
 .. code-tab:: gdscript GDScript

    OS.set_environment("GODOT_WAYLAND_DISABLE_LIBDECOR", "1")
