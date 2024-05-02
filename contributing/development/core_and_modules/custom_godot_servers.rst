.. _doc_custom_godot_servers:

Custom Godot servers
====================

Introduction
------------

Godot implements multi-threading as servers. Servers are daemons which
manage data, process it, and push the result. Servers implement the
mediator pattern which interprets resource ID and process data for the
engine and other modules. In addition, the server claims ownership for
its RID allocations.

This guide assumes the reader knows how to create C++ modules and Godot
data types. If not, refer to :ref:`doc_custom_modules_in_cpp`.

References
~~~~~~~~~~~

- `Why does Godot use servers and RIDs? <https://godotengine.org/article/why-does-godot-use-servers-and-rids>`__
- `Singleton pattern <https://en.wikipedia.org/wiki/Singleton_pattern>`__
- `Mediator pattern <https://en.wikipedia.org/wiki/Mediator_pattern>`__

What for?
---------

- Adding artificial intelligence.
- Adding custom asynchronous threads.
- Adding support for a new input device.
- Adding writing threads.
- Adding a custom VoIP protocol.
- And more...

Creating a Godot server
-----------------------

At minimum, a server must have a static instance, a sleep timer, a thread loop,
an initialization state and a cleanup procedure.

.. code-block:: cpp

	#ifndef HILBERT_HOTEL_H
	#define HILBERT_HOTEL_H

	#include "core/object/object.h"
	#include "core/os/thread.h"
	#include "core/os/mutex.h"
	#include "core/templates/list.h"
	#include "core/templates/rid.h"
	#include "core/templates/set.h"
	#include "core/variant/variant.h"

	class HilbertHotel : public Object {
		GDCLASS(HilbertHotel, Object);

		static HilbertHotel *singleton;
		static void thread_func(void *p_udata);

	private:
		bool thread_exited;
		mutable bool exit_thread;
		Thread *thread;
		Mutex *mutex;

	public:
		static HilbertHotel *get_singleton();
		Error init();
		void lock();
		void unlock();
		void finish();

	protected:
		static void _bind_methods();

	private:
		uint64_t counter;
		RID_Owner<InfiniteBus> bus_owner;
		// https://github.com/godotengine/godot/blob/master/core/templates/rid.h
		Set<RID> buses;
		void _emit_occupy_room(uint64_t room, RID rid);

	public:
		RID create_bus();
		Variant get_bus_info(RID id);
		bool empty();
		bool delete_bus(RID id);
		void clear();
		void register_rooms();
		HilbertHotel();
	};

	#endif

.. code-block:: cpp

	#include "hilbert_hotel.h"

	#include "core/variant/dictionary.h"
	#include "core/os/os.h"

	#include "prime_225.h"

	void HilbertHotel::thread_func(void *p_udata) {

		HilbertHotel *ac = (HilbertHotel *) p_udata;
		uint64_t msdelay = 1000;

		while (!ac->exit_thread) {
			if (!ac->empty()) {
				ac->lock();
				ac->register_rooms();
				ac->unlock();
			}
			OS::get_singleton()->delay_usec(msdelay * 1000);
		}
	}

	Error HilbertHotel::init() {
		thread_exited = false;
		counter = 0;
		mutex = Mutex::create();
		thread = Thread::create(HilbertHotel::thread_func, this);
		return OK;
	}

	HilbertHotel *HilbertHotel::singleton = NULL;

	HilbertHotel *HilbertHotel::get_singleton() {
		return singleton;
	}

	void HilbertHotel::register_rooms() {
		for (Set<RID>::Element *e = buses.front(); e; e = e->next()) {
			auto bus = bus_owner.getornull(e->get());

			if (bus) {
				uint64_t room = bus->next_room();
				_emit_occupy_room(room, bus->get_self());
			}
		}
	}

	void HilbertHotel::unlock() {
		if (!thread || !mutex) {
			return;
		}

		mutex->unlock();
	}

	void HilbertHotel::lock() {
		if (!thread || !mutex) {
			return;
		}

		mutex->lock();
	}

	void HilbertHotel::_emit_occupy_room(uint64_t room, RID rid) {
		_HilbertHotel::get_singleton()->_occupy_room(room, rid);
	}

	Variant HilbertHotel::get_bus_info(RID id) {
		InfiniteBus *bus = bus_owner.getornull(id);

		if (bus) {
			Dictionary d;
			d["prime"] = bus->get_bus_num();
			d["current_room"] = bus->get_current_room();
			return d;
		}

		return Variant();
	}

	void HilbertHotel::finish() {
		if (!thread) {
			return;
		}

		exit_thread = true;
		Thread::wait_to_finish(thread);

		memdelete(thread);

		if (mutex) {
			memdelete(mutex);
		}

		thread = NULL;
	}

	RID HilbertHotel::create_bus() {
		lock();
		InfiniteBus *ptr = memnew(InfiniteBus(PRIME[counter++]));
		RID ret = bus_owner.make_rid(ptr);
		ptr->set_self(ret);
		buses.insert(ret);
		unlock();

		return ret;
	}

	// https://github.com/godotengine/godot/blob/master/core/templates/rid.h
	bool HilbertHotel::delete_bus(RID id) {
		if (bus_owner.owns(id)) {
			lock();
			InfiniteBus *b = bus_owner.get(id);
			bus_owner.free(id);
			buses.erase(id);
			memdelete(b);
			unlock();
			return true;
		}

		return false;
	}

	void HilbertHotel::clear() {
		for (Set<RID>::Element *e = buses.front(); e; e = e->next()) {
			delete_bus(e->get());
		}
	}

	bool HilbertHotel::empty() {
		return buses.size() <= 0;
	}

	void HilbertHotel::_bind_methods() {
	}

	HilbertHotel::HilbertHotel() {
		singleton = this;
	}

.. code-block:: cpp

	/* prime_225.h */

	const uint64_t PRIME[225] = {
			2,3,5,7,11,13,17,19,23,
			29,31,37,41,43,47,53,59,61,
			67,71,73,79,83,89,97,101,103,
			107,109,113,127,131,137,139,149,151,
			157,163,167,173,179,181,191,193,197,
			199,211,223,227,229,233,239,241,251,
			257,263,269,271,277,281,283,293,307,
			311,313,317,331,337,347,349,353,359,
			367,373,379,383,389,397,401,409,419,
			421,431,433,439,443,449,457,461,463,
			467,479,487,491,499,503,509,521,523,
			541,547,557,563,569,571,577,587,593,
			599,601,607,613,617,619,631,641,643,
			647,653,659,661,673,677,683,691,701,
			709,719,727,733,739,743,751,757,761,
			769,773,787,797,809,811,821,823,827,
			829,839,853,857,859,863,877,881,883,
			887,907,911,919,929,937,941,947,953,
			967,971,977,983,991,997,1009,1013,1019,
			1021,1031,1033,1039,1049,1051,1061,1063,1069,
			1087,1091,1093,1097,1103,1109,1117,1123,1129,
			1151,1153,1163,1171,1181,1187,1193,1201,1213,
			1217,1223,1229,1231,1237,1249,1259,1277,1279,
			1283,1289,1291,1297,1301,1303,1307,1319,1321,
			1327,1361,1367,1373,1381,1399,1409,1423,1427
	};

Custom managed resource data
----------------------------

Godot servers implement a mediator pattern. All data types inherit ``RID_Data``.
``RID_Owner<MyRID_Data>`` owns the object when ``make_rid`` is called. During debug mode only,
RID_Owner maintains a list of RIDs. In practice, RIDs are similar to writing
object-oriented C code.

.. code-block:: cpp

	class InfiniteBus : public RID_Data {
		RID self;

	private:
		uint64_t prime_num;
		uint64_t num;

	public:
		uint64_t next_room() {
			return prime_num * num++;
		}

		uint64_t get_bus_num() const {
			return prime_num;
		}

		uint64_t get_current_room() const {
			return prime_num * num;
		}

		_FORCE_INLINE_ void set_self(const RID &p_self) {
			self = p_self;
		}

		_FORCE_INLINE_ RID get_self() const {
			return self;
		}

		InfiniteBus(uint64_t prime) : prime_num(prime), num(1) {};
		~InfiniteBus() {};
	}

References
~~~~~~~~~~~

- :ref:`RID<class_rid>`
- `core/templates/rid.h <https://github.com/godotengine/godot/blob/master/core/templates/rid.h>`__

Registering the class in GDScript
---------------------------------

Servers are allocated in ``register_types.cpp``. The constructor sets the static
instance and ``init()`` creates the managed thread; ``unregister_types.cpp``
cleans up the server.

Since a Godot server class creates an instance and binds it to a static singleton,
binding the class might not reference the correct instance. Therefore, a dummy
class must be created to reference the proper Godot server.

In ``register_server_types()``, ``Engine::get_singleton()->add_singleton``
is used to register the dummy class in GDScript.

.. code-block:: cpp

	/* register_types.cpp */

	#include "register_types.h"

	#include "core/object/class_db.h"
	#include "core/config/engine.h"

	#include "hilbert_hotel.h"

	static HilbertHotel *hilbert_hotel = NULL;
	static _HilbertHotel *_hilbert_hotel = NULL;

	void register_hilbert_hotel_types() {
		hilbert_hotel = memnew(HilbertHotel);
		hilbert_hotel->init();
		_hilbert_hotel = memnew(_HilbertHotel);
		ClassDB::register_class<_HilbertHotel>();
		Engine::get_singleton()->add_singleton(Engine::Singleton("HilbertHotel", _HilbertHotel::get_singleton()));
	}

	void unregister_hilbert_hotel_types() {
		if (hilbert_hotel) {
			hilbert_hotel->finish();
			memdelete(hilbert_hotel);
		}

		if (_hilbert_hotel) {
			memdelete(_hilbert_hotel);
		}
	}

.. code-block:: cpp

	/* register_types.h */

	/* Yes, the word in the middle must be the same as the module folder name */
	void register_hilbert_hotel_types();
	void unregister_hilbert_hotel_types();

- `servers/register_server_types.cpp <https://github.com/godotengine/godot/blob/master/servers/register_server_types.cpp>`__

Bind methods
~~~~~~~~~~~~

The dummy class binds singleton methods to GDScript. In most cases, the dummy class methods wraps around.

.. code-block:: cpp

	Variant _HilbertHotel::get_bus_info(RID id) {
		return HilbertHotel::get_singleton()->get_bus_info(id);
	}

Binding Signals

It is possible to emit signals to GDScript by calling the GDScript dummy object.

.. code-block:: cpp

	void HilbertHotel::_emit_occupy_room(uint64_t room, RID rid) {
		_HilbertHotel::get_singleton()->_occupy_room(room, rid);
	}

.. code-block:: cpp

	class _HilbertHotel : public Object {
		GDCLASS(_HilbertHotel, Object);

		friend class HilbertHotel;
		static _HilbertHotel *singleton;

	protected:
		static void _bind_methods();

	private:
		void _occupy_room(int room_number, RID bus);

	public:
		RID create_bus();
		void connect_signals();
		bool delete_bus(RID id);
		static _HilbertHotel *get_singleton();
		Variant get_bus_info(RID id);

		_HilbertHotel();
		~_HilbertHotel();
	};

	#endif

.. code-block:: cpp

	_HilbertHotel *_HilbertHotel::singleton = NULL;
	_HilbertHotel *_HilbertHotel::get_singleton() { return singleton; }

	RID _HilbertHotel::create_bus() {
		return HilbertHotel::get_singleton()->create_bus();
	}

	bool _HilbertHotel::delete_bus(RID rid) {
		return HilbertHotel::get_singleton()->delete_bus(rid);
	}

	void _HilbertHotel::_occupy_room(int room_number, RID bus) {
		emit_signal("occupy_room", room_number, bus);
	}

	Variant _HilbertHotel::get_bus_info(RID id) {
		return HilbertHotel::get_singleton()->get_bus_info(id);
	}

	void _HilbertHotel::_bind_methods() {
		ClassDB::bind_method(D_METHOD("get_bus_info", "r_id"), &_HilbertHotel::get_bus_info);
		ClassDB::bind_method(D_METHOD("create_bus"), &_HilbertHotel::create_bus);
		ClassDB::bind_method(D_METHOD("delete_bus"), &_HilbertHotel::delete_bus);
		ADD_SIGNAL(MethodInfo("occupy_room", PropertyInfo(Variant::INT, "room_number"), PropertyInfo(Variant::_RID, "r_id")));
	}

	void _HilbertHotel::connect_signals() {
		HilbertHotel::get_singleton()->connect("occupy_room", _HilbertHotel::get_singleton(), "_occupy_room");
	}

	_HilbertHotel::_HilbertHotel() {
		singleton = this;
	}

	_HilbertHotel::~_HilbertHotel() {
	}

MessageQueue
------------

In order to send commands into SceneTree, MessageQueue is a thread-safe buffer
to queue set and call methods for other threads. To queue a command, obtain
the target object RID and use either ``push_call``, ``push_set``, or ``push_notification``
to execute the desired behavior. The queue will be flushed whenever either
``SceneTree::idle`` or ``SceneTree::iteration`` is executed.

References:
~~~~~~~~~~~

- `core/object/message_queue.cpp <https://github.com/godotengine/godot/blob/master/core/object/message_queue.cpp>`__

Summing it up
-------------

Here is the GDScript sample code:

::

    extends Node

    func _ready():
        print("Start debugging")
        HilbertHotel.connect("occupy_room", self, "_print_occupy_room")
        var rid = HilbertHotel.create_bus()
        OS.delay_msec(2000)
        HilbertHotel.create_bus()
        OS.delay_msec(2000)
        HilbertHotel.create_bus()
        OS.delay_msec(2000)
        print(HilbertHotel.get_bus_info(rid))
        HilbertHotel.delete_bus(rid)
        print("Ready done")

    func _print_occupy_room(room_number, r_id):
        print("Room number: "  + str(room_number) + ", RID: " + str(r_id))
        print(HilbertHotel.get_bus_info(r_id))

Notes
~~~~~

- The actual `Hilbert Hotel <https://en.wikipedia.org/wiki/Hilbert%27s_paradox_of_the_Grand_Hotel>`__ is impossible.
- Connecting signal example code is pretty hacky.
