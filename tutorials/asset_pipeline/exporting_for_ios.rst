.. _doc_exporting_for_ios:

Exporting for iOS
=================

Exporting for iOS is done manually at the moment. These are the steps to
load your game in an XCode project, where you can deploy to a device,
publish, etc.

Requirements
------------

-  Download XCode for iOS
-  Download the export templates: https://godotengine.org/download
-  Since there is no automatic deployer yet, unzip export_templates.tpz
   manually and extract GodotiOSXCode.zip from it.

The zip contains an XCode project, godot_ios.xcodeproj, an empty
data.pck file and the engine executable. Open the project, and modify
the game name, icon, organization, provisioning signing certificate
identities (??), etc.

Add your project data
---------------------

Using the Godot editor, :ref:`doc_exporting_for_pc`, to obtain the data.pck
file. Replace the empty data.pck in the XCode project with the new one,
and run/archive.

If you want to test your scenes on the iOS device as you edit them, you
can add your game directory to the project (instead of data.pck), and
add a property "godot_path" to Info.plist, with the name of your
directory as its value.

.. image:: /img/godot_path.png

Alternatively you can add all the files from your game directly, with
"engine.cfg" at the root.

Loading files from a host
-------------------------

Sometimes your game becomes too big and deploying to the device takes
too long every time you run. In that case you can deploy only the engine
executable, and serve the game files from your computer.

Setting up the file host
~~~~~~~~~~~~~~~~~~~~~~~~

On your PC, open the editor, and click the righ-most icon on the
top-center group of icons, and select "Enable File Server". The icon
turns red. Your PC will open a port and accept connections to serve
files from your project's directory (so enable your local firewall
accordingly).

.. image:: /img/rfs_server.png

Setting up the game
~~~~~~~~~~~~~~~~~~~

On XCode, click on your app name (top left, next to the "Stop" button),
and select "Edit Scheme". Go to the "Arguments" tab, and add 2
arguments, "-rfs" and the IP of your PC.

.. image:: /img/edit_scheme.png

When you run, your device will connect to the host and open the files
remotely. Note that the directory with the game data ("platformer") is
no longer added to the project, only the engine executable.

Services for iOS
----------------

Special iOS services can be used in Godot. Check out the
:ref:`doc_services_for_ios` page.
