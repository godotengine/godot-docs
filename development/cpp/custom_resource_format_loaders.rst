.. _doc_custom_resource_format_loaders:

Custom resource format loaders
==============================

Introduction
------------

ResourceFormatLoader is a factory interface for loading file assets. 
Resources are primary containers. When load is called on the same file 
path again, the previous loaded Resource will be referenced. Naturally, 
loaded resources must be stateless.

This guide assumes the reader knows how to create C++ modules and godot 
data types. If not, refer to this guide :ref:`doc_custom_modules_in_c++`.

References
~~~~~~~~~~

- :ref:`ResourceLoader<class_resourceloader>`
- `core/io/resource_loader.cpp <https://github.com/godotengine/godot/blob/master/core/io/resource_loader.cpp#L258>`__

What for?
---------

- Adding new support for many file formats
- Audio formats
- Video formats
- Machine learning models

What not?
---------

- Raster images

ImageFormatLoader should be used to load images.

References
~~~~~~~~~~

- `core/io/image_loader.h <https://github.com/godotengine/godot/blob/master/core/io/image_loader.h>`__


Creating a ResourceFormatLoader
-------------------------------

Each file format consist of a data container and a ``ResourceFormatLoader``. 

ResourceFormatLoaders are usually simple classes which return all the 
necessary metadata for supporting new extensions in Godot. The 
class must the return the format name and the extension string.

In addition, ResourceFormatLoaders must convert file paths into 
resources with the ``load`` function. To load a resource, ``load`` must 
read and handle data serialization. 


.. code:: cpp

	#ifndef MY_JSON_LOADER_H
	#define MY_JSON_LOADER_H

	#include "io/resource_loader.h"

	class ResourceFormatLoaderMyJson : public ResourceFormatLoader {
	public:
		virtual RES load(const String &p_path, const String &p_original_path, Error *r_error = NULL);
		virtual void get_recognized_extensions(List<String> *p_extensions) const;
		virtual bool handles_type(const String &p_type) const;
		virtual String get_resource_type(const String &p_path) const;

		ResourceFormatLoaderMyJson();
		virtual ~ResourceFormatLoaderMyJson() {}
	};
	#endif // MY_JSON_LOADER_H

.. code:: cpp

	#include "my_json_loader.h"
	#include "my_json.h"

	ResourceFormatLoaderMyJson::ResourceFormatLoaderMyJson() {
	}

	RES ResourceFormatLoaderMyJson::load(const String &p_path, const String &p_original_path, Error *r_error) {
		MyJson *my = memnew(MyJson);
		if (r_error)
			*r_error = OK;
		Error err = my->set_file(p_path);
		return Ref<MyJson>(my);
	}

	void ResourceFormatLoaderMyJson::get_recognized_extensions(List<String> *p_extensions) const {
		p_extensions->push_back("mjson");
	}

	String ResourceFormatLoaderMyJson::get_resource_type(const String &p_path) const {

		if (p_path.get_extension().to_lower() == "mjson")
			return "MyJson";
		return "";
	}

	bool ResourceFormatLoaderMyJson::handles_type(const String &p_type) const {
		return (p_type == "MyJson");
	}


Creating custom data types
--------------------------

Godot may not have a proper substitute within its :ref:`doc_core_types`
or managed resources. Godot needs a new registered data type to
understand additional binary formats such as machine learning models.

Here is an example of how to create a custom datatype

.. code:: cpp

	#ifndef MY_JSON_H
	#define MY_JSON_H

	#include "core/variant.h"
	#include "reference.h"
	#include "variant_parser.h"
	#include "io/json.h"
	#include "dictionary.h"

	class MyJson : public Resource{
		GDCLASS(MyJson, Resource);

	protected:
		static void _bind_methods() {
			ClassDB::bind_method(D_METHOD("toString"), &MyJson::toString);
		}

	private:
		Dictionary dict;
	public:
		Error set_file(const String &p_path){
			Error error_file;
			FileAccess *file = FileAccess::open(p_path, FileAccess::READ, &error_file);

			String buf = String("");
			while(!file->eof_reached()){
				buf += file->get_line();
			}
			String err_string;
			int err_line;
			JSON cmd;
			Variant ret;
			Error err = cmd.parse( buf, ret, err_string, err_line);
			dict = Dictionary(ret);
			file -> close();
			return OK;
		}

		String toString() const {
			return String(*this);
		}

		operator String() const {
			JSON a; 
			return a.print(dict);
		}

	    MyJson() {};
	    ~MyJson() {};
	};
	#endif

Considerations
~~~~~~~~~~~~~~

Some libraries may not define certain common routines such as i/o handling. 
Therefore, Godot call translations are required.

For example, here is the code for translating ``FileAccess`` 
calls into ``std::istream``.

.. code:: cpp

	#include <istream>
	#include <streambuf>
    
	class GodotFileInStreamBuf : public std::streambuf{
	public:
		GodotFileInStreamBuf(FileAccess * fa) {
			_file = fa;
		}
		int underflow() {
			if (_file->eof_reached()) {
				return EOF;
			} else {
				size_t pos = _file->get_position();
				uint8_t ret = _file->get_8();
				_file->seek(pos); //required since get_8() advances the read head
				return ret;
			}
		}
		int uflow() {
			return _file->eof_reached() ?  EOF : _file -> get_8();
		}
	private:
		FileAccess * _file;
	};


References
~~~~~~~~~~

- `istream <http://www.cplusplus.com/reference/istream/istream/>`__
- `streambuf <http://www.cplusplus.com/reference/streambuf/streambuf/?kw=streambuf>`__
- `core/io/fileaccess.h <https://github.com/godotengine/godot/blob/master/core/os/file_access.h>`__

Registering the new file format
-------------------------------

Godot registers ``ResourcesFormatLoader`` with a ``ResourceLoader``
handler. The handler selects the proper loader automatically
when ``load`` is called.

.. code:: cpp

	/* register_types.cpp */
	#include "register_types.h"
	#include "class_db.h"

	#include "my_json_loader.h"
	#include "my_json.h"

	static ResourceFormatLoaderMyJson *my_json_loader = NULL;
	void register_my_json_types() {
		my_json_loader = memnew(ResourceFormatLoaderMyJson);
		ResourceLoader::add_resource_format_loader(my_json_loader);
		ClassDB::register_class<MyJson>();
	}

	void unregister_my_json_types() {
		memdelete(my_json_loader);
	}

References
~~~~~~~~~~

- `core/io/resource_loader.cpp <https://github.com/godotengine/godot/blob/master/core/io/resource_loader.cpp#L280>`__

Loading it on GDScript
----------------------


.. code::

	{
	  "savefilename" : "demo.mjson",
	  "demo": [
	    "welcome",
	    "to",
	    "godot",
	    "resource",
	    "loaders"
	  ]
	}

.. code:: 

	extends Node 
	
	func _ready():
		var myjson = load("res://demo.mjson")
		print( myjson.toString())
