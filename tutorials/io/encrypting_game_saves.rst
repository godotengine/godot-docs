.. _doc_encrypting_game_saves:

Encrypting game saves
=====================

Why?
----

Most users that care whether a game save is encrypted will prefer no
encryption at all. But there may be reasons to implement this feature
anyway. Encrypting saves will curb cheating; this may not be fun for users
but may be necessary in multiplayer games, games with microtransactions, or
games that hide secrets to surprise the player. This method of save
encryption is still able to be bypassed by a sufficiently savvy user
because, since the encryption key is stored inside the game, the player can
still decrypt and edit the file themselves.

The only way to prevent this from being possible is to store the save data
on a remote server, where players can only make authorized changes to their
save data. If your game deals with real money, you need to be doing this
anyway.

How?
----

The class :ref:`File <class_File>` can open a file at a
location and read/write data (integers, strings and variants).
It also supports encryption.
To create an encrypted file, a passphrase must be provided. If we just
store the passphrase in plaintext in our code, it will look something
like this:

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

We could instead extract the passphrase string from a local or remote
file, but all these methods are imperfect solutions as long as the save data
is local.

We have now curbed the reading/writing of the file by users. However, this
does not prevent users from swapping savefiles. To solve this on
iOS/Android, use OS.get_unique_id().

This function only works on mobile, but another unique user identifier
could be found for the desktop with some extra work.

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


