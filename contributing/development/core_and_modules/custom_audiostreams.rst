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

    /* audio_stream_mytone.h */

    #ifndef AUDIOSTREAMMYTONE_H
    #define AUDIOSTREAMMYTONE_H

    #include <godot_cpp/classes/audio_frame.hpp>
    #include <godot_cpp/classes/audio_stream.hpp>
    #include <godot_cpp/godot.hpp>

    namespace godot {

    class AudioStreamMyTone : public AudioStream {
        GDCLASS(AudioStreamMyTone, AudioStream)

    private:
        friend class AudioStreamPlaybackMyTone;
        float pos = 0;
        int mix_rate = 44100;
        float hz = 639;

    public:
        void reset();
        void set_position(uint64_t pos);
        virtual String get_stream_name() const;
        void gen_tone(AudioFrame *p_buffer, double p_rate, int p_frames);
        void set_hz(float p_hz);
        float get_hz();
        virtual float get_length() const;
        AudioStreamMyTone();
        virtual Ref<AudioStreamPlayback> _instantiate_playback() const override;

    protected:
        static void _bind_methods();
    };
    } // namespace godot

    #endif

.. code-block:: cpp

    /* audio_stream_mytone.cpp */

    #include "audio_stream_mytone.h"
    #include "audio_stream_player_mytone.h"
    #include "godot_cpp/classes/audio_server.hpp"

    using namespace godot;

    AudioStreamMyTone::AudioStreamMyTone() : hz(639) {
        mix_rate = AudioServer::get_singleton()->get_mix_rate();
        pos = 0;
    }

    Ref<AudioStreamPlayback> AudioStreamMyTone::_instantiate_playback() const {
        Ref<AudioStreamPlaybackMyTone> talking_tree;
        talking_tree.instantiate();
        talking_tree->base = Ref<AudioStreamMyTone>(this);
        return talking_tree;
    }

    String AudioStreamMyTone::get_stream_name() const {
        return "MyTone";
    }

    void AudioStreamMyTone::reset() {
        set_position(0);
    }

    void AudioStreamMyTone::set_position(uint64_t p) {
        pos = p;
    }

    void AudioStreamMyTone::gen_tone(AudioFrame *p_buffer, double p_rate, int p_frames) {
        for (int i = 0; i < p_frames; i++) {
            float inc = 1.0 / (float(mix_rate) / hz);
            pos += inc;
            if (pos > 1.0) {
                pos -= 1.0;
            }
            p_buffer[i].left = sin(2.0 * Math_PI * pos);
            p_buffer[i].right = sin(2.0 * Math_PI * pos);
        }
    }

    void AudioStreamMyTone::set_hz(float p_hz) {
        hz = p_hz;
    }

    float AudioStreamMyTone::get_hz() {
        return hz;
    }

    float AudioStreamMyTone::get_length() const {
        return 0;
    }

    void AudioStreamMyTone::_bind_methods() {
        ClassDB::bind_method(D_METHOD("reset"), &AudioStreamMyTone::reset);
        ClassDB::bind_method(D_METHOD("get_stream_name"), &AudioStreamMyTone::get_stream_name);
        ClassDB::bind_method(D_METHOD("get_hz"), &AudioStreamMyTone::get_hz);
        ClassDB::bind_method(D_METHOD("set_hz", "hz"), &AudioStreamMyTone::set_hz);

        ClassDB::add_property("AudioStreamMyTone",
                              PropertyInfo(Variant::FLOAT, "hz", PROPERTY_HINT_RANGE, "10,20000,suffix:Hz"), "set_hz",
                              "get_hz");
    }

References:
~~~~~~~~~~~

-  `servers/audio/audio_stream.h <https://github.com/godotengine/godot/blob/master/servers/audio/audio_stream.h>`__


Create an AudioStreamPlayback
-----------------------------

AudioStreamPlayer uses ``mix`` callback to obtain PCM data. The callback must match sample rate and fill the buffer.

Since AudioStreamPlayback is controlled by the audio thread, i/o and dynamic memory allocation are forbidden.

.. code-block:: cpp

    /*  audio_stream_player_mytone.h */

    #ifndef AUDIOSTREAMPLAYERMYTONE_H
    #define AUDIOSTREAMPLAYERMYTONE_H

    #include <godot_cpp/classes/audio_frame.hpp>
    #include <godot_cpp/classes/audio_server.hpp>
    #include <godot_cpp/classes/audio_stream.hpp>
    #include <godot_cpp/classes/audio_stream_playback.hpp>
    #include <godot_cpp/godot.hpp>

    #include "audio_stream_mytone.h"

    namespace godot {

    class AudioStreamPlaybackMyTone : public AudioStreamPlayback {
        GDCLASS(AudioStreamPlaybackMyTone, AudioStreamPlayback)
        friend class AudioStreamMyTone;

    private:
        enum {
            PCM_BUFFER_SIZE = 4096
        };
        enum {
            MIX_FRAC_BITS = 13,
            MIX_FRAC_LEN = (1 << MIX_FRAC_BITS),
            MIX_FRAC_MASK = MIX_FRAC_LEN - 1,
        };
        Ref<AudioStreamMyTone> base;
        bool active;
        float mixed;

    public:
        static void _bind_methods();

        virtual void _start(double p_from_pos = 0.0) override;
        virtual void _stop() override;
        virtual bool _is_playing() const override;
        virtual int _get_loop_count() const override; // times it looped
        virtual double _get_playback_position() const override;
        virtual void _seek(double p_time) override;
        virtual int _mix(AudioFrame *p_buffer, double p_rate_scale, int p_frames) override;
        virtual float _get_length() const; // if supported, otherwise return 0
        AudioStreamPlaybackMyTone();
        ~AudioStreamPlaybackMyTone();
    };
    } // namespace godot

    #endif

.. code-block:: cpp

    /* audio_stream_player_mytone.cpp */

    #include "audio_stream_player_mytone.h"
    #include "audio_stream_mytone.h"

    using namespace godot;

    AudioStreamPlaybackMyTone::AudioStreamPlaybackMyTone() : active(false) {
    }

    AudioStreamPlaybackMyTone::~AudioStreamPlaybackMyTone() {
    }

    void AudioStreamPlaybackMyTone::_stop() {
        active = false;
        base->reset();
    }

    void AudioStreamPlaybackMyTone::_start(double p_from_pos) {
        active = true;
        mixed = 0.0;
    }

    void AudioStreamPlaybackMyTone::_seek(double p_time) {
        if (p_time < 0) {
            p_time = 0;
        }
    }

    int AudioStreamPlaybackMyTone::_mix(AudioFrame *p_buffer, double p_rate, int p_frames) {
        ERR_FAIL_COND_V(!active, 0);
        if (!active) {
            return 0;
        }
        base->gen_tone(p_buffer, p_rate, p_frames);
        float mix_rate = base->mix_rate;
        mixed += p_frames / mix_rate;
        return p_frames;
    }

    int AudioStreamPlaybackMyTone::_get_loop_count() const {
        return 10;
    }

    double AudioStreamPlaybackMyTone::_get_playback_position() const {
        return 0;
    }

    float AudioStreamPlaybackMyTone::_get_length() const {
        return 0.0;
    }

    bool AudioStreamPlaybackMyTone::_is_playing() const {
        return active;
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

	#include "core/reference.h"
	#include "core/resource.h"
	#include "servers/audio/audio_stream.h"

	class AudioStreamMyToneResampled;

	class AudioStreamPlaybackResampledMyTone : public AudioStreamPlaybackResampled {
		GDCLASS(AudioStreamPlaybackResampledMyTone, AudioStreamPlaybackResampled)
		friend class AudioStreamMyToneResampled;

	private:
		enum {
			PCM_BUFFER_SIZE = 4096
		};
		enum {
			MIX_FRAC_BITS = 13,
			MIX_FRAC_LEN = (1 << MIX_FRAC_BITS),
			MIX_FRAC_MASK = MIX_FRAC_LEN - 1,
		};
		void *pcm_buffer;
		Ref<AudioStreamMyToneResampled> base;
		bool active;

	protected:
		virtual void _mix_internal(AudioFrame *p_buffer, int p_frames);

	public:
		virtual void start(float p_from_pos = 0.0);
		virtual void stop();
		virtual bool is_playing() const;
		virtual int get_loop_count() const; // times it looped
		virtual float get_playback_position() const;
		virtual void seek(float p_time);
		virtual float get_length() const; // if supported, otherwise return 0
		virtual float get_stream_sampling_rate();
		AudioStreamPlaybackResampledMyTone();
		~AudioStreamPlaybackResampledMyTone();
	};

.. code-block:: cpp

	#include "mytone_audiostream_resampled.h"

	#include "core/math/math_funcs.h"
	#include "core/print_string.h"

	AudioStreamPlaybackResampledMyTone::AudioStreamPlaybackResampledMyTone()
			: active(false) {
		AudioServer::get_singleton()->lock();
		pcm_buffer = AudioServer::get_singleton()->audio_data_alloc(PCM_BUFFER_SIZE);
		zeromem(pcm_buffer, PCM_BUFFER_SIZE);
		AudioServer::get_singleton()->unlock();
	}
	AudioStreamPlaybackResampledMyTone::~AudioStreamPlaybackResampledMyTone() {
		if (pcm_buffer) {
			AudioServer::get_singleton()->audio_data_free(pcm_buffer);
			pcm_buffer = NULL;
		}
	}
	void AudioStreamPlaybackResampledMyTone::stop() {
		active = false;
		base->reset();
	}
	void AudioStreamPlaybackResampledMyTone::start(float p_from_pos) {
		seek(p_from_pos);
		active = true;
	}
	void AudioStreamPlaybackResampledMyTone::seek(float p_time) {
		float max = get_length();
		if (p_time < 0) {
				p_time = 0;
		}
		base->set_position(uint64_t(p_time * base->mix_rate) << MIX_FRAC_BITS);
	}
	void AudioStreamPlaybackResampledMyTone::_mix_internal(AudioFrame *p_buffer, int p_frames) {
		ERR_FAIL_COND(!active);
		if (!active) {
			return;
		}
		zeromem(pcm_buffer, PCM_BUFFER_SIZE);
		int16_t *buf = (int16_t *)pcm_buffer;
		base->gen_tone(buf, p_frames);

		for(int i = 0;  i < p_frames; i++) {
			float sample = float(buf[i]) / 32767.0;
				p_buffer[i] = AudioFrame(sample, sample);
		}
	}
	float AudioStreamPlaybackResampledMyTone::get_stream_sampling_rate() {
		return float(base->mix_rate);
	}
	int AudioStreamPlaybackResampledMyTone::get_loop_count() const {
		return 0;
	}
	float AudioStreamPlaybackResampledMyTone::get_playback_position() const {
		return 0.0;
	}
	float AudioStreamPlaybackResampledMyTone::get_length() const {
		return 0.0;
	}
	bool AudioStreamPlaybackResampledMyTone::is_playing() const {
		return active;
	}

References:
~~~~~~~~~~~
-  `core/math/audio_frame.h <https://github.com/godotengine/godot/blob/master/core/math/audio_frame.h>`__
-  `servers/audio/audio_stream.h <https://github.com/godotengine/godot/blob/master/servers/audio/audio_stream.h>`__
-  `scene/audio/audio_stream_player.cpp <https://github.com/godotengine/godot/blob/master/scene/audio/audio_stream_player.cpp>`__
