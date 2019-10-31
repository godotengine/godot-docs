.. _doc_recording_with_microphone:

Recording with microphone
=========================

Introduction
------------

Godot supports in-game audio recording for Windows, MacOS, Linux, Android and iOS. A simple demo is included in the official demo projects. You can download it on the `Godot download page <https://godotengine.org/download/linux>`_. It is located at godot-demo-project/audio/mic_record .

The structure of the demo
-------------------------

The demo consists of only 1 scene. This scene includes 2 major parts: GUI and the audio.

We will focus on the audio part. In this demo, a bus named ``Record`` with the effect : ``Record`` is created to handle the recording audio. An ``AudioStreamPlayer`` named ``AudioStreamRecord`` is used for recording.

.. image:: img/record_bus.png

.. image:: img/record_stream_player.png

.. tabs::
 .. code-tab:: gdscript GDScript

    var effect
    var recording
    
    func _ready():
        var idx = AudioServer.get_bus_index("Record")
        # the bus named "Record"
        effect = AudioServer.get_bus_effect(idx, 0)
        # the effect "Record"

The recording audio is a resource called ``AudioEffectRecord`` which has 3 methods: ``get_recording``, ``is_recording_active``, and ``set_recording_active``.
        
.. tabs::
  .. code-tab:: gdscript GDScript

    func _on_RecordButton_pressed():
        if effect.is_recording_active():
            recording = effect.get_recording()
            $PlayButton.disabled = false
            $SaveButton.disabled = false
            effect.set_recording_active(false)
            $RecordButton.text = "Record"
            $Status.text = ""
        else:
            $PlayButton.disabled = true
            $SaveButton.disabled = true
            effect.set_recording_active(true)
            $RecordButton.text = "Stop"
            $Status.text = "Recording..."

At the start of the demo, the recording effect is not active, when you pressed the ``RecordButton``, by set_recording_active(true), you start the recording. As effect.is_recording_active() is ``true``, the recording can be store as a variable by calling effect.get_recording().

.. tabs::
  .. code-tab:: gdscript GDScript

    func _on_PlayButton_pressed():
        print(recording)
        print(recording.format)
        print(recording.mix_rate)
        print(recording.stereo)
        var data = recording.get_data()
        print(data)
        print(data.size())
        $AudioStreamPlayer.stream = recording
        $AudioStreamPlayer.play()

To playback the recording, you assign the recording as the stream of the ``AudioStreamPlayer`` and call play().

.. tabs::
  .. code-tab:: gdscript GDScript

  func _on_SaveButton_pressed():
	var save_path = $SaveButton/Filename.text
	recording.save_to_wav(save_path)
	$Status.text = "Saved WAV file to: %s\n(%s)" % [save_path, ProjectSettings.globalize_path(save_path)]

To save the recording, you call save_to_wav().




 
