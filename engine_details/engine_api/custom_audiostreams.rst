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

    
    #include "godot_cpp/classes/audio_stream.hpp"
    #include "godot_cpp/classes/ref_counted.hpp"
    #include "godot_cpp/classes/wrapped.hpp"

    namespace godot {
    struct AudioFrame;
    }

    using godot::AudioFrame;
    using godot::AudioStream;
    using godot::AudioStreamPlayback;
    using godot::String;

    class AudioStreamMyTone : public AudioStream {
        GDCLASS(AudioStreamMyTone, AudioStream)
        friend class AudioStreamPlaybackResampledMyTone;

    private:
        uint64_t pos = 0;
        float mix_rate = 44100.0F; // AudioDriverManager::DEFAULT_MIX_RATE
        double hz = 639.0;

    public:
        virtual godot::Ref<AudioStreamPlayback> _instantiate_playback() const override;
        virtual String _get_stream_name() const override;

        virtual double _get_length() const override { return 0.0; }

        void gen_tone(AudioFrame *pcm_buf, int size);
        void reset();
        void set_position(uint64_t p);

        float get_mix_rate() const;
        double get_freq() const;
        bool set_freq(double freq_hz);

    protected:
        static void _bind_methods();
    };

.. code-block:: cpp
    :caption: audiostream_mytone.cpp

    #include "audio_stream_mytone.h"

    #include <godot_cpp/core/math.hpp>
    #include <godot_cpp/core/math_defs.hpp>

    #include "audio_streamplaybackresampled_mytone.h"

    using namespace godot;

    Ref<AudioStreamPlayback> AudioStreamMyTone::_instantiate_playback() const {
        Ref<AudioStreamPlaybackResampledMyTone> playback;
        playback.instantiate();
        playback->base = Ref<AudioStreamMyTone>(this);
        return playback;
    }
    String AudioStreamMyTone::_get_stream_name() const {
        return "MyTone";
    }
    void AudioStreamMyTone::gen_tone(AudioFrame *pcm_buf, int size) {
        for (int i = 0; i < size; i++) {
            const float value = Math::sin(2.0 * Math::PI * double(pos + i) / (double(mix_rate) / hz));
            pcm_buf[i].left = value;
            pcm_buf[i].right = value;
        }
        pos += size;
    }
    void AudioStreamMyTone::reset() {
        set_position(0);
    }
    void AudioStreamMyTone::set_position(uint64_t p) {
        pos = p;
    }
    float AudioStreamMyTone::get_mix_rate() const {
        return mix_rate;
    }
    double AudioStreamMyTone::get_freq() const {
        return hz;
    }
    bool AudioStreamMyTone::set_freq(double freq_hz) {
        if (freq_hz > 0 && freq_hz < mix_rate / 2.0f) {
            hz = freq_hz;
            return true;
        }
        return false;
    }
    void AudioStreamMyTone::_bind_methods() {
        ClassDB::bind_method(D_METHOD("reset"), &AudioStreamMyTone::reset);
        ClassDB::bind_method(D_METHOD("get_freq"), &AudioStreamMyTone::get_freq);
        ClassDB::bind_method(D_METHOD("set_freq"), &AudioStreamMyTone::set_freq);
    }

References:
~~~~~~~~~~~

-  `servers/audio/audio_stream.h <https://github.com/godotengine/godot/blob/master/servers/audio/audio_stream.h>`__


Create an AudioStreamPlayback
-----------------------------

AudioStreamPlayer uses ``mix`` callback to obtain PCM data. The callback must match sample rate and fill the buffer.

Since AudioStreamPlayback is controlled by the audio thread, i/o and dynamic memory allocation are forbidden.

.. code-block:: cpp
    :caption: audiostreamplayer_mytone.h

    #pragma once

    #include "godot_cpp/classes/audio_frame.hpp"
    #include "godot_cpp/classes/audio_stream_playback.hpp"
    #include "godot_cpp/classes/ref_counted.hpp"
    #include "godot_cpp/classes/wrapped.hpp"

    using godot::AudioFrame;
    using godot::AudioStreamPlayback;

    class AudioStreamMyTone;

    class AudioStreamPlaybackMyTone : public AudioStreamPlayback {
        GDCLASS(AudioStreamPlaybackMyTone, AudioStreamPlayback)
        friend AudioStreamMyTone;

    private:
        enum {
            PCM_BUFFER_SIZE = 4096
        };
        enum {
            MIX_FRAC_BITS = 13,
            MIX_FRAC_LEN = (1 << MIX_FRAC_BITS),
            MIX_FRAC_MASK = MIX_FRAC_LEN - 1,
        };
        godot::Ref<AudioStreamMyTone> base;
        bool active = false;

    public:
        virtual void _start(double p_from_pos = 0.0) override;
        virtual void _stop() override;
        virtual bool _is_playing() const override;

        virtual int _get_loop_count() const override;

        virtual double _get_playback_position() const override;
        virtual void _seek(double p_time) override;

        virtual int _mix(AudioFrame *p_buffer, float p_rate_scale, int p_frames) override;

    protected:
        static void _bind_methods();
    };

.. code-block:: cpp
    :caption: audiostreamplayer_mytone.cpp

    #include "audio_streamplayback_mytone.h"

    #include "audio_stream_mytone.h"

    using namespace godot;

    void AudioStreamPlaybackMyTone::_start(double p_from_pos) {
        seek(p_from_pos);
        active = true;
    }
    void AudioStreamPlaybackMyTone::_stop() {
        active = false;
        base->reset();
    }
    bool AudioStreamPlaybackMyTone::_is_playing() const {
        return active;
    }
    int AudioStreamPlaybackMyTone::_get_loop_count() const {
        return 0;
    }
    double AudioStreamPlaybackMyTone::_get_playback_position() const {
        return 0.0;
    }
    void AudioStreamPlaybackMyTone::_seek(double p_time) {
        if (p_time < 0) {
            p_time = 0;
        }

        base->set_position(uint64_t(p_time * base->mix_rate) << MIX_FRAC_BITS);
    }
    int AudioStreamPlaybackMyTone::_mix(AudioFrame *p_buffer, float p_rate, int p_frames) {
        ERR_FAIL_COND_V(!active, 0);
        if (!active) {
            return 0;
        }

        base->gen_tone(p_buffer, p_frames);
        return p_frames;
    }
    void AudioStreamPlaybackMyTone::_bind_methods() {
    }

Resampling
~~~~~~~~~~

Godot's AudioServer currently uses 44100 Hz sample rate. When other sample rates are
needed such as 48000, either provide one or use AudioStreamPlaybackResampled.
Godot provides cubic interpolation for audio resampling.

Instead of overloading ``mix``, AudioStreamPlaybackResampled uses ``_mix_internal`` to
query AudioFrames and ``get_stream_sampling_rate`` to query current mix rate.

.. code-block:: cpp
    :caption: mytone_audiostream_resampled.h

    #pragma once

    #include "godot_cpp/classes/audio_frame.hpp"
    #include "godot_cpp/classes/audio_stream_playback_resampled.hpp"
    #include "godot_cpp/classes/ref_counted.hpp"
    #include "godot_cpp/classes/wrapped.hpp"

    using godot::AudioFrame;
    using godot::AudioStreamPlaybackResampled;

    class AudioStreamMyTone;

    class AudioStreamPlaybackResampledMyTone : public AudioStreamPlaybackResampled {
        GDCLASS(AudioStreamPlaybackResampledMyTone, AudioStreamPlaybackResampled)
        friend AudioStreamMyTone;

    private:
        enum {
            PCM_BUFFER_SIZE = 4096
        };
        enum {
            MIX_FRAC_BITS = 13,
            MIX_FRAC_LEN = (1 << MIX_FRAC_BITS),
            MIX_FRAC_MASK = MIX_FRAC_LEN - 1,
        };
        godot::Ref<AudioStreamMyTone> base;
        bool active = false;

    public:
        virtual void _start(double p_from_pos = 0.0) override;
        virtual void _stop() override;
        virtual bool _is_playing() const override;

        virtual int _get_loop_count() const override;

        virtual double _get_playback_position() const override;
        virtual void _seek(double p_time) override;

        virtual int _mix_resampled(AudioFrame *p_buffer, int p_frames) override;
        virtual float _get_stream_sampling_rate() const override;

    protected:
        static void _bind_methods();
    };

.. code-block:: cpp
    :caption: mytone_audiostream_resampled.cpp

    #include "audio_streamplaybackresampled_mytone.h"

    #include "audio_stream_mytone.h"

    using namespace godot;

    void AudioStreamPlaybackResampledMyTone::_start(double p_from_pos) {
        seek(p_from_pos);
        active = true;
    }
    void AudioStreamPlaybackResampledMyTone::_stop() {
        active = false;
        base->reset();
    }
    bool AudioStreamPlaybackResampledMyTone::_is_playing() const {
        return active;
    }
    int AudioStreamPlaybackResampledMyTone::_get_loop_count() const {
        return 0;
    }
    double AudioStreamPlaybackResampledMyTone::_get_playback_position() const {
        return 0.0;
    }
    void AudioStreamPlaybackResampledMyTone::_seek(double p_time) {
        if (p_time < 0) {
            p_time = 0;
        }

        base->set_position(uint64_t(p_time * base->mix_rate) << MIX_FRAC_BITS);
    }
    int AudioStreamPlaybackResampledMyTone::_mix_resampled(AudioFrame *p_buffer, int p_frames) {
        ERR_FAIL_COND_V(!active, 0);
        if (!active) {
            return 0;
        }

        base->gen_tone(p_buffer, p_frames);
        return p_frames;
    }
    float AudioStreamPlaybackResampledMyTone::_get_stream_sampling_rate() const {
        return base->get_mix_rate();
    }
    void AudioStreamPlaybackResampledMyTone::_bind_methods() {
    }

References:
~~~~~~~~~~~
-  `core/math/audio_frame.h <https://github.com/godotengine/godot/blob/master/core/math/audio_frame.h>`__
-  `servers/audio/audio_stream.h <https://github.com/godotengine/godot/blob/master/servers/audio/audio_stream.h>`__
-  `scene/audio/audio_stream_player.cpp <https://github.com/godotengine/godot/blob/master/scene/audio/audio_stream_player.cpp>`__
