Object class
============

Object is the base class for almost everything. Most classes in Godot
inherit directly or indirectly from it. Objects provide reflection and
editable properties, and declaring them is a matter of using a single
macro like this.

| <pre class=\\"cpp\\">
| class CustomObject : public Object {

| OBJ\_TYPE(CustomObject,Object); // this required to inherit
| };

.. raw:: html

   </pre>

This makes objects gain a lot of functionality, like for example

| <pre class=\\"cpp\\">
| obj = memnew(CustomObject);
| print\_line("Object Type: ",obj->get\_type()); //print object type

obj2 = obj->cast\_to&lt;OtherType&gt;(); // converting between types,
this also works without RTTI enabled.

.. raw:: html

   </pre>

References:
~~~~~~~~~~~

-  \\\ `core/object.h\\ <https://github.com/okamstudio/godot/blob/master/core/object.h>`__

Registering an Object
---------------------

ObjectTypeDB is a static class that hold the entire list of registered
classes that inherit from object, as well as dynamic bindings to all
their methods properties and integer constants.

Classes are registered by calling:

<pre class=\\"cpp\\">ObjectTypeDB::register\_type()

.. raw:: html

   </pre>

Registering it will allow the type to be instanced by scripts, code, or
creating them again when deserializing.

Registering as virtual is the same but it can't be instanced.

<pre class=\\"cpp\\">ObjectTypeDB::register\_virtual\_type()

.. raw:: html

   </pre>

Object derived classes can override a static function
``static void _bind_methods()``, when one class is registered, this
static function is called to register all the object methods,
properties, constants, etc. It's only called once. If an Object derived
class is instanced but has not been registered, it will be registered as
virtual automatically.

Inside ``_bind_methods``, there are a couple of things that can be done.
Registering functions is one:

<pre
class=\\"cpp\\">ObjectTypeDB::register\_method(\_MD (\\"methodname\\",\\"arg1name\\",\\"arg2name\\"),&MyCustethod);

.. raw:: html

   </pre>

Default values for arguments can be passed in reverse order:

<pre
class=\\"cpp\\">ObjectTypeDB::register\_method(\_MD (\\"methodname\\",\\"arg1name\\",\\"arg2name\\"),&MyCustomType::method,DEFVAL (-1));
//default argument for arg2name

.. raw:: html

   </pre>

``_MD`` is a macro that convers \\"methodname\\" to a stringname for
more efficiency. Argument names are used for instrospection, but when
compiling on release, the macro ignores them, so the strings are unused
and optimized away.

Check ``_bind_methods`` of Control or Object for more examples.

If just adding modules and functionality that is not expected to be
documented as throughly, the ``_MD()`` macro can safely be ignore and a
string passing the name can be passed for brevity.

References:
~~~~~~~~~~~

-  \\\ `core/object\_type\_db.h\\ <https://github.com/okamstudio/godot/blob/master/core/object_type_db.h>`__

Constants
---------

Classes often have enums such as:

| <pre class=\\"cpp\\">
| enum SomeMode {
| MODE\_FIRST,
| MODE\_SECOND
| };

.. raw:: html

   </pre>

For these to work when binding to methods, the enum must be declared
convertible to int, for this a macro is provided:

<pre class=\\"cpp\\">VARIANT\_ENUM\_CAST( MyClass::SomeMode); // now
functions that take SomeMode can be bound.

.. raw:: html

   </pre>

The constants can also be bound inside ``_bind_methods``, by using:

| <pre class=\\"cpp\\">
| BIND\_CONSTANT( MODE\_FIRST );
| BIND\_CONSTANT( MODE\_SECOND );

.. raw:: html

   </pre>

Properties (set/get)
--------------------

Objects export properties, properties are useful for the following:

-  Serializing and deserializing the object.
-  Creating a list of editable values for the Object derived class.

Properties are usually defined by the PropertyInfo() class. Usually
constructed as:

<pre
class=\\"cpp\\">PropertyInfo(type,name,hint,hint\_string,usage\_flags)

.. raw:: html

   </pre>

For example:

<pre
class=\\"cpp\\">PropertyInfo(Variant::INT,\\"amount\\",PROPERTY\_HINT\_RANGE,\\"0,49,1\\",PROPERTY\_USAGE\_EDITOR)

.. raw:: html

   </pre>

This is an integer property, named \\"amount\\", hint is a range, range
goes from 0 to 49 in steps of 1 (integers). It is only usable for the
editor (edit value visually) but wont be serialized.

or

<pre
class=\\"cpp\\">PropertyInfo(Variant::STRING,\\"modes\\",PROPERTY\_HINT\_ENUM,\\"Enabled,Disabled,Turbo\\")

.. raw:: html

   </pre>

This is a string property, can take any string but the editor will only
allow the defined hint ones. Since no hint flags were specified, the
default ones are PROPERTY\_USAGE\_STORAGE and PROPERTY\_USAGE\_EDITOR.

There are plenty of hints and usages available in object.h, give them a
check.

Properties can also work like C# properties and be accessed from script
using indexing, but ths usage is generally discouraged, as using
functions is preferred for legibility. Many properties are also bound
with categories, such as \\"animation/frame\\" which also make indexing
imposssible unless using operator [].

From ``_bind_methods()``, properties can be created and bound as long as
a set/get functions exist. Example:

<pre class=\\"cpp\\">ADD\_PROPERTY(
PropertyInfo(Variant::INT,\\"amount\\"), \_SCS (\\"set\_amount\\"),
\_SCS (\\"get\_amount\\") )

.. raw:: html

   </pre>

This creates the property using the setter and the getter. ``_SCS`` is a
macro that creates a StringName efficiently.

Binding properties using ``_set``/``_get``/``_get_property_list``
-----------------------------------------------------------------

An additional method of creating properties exists when more flexibility
is desired (i.e. adding or removing properties on context):

The following functions can be overriden in an Object derived class,
they are NOT virtual, DO NOT make them virtual, they are called for
every override and the previous ones are not invalidated (multilevel
call).

| <pre class=\\"cpp\\">
| void \_get\_property\_info(List \*r\_props); //return list of
  propertes
| bool \_get(const StringName& p\_property, Variany& r\_value) const;
  //return true if property was found
| bool \_set(const StringName& p\_property, const Variany& p\_value);
  //return true if property was found

.. raw:: html

   </pre>

This is also a little less efficient since ``p_property`` must be
compared against the desired names in serial order.

Dynamic casting
---------------

Godot provides dynamic casting between Object Derived classes, for
example:

| <pre class=\\"cpp\\">
| void somefunc(Object \*some\_obj) {

| Button \* button = some\_obj->cast\_to&lt;Button&gt;();
| }

.. raw:: html

   </pre>

If cast fails, NULL is returned. This system uses RTTI, but it also
works fine (although a bit slower) when RTTI is disabled. This is useful
on platforms where a very small binary size is ideal, such as HTML5 or
consoles (with low memory footprint).

Signals
-------

Objects can have a set of signals defined (similar to Delegates in other
languages). Connecting to them is rather easy:

| <pre class=\\"cpp\\">
| obj->connect(,target\_instance,target\_method)
| //for example
| obj->connect(\\"enter\_tree\\",this,\\"\_node\_entered\_tree\\")

.. raw:: html

   </pre>

The method ``_node_entered_tree`` must be registered to the class using
``ObjectTypeDB::register_method`` (explained before).

Adding signals to a class is done in ``_bind_methods``, using the
``ADD_SIGNAL`` macro, for example:

<pre class=\\"cpp\\">ADD\_SIGNAL( MethodInfo(\\"been\_killed\\") )

.. raw:: html

   </pre>

References
----------

Reference inherits from Object and holds a reference count. It is the
base for reference counted object types. Declaring them must be done
using Ref<> template. For example.

| <pre class=\\"cpp\\">
| class MyReference: public Reference {
| OBJ\_TYPE( MyReference ,Reference);
| };

Ref myref = memnew( MyReference );

.. raw:: html

   </pre>

``myref`` is reference counted. It will be freed when no more Ref<>
templates point to it.

References:
~~~~~~~~~~~

-  \\\ `core/reference.h\\ <https://github.com/okamstudio/godot/blob/master/core/reference.h>`__

Resources:
----------

Resource inherits from Reference, so all resources are reference
counted. Resources can optionally contain a path, which reference a file
on disk. This can be set with ``resource.set_path(path)``. This is
normally done by the resource loader though. No two different resources
can have the same path, attempt to do so will result in an error.

Resources without a path are fine too.

References:
~~~~~~~~~~~

-  \\\ `core/resource.h\\ <https://github.com/okamstudio/godot/blob/master/core/resource.h>`__

Resource loading
----------------

Resources can be loaded with the ResourceLoader API, like this:

<pre class=\\"cpp\\">Ref res =
ResourceLoader::load(\\"res://someresource.res\\")

.. raw:: html

   </pre>

If a reference to that resource has been loaded previously and is in
memory, the resource loader will return that reference. This means that
there can be only one resource loaded from a file referenced on disk at
the same time.

-  resourceinteractiveloader (TODO)

References:
~~~~~~~~~~~

-  \\\ `core/io/resource\_loader.h\\ <https://github.com/okamstudio/godot/blob/master/core/io/resource_loader.h>`__

Resource saving
---------------

Saving a resource can be done with the resource saver API:

<pre
class=\\"cpp\\">ResourceSaver::save(\\"res://someresource.res\\",instance)

.. raw:: html

   </pre>

Instance will be saved. Sub resources that have a path to a file will be
saved as a reference to that resource. Sub resources without a path will
be bundled with the saved resource and assigned sub-IDs, like
\\"res://somereource.res::1\\". This also helps to cache them when
loaded.

References:
~~~~~~~~~~~

-  \\\ `core/io/resource\_saver.h\\ <https://github.com/okamstudio/godot/blob/master/core/io/resource_saver.h>`__
