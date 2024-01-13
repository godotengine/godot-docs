.. _doc_a_better_xr_start_script:

A better XR start script
========================

In :ref:`doc_setting_up_xr` we introduced a startup script that initialises our setup which we used as our script on our main node.
This script performs the minimum steps required for any given interface.

When using OpenXR there are a number of improvements we should do here.
For this we've created a more elaborate starting script.
You will find these used in our demo projects.

Alternatively, if you are using XR Tools (see :ref:`doc_introducing_xr_tools`) it contains a version of this script updated with some features related to XR tools.

Below we will detail out the script used in our demos and explain the parts that are added.

Signals for our script
----------------------

We are introducing 3 signals to our script so that our game can add further logic:

- ``focus_lost`` is emitted when the player takes off their headset or when the player enters the menu system of the headset.
- ``focus_gained`` is emitted when the player puts their headset back on or exists the menu system and returns to the game.
- ``pose_recentered`` is emitted when the headset requests the players position to be reset.

Our game should react accordingly to these signals.

.. tabs::
  .. code-tab:: gdscript GDScript

    extends Node3D

    signal focus_lost
    signal focus_gained
    signal pose_recentered

    ...

  .. code-tab:: csharp

    using Godot;

    public partial class MyNode3D : Node3D
    {
        [Signal]
        public delegate void FocusLostEventHandler();

        [Signal]
        public delegate void FocusGainedEventHandler();

        [Signal]
        public delegate void PoseRecenteredEventHandler();

    ...


Variables for our script
------------------------

We introduce a few new variables to our script as well:

- ``maximum_refresh_rate`` will control the headsets refresh rate if this is supported by the headset.
- ``xr_interface`` holds a reference to our XR interface, this already existed but we now type it to get full access to our :ref:`XRInterface <class_xrinterface>` API.
- ``xr_is_focussed`` will be set to true whenever our game has focus.

.. tabs::
  .. code-tab:: gdscript GDScript

    ...

    @export var maximum_refresh_rate : int = 90

    var xr_interface : OpenXRInterface
    var xr_is_focussed = false

    ...

  .. code-tab:: csharp

    ...

        [Export]
        public int MaximumRefreshRate { get; set; } = 90;

        private OpenXRInterface _xrInterface;

        private bool _xrIsFocused;

    ...

Our updated ready function
--------------------------

The ready function mostly remains the same but we hook up a number of signals that will be emitted by the :ref:`XRInterface <class_xrinterface>`.
We'll provide more detail about these signals as we implement them.

We also quit our application if we couldn't successfully initialise OpenXR.
Now this can be a choice.
If you are making a mixed mode game you setup the VR mode of your game on success,
and setup the non-VR mode of your game on failure.
However, when running a VR only application on a standalone headset,
it is nicer to exit on failure than to hang the system.

.. tabs::
  .. code-tab:: gdscript GDScript

    ...

    # Called when the node enters the scene tree for the first time.
    func _ready():
        xr_interface = XRServer.find_interface("OpenXR")
        if xr_interface and xr_interface.is_initialized():
            print("OpenXR instantiated successfully.")
            var vp : Viewport = get_viewport()

            # Enable XR on our viewport
            vp.use_xr = true

            # Make sure v-sync is off, v-sync is handled by OpenXR
            DisplayServer.window_set_vsync_mode(DisplayServer.VSYNC_DISABLED)

            # Connect the OpenXR events
            xr_interface.connect("session_begun", _on_openxr_session_begun)
            xr_interface.connect("session_visible", _on_openxr_visible_state)
            xr_interface.connect("session_focussed", _on_openxr_focused_state)
            xr_interface.connect("session_stopping", _on_openxr_stopping)
            xr_interface.connect("pose_recentered", _on_openxr_pose_recentered)
        else:
            # We couldn't start OpenXR.
            print("OpenXR not instantiated!")
            get_tree().quit()

    ...

  .. code-tab:: csharp

    ...

        /// <summary>
        /// Called when the node enters the scene tree for the first time.
        /// </summary>
        public override void _Ready()
        {
            _xrInterface = (OpenXRInterface)XRServer.FindInterface("OpenXR");
            if (_xrInterface != null && _xrInterface.IsInitialized())
            {
                GD.Print("OpenXR instantiated successfully.");
                var vp = GetViewport();

                // Enable XR on our viewport
                vp.UseXR = true;

                // Make sure v-sync is off, v-sync is handled by OpenXR
                DisplayServer.WindowSetVsyncMode(DisplayServer.VSyncMode.Disabled);

                // Connect the OpenXR events
                _xrInterface.SessionBegun += OnOpenXRSessionBegun;
                _xrInterface.SessionVisible += OnOpenXRVisibleState;
                _xrInterface.SessionFocussed += OnOpenXRFocusedState;
                _xrInterface.SessionStopping += OnOpenXRStopping;
                _xrInterface.PoseRecentered += OnOpenXRPoseRecentered;
            }
            else
            {
                // We couldn't start OpenXR.
                GD.Print("OpenXR not instantiated!");
                GetTree().Quit();
            }
        }

    ...


On session begun
----------------

This signal is emitted by OpenXR when our session is setup.
This means the headset has run through setting everything up and is ready to begin receiving content from us.
Only at this time various information is properly available.

The main thing we do here is to check our headsets refresh rate.
We also check the available refresh rates reported by the XR runtime to determine if we want to set our headset to a higher refresh rate.

Finally we match our physics update rate to our headset update rate.
Godot runs at a physics update rate of 60 updates per second by default while headsets run at a minimum of 72,
and for modern headsets often up to 144 frames per second.
Not matching the physics update rate will cause stuttering as frames are rendered without objects moving.

.. tabs::
  .. code-tab:: gdscript GDScript

    ...

    # Handle OpenXR session ready
    func _on_openxr_session_begun() -> void:
        # Get the reported refresh rate
        var current_refresh_rate = xr_interface.get_display_refresh_rate()
        if current_refresh_rate > 0:
            print("OpenXR: Refresh rate reported as ", str(current_refresh_rate))
        else:
            print("OpenXR: No refresh rate given by XR runtime")

        # See if we have a better refresh rate available
        var new_rate = current_refresh_rate
        var available_rates : Array = xr_interface.get_available_display_refresh_rates()
        if available_rates.size() == 0:
            print("OpenXR: Target does not support refresh rate extension")
        elif available_rates.size() == 1:
            # Only one available, so use it
            new_rate = available_rates[0]
        else:
            for rate in available_rates:
                if rate > new_rate and rate <= maximum_refresh_rate:
                    new_rate = rate

        # Did we find a better rate?
        if current_refresh_rate != new_rate:
            print("OpenXR: Setting refresh rate to ", str(new_rate))
            xr_interface.set_display_refresh_rate(new_rate)
            current_refresh_rate = new_rate

        # Now match our physics rate
        Engine.physics_ticks_per_second = current_refresh_rate
 
    ...

  .. code-tab:: csharp

    ...

        /// <summary>
        /// Handle OpenXR session ready
        /// </summary>
        private void OnOpenXRSessionBegun()
        {
            // Get the reported refresh rate
            var currentRefreshRate = _xrInterface.DisplayRefreshRate;
            GD.Print(currentRefreshRate > 0.0F
                ? $"OpenXR: Refresh rate reported as {currentRefreshRate}"
                : "OpenXR: No refresh rate given by XR runtime");

            // See if we have a better refresh rate available
            var newRate = currentRefreshRate;
            var availableRates = _xrInterface.GetAvailableDisplayRefreshRates();
            if (availableRates.Count == 0)
            {
                GD.Print("OpenXR: Target does not support refresh rate extension");
            }
            else if (availableRates.Count == 1)
            {
                // Only one available, so use it
                newRate = (float)availableRates[0];
            }
            else
            {
                GD.Print("OpenXR: Available refresh rates: ", availableRates);
                foreach (float rate in availableRates)
                    if (rate > newRate && rate <= MaximumRefreshRate)
                        newRate = rate;
            }

            // Did we find a better rate?
            if (currentRefreshRate != newRate)
            {
                GD.Print($"OpenXR: Setting refresh rate to {newRate}");
                _xrInterface.DisplayRefreshRate = newRate;
                currentRefreshRate = newRate;
            }

            // Now match our physics rate
            Engine.PhysicsTicksPerSecond = (int)currentRefreshRate;
        }

    ...

On visible state
----------------

This signal is emitted by OpenXR when our game becomes visible but is not focussed.
This is a bit of a weird description in OpenXR but it basically means that our game has just started
and we're about to switch to the focussed state next,
that the user has opened a system menu or the users has just took their headset off.

On receiving this signal we'll update our focussed state,
we'll change the process mode of our node to disabled which will pause processing on this node and it's children,
and emit our ``focus_lost`` signal.

If you've added this script to your root node,
this means your game will automatically pause when required.
If you haven't, you can connect a method to the signal that performs additional changes.

.. note::

  While your game is in visible state because the user has opened a system menu,
  Godot will keep rendering frames and head tracking will remain active so your game will remain visible in the background.
  However controller and hand tracking will be disabled until the user exits the system menu.

.. tabs::
  .. code-tab:: gdscript GDScript

    ...

    # Handle OpenXR visible state
    func _on_openxr_visible_state() -> void:
        # We always pass this state at startup,
        # but the second time we get this it means our player took off their headset
        if xr_is_focussed:
            print("OpenXR lost focus")

            xr_is_focussed = false

            # pause our game
            process_mode = Node.PROCESS_MODE_DISABLED

            emit_signal("focus_lost")
 
    ...

  .. code-tab:: csharp

    ...

        /// <summary>
        /// Handle OpenXR visible state
        /// </summary>
        private void OnOpenXRVisibleState()
        {
            // We always pass this state at startup,
            // but the second time we get this it means our player took off their headset
            if (_xrIsFocused)
            {
                GD.Print("OpenXR lost focus");

                _xrIsFocused = false;

                // Pause our game
                ProcessMode = ProcessModeEnum.Disabled;

                EmitSignal(SignalName.FocusLost);
            }
        }

    ...

On focussed state
-----------------

This signal is emitted by OpenXR when our game gets focus.
This is done at the completion of our startup,
but it can also be emitted when the user exits a system menu, or put their headset back on.

Note also that when your game starts while the user is not wearing their headset,
the game stays in 'visible' state until the user puts their headset on.

.. warning::

  It is thus important to keep your game paused while in visible mode.
  If you don't the game will keep on running while your user isn't interacting with your game.
  Also when the game returns to focussed mode,
  suddenly all controller and hand tracking is re-enabled and could have game breaking consequences
  if you do not react to this accordingly.
  Be sure to test this behaviour in your game!

While handling our signal we will update the focusses state, unpause our node and emit our ``focus_gained`` signal.

.. tabs::
  .. code-tab:: gdscript GDScript

    ...

    # Handle OpenXR focused state
    func _on_openxr_focused_state() -> void:
        print("OpenXR gained focus")
        xr_is_focussed = true

        # unpause our game
        process_mode = Node.PROCESS_MODE_INHERIT

        emit_signal("focus_gained")

    ...

  .. code-tab:: csharp

    ...

        /// <summary>
        /// Handle OpenXR focused state
        /// </summary>
        private void OnOpenXRFocusedState()
        {
            GD.Print("OpenXR gained focus");
            _xrIsFocused = true;

            // Un-pause our game
            ProcessMode = ProcessModeEnum.Inherit;

            EmitSignal(SignalName.FocusGained);
        }

    ...

On stopping state
-----------------

This signal is emitted by OpenXR when we enter our stop state.
There are some differences between platforms when this happens.
On some platforms this is only emitted when the game is being closed.
But on other platforms this will also be emitted every time the player takes off their headset.

For now this method is only a place holder.

.. tabs::
  .. code-tab:: gdscript GDScript

    ...

    # Handle OpenXR stopping state
    func _on_openxr_stopping() -> void:
        # Our session is being stopped.
        print("OpenXR is stopping")

    ...

  .. code-tab:: csharp

    ...

        /// <summary>
        /// Handle OpenXR stopping state
        /// </summary>
        private void OnOpenXRStopping()
        {
            // Our session is being stopped.
            GD.Print("OpenXR is stopping");
        }

    ...


On pose recentered
------------------

This signal is emitted by OpenXR when the user requests their view to be recentered.
Basically this communicates to your game that the user is now facing forward
and you should re-orient the player so they are facing forward in the virtual world.

As doing so is dependent on your game, your game needs to react accordingly.

All we do here is emit the ``pose_recentered`` signal.
You can connect to this signal and implement the actual recenter code.
Often it is enough to call :ref:`center_on_hmd() <class_XRServer_method_center_on_hmd>`.

.. tabs::
  .. code-tab:: gdscript GDScript

    ...

    # Handle OpenXR pose recentered signal
    func _on_openxr_pose_recentered() -> void:
        # User recentered view, we have to react to this by recentering the view.
        # This is game implementation dependent.
        emit_signal("pose_recentered")

  .. code-tab:: csharp

    ...

        /// <summary>
        /// Handle OpenXR pose recentered signal
        /// </summary>
        private void OnOpenXRPoseRecentered()
        {
            // User recentered view, we have to react to this by recentering the view.
            // This is game implementation dependent.
            EmitSignal(SignalName.PoseRecentered);
        }
    }

And that finished our script. It was written so that it can be re-used over multiple projects.
Just add it as the script on your main node (and extend it if needed)
or add it on a child node specific for this script.
