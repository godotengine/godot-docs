.. _doc_using_multiple_threads:

Using multiple threads
======================

Threads
-------

Threads allow simultaneous execution of code. It allows off-loading work
from the main thread.

Godot supports threads and provides many handy functions to use them.

.. note:: If using other languages (C#, C++), it may be easier to use the
          threading classes they support.

.. warning::

    Before using a built-in class in a thread, read :ref:`doc_thread_safe_apis`
    first to check whether it can be safely used in a thread.

Creating a Thread
-----------------

To create a thread, use the following code:

.. tabs::
 .. code-tab:: gdscript GDScript

    var thread: Thread

    # The thread will start here.
    func _ready():
        thread = Thread.new()
        # You can bind multiple arguments to a function Callable.
        thread.start(_thread_function.bind("Wafflecopter"))


    # Run here and exit.
    # The argument is the bound data passed from start().
    func _thread_function(userdata):
        # Print the userdata ("Wafflecopter")
        print("I'm a thread! Userdata is: ", userdata)


    # Thread must be disposed (or "joined"), for portability.
    func _exit_tree():
        thread.wait_to_finish()

 .. code-tab:: cpp C++ .H File

    #pragma once

    #include <godot_cpp/classes/node.hpp>
    #include <godot_cpp/classes/thread.hpp>

    namespace godot {
        class MultithreadingDemo : public Node {
            GDCLASS(MultithreadingDemo, Node);

        private:
            Ref<Thread> worker;

        protected:
            static void _bind_methods();
            void _notification(int p_what);

        public:
            MultithreadingDemo();
            ~MultithreadingDemo();

            void demo_threaded_function();
        };
    } // namespace godot

 .. code-tab:: cpp C++ .CPP File

    #include "multithreading_demo.h"

    #include <godot_cpp/classes/engine.hpp>
    #include <godot_cpp/classes/os.hpp>
    #include <godot_cpp/classes/time.hpp>
    #include <godot_cpp/core/class_db.hpp>
    #include <godot_cpp/variant/utility_functions.hpp>

    using namespace godot;

    void MultithreadingDemo::_bind_methods() {
        ClassDB::bind_method(D_METHOD("threaded_function"), &MultithreadingDemo::demo_threaded_function);
    }

    void MultithreadingDemo::_notification(int p_what) {
        // Prevents this from running in the editor, only during game mode. In Godot 4.3+ use Runtime classes.
        if (Engine::get_singleton()->is_editor_hint()) {
            return;
        }

        switch (p_what) {
            case NOTIFICATION_READY: {
                worker.instantiate();
                worker->start(callable_mp(this, &MultithreadingDemo::demo_threaded_function), Thread::PRIORITY_NORMAL);
            } break;
            case NOTIFICATION_EXIT_TREE: { // Thread must be disposed (or "joined"), for portability.
                // Wait until it exits.
                if (worker.is_valid()) {
                    worker->wait_to_finish();
                }

                worker.unref();
            } break;
        }
    }

    MultithreadingDemo::MultithreadingDemo() {
        // Initialize any variables here.
    }

    MultithreadingDemo::~MultithreadingDemo() {
        // Add your cleanup here.
    }

    void MultithreadingDemo::demo_threaded_function() {
        UtilityFunctions::print("demo_threaded_function started!");
        int i = 0;
        uint64_t start = Time::get_singleton()->get_ticks_msec();
        while (Time::get_singleton()->get_ticks_msec() - start < 5000) {
            OS::get_singleton()->delay_msec(10);
            i++;
        }

        UtilityFunctions::print("demo_threaded_function counted to: ", i, ".");
    }

Your function will, then, run in a separate thread until it returns.
Even if the function has returned already, the thread must collect it, so call
:ref:`Thread.wait_to_finish()<class_Thread_method_wait_to_finish>`, which will
wait until the thread is done (if not done yet), then properly dispose of it.

.. warning::

    Creating threads is a slow operation, especially on Windows. To avoid
    unnecessary performance overhead, make sure to create threads before heavy
    processing is needed instead of creating threads just-in-time.

    For example, if you need multiple threads during gameplay, you can create
    threads while the level is loading and only actually start processing with
    them later on.

    Additionally, locking and unlocking of mutexes can also be an expensive
    operation. Locking should be done carefully; avoid locking too often (or for
    too long).

Mutexes
-------

Accessing objects or data from multiple threads is not always supported (if you
do it, it will cause unexpected behaviors or crashes). Read the
:ref:`doc_thread_safe_apis` documentation to understand which engine APIs
support multiple thread access.

When processing your own data or calling your own functions, as a rule, try to
avoid accessing the same data directly from different threads. You may run into
synchronization problems, as the data is not always updated between CPU cores
when modified. Always use a :ref:`Mutex<class_Mutex>` when accessing
a piece of data from different threads.

When calling :ref:`Mutex.lock()<class_Mutex_method_lock>`, a thread ensures that
all other threads will be blocked (put on suspended state) if they try to *lock*
the same mutex. When the mutex is unlocked by calling
:ref:`Mutex.unlock()<class_Mutex_method_unlock>`, the other threads will be
allowed to proceed with the lock (but only one at a time).

Here is an example of using a Mutex:

.. tabs::
 .. code-tab:: gdscript GDScript

    var counter := 0
    var mutex: Mutex
    var thread: Thread


    # The thread will start here.
    func _ready():
        mutex = Mutex.new()
        thread = Thread.new()
        thread.start(_thread_function)

        # Increase value, protect it with Mutex.
        mutex.lock()
        counter += 1
        mutex.unlock()


    # Increment the value from the thread, too.
    func _thread_function():
        mutex.lock()
        counter += 1
        mutex.unlock()


    # Thread must be disposed (or "joined"), for portability.
    func _exit_tree():
        thread.wait_to_finish()
        print("Counter is: ", counter) # Should be 2.

 .. code-tab:: cpp C++ .H File

    #pragma once

    #include <godot_cpp/classes/mutex.hpp>
    #include <godot_cpp/classes/node.hpp>
    #include <godot_cpp/classes/thread.hpp>

    namespace godot {
        class MutexDemo : public Node {
            GDCLASS(MutexDemo, Node);

        private:
            int counter = 0;
            Ref<Mutex> mutex;
            Ref<Thread> thread;

        protected:
            static void _bind_methods();
            void _notification(int p_what);

        public:
            MutexDemo();
            ~MutexDemo();

            void thread_function();
        };
    } // namespace godot

 .. code-tab:: cpp C++ .CPP File

    #include "mutex_demo.h"

    #include <godot_cpp/classes/engine.hpp>
    #include <godot_cpp/classes/time.hpp>
    #include <godot_cpp/core/class_db.hpp>
    #include <godot_cpp/variant/utility_functions.hpp>

    using namespace godot;

    void MutexDemo::_bind_methods() {
        ClassDB::bind_method(D_METHOD("thread_function"), &MutexDemo::thread_function);
    }

    void MutexDemo::_notification(int p_what) {
        // Prevents this from running in the editor, only during game mode.
        if (Engine::get_singleton()->is_editor_hint()) {
            return;
        }

        switch (p_what) {
            case NOTIFICATION_READY: {
                UtilityFunctions::print("Mutex Demo Counter is starting at: ", counter);
                mutex.instantiate();
                thread.instantiate();
                thread->start(callable_mp(this, &MutexDemo::thread_function), Thread::PRIORITY_NORMAL);

                // Increase value, protect it with Mutex.
                mutex->lock();
                counter += 1;
                UtilityFunctions::print("Mutex Demo Counter is ", counter, " after adding with Mutex protection.");
                mutex->unlock();
            } break;
            case NOTIFICATION_EXIT_TREE: { // Thread must be disposed (or "joined"), for portability.
                // Wait until it exits.
                if (thread.is_valid()) {
                    thread->wait_to_finish();
                }
                thread.unref();

                UtilityFunctions::print("Mutex Demo Counter is ", counter, " at EXIT_TREE."); // Should be 2.
            } break;
        }
    }

    MutexDemo::MutexDemo() {
        // Initialize any variables here.
    }

    MutexDemo::~MutexDemo() {
        // Add your cleanup here.
    }

    // Increment the value from the thread, too.
    void MutexDemo::thread_function() {
        mutex->lock();
        counter += 1;
        mutex->unlock();
    }

Semaphores
----------

Sometimes you want your thread to work *"on demand"*. In other words, tell it
when to work and let it suspend when it isn't doing anything.
For this, :ref:`Semaphores<class_Semaphore>` are used. The function
:ref:`Semaphore.wait()<class_Semaphore_method_wait>` is used in the thread to
suspend it until some data arrives.

The main thread, instead, uses
:ref:`Semaphore.post()<class_Semaphore_method_post>` to signal that data is
ready to be processed:

.. tabs::
 .. code-tab:: gdscript GDScript

    var counter := 0
    var mutex: Mutex
    var semaphore: Semaphore
    var thread: Thread
    var exit_thread := false


    # The thread will start here.
    func _ready():
        mutex = Mutex.new()
        semaphore = Semaphore.new()
        exit_thread = false

        thread = Thread.new()
        thread.start(_thread_function)


    func _thread_function():
        while true:
            semaphore.wait() # Wait until posted.

            mutex.lock()
            var should_exit = exit_thread # Protect with Mutex.
            mutex.unlock()

            if should_exit:
                break

            mutex.lock()
            counter += 1 # Increment counter, protect with Mutex.
            mutex.unlock()


    func increment_counter():
        semaphore.post() # Make the thread process.


    func get_counter():
        mutex.lock()
        # Copy counter, protect with Mutex.
        var counter_value = counter
        mutex.unlock()
        return counter_value


    # Thread must be disposed (or "joined"), for portability.
    func _exit_tree():
        # Set exit condition to true.
        mutex.lock()
        exit_thread = true # Protect with Mutex.
        mutex.unlock()

        # Unblock by posting.
        semaphore.post()

        # Wait until it exits.
        thread.wait_to_finish()

        # Print the counter.
        print("Counter is: ", counter)

 .. code-tab:: cpp C++ .H File

    #pragma once

    #include <godot_cpp/classes/mutex.hpp>
    #include <godot_cpp/classes/node.hpp>
    #include <godot_cpp/classes/semaphore.hpp>
    #include <godot_cpp/classes/thread.hpp>

    namespace godot {
        class SemaphoreDemo : public Node {
            GDCLASS(SemaphoreDemo, Node);

        private:
            int counter = 0;
            Ref<Mutex> mutex;
            Ref<Semaphore> semaphore;
            Ref<Thread> thread;
            bool exit_thread = false;

        protected:
            static void _bind_methods();
            void _notification(int p_what);

        public:
            SemaphoreDemo();
            ~SemaphoreDemo();

            void thread_function();
            void increment_counter();
            int get_counter();
        };
    } // namespace godot

 .. code-tab:: cpp C++ .CPP File

    #include "semaphore_demo.h"

    #include <godot_cpp/classes/engine.hpp>
    #include <godot_cpp/classes/time.hpp>
    #include <godot_cpp/core/class_db.hpp>
    #include <godot_cpp/variant/utility_functions.hpp>

    using namespace godot;

    void SemaphoreDemo::_bind_methods() {
        ClassDB::bind_method(D_METHOD("thread_function"), &SemaphoreDemo::thread_function);
    }

    void SemaphoreDemo::_notification(int p_what) {
        // Prevents this from running in the editor, only during game mode.
        if (Engine::get_singleton()->is_editor_hint()) {
            return;
        }

        switch (p_what) {
            case NOTIFICATION_READY: {
                UtilityFunctions::print("Semaphore Demo Counter is starting at: ", counter);
                mutex.instantiate();
                semaphore.instantiate();
                exit_thread = false;

                thread.instantiate();
                thread->start(callable_mp(this, &SemaphoreDemo::thread_function), Thread::PRIORITY_NORMAL);

                increment_counter(); // Call increment counter to test.
            } break;
            case NOTIFICATION_EXIT_TREE: { // Thread must be disposed (or "joined"), for portability.
                // Set exit condition to true.
                mutex->lock();
                exit_thread = true; // Protect with Mutex.
                mutex->unlock();

                // Unblock by posting.
                semaphore->post();

                // Wait until it exits.
                if (thread.is_valid()) {
                    thread->wait_to_finish();
                }
                thread.unref();

                // Print the counter.
                UtilityFunctions::print("Semaphore Demo Counter is ", get_counter(),  " at EXIT_TREE.");
            } break;
        }
    }

    SemaphoreDemo::SemaphoreDemo() {
        // Initialize any variables here.
    }

    SemaphoreDemo::~SemaphoreDemo() {
        // Add your cleanup here.
    }

    // Increment the value from the thread, too.
    void SemaphoreDemo::thread_function() {
        while (true) {
            semaphore->wait(); // Wait until posted.

            mutex->lock();
            bool should_exit = exit_thread; // Protect with Mutex.
            mutex->unlock();

            if (should_exit) {
                break;
            }

            mutex->lock();
            counter += 1; // Increment counter, protect with Mutex.
            mutex->unlock();
        }
    }

    void SemaphoreDemo::increment_counter() {
        semaphore->post(); // Make the thread process.
    }

    int SemaphoreDemo::get_counter() {
        mutex->lock();
        // Copy counter, protect with Mutex.
        int counter_value = counter;
        mutex->unlock();
        return counter_value;
    }
