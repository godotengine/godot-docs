.. _doc_exporting_for_linux:

Exporting for Linux
===================

.. seealso::

    This page describes how to export a Godot project to Linux.
    If you're looking to compile editor or export template binaries from source instead,
    read :ref:`doc_compiling_for_linuxbsd`.

The simplest way to distribute a game for PC is to copy the executable
(``godot``), compress the folder and send it to someone else. However, this is
often not desired.

Godot offers a more elegant approach for PC distribution when using the export
system. When exporting for Linux, the exporter takes all the project files and
creates a ``data.pck`` file. This file is bundled with a specially optimized
binary that is smaller, faster and does not contain the editor and debugger.

Architecture
------------

There are 7 different processor architectures that exported Godot projects can run
on in Linux:

- x86_64
- x86_32
- arm64
- arm32
- rv64
- ppc64
- loongarch64

The default is x86_64, this is the most common architecture of PC processors
today. All modern Intel and AMD processors as of writing this are x86_64.

x86_32 will give you a 32bit executable that can run on 32bit only distributions
of Linux as well as some modern distributions that are 64bit. It is NOT recommended
to use this option unless you are trying to get your project to run on an old 32bit
distribution and processor. It should also be noted that several prominent
distributions, such as Fedora, have been discussing removing their 32bit libraries
which would prevent executables made this way from running on future versions of
that distribution.

arm64 executables can run on 64bit ARM processors. If you're familiar with the
Raspberry Pi, those have utilized 64bit ARM processors since the Pi 3 (older
versions used 32bit ARM processors). If you're uploading to a platform that
supports multiple executables, such as itch.io, and you're confident your game
could run on a common ARM computer, such as the Pi 5, then we'd recommend exporting
this version and providing it as an option.

arm32 executables are for older 32bit arm processors, such as what the Raspberry Pi 1
and 2 used. Given that they're not common at all these days we do not recommend
exporting for this unless you have a computer with one of these processors you know
you can, and want to have your game running on.

rv64 is for RISC-V processors, ppc64 is for 64bit PowerPC processors, and
loongarch64 is for 64bit LoongArch processors. All of these architectures are
substantially more niche when it comes to running videogames on them. And we only
recommend exporting for them if you have a reason to, such as if you're an
enthusiast who owns hardware. Official export templates are not provided by Godot,
you will have to create them on your own. Instructions for compiling the engine for
RISC-V and creating export templates can be found on the :ref:`doc_compiling_for_linuxbsd`
page.


Environment variables
---------------------

You can use the following environment variables to set export options outside of
the editor. During the export process, these override the values that you set in
the export menu.

.. list-table:: Linux export environment variables
   :header-rows: 1

   * - Export option
     - Environment variable
   * - Encryption / Encryption Key
     - ``GODOT_SCRIPT_ENCRYPTION_KEY``

Export options
--------------

You can find a full list of export options available in the
:ref:`class_EditorExportPlatformLinuxBSD` class reference.
