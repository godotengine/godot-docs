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

	/* audiostream_mytone.h */

	#include "core/reference.h"
	#include "core/resource.h"
	#include "servers/audio/audio_stream.h"

	class AudioStreamMyTone : public AudioStream {
		GDCLASS(AudioStreamMyTone, AudioStream)

	private:
		friend class AudioStreamPlaybackMyTone;
		uint64_t pos;
		int mix_rate;
		bool stereo;
		int hz;

	public:
		void reset();
		void set_position(uint64_t pos);
		virtual Ref<AudioStreamPlayback> instance_playback();
		virtual String get_stream_name() const;
		void gen_tone(int16_t *pcm_buf, int size);
		virtual float get_length() const { return 0; } // if supported, otherwise return 0
		AudioStreamMyTone();

	protected:
		static void _bind_methods();
	};

.. code-block:: cpp

	/* audiostream_mytone.cpp */

	#include "audiostream_mytone.h"

	AudioStreamMyTone::AudioStreamMyTone()
			: mix_rate(44100), stereo(false), hz(639) {
	}

	Ref<AudioStreamPlayback> AudioStreamMyTone::instance_playback() {
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
	void AudioStreamMyTone::gen_tone(int16_t *pcm_buf, int size) {
		for (int i = 0; i < size; i++) {
			pcm_buf[i] = 32767.0 * sin(2.0 * Math_PI * double(pos + i) / (double(mix_rate) / double(hz)));
		}
		pos += size;
	}
	void AudioStreamMyTone::_bind_methods() {
		ClassDB::bind_method(D_METHOD("reset"), &AudioStreamMyTone::reset);
		ClassDB::bind_method(D_METHOD("get_stream_name"), &AudioStreamMyTone::get_stream_name);
	}

References:
~~~~~~~~~~~

-  `servers/audio/audio_stream.h <https://github.com/godotengine/godot/blob/master/servers/audio/audio_stream.h>`__


Create an AudioStreamPlayback
-----------------------------

AudioStreamPlayer uses ``mix`` callback to obtain PCM data. The callback must match sample rate and fill the buffer.

Since AudioStreamPlayback is controlled by the audio thread, i/o and dynamic memory allocation are forbidden.

.. code-block:: cpp

	/*  audiostreamplayer_mytone.h */

	#include "core/reference.h"
	#include "core/resource.h"
	#include "servers/audio/audio_stream.h"

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
		void *pcm_buffer;
		Ref<AudioStreamMyTone> base;
		bool active;

	public:
		virtual void start(float p_from_pos = 0.0);
		virtual void stop();
		virtual bool is_playing() const;
		virtual int get_loop_count() const; // times it looped
		virtual float get_playback_position() const;
		virtual void seek(float p_time);
		virtual void mix(AudioFrame *p_buffer, float p_rate_scale, int p_frames);
		virtual float get_length() const; // if supported, otherwise return 0
		AudioStreamPlaybackMyTone();
		~AudioStreamPlaybackMyTone();
	};

.. code-block:: cpp

	/* audiostreamplayer_mytone.cpp */

	#include "audiostreamplayer_mytone.h"

	#include "core/math/math_funcs.h"
	#include "core/print_string.h"

	AudioStreamPlaybackMyTone::AudioStreamPlaybackMyTone()
			: active(false) {
		AudioServer::get_singleton()->lock();
		pcm_buffer = AudioServer::get_singleton()->audio_data_alloc(PCM_BUFFER_SIZE);
		zeromem(pcm_buffer, PCM_BUFFER_SIZE);
		AudioServer::get_singleton()->unlock();
	}
	AudioStreamPlaybackMyTone::~AudioStreamPlaybackMyTone() {
		if(pcm_buffer) {
			AudioServer::get_singleton()->audio_data_free(pcm_buffer);
			pcm_buffer = NULL;
		}
	}
	void AudioStreamPlaybackMyTone::stop() {
		active = false;
		base->reset();
	}
	void AudioStreamPlaybackMyTone::start(float p_from_pos) {
		seek(p_from_pos);
		active = true;
	}
	void AudioStreamPlaybackMyTone::seek(float p_time) {
		float max = get_length();
		if (p_time < 0) {
				p_time = 0;
		}
		base->set_position(uint64_t(p_time * base->mix_rate) << MIX_FRAC_BITS);
	}
	void AudioStreamPlaybackMyTone::mix(AudioFrame *p_buffer, float p_rate, int p_frames) {
		ERR_FAIL_COND(!active);
		if (!active) {
				return;
		}
		zeromem(pcm_buffer, PCM_BUFFER_SIZE);
		int16_t *buf = (int16_t *)pcm_buffer;
		base->gen_tone(buf, p_frames);

		for(int i = 0; i < p_frames; i++) {
			float sample = float(buf[i]) / 32767.0;
			p_buffer[i] = AudioFrame(sample, sample);
		}
	}
	int AudioStreamPlaybackMyTone::get_loop_count() const {
		return 0;
	}
	float AudioStreamPlaybackMyTone::get_playback_position() const {
		return 0.0;
	}
	float AudioStreamPlaybackMyTone::get_length() const {
		return 0.0;
	}
	bool AudioStreamPlaybackMyTone::is_playing() const {
		return active;
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
