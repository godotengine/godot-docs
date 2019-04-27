.. _doc_sync_with_audio:

Sync the gameplay with audio and music
=======================================

Introduction
------------

Normally, music plays on the background, without precise interaction with the gameplay.

For sound effects, there may be a slight delay and latency in the output, but it's so small players won't really care in most cases.

Still, for some games (mainly, rythm games), it may be required to synchronize player actions with something happening in a song (usually in sync with the BPM). For this, having more precise timing information for an exact playback position is very welcome.

Achieving very low playback timing precision is very difficult. This because many factors are at play during audio playback, not just the song:

* Audio is mixed in chunks (not continuously), depending on the size of buffers used.
* Audio has latency after mixed, it doesn't immediately play after mixed.
* Graphics APIs display two or three frames late.
* When playing on TVs, some delay may be added due to image processing.

That said, beginning Godot 3.2, some helpers were added to obtain more precise playback timing.

Using the system clock to sync
-------------------------------

If you call :ref:`AudioStreamPlayer.play()<class_AudioStreamPlayer_method_play>`, sound will not begin immediately, but when the 
audio thread processes the next block. 

The timing when the next mix callback will happen can be estimated by calling :ref:`AudioServer.get_time_to_next_mix()<class_AudioServer_method_get_time_to_next_mix>` and the output latency can also be guessed by calling :ref:`AudioServer.get_output_latency()<class_AudioServer_get_output_latency>`. Add these two and it's possible to know almost exactly when a song will begin playing.

.. tabs::
 .. code-tab:: gdscript GDScript

    var actual_play_time = AudioServer.get_time_to_next_mix() + AudioServer.get_output_latency()
    $Song.play()

This way, obtaining the actual playback position is possible:

.. tabs::
 .. code-tab:: gdscript GDScript

    var time_begin 
    var time_delay
     
    func _ready()
        time_begin = OS.get_ticks_usec()
        time_delay = AudioServer.get_time_to_next_mix() + AudioServer.get_output_latency()
        $Player.play()
    
    func _process(delta):
        # obtain from ticks
        var time = (OS.get_ticks_usec() - time_begin) / 1000000.0
        # compensate for latency
        time -= time_delay		
        # may be below 0 (did not being yet)
        time = max(0, time)
        print("Time is: ",time)


In the long run, though, the sound hardware clock is never exactly in sync with the system clock, so they will slowly drift. For a rythm game where a song begins and ends after a few minutes, this approach is fine. For a game where playback can last a much longer time, the game will eventually go out of sync and a different approach is needed.

Using the sound hardware clock to sync
-------------------------------

Using :ref:`AudioStreamPlayer.get_playback_position()<class_AudioStreamPlayer_method_get_playback_position>` to obtain the current position for the song sounds ideal, but it's not that useful as-is. This value will increment in chunks, so many calls can return the same value. Added to this, the value will be out of sync with the speakers.

To compensate for the chunked output, there is a function that can help: :ref:`AudioServer.get_time_since_last_mix()<class_AudioServer_get_time_since_last_mix>`. Adding the return value from this function increases precision:

.. tabs::
 .. code-tab:: gdscript GDScript

    var time = $Player.get_playback_position() + AudioServer.get_time_since_last_mix()

Finally, substract the latency:

.. tabs::
 .. code-tab:: gdscript GDScript

    var time = $Player.get_playback_position() + AudioServer.get_time_since_last_mix() - AudioServer.get_output_latency()

The result may be a bit jittery due how multiple threads work. Just check that the value is not less than in the previous frame (discard it if so). This is also a less precise approach than the one before, but it will work for songs of any length, or synchronizing anything (sound effects, as an example) to music.

Here is the same code as before using this approach:

.. tabs::
 .. code-tab:: gdscript GDScript

     
    func _ready()
        $Player.play()
    
    func _process(delta):
        var time = $Player.get_playback_position() + AudioServer.get_time_since_last_mix()
        # Compensate for output latency
        time -= AudioServer.get_output_latency()
        print("Time is: ",time)



