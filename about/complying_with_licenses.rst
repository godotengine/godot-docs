.. _doc_complying_with_licenses:

Complying with Licenses
=======================

What are licenses?
------------------

Godot is created and distributed under the `MIT License <https://opensource.org/licenses/MIT>`_. It doesn't have a sole owner either, as every contributor that submits code to the project does it under this same license and keeps ownership of the contribution.

The license is the legal requirement for you (or your company) to use and distribute the software (and derivative projects, including games made with it). Your game or project can have a different license, but it still needs to comply with the original one.


Requirements
------------

In the case of the MIT license, the only requirement is to include the license text somewhere in your game or derivative project.

This text reads as follows:


	This game uses Godot Engine, available under the following license:

	Copyright (c) 2007-2020 Juan Linietsky, Ariel Manzur.
	Copyright (c) 2014-2020 Godot Engine contributors.

	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


.. note:: Your games do not need to be under the same license. You are free to release your Godot projects under any license and to create commercial games with the engine.

Inclusion
---------

The license does not specify how it has to be included, so anything is valid as long as it can be displayed under some condition. These are the most common approaches (only need to implement one of them, not all).

Credits screen
^^^^^^^^^^^^^^

Include the above license text somewhere in the credits screen. It can be at the bottom after showing the rest of the credits. Most large studios use this approach with open source licenses.

Licenses screen
^^^^^^^^^^^^^^^

Some games have a special menu (often in the settings) to display licenses.

Output log
^^^^^^^^^^

Just printing the licensing text using a :ref:`print() <class_@GDScript_method_print>` function may be enough on platforms where a global output log is readable (as an example, mobile devices).

Accompanying file
^^^^^^^^^^^^^^^^^

If the game is distributed on desktop operating systems, a file containing the license can be added to the software that is installed to the user PC.

Printed manual
^^^^^^^^^^^^^^

If the game includes printed manuals, license text can be included there.

Third Party licenses
--------------------

Godot itself contains software written by `third parties <https://github.com/godotengine/godot/blob/master/COPYRIGHT.txt>`_. Most of it does not require license inclusion, but some do. Make sure to do it if you are using them. Here is a list of which ones require it:

FreeType
^^^^^^^^

Godot uses `FreeType <https://www.freetype.org/>`_ to render fonts. Its license requires attribution, so the following text must be included together with the Godot license:


	Portions of this software are copyright © <year> The FreeType Project (www.freetype.org).  All rights reserved.


ENet
^^^^

If the project being created is a multiplayer game using the `ENet <http://enet.bespin.org/>`_ driver, ENet has similar licensing terms as Godot


	Copyright (c) 2002-2016 Lee Salzman

	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

MBedTLS
^^^^^^^

If the project is done with Godot 3.1 or above and it utilizes SSL (usually through HTTP requests), the `MBedTLS <https://tls.mbed.org>`_ Apache license needs to be complied by including the following text:


	MBedTLS is Copyright (C) 2013-2019 ARM

	Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

Keep in mind that Godot 2.x and 3.0 use `OpenSSL <https://www.openssl.org>`_ instead.
