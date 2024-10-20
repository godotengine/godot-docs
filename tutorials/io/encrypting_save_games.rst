.. _doc_encrypting_save_games:

Encrypting save games
=====================

The class :ref:`FileAccess <class_FileAccess>` can open a file at a
location and read/write data (integers, strings and variants).
It also supports encryption.
To create an encrypted file, a passphrase must be provided, like this:

.. tabs::
 .. code-tab:: gdscript GDScript

    var f = FileAccess.open_encrypted_with_pass("user://savedata.bin", FileAccess.WRITE, "mypass")
    f.store_var(game_state)

 .. code-tab:: csharp

    var f = FileAccess.OpenEncryptedWithPass("user://savedata.bin", (int)FileAccess.ModeFlags.Write, "mypass");
    f.StoreVar(gameState);

This will make the file unreadable to users, but will still not prevent
them from sharing savefiles. To solve this, use the device unique id or
some unique user identifier, for example:

.. tabs::
 .. code-tab:: gdscript GDScript

    var f = FileAccess.open_encrypted_with_pass("user://savedata.bin", FileAccess.WRITE, OS.get_unique_id())
    f.store_var(game_state)

 .. code-tab:: csharp

    var f = FileAccess.OpenEncryptedWithPass("user://savedata.bin", (int)FileAccess.ModeFlags.Write, OS.GetUniqueId());
    f.StoreVar(gameState);

Note that ``OS.get_unique_id()`` does not work on UWP or HTML5.

That is all! Thank you for your cooperation, citizen.

.. note:: This method cannot really prevent players from editing their savegames
          locally because, since the encryption key is stored inside the game, the player
          can still decrypt and edit the file themselves. The only way to prevent this
          from being possible is to store the save data on a remote server, where players
          can only make authorized changes to their save data. If your game deals with
          real money, you need to be doing this anyway.
