.. _class_StreamPeer:

StreamPeer
==========

**Inherits:** :ref:`Reference<class_reference>` **<** :ref:`Object<class_object>`

**Inherited By:** :ref:`StreamPeerSSL<class_streampeerssl>`, :ref:`StreamPeerTCP<class_streampeertcp>`

**Category:** Core

Brief Description
-----------------

Abstraction and base class for stream-based protocols.

Member Functions
----------------

+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`put_data<class_StreamPeer_put_data>`  **(** :ref:`RawArray<class_rawarray>` data  **)**                 |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`    | :ref:`put_partial_data<class_StreamPeer_put_partial_data>`  **(** :ref:`RawArray<class_rawarray>` data  **)** |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`    | :ref:`get_data<class_StreamPeer_get_data>`  **(** :ref:`int<class_int>` bytes  **)**                          |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`    | :ref:`get_partial_data<class_StreamPeer_get_partial_data>`  **(** :ref:`int<class_int>` bytes  **)**          |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_available_bytes<class_StreamPeer_get_available_bytes>`  **(** **)** const                           |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_big_endian<class_StreamPeer_set_big_endian>`  **(** :ref:`bool<class_bool>` enable  **)**           |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_big_endian_enabled<class_StreamPeer_is_big_endian_enabled>`  **(** **)** const                       |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`put_8<class_StreamPeer_put_8>`  **(** :ref:`int<class_int>` val  **)**                                  |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`put_u8<class_StreamPeer_put_u8>`  **(** :ref:`int<class_int>` val  **)**                                |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`put_16<class_StreamPeer_put_16>`  **(** :ref:`int<class_int>` val  **)**                                |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`put_u16<class_StreamPeer_put_u16>`  **(** :ref:`int<class_int>` val  **)**                              |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`put_32<class_StreamPeer_put_32>`  **(** :ref:`int<class_int>` val  **)**                                |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`put_u32<class_StreamPeer_put_u32>`  **(** :ref:`int<class_int>` val  **)**                              |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`put_64<class_StreamPeer_put_64>`  **(** :ref:`int<class_int>` val  **)**                                |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`put_u64<class_StreamPeer_put_u64>`  **(** :ref:`int<class_int>` val  **)**                              |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`put_float<class_StreamPeer_put_float>`  **(** :ref:`float<class_float>` val  **)**                      |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`put_double<class_StreamPeer_put_double>`  **(** :ref:`float<class_float>` val  **)**                    |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`put_utf8_string<class_StreamPeer_put_utf8_string>`  **(** :ref:`String<class_string>` val  **)**        |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`put_var<class_StreamPeer_put_var>`  **(** Variant val  **)**                                            |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_8<class_StreamPeer_get_8>`  **(** **)**                                                             |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_u8<class_StreamPeer_get_u8>`  **(** **)**                                                           |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_16<class_StreamPeer_get_16>`  **(** **)**                                                           |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_u16<class_StreamPeer_get_u16>`  **(** **)**                                                         |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_32<class_StreamPeer_get_32>`  **(** **)**                                                           |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_u32<class_StreamPeer_get_u32>`  **(** **)**                                                         |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_64<class_StreamPeer_get_64>`  **(** **)**                                                           |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_u64<class_StreamPeer_get_u64>`  **(** **)**                                                         |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`    | :ref:`get_float<class_StreamPeer_get_float>`  **(** **)**                                                     |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`    | :ref:`get_double<class_StreamPeer_get_double>`  **(** **)**                                                   |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`  | :ref:`get_string<class_StreamPeer_get_string>`  **(** :ref:`int<class_int>` bytes  **)**                      |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`  | :ref:`get_utf8_string<class_StreamPeer_get_utf8_string>`  **(** :ref:`int<class_int>` bytes  **)**            |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| Variant                      | :ref:`get_var<class_StreamPeer_get_var>`  **(** **)**                                                         |
+------------------------------+---------------------------------------------------------------------------------------------------------------+

Description
-----------

StreamPeer is an abstraction and base class for stream-based protocols (such as TCP or Unix Sockets). It provides an API for sending and receiving data through streams as raw data or strings.

Member Function Description
---------------------------

.. _class_StreamPeer_put_data:

- :ref:`int<class_int>`  **put_data**  **(** :ref:`RawArray<class_rawarray>` data  **)**

Send a chunk of data through the connection, blocking if necessary until the data is done sending. This function returns an Error code.

.. _class_StreamPeer_put_partial_data:

- :ref:`Array<class_array>`  **put_partial_data**  **(** :ref:`RawArray<class_rawarray>` data  **)**

Send a chunk of data through the connection, if all the data could not be sent at once, only part of it will. This function returns two values, an Error code and an integer, describing how much data was actually sent.

.. _class_StreamPeer_get_data:

- :ref:`Array<class_array>`  **get_data**  **(** :ref:`int<class_int>` bytes  **)**

Return a chunk data with the received bytes. The amount of bytes to be received can be requested in the "bytes" argument. If not enough bytes are available, the function will block until the desired amount is received. This function returns two values, an Error code and a data array.

.. _class_StreamPeer_get_partial_data:

- :ref:`Array<class_array>`  **get_partial_data**  **(** :ref:`int<class_int>` bytes  **)**

Return a chunk data with the received bytes. The amount of bytes to be received can be requested in the "bytes" argument. If not enough bytes are available, the function will return how many were actually received. This function returns two values, an Error code, and a data array.

.. _class_StreamPeer_get_available_bytes:

- :ref:`int<class_int>`  **get_available_bytes**  **(** **)** const

.. _class_StreamPeer_set_big_endian:

- void  **set_big_endian**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_StreamPeer_is_big_endian_enabled:

- :ref:`bool<class_bool>`  **is_big_endian_enabled**  **(** **)** const

.. _class_StreamPeer_put_8:

- void  **put_8**  **(** :ref:`int<class_int>` val  **)**

.. _class_StreamPeer_put_u8:

- void  **put_u8**  **(** :ref:`int<class_int>` val  **)**

.. _class_StreamPeer_put_16:

- void  **put_16**  **(** :ref:`int<class_int>` val  **)**

.. _class_StreamPeer_put_u16:

- void  **put_u16**  **(** :ref:`int<class_int>` val  **)**

.. _class_StreamPeer_put_32:

- void  **put_32**  **(** :ref:`int<class_int>` val  **)**

.. _class_StreamPeer_put_u32:

- void  **put_u32**  **(** :ref:`int<class_int>` val  **)**

.. _class_StreamPeer_put_64:

- void  **put_64**  **(** :ref:`int<class_int>` val  **)**

.. _class_StreamPeer_put_u64:

- void  **put_u64**  **(** :ref:`int<class_int>` val  **)**

.. _class_StreamPeer_put_float:

- void  **put_float**  **(** :ref:`float<class_float>` val  **)**

.. _class_StreamPeer_put_double:

- void  **put_double**  **(** :ref:`float<class_float>` val  **)**

.. _class_StreamPeer_put_utf8_string:

- void  **put_utf8_string**  **(** :ref:`String<class_string>` val  **)**

.. _class_StreamPeer_put_var:

- void  **put_var**  **(** Variant val  **)**

.. _class_StreamPeer_get_8:

- :ref:`int<class_int>`  **get_8**  **(** **)**

.. _class_StreamPeer_get_u8:

- :ref:`int<class_int>`  **get_u8**  **(** **)**

.. _class_StreamPeer_get_16:

- :ref:`int<class_int>`  **get_16**  **(** **)**

.. _class_StreamPeer_get_u16:

- :ref:`int<class_int>`  **get_u16**  **(** **)**

.. _class_StreamPeer_get_32:

- :ref:`int<class_int>`  **get_32**  **(** **)**

.. _class_StreamPeer_get_u32:

- :ref:`int<class_int>`  **get_u32**  **(** **)**

.. _class_StreamPeer_get_64:

- :ref:`int<class_int>`  **get_64**  **(** **)**

.. _class_StreamPeer_get_u64:

- :ref:`int<class_int>`  **get_u64**  **(** **)**

.. _class_StreamPeer_get_float:

- :ref:`float<class_float>`  **get_float**  **(** **)**

.. _class_StreamPeer_get_double:

- :ref:`float<class_float>`  **get_double**  **(** **)**

.. _class_StreamPeer_get_string:

- :ref:`String<class_string>`  **get_string**  **(** :ref:`int<class_int>` bytes  **)**

.. _class_StreamPeer_get_utf8_string:

- :ref:`String<class_string>`  **get_utf8_string**  **(** :ref:`int<class_int>` bytes  **)**

.. _class_StreamPeer_get_var:

- Variant  **get_var**  **(** **)**


