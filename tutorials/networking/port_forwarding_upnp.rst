.. _doc_port_forwarding_upnp:

Port Forwarding & Universal Plug n' Play
======================

Why Universal Plug n' Play?
---------------------------

After you are done testing solo with localhost(127.0.0.1) you want to test on a *real* connection.
You will be likely overwhelmed with your choices:

1. Host a real server and deploy there (deployment of a build will be a chore unless you learn advanced methods like remote ssh deployment which are included in Godot)

2. Peer-to-Peer connection, straight to a computer. This includes NAT Holepunching, STUN/TURN and other methods which are overwhelming compared to :abbr:`UPNP (Universal Plug n Play)`.

Before any code, let's look into the router setup; Not all Routers support :abbr:`UPNP (Universal Plug n Play)`, nor do all users have :abbr:`UPNP (Universal Plug n Play)` enabled. For this reason it is suggested you use :abbr:`UPNP (Universal Plug n Play)` for testing instead of your final public deployment. Even if you enable your router's :abbr:`UPNP (Universal Plug n Play)` (assuming it is a choice), you need to port-forward the port, because the IP is public but all your router's ports are closed by default.


How to port-forward
-------------------

1. Login to your router (username/password is on the router's bottom where it has barcode tag and original wifi password)
2. Enable UPNP if it exists.
3. Find a section called 'Port Forwarding' or 'Port Mapping'
4. Add new
5. Title/Name: "godot_tcp" (do not capitalize)
6. Local IP Address: 192.168.x.y (x,y depends on your local IP, do find it)
7. Protocol: TCP
8. LAN Port: 9999-9999 (or whichever number you want, just make sure its the same everywhere)
9. Public Port: 9999-9999
10. Apply/Save
11. Add new (this time for UDP)
12. Title/Name: "godot_udp" (do not capitalize)
13. Local IP Address: 192.168.x.y
14. Protocol: UDP
15. LAN Port: 9999-9999
16. Public Port: 9999-9999
17. Apply/Save

UPNP Code
---------------

Now, let's take the following minimal host/client code:

::

    @export var port: int = 9999
    @export var ip: String = "localhost"
    var peer = ENetMultiplayerPeer.new()

    func _enter_tree():
	    multiplayer.peer_connected.connect(add_peer)
	    multiplayer.peer_disconnected.connect(del_peer)

    func start_server():
        peer.create_server(port)
        multiplayer.multiplayer_peer = peer

    func start_client():
        peer.create_client(ip, port)
        multiplayer.multiplayer_peer = peer

and convert it into UPNP. Reminder that **only the host must use UPNP**. Because the goal is after all to expose a public IP onto the wide internet, accessible by anyone.

Let's expand onto start_server()

::

    func start_server():
        peer.create_server(port)
        multiplayer.multiplayer_peer = peer

        initialize_UPNP()

As you can see above, :abbr:`UPNP (Universal Plug n Play)` initialization happens **after** your setup. Now let's create the actual :abbr:`UPNP (Universal Plug n Play)` logic.

::

    var upnp: UPNP
    func initialize_UPNP():

        upnp = UPNP.new()
        var discover_result = upnp.discover()

        # Did it find anything?
        if (discover_result == UPNP.UPNP_RESULT_SUCCESS):
            # upnp.get_gateway() is your router
            if (upnp.get_gateway() && upnp.get_gateway().is_valid_gateway()):
                # Map the port connections
                var map_result_udp = upnp.add_port_mapping(port, port, "godot_udp", "UDP")
                var map_result_tcp = upnp.add_port_mapping(port, port, "godot_tcp", "TCP")

                # If there are NO port forward rules with the above titles
                # then fallback to empty port forward name
                if (map_result_udp != UPNP.UPNP_RESULT_SUCCESS):
                    map_result_udp = upnp.add_port_mapping(port, port, "", "UDP")
                if (map_result_tcp != UPNP.UPNP_RESULT_SUCCESS):
                    map_result_tcp = upnp.add_port_mapping(port, port, "", "TCP")

                # It is suggested you use a label or textfield for the server
                # which displays the public IP where clients should connect to
                #$WorldUI/HostIPLabel.text = upnp.query_external_address()

And like every server has a disconnected signal once developed, it is suggested you un-map the port connections when your server/game closes, with the following code:

::

    upnp.delete_port_mapping(9999, "UDP")
    upnp.delete_port_mapping(9999, "TCP")
