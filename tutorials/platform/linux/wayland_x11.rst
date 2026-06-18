.. _doc_wayland_x11:

Wayland/X11
===========

Overview
--------

One of the important components of any operating system is its display server.
Windows, macOS, iOS, visionOS, and Android only provide one option.
However, Linux has two options: X11 and Wayland.

X11 is an older standard and is being gradually phased out by the majority of
Linux distributions in favor of supporting Wayland, which has been developed as
a replacement. Wayland aims to provide modern functionality while featuring a
more robust security model compared to X11. Applications running on X11 can
still work when a distribution is using Wayland, thanks to a compatibility layer
known as Xwayland.

Godot's support is still a work in progress, so for now, X11 remains the default
setting for projects. This will likely change in a future version.

When to use Wayland
-------------------

If you're an engine developer who wants to help improve support, or if you think
Xwayland might be causing visual glitches in your exported project for whatever
reason, then we would recommend using Wayland. But outside of that it's recommended
to stick with X11 for now. It's important to note that while X11 applications can
run on Wayland, the reverse is not true.

As of June 2026, most popular distributions are using Wayland by default,
including (but not limited to) the following:

- SteamOS
- Bazzite
- CachyOS
- Fedora
- Fedora Silverblue
- Ubuntu
- OpenSUSE

Keep in mind that for some distributions like Ubuntu, users may have
changed the display server to X11 manually themselves.

.. _doc_wayland_x11_changing_display_server:

Changing the display server setting
-----------------------------------

To change your display server to Wayland, click on :menu:`Project > Project Settings`,
from here, go to :button:`Display Server` and change the :button:`driver.linuxbsd`
option to ``wayland``.

It's also possible to temporarily override the display server using the
``--display-server <x11|wayland>`` :ref:`command line argument <doc_command_line_tutorial>`
when launching the project.

.. note::

    Regardless of how the display server is defined, if the project is
    configured to use Wayland, it will automatically fall back to X11 if Wayland
    is not available.

    This also occurs the other way around; if the project is configured to use
    X11, it will fall back to Wayland if X11 is not available (i.e. when
    Xwayland isn't present on the system).

Disabling libdecor loading
--------------------------

`libdecor <https://github.com/neonkore/libdecor>`__ loading on Wayland
has some quirks; it may be useful to disable it depending on your situation.
To do that, you need to set the ``GODOT_WAYLAND_DISABLE_LIBDECOR``
environment variable to ``1`` like this:

.. tabs::
 .. code-tab:: gdscript GDScript

    OS.set_environment("GODOT_WAYLAND_DISABLE_LIBDECOR", "1")

High dynamic range support
--------------------------

Godot supports :ref:`HDR output <doc_hdr_output>` on Linux since 4.7. However,
due to display server limitations, HDR output is only supported on Wayland, not
on X11 (even through Xwayland).

Therefore, to make use of HDR output, you must
:ref:`set the display server to Wayland <doc_wayland_x11_changing_display_server>`.

.. note::

   GNOME versions prior to 50 have a bug that prevents HDR output from working
   on Wayland. If you are using an older version of GNOME, you will need to
   upgrade to version 50 or later to use HDR output on Wayland.
