:article_outdated: True

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

    # Our WebSocketClient instance
    var _client = WebSocketPeer.new()

    func _ready():
        # Initiate connection to the given URL.
        # remote ip addr and port
        var err = _client.connect_to_url("wss://addr:port")
        if err != OK:
            print("Unable to connect")
            set_process(false)

    func _process(delta):
        _client.poll()
        var state = socket.get_ready_state()
    	if state == WebSocketPeer.STATE_OPEN:
    		while socket.get_available_packet_count():
    			print("data packet：", socket.get_packet())
    	elif state == WebSocketPeer.STATE_CLOSING:
    		# closing
    		pass
    	elif state == WebSocketPeer.STATE_CLOSED:
    		var code = socket.get_close_code()
    		var reason = socket.get_close_reason()
    		print("WebSocket close,code：%d,reason %s." % [code, reason])
    		set_process(false) #  stop _process


Minimal server example
^^^^^^^^^^^^^^^^^^^^^^

This example will show you how to create a WebSocket server that listens for remote connections, and how to send and receive data.

::

    extends Node

    # The port we will listen to
    const PORT = 8999
    # Our WebSocketServer instance
    var _server = WebSocketMultiplayerPeer.new()
    var dict = {}

    func _ready():
        # Connect base signals to get notified of new client connections,
        # disconnections, and disconnect requests.
        _server.peer_connected.connect(_connect)
        _server.peer_disconnected.connect(_disconnect)

        # Start listening on the given port.
        var err = _server.create_server(PORT)
        if err != OK:
            print("Unable to start server")
            set_process(false)

    func _connected(id):
        # This is called when a new peer connects, "id" will be the assigned peer id,
        print("Client %d connected % [id])

    func _disconnected(id):
        # This is called when a client disconnects, "id" will be the one of the
        # disconnecting client, "was_clean" will tell you if the disconnection
        # was correctly notified by the remote peer before closing the socket.
        print("Client %d disconnected % [id])

    #handle msg
    func _handlemsg():
    	for key in dict :
    		var peer = dict[key]
    		peer.poll()
    		var state = peer.get_ready_state()
    		if state == WebSocketPeer.STATE_OPEN:#If the connection is closed too quickly,data cannot be read
    			while peer.get_available_packet_count():
    				print("packet：", peer.get_packet())
    
    func _process(delta):
        # Call this in _process or _physics_process.
        # Data transfer, and signals emission will only happen when calling this function.
        _server.poll()
        _handlemsg()

This will print (when a client connects) something similar to this:

::

    Client 1348090059 connected

Advanced chat demo
^^^^^^^^^^^^^^^^^^

A more advanced chat demo which optionally uses the multiplayer mid-level abstraction and a high level multiplayer demo are available in the `godot demo projects <https://github.com/godotengine/godot-demo-projects>`_ under `networking/websocket_chat` and `networking/websocket_multiplayer`.
