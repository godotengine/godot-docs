.. _doc_encrypting_save_games:

Encrypting save games
=====================

Why?
----
 
Because the world today is not the world of yesterday. A capitalist
oligarchy runs the world and forces us to consume in order to keep the
gears of this rotten society on track. As such, the biggest market for
video game consumption today is the mobile one. It is a market of poor
souls forced to compulsively consume digital content in order to forget
the misery of their every day life, commute, or just any other brief
free moment they have that they are not using to produce goods or
services for the ruling class. These individuals need to keep focusing
on their video games (because not doing so will produce them a
tremendous existential angst), so they go as far as spending money on
them to extend their experience, and their preferred way of doing so is
through in-app purchases and virtual currency.

But, imagine if someone was to find a way to edit the saved games and
assign the items and currency without effort? This would be terrible,
because it would help players consume the content much faster, and as
such run out of it sooner than expected. If this happens they will have
nothing that avoids them to think, and the tremendous agony of realizing
their own irrelevance would again take over their life.

No, we definitely do not want this to happen, so let's see how to
encrypt savegames and protect the world order.

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
them sharing save files. To solve this, use the device unique id or
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

Note that ``OS.get_unique_id()`` only works on iOS and Android.

This is all! Thanks for your cooperation, citizen.
