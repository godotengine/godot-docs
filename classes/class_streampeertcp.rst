.. _class_StreamPeerTCP:

StreamPeerTCP
=============

**Inherits:** :ref:`StreamPeer<class_streampeer>`

**Category:** Core

TCP Stream peer.

Member Functions
----------------

+------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`connect<class_StreamPeerTCP_connect>`  **(** :ref:`String<class_string>` host, :ref:`int<class_int>` port  **)** |
+------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_connected<class_StreamPeerTCP_is_connected>`  **(** **)** const                                               |
+------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_status<class_StreamPeerTCP_get_status>`  **(** **)** const                                                   |
+------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`  | :ref:`get_connected_host<class_StreamPeerTCP_get_connected_host>`  **(** **)** const                                   |
+------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_connected_port<class_StreamPeerTCP_get_connected_port>`  **(** **)** const                                   |
+------------------------------+------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`disconnect<class_StreamPeerTCP_disconnect>`  **(** **)**                                                         |
+------------------------------+------------------------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

- **STATUS_NONE** = **0**
- **STATUS_CONNECTING** = **1**
- **STATUS_CONNECTED** = **2**
- **STATUS_ERROR** = **3**

Description
-----------

TCP Stream peer. This object can be used to connect to TCP servers, or also is returned by a tcp server.

Member Function Description
---------------------------

.. _class_StreamPeerTCP_connect:

- :ref:`int<class_int>`  **connect**  **(** :ref:`String<class_string>` host, :ref:`int<class_int>` port  **)**

.. _class_StreamPeerTCP_is_connected:

- :ref:`bool<class_bool>`  **is_connected**  **(** **)** const

.. _class_StreamPeerTCP_get_status:

- :ref:`int<class_int>`  **get_status**  **(** **)** const

.. _class_StreamPeerTCP_get_connected_host:

- :ref:`String<class_string>`  **get_connected_host**  **(** **)** const

.. _class_StreamPeerTCP_get_connected_port:

- :ref:`int<class_int>`  **get_connected_port**  **(** **)** const

.. _class_StreamPeerTCP_disconnect:

- void  **disconnect**  **(** **)**


