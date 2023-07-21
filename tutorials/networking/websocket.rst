:article_outdated: False

.. _doc_websocket:

WebSocket
=========

HTML5 and WebSocket
-------------------

The WebSocket protocol was standardized in 2011 with the original goal of allowing browsers to create stable and bidirectional connections with a server.
Before that, browsers used to only support HTTPRequests, which is not well-suited for bidirectional communication.

The protocol is message based and a very powerful tool to send push notifications to browsers, and has been used to implement chats, turn-based games, etc. It still uses a TCP connection, which is good for reliability but not for latency, so not good for real-time applications like VoIP and fast-paced games (see :ref:`WebRTC <doc_webrtc>` for those use cases).

Due to its simplicity, its wide compatibility, and being easier to use than a raw TCP connection, WebSocket soon started to spread outside the browsers, in native applications as a mean to communicate with network servers.

Godot supports WebSocket in both native and HTML5 exports.

Using WebSocket in Godot
------------------------

WebSocket is implemented in Godot via :ref:`WebSocketPeer <class_WebSocketPeer>`. The WebSocket implementation is compatible with the High Level Multiplayer. See section on :ref:`high-level multiplayer <doc_high_level_multiplayer>` for more details.

.. warning::

    When exporting to Android, make sure to enable the ``INTERNET``
    permission in the Android export preset before exporting the project or
    using one-click deploy. Otherwise, network communication of any kind will be
    blocked by Android.

Minimal client example
^^^^^^^^^^^^^^^^^^^^^^

This example will show you how to create a WebSocket connection to a remote server, and how to send and receive data.

::

	extends Node

    # The URL we will connect to
	@export var websocket_url = "wss://ws.postman-echo.com/raw"

	var socket = WebSocketPeer.new()


	func _ready():
		socket.connect_to_url(websocket_url)

		# Send a message every 5 seconds.
		var timer = Timer.new()
		timer.wait_time = 5.0
		timer.timeout.connect(_send_message)
		add_child(timer)
		timer.start()


	func _send_message():
		socket.send_text("Hello websockets!")


	func _process(delta):
		socket.poll()
		var state = socket.get_ready_state()
		if state == WebSocketPeer.STATE_OPEN:
			while socket.get_available_packet_count():
				print("Packet: ", socket.get_packet().get_string_from_utf8())
		elif state == WebSocketPeer.STATE_CLOSING:
			# Keep polling to achieve proper close.
			pass
		elif state == WebSocketPeer.STATE_CLOSED:
			var code = socket.get_close_code()
			var reason = socket.get_close_reason()
			print("WebSocket closed with code: %d, reason %s. Clean: %s" % [code, reason, code != -1])
			set_process(false) # Stop processing.


This will send a message every 5 seconds that will be echoed back

::

    Packet: Hello websockets!

Minimal server example
^^^^^^^^^^^^^^^^^^^^^^

This example will show you how to create a WebSocket server that listens for remote connections, and how to send and receive data.

::

	extends Node

	# The port we will listen to.
	const PORT = 9080

	# Our WebSocketServer instance.
	var _server = WebSocketMultiplayerPeer.new()

	# Keeps track of the connected peer IDs.
	var peer_ids: Array[int] = []


	func _ready():
		# Connect base signals to get notified of new client connections,
		# and disconnections.
		_server.peer_connected.connect(_connected)
		_server.peer_disconnected.connect(_disconnected)

		# Start listening on the given port.
		var err = _server.create_server(PORT)
		if err != OK:
			print("Unable to start server")
			set_process(false)


	func _connected(id):
		peer_ids.append(id)

		# This is called when a new peer connects, "id" will be the assigned peer id.
		print("Peer %d connected" % id)


	func _disconnected(id):
		peer_ids.erase(id)

		# This is called when a client disconnects, "id" will be the one of the
		# disconnecting client.
		var peer = _server.get_peer(id)
		var code = peer.get_close_code()
		var reason = peer.get_close_reason()
		print("Peer %s closed with code: %d, reason %s. Clean: %s" % [id, code, reason, code != -1])


	func _process(delta):
		# Call this in _process or _physics_process.
		# Data transfer, and signals emission will only happen when calling this function.
		_server.poll()

		for peer_id in peer_ids:
			var peer = _server.get_peer(peer_id)
			peer.poll()

			var peer_state = peer.get_ready_state()
			if peer_state == WebSocketPeer.STATE_OPEN:
				while peer.get_available_packet_count():
					var packet_text = peer.get_packet().get_string_from_utf8()
					print("Got data from peer %d: %s ... echoing" % [peer_id, packet_text])

					# Echo the packet back.
					peer.send_text(packet_text)
			elif peer_state == WebSocketPeer.STATE_CLOSING:
				# Keep polling to achieve proper close.
				pass

This will print (when a client connects) something similar to this:

::

    Client 1348090059 connected
    Got data from client 1348090059: Test packet ... echoing

Advanced chat demo
^^^^^^^^^^^^^^^^^^

A more advanced chat demo which optionally uses the multiplayer mid-level abstraction and a high level multiplayer demo are available in the `godot demo projects <https://github.com/godotengine/godot-demo-projects>`_ under `networking/websocket_chat` and `networking/websocket_multiplayer`.
