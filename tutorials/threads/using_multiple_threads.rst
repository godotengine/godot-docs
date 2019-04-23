.. _doc_using_multiple_threads:

Using Multiple Threads
======================

Threads
-------

Threads allow simultaneous execution of code. It allows off-loading work.

Godot supports threads and provides many handy functions for GDScript to use them. 

.. note:: If using other languages (C#, C++), it may be easier to use the threading classes they support.

Creating a Thread
------------------

Creating a thread is very simple, just use the following code:

.. tabs::
 .. code-tab:: gdscript GDScript

    var thread = null

    # The thread will start here
    func _ready():

        thread = Thread.new()
        thread.start(self,"_thread_function","Wafflecopter")

    # Run here and exit
    func _thread_function(userdata):

        print("I'm a thread! Userdata is: ",userdata)

    # Thread must be disposed (or "Joined"), for portability
    func _exit_tree():
        thread.wait_to_finish()


Your function will, then, run in a separate thread, then will exit. 
Even if the function exits, the thread must collect it, so call :ref:`Thread.wait_to_finish()<class_Thread_method_wait_to_finish>', which will wait until the thread is done (if not done yet), then collect it.

Mutexes
-------

Accessing objects or data from multiple threads is not always supported (if you do it, it will cause unexpected behaviors or crashes). Read the :ref:`Thread Safe APIs<doc_thread_safe_apis>` to understand which engine APIs support multiple thread access.

When processing your own data or calling your own functions, as a rule, try to avoid accessing the same data from different threads.

Even if your data supports this, you may run into synchronization problems, as the data is not allways updated between CPU cores when modified. Always use a :ref`Mutex<class_Mutex>` when accessing a piece of data from different threads.

Here is an example of using a mutex to access data:

.. tabs::
 .. code-tab:: gdscript GDScript

    var counter = 0
    var mutex = null
    var thread = null

    # The thread will start here
    func _ready():
        mutex = Mutex.new()
        thread = Thread.new()
        thread.start(self,"_thread_function","Wafflecopter")
        
        #increase value, protect it with mutex
        mutex.lock()
        counter+=1
        mutex.unlock()

    # Increment the value from the thread, too
    func _thread_function(userdata):
        mutex.lock()
        counter+=1
        mutex.unlock()

    # Thread must be disposed (or "Joined"), for portability
    func _exit_tree():
        thread.wait_to_finish()
        print("Counter is: ",counter) # Should be 2

Semaphores
-----------

Sometimes you want your thread to work *"On Demand"*. In other words, tell it when to work and let it suspend when it doesn't.
For this *:ref`Semaphores<class_Semaphore>`* are used. The function *wait()* is used in the thread to suspend it until some data arrives.

The main thread, instead, uses *post()* to signal that data is ready:

.. tabs::
 .. code-tab:: gdscript GDScript

    var counter = 0
    var mutex = null
    var semaphore = null
    var thread = null
    var exit_thread = false

    # The thread will start here
    func _ready():
        mutex = Mutex.new()
        semaphore = Semaphore.new()
        exit_thread=false

        thread = Thread.new()
        thread.start(self,"_thread_function","Wafflecopter")
        

    func _thread_function(userdata):

        while(true):
            semaphore.wait() # wait until posted

            mutex.lock()
            var should_exit = exit_thread # protect with mutex
            mutex.unlock()

            if (should_exit):
                break

            mutex.lock()
            counter+=1 # increment counter, protect with mutex
            mutex.unlock()

    func increment_counter():
        semaphore.post() # Make the thread process 

    func get_counter():
        mutex.lock()
        # copy counter, protect with mutex
        var counter_value = counter 
        mutex.unlock()
        return counter_value


    # Thread must be disposed (or "Joined"), for portability
    func _exit_tree():
        # Set exit condition to true       
        mutex.lock()
        exit_thread = true # protect with mutex
        mutex.unlock()

        # unblock by posting
        semaphore.post()

        # wait until it exits
        thread.wait_to_finish()

        # Print the counter
        print("Counter is: ",counter)



