.. _doc_port_forwarding_upnp:

Port Forwarding & Universal Plug and Play
==================================================

Why Universal Plug and Play?
-----------------------------

Besides testing locally on your own, you should test on a *real* network connection to make sure your game actually works under real-life networking conditions. There are multiple ways to achieve this:

    1. Keep hosting your game locally, but expose it to the public internet. This is easy and quick, but comes with a few downsides. Your public IP is likely dynamically assigned and changes, which requires you to let your testers know each time what to connect to, or to use a dynamic DNS service to point at your changing IP. You also need to deal with any firewalls blocking external access to your local game, most notably on your router, and in the likely case it uses NAT (network address translation), you also need to configure port forwarding on your router. Finally, you open a (small part of) your computer and home entwork to the public internet, which always has some risks.

    2. Host a real (physical or virtual) server and deploy there. This requires the knowledge to securely administrate and setup a server and deployment of your game to that server.

    3. Peer-to-Peer connection using automatic NAT traversal with technologies like STUN/TURN hole punching. Relieves you of the headache of manual firewall and port forwarding configuration, but has some added complexity and may depend on the NAT configurations involved.

    4. Use Universal Plug and Play to automatically open and forward the require port on the local router.
    In a fully finished game, you may want to use a mix of these depending on your intended networking model. Maybe you expect your players to host their own servers, and just let them deal with it, or maybe you will be hosting all of the game's servers on your own, official servers. Maybe it's a purely peer-to-peer game and you use a mix of STUN/TURN NAT traversal and Universal Plug and Play port forwarding, depending on what works best on each player's machine. Also, some third-party networking solutions (like Steam's Steamworks networking) take care of most of this for you.

Here, we're going to look into using :abbr:`UPNP (Universal Plug and Play)` for port forwarding. Notably, this will only work if the local router supports Universal Plug and Play port forwarding and has it enabled and configured.

How to port-forward
-------------------

1. Login to your router (192.168.1.1) through your browser (username/password is on the router's bottom where it has barcode tag and original wifi password)
2. Enable :abbr:`UPNP (Universal Plug and Play)` if it exists.
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

and convert it so it uses :abbr:`UPNP (Universal Plug and Play)`. Reminder that **only the host needs :abbr:`UPNP (Universal Plug and Play)`**. Because the goal is after all to expose the host's IP onto the wide internet, accessible by anyone.

Let's expand onto start_server()

::

    func start_server():
        peer.create_server(port)
        multiplayer.multiplayer_peer = peer

        initialize_UPNP()

As you can see above, :abbr:`UPNP (Universal Plug and Play)` initialization happens **after** your setup. Now let's create the actual :abbr:`UPNP (Universal Plug and Play)` logic.

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

And like every server has a disconnected signal once late in development, it is suggested you un-map the port connections when your server/game closes, with the following code:

::

    upnp.delete_port_mapping(9999, "UDP")
    upnp.delete_port_mapping(9999, "TCP")
