.. _doc_networked_player_movement:

Networked player movement
=========================

Most modern online multiplayer games operate under what is called a server authoritative client-server model. 
In this model, clients connect directly to a game server over a socket connection and pass messages back and forth. 
Being server-authoritative means that the clients are "thin" or "dumb" and make no decisions about the state of the game
world themselves. Instead, they merely pass player input to the server and handle the display of whatever the server tells it
that the current state of the game world is. In other words, the server is the arbiter of the game world that all clients must abide by.

Normally, this isn't that big of a deal. A client informs the server of its intent, such as :code:`Player swings sword` and the server 
receives this intent, modifies its local game world state, and then broadcasts the relevant new state to all clients. When a client receives
this new state, it updates its own local copy of the game world state and renders it. This asynchronous nature of communication between the 
server and clients is what allows players spanning geographical regions to interact with a shared game world in real time. There is one facet 
of online multiplayer games that doesn't work so seamlessly in a sever authoritative model. That being player movement.

If you consider how player movement would work if implemented using the appraoch above, it would go something like this:

1. Player sends intent to move left
2. Server receives players intent
3. Server moves player left in its local game world
4. Server broadcasts player's new transform to all clients
5. Clients update individual local game worlds with the player's new transform and renders it


At a glance this may seem fine, however remember that in a networked environment, we have latency to deal with. Even with a good network connection, 
transfering data over the internet always has at least *some* inherent latency. For instance, it's not unusual for the time between the player sending 
its intent to the server and the time at which a client receives the new authoritative server state to exceed 200ms. If you consider how this would look
from a player's perspective, you'll quickly realize how choppy the user experience can be. Fortunately, people have been making online multiplayer games 
for a relatively long time now, and techniques have been developed to combat these shortcomings, while still allowing the server to remain authoritative.

Client-side prediction
----------------------

Client-side prediction is a rather simple technique to relieve the choppiness of sever authoritative player movement from the player performing the movement.
Alone, it's not very useful, but when combined with server reconciliation (as described below) it allows the player to move fluidly while still leaving arbitration
in the hands of the server. To be honest, client-side predicition here is a bit of a misnomer. A more accurate term would be "client-side assumption," as we will see.

Essentially, client-side prediciton boils down to performing the intended movement on the client, assuming that no shenanigans like cheating occur and the the network
connection is stable. Let's take a look at how we can implement basic client-side prediciton for a networked KinematicBody2D. We will expand upon this example as we 
introduce the other components of networked player movement.

::

    # networked_player.gd
    extends KinematicBody2D
    class_name NetworkedPlayer

    export var speed = 3.0

    func move(direction):
        if direction.length() == 0:
            return
        
        rpc_unreliable_id(NetworkedMultiplayerPeer.TARGET_PEER_SERVER, "_move_server", direction)
        move_and_slide(direction*speed)
    
    puppet func _move_server(direction):
        if not multiplayer.is_network_server():
            return
        move_and_slide(direction*speed)
        rpc_unreliable("_set_peer_position", position)
    
    remote func _set_peer_position(pos):
        if multiplayer.get_rpc_sender_id() == NetworkedMultiplayerPeer.TARGET_PEER_SERVER and not multiplayer.is_network_master():
            position = pos


In this example, we send the move intent (direction) to the server and then immediately move the character locally how we assume the server will do so.
When the server eventually receives our intent to move, it will move the character in the authoritative game world as well and then tell the clients what 
the new position is. All of the clients except the network master (the one controlling the player) will update their local positions to match.

Server reconciliation
---------------------
Client side prediciton gets us part of the way there for our player's character, however it only solves the issue of choppiness introduced by latency. The
server authoritative state is never applied to the player character of the controlling player, only its peers. We could naively solve this by simple overriding
the position of the controlling player's character as well, just like we already do for the peers' copyies of the character however is we again consider latency,
we realize that this might not be the best idea. Since introducing client-side predicition, we now move the player character locally every time :code:`move` is called, 
which is likely every frame or every physics frame. This means that by the time the authoritative position comes back from the server, the local character would have
already moved even further. Resetting the local position to the server authoritative state now would result in the character appearing to teleport backwards, resulting
in a phenomenon known as "rubber banding." It turns out, solving this problem isn't so simple and requires some substantial changes to our code. The teqnique we use here
is known as server reconciliation.

Essentially, before we send out input off to the server, we store it in an input buffer along with an sequence number. We also buffer the input on the server as well and 
introduce a polling frequency in order to reduce bandwidth. This is an optimization that is mostly orthogonal to the topic at hand, but it's a good practice none-the-less. 
Whenever the server processes an input from the buffer, it broadcasts the resulting state to all clients. Clients store the last known state in a member varibale and ever 
physics frame on the controlling client, we reset the character's local position to that of the last known server state and then we loop through all of the inputs in the 
input buffer and for each one whose sequence number is greater than that of the last known server state, we reapply it locally. If there was no cheating and the network 
connection was stable, the resulting posiiton should be the same as it was before, however if there was some cheating or dropped messages, then the resulting state will be 
synchroized to what the server thinks + any predicted movement since. In code, this would look something like this:

::

    # networked_player.gd
    extends KinematicBody2D
    class_name NetworkedPlayer

    export var speed = 3.0
    export server_tick_interval = 100

    var _last_server_state = {}
    var _input_buff = []
    var _accum = 0.0
    var seq = 0

    func move(direction):
        if direction.length() == 0:
            return
        var cmd = {
            "d": direction,
            "seq": seq,
        }
        rpc_unreliable_id(NetworkedMultiplayerPeer.TARGET_PEER_SERVER, "_buffer_input", cmd)
        _buffer_input(cmd)
        move_and_slide(direction*speed)
        seq+=1
    
    func _physics_process(delta):
    	# If this player instance is the server, then it
	    # is the source of truth. It should process the
    	# buffered input and replicate it back to the client.
        if multiplayer.is_network_server():
            var curr = OS.get_system_time_msecs()
            if (curr - _accum) >= server_tick_interval:
                _process_server_input(delta)
                _accum = curr
        
        # If this is the entity who sent the input, then reconcile 
	    # with whatever the last known server state is. This might 
	    # contradict what was sent if the sent input was invalid or 
    	# deemed incorrect by the server.
        elif is_network_master():
            _reconcile(delta)
    
    # Server reconciliation. Directly set the current position to that
    # of the last known server state, and then reapply all inputs since then.
    # This ensures client consistency with the server state.
    # @see https://www.gabrielgambetta.com/client-side-prediction-server-reconciliation.html
    func _reconcile(delta):
        var last_state = _last_server_state
        if last_state:
            # set the current position to the last known server state
            position = last_state.p
            
            # reapply any input since the last known server state.
            var del = []
            while not _input_buff.empty():
                var cmd = _input_buff.pop_front()
                if cmd.seq > last_state.seq:
                    move_and_slide(cmd.d * speed)

    func _process_server_state(delta):
        if _input_buff.empty():
            return
        var last_seq = 0
        while not _input_buff.empty():
            var cmd = _input_buff.pop_front()
            last_seq = cmd.seq
            move_and_slide(cmd.d * speed)
        rpc_unreliable("_append_server_state, {"p": position, "seq": last_seq})

    remote func _append_server_state(state):
        if multiplayer.get_rpc_sender_id() == NetworkedMultiplayerPeer.TARGET_PEER_SERVER:
            _last_server_state = state

    # Keep a buffer of inputs. This is executed on the server and the client
    # that sent the inputs. The server will use this buffer for processing,
    # while the client will use it for server reconciliation.
    puppet func _buffer_input(input : Dictionary) -> void:
        _input_buff.append(input)

.. note:: For more information on client side prediction and server reconciliation, check out `the wonderful article by Gabriel Gambetta <https://www.gabrielgambetta.com/client-side-prediction-server-reconciliation.html>`__.

Entity interpolation
--------------------
The final piece to the networked player character puzzle is *entity interpolation*. Client-side prediction and server reconciliation solve the problem of networked movement for 
the character the player is controlling, but they don't help with movement from *other* players. Luckily entity inerpolation can solve this for us rather easily. If we consider that
we are actually receiving character state from the *past*, it might become apparent that all we need to do is lerp to the last known server position and call it a day. This, of course means that peers will always appear 
slightly behind real time ("slightly" here depends on latency, but typically no more than around 250ms unless your connection is unstable), but in the case of peer movement, this is usually find. In the end, in most games, 
the exact position of a peer player at any given time isn't that important. A coarse estimation is usually enough. We can easily add entity inerpolation to our example code.

::

    # networked_player.gd
    extends KinematicBody2D
    class_name NetworkedPlayer

    export var speed = 3.0
    export server_tick_interval = 100

    var _last_server_state = {}
    var _input_buff = []
    var _accum = 0.0
    var seq = 0

    func move(direction):
        if direction.length() == 0:
            return
        var cmd = {
            "d": direction,
            "seq": seq,
        }
        rpc_unreliable_id(NetworkedMultiplayerPeer.TARGET_PEER_SERVER, "_buffer_input", cmd)
        _buffer_input(cmd)
        move_and_slide(direction*speed)
        seq+=1

    func _process(delta):
        # Remote client peers should lerp to to the last known server 
        # state.
        if not multiplayer.is_network_server() and not is_network_master():
            _interpolate(delta)

    func _physics_process(delta):
    	# If this player instance is the server, then it
	    # is the source of truth. It should process the
    	# buffered input and replicate it back to the client.
        if multiplayer.is_network_server():
            var curr = OS.get_system_time_msecs()
            if (curr - _accum) >= server_tick_interval:
                _process_server_input(delta)
                _accum = curr
        
        # If this is the entity who sent the input, then reconcile 
	    # with whatever the last known server state is. This might 
	    # contradict what was sent if the sent input was invalid or 
    	# deemed incorrect by the server.
        elif is_network_master():
            _reconcile(delta)
    
    # Server reconciliation. Directly set the current position to that
    # of the last known server state, and then reapply all inputs since then.
    # This ensures client consistency with the server state.
    # @see https://www.gabrielgambetta.com/client-side-prediction-server-reconciliation.html
    func _reconcile(delta):
        var last_state = _last_server_state
        if last_state:
            # set the current position to the last known server state
            position = last_state.p
            
            # reapply any input since the last known server state.
            var del = []
            while not _input_buff.empty():
                var cmd = _input_buff.pop_front()
                if cmd.seq > last_state.seq:
                    move_and_slide(cmd.d * speed)

    # Entity interpolation. Lerp remote entities to last known server state. This ensures eventual 
    # remote client consistency with the server state.
    # @see https://www.gabrielgambetta.com/entity-interpolation.html
    func _interpolate(delta) -> void:
        var last_state = _last_server_state
        if last_state:
            # You can adjust the lerp weight to fit your needs.
            position = lerp(position, last_state.p, 0.5)


    func _process_server_state(delta):
        if _input_buff.empty():
            return
        var last_seq = 0
        while not _input_buff.empty():
            var cmd = _input_buff.pop_front()
            last_seq = cmd.seq
            move_and_slide(cmd.d * speed)
        rpc_unreliable("_append_server_state, {"p": position, "seq": last_seq})

    remote func _append_server_state(state):
        if multiplayer.get_rpc_sender_id() == NetworkedMultiplayerPeer.TARGET_PEER_SERVER:
            _last_server_state = state

    # Keep a buffer of inputs. This is executed on the server and the client
    # that sent the inputs. The server will use this buffer for processing,
    # while the client will use it for server reconciliation.
    puppet func _buffer_input(input : Dictionary) -> void:
        _input_buff.append(input)

.. note:: For more information on entity interpolation, check out `the article by Gabriel Gambetta <https://www.gabrielgambetta.com/entity-interpolation.html>`__.

Conclusion
----------

This tutorial preovided a brief explanation of server authoritative client-server games and explained the challenges that this model brings to player movement, as well 
as some of the techniques that can be used to solve these problems. These techniques are commonly used in many online multiplayer games, however depending on your game's 
design, other techniques may be required either in lieu of, or in addition to the ones described here. Some of these techniques include lag compensation, which is common 
in fast-paced first-person shooters and dead reckoning, prevailent in most online racing games. For more reading on these topics, I can recommend the fantastic book series 
by "No Bugs Hare" called *Development and Deployment of Multiplayer Online Games*. Vol I. is available `on Amazon <https://www.amazon.com/Development-Deployment-Multiplayer-Online-Games/dp/3903213055>`__
and the beta versions of the rest of the series is available on `No Bugs' website <http://ithare.com/contents-of-development-and-deployment-of-massively-multiplayer-games-from-social-games-to-mmofps-with-stock-exchanges-in-between/>`__ for free.