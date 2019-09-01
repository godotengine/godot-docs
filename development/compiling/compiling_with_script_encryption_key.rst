.. _doc_compiling_with_script_encryption_key:

Compiling with script encryption key
====================================

.. highlight:: shell

The export dialog gives you the option to encrypt your scripts with an 256bit
AES key, when releasing your game. This will make sure your scripts are not
stored in plain text and can not easily be ripped by some script kiddie.
Of course the key needs to be stored in the binary, but if it's compiled,
optimized and without symbols, it would take some effort to find it.

For this to work, you need to build the export templates from source,
with that same key.

Step by step
------------

1. Generate a 256bit AES key in HEX. You can use the aes-256-cbc variant from
   `this service <https://asecuritysite.com/encryption/keygen>`_.

   Alternatively, you can generate it yourself by using OpenSSL:

   ::

       openssl enc -aes-256-cbc -k secret -P -md sha1 > godot.gdkey

   This should output the following to ``godot.gdkey`` file:

   ::

       salt=5786FE8B91CA048A
       key=D2F90FCC4FCA64B8990F916EF5A73230C1841601D1EA06B2380EC0F530E4EF85
       iv =047C353AEC9E6C211515E3341BF9C61B

   You can generate the key without redirecting the output to a file, but
   that way you can minimize the risk of exposing the key.

2. Set this key as environment variable in the console that you will use to
   compile Godot, like this:

   .. tabs::
    .. code-tab:: bash Linux/macOS

       export SCRIPT_AES256_ENCRYPTION_KEY="your_generated_key"

    .. code-tab:: bat Windows

       set SCRIPT_AES256_ENCRYPTION_KEY=your_generated_key

3. Compile Godot export templates and set them as custom export templates
   in the export preset options.

4. Set the encryption key in the ``Script`` tab of the export preset:

   .. image:: img/script_encryption_key.png

5. Export the project. The game should run with encrypted scripts now.

Possible Errors
---------------

If you get an error like below, it means the key wasn't properly included in
your Godot build. Godot is encrypting the scripts during export, but can't read
them at runtime.

::

   ERROR: open_and_parse: Condition ' String::md5(md5.digest) != String::md5(md5d) ' is true. returned: ERR_FILE_CORRUPT
      At: core/io/file_access_encrypted.cpp:103
   ERROR: load_byte_code: Condition ' err ' is true. returned: err
      At: modules/gdscript/gdscript.cpp:755
   ERROR: load: Condition ' err != OK ' is true. returned: RES()
      At: modules/gdscript/gdscript.cpp:2135
   ERROR: Failed loading resource: res://Node2D.gde
      At: core/io/resource_loader.cpp:279
   ERROR: poll: res://Node2D.tscn:3 - Parse Error: [ext_resource] referenced nonexistent resource at: res://Node2D.gd
      At: scene/resources/scene_format_text.cpp:439
   ERROR: load: Condition ' err != OK ' is true. returned: RES()
      At: core/io/resource_loader.cpp:202
   ERROR: Failed loading resource: res://Node2D.tscn
      At: core/io/resource_loader.cpp:279
   ERROR: Failed loading scene: res://Node2D.tscn
      At: main/main.cpp:1727
   WARNING: cleanup: ObjectDB Instances still exist!
        At: core/object.cpp:2081
   ERROR: clear: Resources Still in use at Exit!
      At: core/resource.cpp:425
