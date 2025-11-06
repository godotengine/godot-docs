.. _doc_object_class:

Object class
============

.. seealso::

    This page describes the C++ implementation of objects in Godot.
    Looking for the Object class reference? :ref:`Have a look here. <class_Object>`

General definition
------------------

:ref:`Object <class_object>` is the base class for almost everything. Most classes in Godot
inherit directly or indirectly from it. Declaring them is a matter of using a single
macro like this:

.. code-block:: cpp

    class CustomObject : public Object {
        GDCLASS(CustomObject, Object); // This is required to inherit from Object.
    };

Objects come with a lot of built-in functionality, like reflection and editable properties:

.. code-block:: cpp

    CustomObject *obj = memnew(CustomObject);
    print_line("Object class: ", obj->get_class()); // print object class

    OtherClass *obj2 = Object::cast_to<OtherClass>(obj); // Converting between classes, similar to dynamic_cast

References:
~~~~~~~~~~~

-  `core/object/object.h <https://github.com/godotengine/godot/blob/master/core/object/object.h>`__

Registering Object classes
--------------------------

Most ``Object`` subclasses are registered by calling ``GDREGISTER_CLASS``.

.. code-block:: cpp

    GDREGISTER_CLASS(MyCustomClass)

This will register it as a named, public class in the ``ClassDB``, which will allow the class to be instantiated by
scripts, code, or by deserialization. Note that classes registered as ``GDREGISTER_CLASS`` should expect to be
instantiated or freed automatically, for example by the editor or the documentation system.

Besides ``GDREGISTER_CLASS``, there are a few other modes of privateness:

.. code-block:: cpp

    // Registers the class publicly, but prevents automatic instantiation through ClassDB.
    GDREGISTER_VIRTUAL_CLASS(MyCustomClass);

    // Registers the class publicly, but prevents all instantiation through ClassDB.
    GDREGISTER_ABSTRACT_CLASS(MyCustomClass);

    // Registers the class in ClassDB, but marks it as private,
    // such that it is not visible to scripts or extensions.
    // This is the same as not registering the class explicitly at all
    // - in this case, the class is registered as internal automatically
    // when it is first constructed.
    GDREGISTER_INTERNAL_CLASS(MyCustomClass);

    // Registers the class such that it is only available at runtime (but not in the editor).
    GDREGISTER_RUNTIME_CLASS(MyCustomClass);

It is also possible to use ``GDSOFTCLASS(MyCustomClass, SuperClass)`` instead of ``GDCLASS(MyCustomClass, SuperClass)``.
Classes defined this way are not registered in the ``ClassDB`` at all. This is sometimes used for platform-specific
subclasses.

Registering bindings
~~~~~~~~~~~~~~~~~~~~

Object-derived classes can override the static function
``static void _bind_methods()``. When the class is registered, this
static function is called to register all the object methods,
properties, constants, etc. It's only called once.

Inside ``_bind_methods``, there are a couple of things that can be done.
Registering functions is one:

.. code-block:: cpp

    ClassDB::bind_method(D_METHOD("methodname", "arg1name", "arg2name", "arg3name"), &MyCustomType::method);

Default values for arguments can be passed as parameters at the end:

.. code-block:: cpp

    ClassDB::bind_method(D_METHOD("methodname", "arg1name", "arg2name", "arg3name"), &MyCustomType::method, DEFVAL(-1), DEFVAL(-2)); // Default values for arg2name (-1) and arg3name (-2).

Default values must be provided in the same order as they are declared,
skipping required arguments and then providing default values for the optional ones.
This matches the syntax for declaring methods in C++.

``D_METHOD`` is a macro that converts "methodname" to a StringName for more
efficiency. Argument names are used for introspection, but when
compiling on release, the macro ignores them, so the strings are unused
and optimized away.

Check ``_bind_methods`` of Control or Object for more examples.

If just adding modules and functionality that is not expected to be
documented as thoroughly, the ``D_METHOD()`` macro can safely be ignored and a
string passing the name can be passed for brevity.

References:
^^^^^^^^^^^

-  `core/object/class_db.h <https://github.com/godotengine/godot/blob/master/core/object/class_db.h>`__

Constants
~~~~~~~~~

Classes often have enums such as:

.. code-block:: cpp

    enum SomeMode {
       MODE_FIRST,
       MODE_SECOND
    };

For these to work when binding to methods, the enum must be declared
convertible to int. A macro is provided to help with this:

.. code-block:: cpp

    VARIANT_ENUM_CAST(MyClass::SomeMode); // now functions that take SomeMode can be bound.

The constants can also be bound inside ``_bind_methods``, by using:

.. code-block:: cpp

    BIND_CONSTANT(MODE_FIRST);
    BIND_CONSTANT(MODE_SECOND);

Properties (set/get)
~~~~~~~~~~~~~~~~~~~~

Objects export properties, properties are useful for the following:

-  Serializing and deserializing the object.
-  Creating a list of editable values for the Object derived class.

Properties are usually defined by the PropertyInfo() class and
constructed as:

.. code-block:: cpp

    PropertyInfo(type, name, hint, hint_string, usage_flags)

For example:

.. code-block:: cpp

    PropertyInfo(Variant::INT, "amount", PROPERTY_HINT_RANGE, "0,49,1", PROPERTY_USAGE_EDITOR)

This is an integer property named "amount". The hint is a range, and the range
goes from 0 to 49 in steps of 1 (integers). It is only usable for the editor
(editing the value visually) but won't be serialized.

Another example:

.. code-block:: cpp

    PropertyInfo(Variant::STRING, "modes", PROPERTY_HINT_ENUM, "Enabled,Disabled,Turbo")

This is a string property, can take any string but the editor will only
allow the defined hint ones. Since no usage flags were specified, the
default ones are PROPERTY_USAGE_STORAGE and PROPERTY_USAGE_EDITOR.

There are plenty of hints and usage flags available in object.h, give them a
check.

Properties can also work like C# properties and be accessed from script
using indexing, but this usage is generally discouraged, as using
functions is preferred for legibility. Many properties are also bound
with categories, such as "animation/frame" which also make indexing
impossible unless using operator [].

From ``_bind_methods()``, properties can be created and bound as long as
set/get functions exist. Example:

.. code-block:: cpp

    ADD_PROPERTY(PropertyInfo(Variant::INT, "amount"), "set_amount", "get_amount")

This creates the property using the setter and the getter.

.. _doc_binding_properties_using_set_get_property_list:

Binding properties using ``_set``/``_get``/``_get_property_list``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An additional method of creating properties exists when more flexibility
is desired (i.e. adding or removing properties on context).

The following functions can be overridden in an Object derived class,
they are NOT virtual, DO NOT make them virtual, they are called for
every override and the previous ones are not invalidated (multilevel
call).

.. code-block:: cpp

    protected:
         void _get_property_list(List<PropertyInfo> *r_props) const;      // return list of properties
         bool _get(const StringName &p_property, Variant &r_value) const; // return true if property was found
         bool _set(const StringName &p_property, const Variant &p_value); // return true if property was found

This is also a little less efficient since ``p_property`` must be
compared against the desired names in serial order.


Signals
~~~~~~~

Objects can have a set of signals defined (similar to Delegates in other
languages). This example shows how to connect to them:

.. code-block:: cpp

    // This is the function signature:
    //
    // Error connect(const StringName &p_signal, const Callable &p_callable, uint32_t p_flags = 0)
    //
    // For example:
    obj->connect("signal_name_here", callable_mp(this, &MyCustomType::method), CONNECT_DEFERRED);

``callable_mp`` is a macro to create a custom callable function pointer to member functions.
For the values of ``p_flags``, see :ref:`ConnectFlags <enum_Object_ConnectFlags>`.

Adding signals to a class is done in ``_bind_methods``, using the
``ADD_SIGNAL`` macro, for example:

.. code-block:: cpp

    ADD_SIGNAL(MethodInfo("been_killed"))

Object ownership and casting
----------------------------

Objects are allocated on the heap. There are two different ownership models:

- Objects derived from ``RefCounted`` are reference counted.
- All other objects are manually memory managed.

The ownership models are fundamentally different. Refer to the section for each respectively to learn how to
create, store, and free the object.

When you do not know whether an object passed to you (via ``Object *``) is ``RefCounted``, and you need to store it,
you should store its ``ObjectID`` rather than a pointer (as explained below, in the manual memory management section).

When an object is passed to you via :ref:`Variant<class_Variant>`, especially when using deferred callbacks, it is
possible that the contained ``Object *`` was already freed by the time your function runs.
Instead of converting directly to ``Object *``, you should use ``get_validated_object``:

.. code-block:: cpp

    void do_something(Variant p_variant) {
        Object *object = p_variant.get_validated_object();
        ERR_FAIL_NULL(object);
    }

Manual memory management
~~~~~~~~~~~~~~~~~~~~~~~~

Manually memory managed objects are created using ``memnew`` and freed using ``memdelete``:

.. code-block:: cpp

    Node *node = memnew(Node);
    // ...
    memdelete(node);
    node = nullptr;

When you are not the sole owner of an object, storing a pointer to it is dangerous: The object may at any point be
freed through other references to it, causing your pointer to become a dangling pointer, which will eventually result in
a crash.

When storing objects you are not the only owner of, you should store its ``ObjectID`` rather than a pointer:

.. code-block:: cpp

    Node *node = memnew(Node);
    ObjectID node_id = node.get_instance_id();
    // ...
    Object *maybe_node = ObjectDB::get_instance(node_id);
    ERR_FAIL_NULL(maybe_node); // The node may have been freed between calls.

``RefCounted`` memory management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`RefCounted <class_RefCounted>` subclasses are memory managed with
`reference counting semantics <https://en.wikipedia.org/wiki/Reference_counting>`__.

They are constructed using ``memnew``, and should be stored in ``Ref`` instances. When the last ``Ref`` instance is
dropped, the object automatically self-destructs.

.. code-block:: cpp

    class MyRefCounted: public RefCounted {
        GDCLASS(MyReference, RefCounted);
    };

    Ref<MyRefCounted> my_ref = memnew(MyRefCounted);
    // ...
    // Ref holds shared ownership over the object, so the object
    // will not be freed. As long as you have a valid, non-null
    // Ref, it can be safely assumed the object is still valid.
    my_ref->get_class_name();

You should never call ``memdelete`` for ``RefCounted`` subclasses, because there may be other owners of it.

You should also never store ``RefCounted`` subclasses using raw pointers, for example
``RefCounted *object = memnew(RefCounted)``. This is unsafe because other owners may destruct the object, leaving you
with a dangling pointer, which will eventually result in a crash.

References:
^^^^^^^^^^^

-  `core/object/ref_counted.h <https://github.com/godotengine/godot/blob/master/core/object/ref_counted.h>`__

Dynamic casting
~~~~~~~~~~~~~~~

Godot provides dynamic casting between Object-derived classes, for example:

.. code-block:: cpp

    void some_func(Object *p_object) {
         Button *button = Object::cast_to<Button>(p_object);
    }

If the cast fails, ``nullptr`` is returned. This works the same as ``dynamic_cast``, but does not use
`C++ RTTI <https://en.wikipedia.org/wiki/Run-time_type_information>`__.

Notifications
-------------

All objects in Godot have a :ref:`_notification <class_Object_private_method__notification>`
method that allows them to respond to engine-level callbacks that may relate to it.
More information can be found on the :ref:`doc_godot_notifications` page.


Resources
----------

:ref:`Resource <class_resource>` inherits from RefCounted, so all resources
are reference counted. Resources can optionally contain a path, which
reference a file on disk. This can be set with ``resource.set_path(path)``,
though this is normally done by the resource loader. No two different
resources can have the same path; attempting to do so will result in an error.

Resources without a path are fine too.

References:
~~~~~~~~~~~

-  `core/io/resource.h <https://github.com/godotengine/godot/blob/master/core/io/resource.h>`__

Resource loading
~~~~~~~~~~~~~~~~

Resources can be loaded with the ResourceLoader API, like this:

.. code-block:: cpp

    Ref<Resource> res = ResourceLoader::load("res://someresource.res")

If a reference to that resource has been loaded previously and is in
memory, the resource loader will return that reference. This means that
there can be only one resource loaded from a file referenced on disk at
the same time.

-  resourceinteractiveloader (TODO)

References:
^^^^^^^^^^^

-  `core/io/resource_loader.h <https://github.com/godotengine/godot/blob/master/core/io/resource_loader.h>`__

Resource saving
~~~~~~~~~~~~~~~

Saving a resource can be done with the resource saver API:

.. code-block:: cpp

    ResourceSaver::save("res://someresource.res", instance)

The instance will be saved, and sub resources that have a path to a file will
be saved as a reference to that resource. Sub resources without a path will
be bundled with the saved resource and assigned sub-IDs, like
``res://someresource.res::1``. This also helps to cache them when loaded.

References:
^^^^^^^^^^^

-  `core/io/resource_saver.h <https://github.com/godotengine/godot/blob/master/core/io/resource_saver.h>`__
