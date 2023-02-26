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

    # The URL we will connect to
    export var websocket_url = "wss://libwebsockets.org"

    # Our WebSocketClient instance
    var _client = WebSocketClient.new()

    func _ready():
        # Connect base signals to get notified of connection open, close, and errors.
        _client.connection_closed.connect(_closed)
        _client.connection_error.connect(_closed)
        _client.connection_established.connect(_connected)
        # This signal is emitted when not using the Multiplayer API every time
        # a full packet is received.
        # Alternatively, you could check get_peer(1).get_available_packets() in a loop.
        _client.data_received.connect(_on_data)

        # Initiate connection to the given URL.
        var err = _client.connect_to_url(websocket_url, ["lws-mirror-protocol"])
        if err != OK:
            print("Unable to connect")
            set_process(false)

    func _closed(was_clean = false):
        # was_clean will tell you if the disconnection was correctly notified
        # by the remote peer before closing the socket.
        print("Closed, clean: ", was_clean)
        set_process(false)

    func _connected(proto = ""):
        # This is called on connection, "proto" will be the selected WebSocket
        # sub-protocol (which is optional)
        print("Connected with protocol: ", proto)
        # You MUST always use get_peer(1).put_packet to send data to server,
        # and not put_packet directly when not using the MultiplayerAPI.
        _client.get_peer(1).put_packet("Test packet".to_utf8())

    func _on_data():
        # Print the received packet, you MUST always use get_peer(1).get_packet
        # to receive data from server, and not get_packet directly when not
        # using the MultiplayerAPI.
        print("Got data from server: ", _client.get_peer(1).get_packet().get_string_from_utf8())

    func _process(delta):
        # Call this in _process or _physics_process. Data transfer, and signals
        # emission will only happen when calling this function.
        _client.poll()

This will print:

::

    Connected with protocol:
    Got data from server: Test packet

Minimal server example
^^^^^^^^^^^^^^^^^^^^^^

This example will show you how to create a WebSocket server that listens for remote connections, and how to send and receive data.

::

    extends Node

    # The port we will listen to
    const PORT = 9080
    # Our WebSocketServer instance
    var _server = WebSocketServer.new()

    func _ready():
        # Connect base signals to get notified of new client connections,
        # disconnections, and disconnect requests.
        _server.client_connected.connect(_connected)
        _server.client_disconnected.connect(_disconnected)
        _server.client_close_request.connect(_close_request)
        # This signal is emitted when not using the Multiplayer API every time a
        # full packet is received.
        # Alternatively, you could check get_peer(PEER_ID).get_available_packets()
        # in a loop for each connected peer.
        _server.data_received.connect(_on_data)
        # Start listening on the given port.
        var err = _server.listen(PORT)
        if err != OK:
            print("Unable to start server")
            set_process(false)

    func _connected(id, proto):
        # This is called when a new peer connects, "id" will be the assigned peer id,
        # "proto" will be the selected WebSocket sub-protocol (which is optional)
        print("Client %d connected with protocol: %s" % [id, proto])

    func _close_request(id, code, reason):
        # This is called when a client notifies that it wishes to close the connection,
        # providing a reason string and close code.
        print("Client %d disconnecting with code: %d, reason: %s" % [id, code, reason])

    func _disconnected(id, was_clean = false):
        # This is called when a client disconnects, "id" will be the one of the
        # disconnecting client, "was_clean" will tell you if the disconnection
        # was correctly notified by the remote peer before closing the socket.
        print("Client %d disconnected, clean: %s" % [id, str(was_clean)])

    func _on_data(id):
        # Print the received packet, you MUST always use get_peer(id).get_packet to receive data,
        # and not get_packet directly when not using the MultiplayerAPI.
        var pkt = _server.get_peer(id).get_packet()
        print("Got data from client %d: %s ... echoing" % [id, pkt.get_string_from_utf8()])
        _server.get_peer(id).put_packet(pkt)

    func _process(delta):
        # Call this in _process or _physics_process.
        # Data transfer, and signals emission will only happen when calling this function.
        _server.poll()

This will print (when a client connects) something similar to this:

::

    Client 1348090059 connected with protocol: selected-protocol
    Got data from client 1348090059: Test packet ... echoing

Advanced chat demo
^^^^^^^^^^^^^^^^^^

A more advanced chat demo which optionally uses the multiplayer mid-level abstraction and a high level multiplayer demo are available in the `godot demo projects <https://github.com/godotengine/godot-demo-projects>`_ under `networking/websocket_chat` and `networking/websocket_multiplayer`.
