:article_outdated: True

.. _doc_exporting_for_dedicated_servers:

Exporting for dedicated servers
===============================

If you want to run a dedicated server for your project on a machine that doesn't
have a GPU or display server available, you'll need to use a server build of Godot.

Platform support
----------------

- **Linux:** `Download an official Linux server binary <https://godotengine.org/download/server>`__.
  To compile a server binary from source, follow instructions in
  :ref:`doc_compiling_for_linuxbsd`.
- **macOS:** :ref:`Compile a server binary from source for macOS <doc_compiling_for_macos>`.
- **Windows:** There is no dedicated server build for Windows yet. As an alternative,
  you can use the ``--no-window`` command-line argument to prevent Godot from
  spawning a window. Note that even with the ``--no-window`` command-line argument,
  you'll need to have OpenGL support available on the Windows machine.

If your project uses C#, you'll have to use a Mono-enabled server binary.

"Headless" versus "server" binaries
-----------------------------------

The `server download page <https://godotengine.org/download/server>`__
offers two kinds of binaries with several differences.

- **Server:** Use this one for running dedicated servers. It does not contain
  editor functionality, and is therefore smaller and more
  optimized.
- **Headless:** This binary contains editor functionality and is intended to be
  used for exporting projects. This binary *can* be used to run dedicated
  servers, but it's not recommended as it's larger and less optimized.

Exporting a PCK file
--------------------

There are two ways to export a project for a server:

- Create a Linux/X11 export preset, define a custom Release export template
  that points to the server binary then export the project as usual.
- Export a PCK file only, preferably from a Linux/X11 export preset.

Both methods should result in identical output. The text below describes the PCK
file approach.

Once you've downloaded a server binary, you should export a PCK file containing
your project data. After creating the export preset, click **Export PCK/ZIP** at
the bottom of the Export dialog then choose a destination path.
The **Export With Debug** checkbox in the file dialog has no bearing on the
final PCK file, so you can leave it as-is.

See :ref:`doc_exporting_projects` for more information.

.. note::

    If you're exporting the project from a headless editor, call the headless
    editor with the `--export-pack` option while in the project folder to export
    only a PCK file.

.. note::

    The PCK file will include resources not normally needed by the server, such
    as textures and sounds. This means the PCK file will be larger than it could
    possibly be. Support for stripping unneeded resources from a PCK for server
    usage is planned in a future Godot release.

    On the bright side, this allows the same PCK file to be used both by a
    client and dedicated server build. This can be useful if you want to ship a
    single archive that can be used both as a client and dedicated server.

Preparing the server distribution
---------------------------------

After downloading or compiling a server binary, you should now place it in the
same folder as the PCK file you've exported. The server binary should have the
same name as the PCK (excluding the extension). This lets Godot detect and use
the PCK file automatically. If you want to start a server with a PCK that has a
different name, you can specify the path to the PCK file using the
``--main-pack`` command-line argument::

    ./godot-server --main-pack my_project.pck

.. warning::

    Make sure the aforementioned ``godot-server`` has the executable permission
    defined by running ``chmod +x godot-server`` (if the binary is called
    ``godot-server``). Otherwise, you may get a "command not found" or
    "permission denied" error message when trying to run the Godot server
    binary.

Starting the dedicated server
-----------------------------

If both your client and server are part of the same Godot project, you will have
to add a way to start the server directly using a command-line argument. This
can be done by adding the following code snippet in your main scene (or a
singleton)'s ``_ready()`` method:

.. tabs::
 .. code-tab:: gdscript

    if "--server" in OS.get_cmdline_args():
        # Run your server startup code here...
        # Using this check, you can start a dedicated server by running
        # a Godot binary (headless or not) with the `--server` command-line argument.
        pass

 .. code-tab:: csharp

    using System.Linq;

    if (OS.GetCmdlineArgs().Contains("--server"))
    {
        // Run your server startup code here...
        // Using this check, you can start a dedicated server by running
        // a Godot binary (headless or not) with the `--server` command-line argument.
    }

Alternatively, you can make the dedicated server always start up if a headless
or server binary is detected:

.. tabs::
 .. code-tab:: gdscript

    # Note: Feature tags are case-sensitive! It's "server", not "Server".
    if OS.has_feature("server"):
        # Run your server startup code here...
        # Note that using this check may break unit testing scripts when
        # running them with headless or server binaries.
        pass

 .. code-tab:: csharp

    // Note: Feature tags are case-sensitive! It's "server", not "Server".
    if (OS.HasFeature("server"))
    {
        // Run your server startup code here...
        // Note that using this check may break unit testing scripts when
        // running them with headless or server binaries.
    }

If your client and server are separate Godot projects, your server should most
likely be configured in a way where running the main scene starts a server
automatically.

Next steps
----------

On Linux, to make your dedicated server restart after a crash or system reboot,
you can
`create a systemd service <https://medium.com/@benmorel/creating-a-linux-service-with-systemd-611b5c8b91d6>`__.
This also lets you view server logs in a more convenient fashion, with automatic
log rotation provided by systemd.

If you have experience with containers, you could also look into wrapping your
dedicated server in a `Docker <https://www.docker.com/>`__ container. This way,
it can be used more easily in an automatic scaling setup (which is outside the
scope of this tutorial).
