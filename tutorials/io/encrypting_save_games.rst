.. _doc_encrypting_save_games:

Encrypting save games
=====================

How?
----

The class :ref:`File <class_File>` can open a file at a
location and read/write data (integers, strings and variants).
It also supports encryption.
To create an encrypted file, a passphrase must be provided, like this:

.. tabs::
 .. code-tab:: gdscript GDScript

    var f = File.new()
    var err = f.open_encrypted_with_pass("user://savedata.bin", File.WRITE, "mypass")
    f.store_var(game_state)
    f.close()

 .. code-tab:: csharp

    var f = new File();
    var err = f.OpenEncryptedWithPass("user://savedata.bin", (int)File.ModeFlags.Write, "mypass");
    f.StoreVar(gameState);
    f.Close();

This will make the file unreadable to users, but will still not prevent
them from sharing savefiles. To solve this, use the device unique id or
some unique user identifier, for example:

.. tabs::
 .. code-tab:: gdscript GDScript

    var f = File.new()
    var err = f.open_encrypted_with_pass("user://savedata.bin", File.WRITE, OS.get_unique_id())
    f.store_var(game_state)
    f.close()

 .. code-tab:: csharp

    var f = new File();
    var err = f.OpenEncryptedWithPass("user://savedata.bin", (int)File.ModeFlags.Write, OS.GetUniqueId());
    f.StoreVar(gameState);
    f.Close();

Note that ``OS.get_unique_id()`` does not work on UWP or HTML5.

That is all! Thank you for your cooperation, citizen.

.. note:: This method cannot really prevent players from editing their savegames
          locally because, since the encryption key is stored inside the game, the player
          can still decrypt and edit the file themselves. The only way to prevent this
          from being possible is to store the save data on a remote server, where players
          can only make authorized changes to their save data. If your game deals with
          real money, you need to be doing this anyway.
