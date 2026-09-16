.. _doc_custom_audiostreams:

Custom AudioStreams
===================

Introduction
------------

AudioStream is the base class of all audio emitting objects.
AudioStreamPlayer binds onto an AudioStream to emit PCM data
into an AudioServer which manages audio drivers.

All audio resources require two audio based classes: AudioStream
and AudioStreamPlayback. As a data container, AudioStream contains
the resource and exposes itself to GDScript. AudioStream references
its own internal custom AudioStreamPlayback which translates
AudioStream into PCM data.

This guide assumes the reader knows how to create C++ modules. If not, refer to this guide
:ref:`doc_custom_modules_in_cpp`.

References:
~~~~~~~~~~~

-  `servers/audio/audio_stream.h <https://github.com/godotengine/godot/blob/master/servers/audio/audio_stream.h>`__
-  `scene/audio/audio_stream_player.cpp <https://github.com/godotengine/godot/blob/master/scene/audio/audio_stream_player.cpp>`__

What for?
---------

- Binding external libraries (like Wwise, FMOD, etc).
- Adding custom audio queues
- Adding support for more audio formats

Create an AudioStream
---------------------

An AudioStream consists of three components: data container, stream name,
and an AudioStreamPlayback friend class generator. Audio data can be
loaded in a number of ways such as with an internal counter for a tone generator,
internal/external buffer, or a file reference.

Some AudioStreams need to be stateless such as objects loaded from
ResourceLoader. ResourceLoader loads once and references the same
object regardless how many times ``load`` is called on a specific resource.
Therefore, playback state must be self-contained in AudioStreamPlayback.

.. code-block:: cpp
    :caption: audiostream_mytone.h

    #pragma once

    #include "servers/audio/audio_stream.h"

    class AudioStreamMyTone : public AudioStream {
        GDCLASS(AudioStreamMyTone, AudioStream)

    private:
        friend class AudioStreamPlaybackMyTone;

    public:
        virtual Ref<AudioStreamPlayback> instantiate_playback() override;
        virtual String get_stream_name() const override;

        virtual double get_length() const override { return 0.0; }

        virtual void get_parameter_list(List<Parameter> *r_parameters) override;

    protected:
        static void _bind_methods();
    };


.. code-block:: cpp
    :caption: audiostream_mytone.cpp

    #include "audiostream_mytone.h"

    #include "audiostream_playback_mytone.h"

    Ref<AudioStreamPlayback> AudioStreamMyTone::instantiate_playback() {
        Ref<AudioStreamPlaybackMyTone> playback;
        playback.instantiate();
        playback->base = Ref<AudioStreamMyTone>(this);
        playback->init();
        return playback;
    }

    String AudioStreamMyTone::get_stream_name() const {
        return "MyTone";
    }

    void AudioStreamMyTone::get_parameter_list(List<Parameter> *r_parameters) {
        r_parameters->push_back(Parameter(PropertyInfo(Variant::FLOAT, "Frequency", PROPERTY_HINT_RANGE, "44.0F, 16000.0"), "220.0"));
    }

    void AudioStreamMyTone::_bind_methods() {}

References:
~~~~~~~~~~~

-  `servers/audio/audio_stream.h <https://github.com/godotengine/godot/blob/master/servers/audio/audio_stream.h>`__


Create an AudioStreamPlayback
-----------------------------

AudioStreamPlayer uses ``mix`` callback to obtain PCM data. The callback must match sample rate and fill the buffer.

Since AudioStreamPlayback is controlled by the audio thread, i/o and dynamic memory allocation are forbidden.

.. code-block:: cpp
    :caption: audiostream_playback_mytone.h

    #pragma once

    #include "servers/audio/audio_stream.h"

    class AudioStreamMyTone;

    class AudioStreamPlaybackMyTone : public AudioStreamPlayback {
        GDCLASS(AudioStreamPlaybackMyTone, AudioStreamPlayback)
        friend AudioStreamMyTone;

    private:
        Ref<AudioStreamMyTone> base;
        double pos = 0.0;
        float freq_hz = 220.0F;
        bool active = false;

    public:
        virtual ~AudioStreamPlaybackMyTone() = default;

        virtual void start(double p_from_pos = 0.0) override;
        virtual void stop() override;
        virtual bool is_playing() const override;

        virtual int get_loop_count() const override;

        virtual double get_playback_position() const override;
        virtual void seek(double p_time) override;

        virtual int mix(AudioFrame *p_buffer, float p_rate_scale, int p_frames) override;

        virtual void set_parameter(const StringName &p_name, const Variant &p_value) override;
        virtual Variant get_parameter(const StringName &p_name) const override;

    protected:
        void reset();
        bool init();

        void generate(AudioFrame *pcm_buf, int size);

        void set_freq(float value);
        float get_freq() const;

        static void _bind_methods();
    };

.. code-block:: cpp
    :caption: audiostream_playback_mytone.cpp

    #include "audiostream_playback_mytone.h"

    #include <core/math/math_funcs.h>
    #include <core/object/class_db.h>
    #include <servers/audio/audio_server.h>

    void AudioStreamPlaybackMyTone::start(double p_from_pos) {
        active = true;
    }

    void AudioStreamPlaybackMyTone::stop() {
        active = false;
    }

    bool AudioStreamPlaybackMyTone::is_playing() const {
        return active;
    }

    int AudioStreamPlaybackMyTone::get_loop_count() const {
        return 0;
    }

    double AudioStreamPlaybackMyTone::get_playback_position() const {
        return 0.0;
    }

    void AudioStreamPlaybackMyTone::seek(double p_time) {
        if (p_time < 0) {
            p_time = 0;
        }

        const float mix_rate = AudioServer::get_singleton()->get_mix_rate();
        pos = p_time * mix_rate;
    }

    int AudioStreamPlaybackMyTone::mix(AudioFrame *p_buffer, float p_rate, int p_frames) {
        ERR_FAIL_COND_V(!is_playing(), 0);
        if (!is_playing()) {
            return 0;
        }

        generate(p_buffer, p_frames);
        return p_frames;
    }

    void AudioStreamPlaybackMyTone::set_parameter(const StringName &p_name, const Variant &p_value) {
        if (p_name == SNAME("Frequency")) {
            const float value = p_value;
            set_freq(value);
        }
    }

    Variant AudioStreamPlaybackMyTone::get_parameter(const StringName &p_name) const {
        if (p_name == SNAME("Frequency")) {
            return Variant(get_freq());
        }
        ERR_FAIL_COND_V(true, Variant());
        return Variant{};
    }

    void AudioStreamPlaybackMyTone::reset() {
        seek(0.0);
    }

    bool AudioStreamPlaybackMyTone::init() {
        reset();
        return true;
    }

    void AudioStreamPlaybackMyTone::generate(AudioFrame *pcm_buf, int size) {
        if (!active) {
            return;
        }
        const float mix_rate = AudioServer::get_singleton()->get_mix_rate();
        for (int i = 0; i < size; i++) {
            const float sample = 32767.0F * Math::sin(2.0F * Math::PI * float(pos + i) / (mix_rate / freq_hz));
            pcm_buf[i].left = sample;
            pcm_buf[i].right = sample;
        }
        pos += size;
    }

    void AudioStreamPlaybackMyTone::set_freq(float value) {
        freq_hz = CLAMP(value, 44.0F, 16000.0F);
    }

    float AudioStreamPlaybackMyTone::get_freq() const {
        return freq_hz;
    }

    void AudioStreamPlaybackMyTone::_bind_methods() {
        ClassDB::bind_method(D_METHOD("reset"), &AudioStreamPlaybackMyTone::reset);
        ClassDB::bind_method(D_METHOD("set_freq", "value"), &AudioStreamPlaybackMyTone::set_freq);
        ClassDB::bind_method(D_METHOD("get_freq"), &AudioStreamPlaybackMyTone::get_freq);
    }

Resampling
~~~~~~~~~~

Godot's AudioServer currently uses 44100 Hz sample rate. When other sample rates are
needed such as 48000, either provide one or use AudioStreamPlaybackResampled.
Godot provides cubic interpolation for audio resampling.

Instead of overloading ``mix``, AudioStreamPlaybackResampled uses ``_mix_internal`` to
query AudioFrames and ``get_stream_sampling_rate`` to query current mix rate.

References:
~~~~~~~~~~~
-  `core/math/audio_frame.h <https://github.com/godotengine/godot/blob/master/core/math/audio_frame.h>`__
-  `servers/audio/audio_stream.h <https://github.com/godotengine/godot/blob/master/servers/audio/audio_stream.h>`__
-  `scene/audio/audio_stream_player.cpp <https://github.com/godotengine/godot/blob/master/scene/audio/audio_stream_player.cpp>`__
