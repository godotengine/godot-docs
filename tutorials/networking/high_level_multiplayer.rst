.. _doc_high_level_multiplayer:

High Level Multiplayer (2.2+)
==============================

Why high level?
----------------

Godot always supported standard networking via UDP, TCP and some high level protocols such as SSL and HTTP.
These protocols are very flexible and should support everything. However, for games themselves (or unless you are working
with a custom server), using them to synchronize game state manually can be an enormous amount of work.
This is due to the inherent limitations of the protocols:

- TCP ensures packets will always arrive, but latency is generally high due to error correction. It's also quite a complex protocol because it understands what a "connection" is.
- UDP is a simpler protocol which only sends packets (no connection required). The fact it does no error correction makes it pretty quick (low latency), but it has the disadvantage that packets may be lost along the way. Added to that, the MTU (maximum packet size) for UDP is generally low (only a few hundred bytes), so transmitting larger packets means splitting them, reorganizing them, retrying if a part fails, etc.

Mid level abstraction
---------------------

Before going into how we would like to synchronize a game across the network, it would be wise to understand how the base network API 
for synchronization works. Godot uses a mid-level object :ref:`NetworkedMultiplayerPeer <class_NetworkedMultiplayerPeer>`.
This object can't be created directly, but it's designed so several implementations can provide it:

.. image:: /img/nmpeer.png

This object extends from :ref:`PacketPeer <class_PacketPeer>`, so it has all the useful methods for serializing data you are used to, thanks to Godot's beautiful 
OO design. It adds methods to set a peer, transfer mode, etc. It also includes signals that will let you know when peers connect
or disconnect.

The idea is that this class interface can abstract most types of network layers, topologies and libraries. By default Godot 
provides an implementation based on ENet (:ref:`NetworkedMultiplayerEnet <class_NetworkedMultiplayerENet>`), but the plan is that this could support mobile APIs (for adhoc wifi, Bluetooth), custom device/console networking APIs, etc.

For most common cases, using this object directly is discouraged, as Godot provides even higher level networking facilities. 
Yet it is made available to scripting in case a game has specific needs for a lower level API.

Initializing the Network
------------------------

The object that controls networking in Godot is the same one that controls everything tree-related: :ref:`SceneTree <class_SceneTree>`.

To initialize high level networking, SceneTree must be provided a NetworkedMultiplayerPeer object.

Initializing as a server, listening on a port, maximum 4 peers:

::

	var host = NetworkedMultiplayerENet.new()
	host.create_server(SERVER_PORT,4) 
	get_tree().set_network_peer(host)

Initializing as a client, connecto an ip:port:

::

	var host = NetworkedMultiplayerENet.new()
	host.create_client(ip,SERVER_PORT)
	get_tree().set_network_peer(host)
	
Finalizing networking:

::

	get_tree().set_network_peer(null)

Managing connections:
---------------------

Some games accept conections at any time, others during the lobby phase. Godot can be requested to no longer accept 
connections at any point. To manage who connects, Godot provides the following signas in SceneTree:

Server and Clients:

-network_peer_connected(int id)
-network_peer_disconnected(int id)

The above signals are called in every connected peer to the server when a new one connects or disconnects. 
Is's very useful to keep track of the ids above (clients will connect with non-zero and non-one unique IDs),
while the server is warranted to always use ID=1. These IDs will be useful mostly for lobby management.

Clients:

-connected_to_server
-connection_failed
-server_disconnected

Again, all these functions are mainly useful for lobby management, or for adding/removing players on the fly. 
For these tasks, the server clearly has to work as a server and you have do tasks manually such as sending a new
player that connected information about other already connected players (ie, their names, stats, etc).

Lobby can be implemented any way you want, but the most common way is to use a node with the same name across scenes in all peers.
Generally, an autoloaded node/singleton is a great fit for this. Imagine you have something like "/root/lobby".

RPC
---

To communicate between peers, the easiest way is to use RPC (remote procedure call). This is implemented as a set of functions
in :ref:`Node <class_Node>`:

- rpc("function_name",<optional_args>)
- rpc_id(<peer_id>,"function_name",<optional_args>)
- rpc_unreliable("function_name",<optional_args>)
- rpc_unreliable_id(<peer_id>,"function_name",<optional_args>)

Functions can be called in two fashions:

- Reliable (call will arrive no matter what, but may take longer because it will be re-transmitted in fails)
- Unreliable (if the function call does not arrive, it will not be re-transmitted, but if it arrives it will do it quickly).

In most cases, Reliable is desired. Unreliable is mostly useful when synchronizing objects that move (sync must happen constantly, 
and if a packet is lost, it's not tbat bad beause a new one will eventually arrive).

Back to Lobby
--------------

Let's back to the lobby. Imagine that each player that connects to the server will tell everyone about it. 

::
	
	# typical lobby implementation, imagine this being in /root/lobby

	extends Node

	# connect all functions
	
	func _ready():
		get_tree().connect("network_peer_connected",self,"_player_connected")
		get_tree().connect("network_peer_disconnected",self,"_player_disconnected")
		get_tree().connect("connected_to_server",self,"_connected_ok")
		get_tree().connect("connection_failed",self,"_connected_fail")
		get_tree().connect("server_disconnected",self,"_server_disconnected")

	# player_info, associate ID to data
	var player_info={}
	# info we send to other players
	var my_info={ name="Johnson Magenta", favorite_color=Color8(255,0,255) }

	func _player_connected(id):
		pass # will go unused, not useful here

	func _player_disconnected(id):

		player_info.erase(id) # erase player from info		
					
	func _connected_ok():
		# Only called on clients, not server. Send my ID and info to all the other peers
		rpc( "register_player", get_tree().get_network_unique_id(), my_info )

	func _server_disconnected():
		pass # server kicked us, show error and abort		

	func _connected_fail():
		pass # could not even connect to server, abort

	remote func register_player(id,info):
		# store the info		
		player_info[id]=info
		# if i'm the server, let the new guy know about existing players
		if ( get_tree().is_network_server() ):
			# send my info to new player
			rpc_id(id,"register_info",1,my_info) 
			# send the info of existing players
			for peer_id in player_info:
				rpc_id(id,"register_info",peer_id,players[peer_id])

		# call function to update lobby UI here

		
You might have noticed already something different, which is the usage of the "remote" keyword on the register_player function:

::
  remote func register_player(id,info):
  
This keyword has two main uses. The first is to let Godot know that this function can be called from RPC. If no keywords are added,
Godot will block any attempts to call functions for security. This makes security work a lot easier (so a client can't call a function
to delete a file in another).

The second use, is to specify how the function will be called via RCP. There are four different keywords:

- remote
- sync
- master
- slave

The "remote" keyword means that the rpc() call will go via network and execute remotely.
The "sync" keyword means that the rpc() call will go via network and execute remotely, but will also execute locally (do a normal function call).
The others will be explained further down.












-
