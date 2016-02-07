.. _class_PacketPeer:

PacketPeer
==========

**Inherits:** :ref:`Reference<class_reference>` **<** :ref:`Object<class_object>`

**Inherited By:** :ref:`PacketPeerStream<class_packetpeerstream>`, :ref:`PacketPeerUDP<class_packetpeerudp>`

**Category:** Core

Brief Description
-----------------

Abstraction and base class for packet-based protocols.

Member Functions
----------------

+----------------------------------+-----------------------------------------------------------------------------------------------------+
| void                             | :ref:`get_var<class_PacketPeer_get_var>`  **(** **)** const                                         |
+----------------------------------+-----------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`put_var<class_PacketPeer_put_var>`  **(** Variant var  **)**                                  |
+----------------------------------+-----------------------------------------------------------------------------------------------------+
| :ref:`RawArray<class_rawarray>`  | :ref:`get_packet<class_PacketPeer_get_packet>`  **(** **)** const                                   |
+----------------------------------+-----------------------------------------------------------------------------------------------------+
| Error                            | :ref:`put_packet<class_PacketPeer_put_packet>`  **(** :ref:`RawArray<class_rawarray>` buffer  **)** |
+----------------------------------+-----------------------------------------------------------------------------------------------------+
| Error                            | :ref:`get_packet_error<class_PacketPeer_get_packet_error>`  **(** **)** const                       |
+----------------------------------+-----------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`get_available_packet_count<class_PacketPeer_get_available_packet_count>`  **(** **)** const   |
+----------------------------------+-----------------------------------------------------------------------------------------------------+

Description
-----------

PacketPeer is an abstraction and base class for packet-based protocols (such as UDP). It provides an API for sending and receiving packets both as raw data or variables. This makes it easy to transfer data over a protocol, without having to encode data as low level bytes or having to worry about network ordering.

Member Function Description
---------------------------

.. _class_PacketPeer_get_var:

- void  **get_var**  **(** **)** const

.. _class_PacketPeer_put_var:

- :ref:`int<class_int>`  **put_var**  **(** Variant var  **)**

.. _class_PacketPeer_get_packet:

- :ref:`RawArray<class_rawarray>`  **get_packet**  **(** **)** const

.. _class_PacketPeer_put_packet:

- Error  **put_packet**  **(** :ref:`RawArray<class_rawarray>` buffer  **)**

.. _class_PacketPeer_get_packet_error:

- Error  **get_packet_error**  **(** **)** const

.. _class_PacketPeer_get_available_packet_count:

- :ref:`int<class_int>`  **get_available_packet_count**  **(** **)** const


