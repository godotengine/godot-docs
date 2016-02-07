.. _class_PacketPeerUDP:

PacketPeerUDP
=============

**Inherits:** :ref:`PacketPeer<class_packetpeer>` **<** :ref:`Reference<class_reference>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------



Member Functions
----------------

+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Error                        | :ref:`listen<class_PacketPeerUDP_listen>`  **(** :ref:`int<class_int>` port, :ref:`int<class_int>` recv_buf_size=65536  **)**            |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`close<class_PacketPeerUDP_close>`  **(** **)**                                                                                     |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Error                        | :ref:`wait<class_PacketPeerUDP_wait>`  **(** **)**                                                                                       |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_listening<class_PacketPeerUDP_is_listening>`  **(** **)** const                                                                 |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`  | :ref:`get_packet_ip<class_PacketPeerUDP_get_packet_ip>`  **(** **)** const                                                               |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_packet_address<class_PacketPeerUDP_get_packet_address>`  **(** **)** const                                                     |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_packet_port<class_PacketPeerUDP_get_packet_port>`  **(** **)** const                                                           |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`set_send_address<class_PacketPeerUDP_set_send_address>`  **(** :ref:`String<class_string>` host, :ref:`int<class_int>` port  **)** |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

Member Function Description
---------------------------

.. _class_PacketPeerUDP_listen:

- Error  **listen**  **(** :ref:`int<class_int>` port, :ref:`int<class_int>` recv_buf_size=65536  **)**

.. _class_PacketPeerUDP_close:

- void  **close**  **(** **)**

.. _class_PacketPeerUDP_wait:

- Error  **wait**  **(** **)**

.. _class_PacketPeerUDP_is_listening:

- :ref:`bool<class_bool>`  **is_listening**  **(** **)** const

.. _class_PacketPeerUDP_get_packet_ip:

- :ref:`String<class_string>`  **get_packet_ip**  **(** **)** const

.. _class_PacketPeerUDP_get_packet_address:

- :ref:`int<class_int>`  **get_packet_address**  **(** **)** const

.. _class_PacketPeerUDP_get_packet_port:

- :ref:`int<class_int>`  **get_packet_port**  **(** **)** const

.. _class_PacketPeerUDP_set_send_address:

- :ref:`int<class_int>`  **set_send_address**  **(** :ref:`String<class_string>` host, :ref:`int<class_int>` port  **)**


