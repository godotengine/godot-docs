.. _doc_webxr_intro:

WebXR
=====

WebXR is a web standard for delivering XR experiences right from a web browser,
without the user needing to install anything. Godot has built-in support for WebXR.

.. note::

    As this uses the HTML export WebXR requires the use of the compatibility renderer.
    Godot currently requires multiview support for stereo rendering which is not available on all WebXR capable devices.

Setup
-----

Setting up WebXR is a little different because your application always starts as a normal non-XR webpage.
We thus define a 2D UI on our main page that includes a button that will switch to XR.

We will need the following code to make things work:

.. tabs::
  .. code-tab:: gdscript GDScript

    extends Node3D

    @onready var start_xr_button: Button = $EnterWebXR

    # Our WebXR interface.
    var xr_interface: WebXRInterface

    # Is a WebXR is_session_supported query running
    var webxr_session_query: bool = false

    # Set this to true if we wish to have an AR session
    var require_ar: bool = false

    # Set this to true if we wish to have hand tracking
    var enable_hand_tracking: bool = false

    # Handle the Enter VR button on the WebXR browser
    func _on_enter_webxr_button_pressed() -> void:
        # Configure the WebXR interface
        xr_interface.session_mode = "immersive-ar" if require_ar else "immersive-vr"
        xr_interface.requested_reference_space_types = "local-floor, local"
        xr_interface.required_features = "local-floor"
        xr_interface.optional_features = ""

        # Add hand-tracking if needed
        if enable_hand_tracking:
            xr_interface.optional_features += ", hand-tracking"

        # Initialize the interface. This should trigger either _on_webxr_session_started
        # or _on_webxr_session_failed
        if not xr_interface.initialize():
            OS.alert("Failed to initialize WebXR")


    # Called when we're ready
    func _ready() -> void:
        xr_interface = XRServer.find_interface("WebXR")
        if xr_interface:
            # Connect our signals
            xr_interface.session_supported.connect(_on_webxr_session_supported)
            xr_interface.session_started.connect(_on_webxr_session_started)
            xr_interface.session_ended.connect(_on_webxr_session_ended)
            xr_interface.session_failed.connect(_on_webxr_session_failed)

           	webxr_session_query = true
        	xr_interface.is_session_supported("immersive-ar" if require_ar else "immersive-vr")
        else:
            print("WebXR is not available")


    # Handle WebXR session supported check
    func _on_webxr_session_supported(session_mode: String, supported: bool) -> void:
        # Skip if not running session-query
        if not webxr_session_query:
            return

        # Clear the query flag
        webxr_session_query = false

        # Report if not supported
        if not supported:
            OS.alert("Your web browser doesn't support " + session_mode + ". Sorry!")
            return

        # WebXR supported - show canvas on web browser to enter WebVR
        start_xr_button.visible = true


    # Called when the WebXR session has started successfully
    func _on_webxr_session_started() -> void:
        # Hide the canvas and switch the viewport to XR
        start_xr_button.visible = false

        get_viewport().transparent_bg = require_ar
        get_viewport().use_xr = true


    # Called when the user ends the immersive VR session
    func _on_webxr_session_ended() -> void:
        # Show the canvas and switch the viewport to non-XR
        start_xr_button.visible = true

        get_viewport().transparent_bg = false
        get_viewport().use_xr = false


    # Called when the immersive VR session fails to start
    func _on_webxr_session_failed(message: String) -> void:
        OS.alert("Unable to enter VR: " + message)
        start_xr_button.visible = true


Make sure the "Enable WebXR" button's ``button_pressed`` signal calls the ``_on_enter_webxr_button_pressed`` method.

.. note::

    In the code above we attempt to use the ``local-floor`` reference spaces.
    This reference spaces assumes gameplay where we need to know the player's height from the floor.

    For games where the player is seated inside of a vehicle, such as flight sims or racing games, the reference space ``local`` may be more appropriate.


Controller input
----------------

The input system in WebXR works against a fixed set of inputs that obfuscate the actual hardware being used. In order to allow for code to be portable between a WebXR and OpenXR application these inputs are mapped to actions that overlap with the default action map used by our OpenXR interface.

There are small differences such as WebXR separating touchpad and thumbsticks as separate inputs, instead of the primary and secondary input setup found in our default OpenXR action map.

The core inputs are available for WebXR:


.. table::
   :widths: auto

   +-----------------------------+-----------+---------------------------------------------------------+
   |  Name                       | Type      | Description                                             |
   +-----------------------------+-----------+---------------------------------------------------------+
   |  trigger_click              | Boolean   | ``true`` if the trigger is pressed                      |
   +-----------------------------+-----------+---------------------------------------------------------+
   |  trigger                    | Float     | Trigger value between 0.0 and 1.0                       |
   +-----------------------------+-----------+---------------------------------------------------------+
   |  grip_click                 | Boolean   | ``true`` if the grip button is pressed                  |
   +-----------------------------+-----------+---------------------------------------------------------+
   |  grip                       | Float     | Grip value between 0.0 and 1.0                          |
   +-----------------------------+-----------+---------------------------------------------------------+
   |  touchpad_click             | Boolean   | ``true`` if the touchpad is pressed                     |
   +-----------------------------+-----------+---------------------------------------------------------+
   |  thumbstick_click           | Boolean   | ``true`` if the thumbstick is pressed                   |
   +-----------------------------+-----------+---------------------------------------------------------+
   |  ax_button                  | Boolean   | ``true`` if the A or X button is pressed                |
   +-----------------------------+-----------+---------------------------------------------------------+
   |  by_button                  | Boolean   | ``true`` if the B or Y button is pressed                |
   +-----------------------------+-----------+---------------------------------------------------------+
   |  touchpad_x                 | Float     | Finger movement on the touchpad in the X direction      |
   +-----------------------------+-----------+---------------------------------------------------------+
   |  touchpad_y                 | Float     | Finger movement on the touchpad in the Y direction      |
   +-----------------------------+-----------+---------------------------------------------------------+
   |  touchpad                   | Vector2   | Touchpad input as a Vector2                             |
   +-----------------------------+-----------+---------------------------------------------------------+
   |  thumbstick_x               | Float     | Thumbstick movement in the X direction                  |
   +-----------------------------+-----------+---------------------------------------------------------+
   |  thumbstick_y               | Float     | Thumbstick movement in the Y direction                  |
   +-----------------------------+-----------+---------------------------------------------------------+
   |  thumbstick                 | Vector2   | Thumbstick input as a Vector2                           |
   +-----------------------------+-----------+---------------------------------------------------------+

WebXR also exposes ``aim`` and ``grip`` poses that respectively identify a forward facing location at the tip of the controller and a position on the controller grip.
