.. _class_PacketPeerStream:

PacketPeerStream
================

**Inherits:** :ref:`PacketPeer<class_packetpeer>`

**Category:** Core

Wrapper to use a PacketPeer over a StreamPeer.

Member Functions
----------------

+-------+-----------------------------------------------------------------------------------------------------------------------+
| void  | :ref:`set_stream_peer<class_PacketPeerStream_set_stream_peer>`  **(** :ref:`StreamPeer<class_streampeer>` peer  **)** |
+-------+-----------------------------------------------------------------------------------------------------------------------+

Description
-----------

PacketStreamPeer provides a wrapper for working using packets over a stream. This allows for using packet based code with StreamPeers. PacketPeerStream implements a custom protocol over the StreamPeer, so the user should not read or write to the wrapped StreamPeer directly.

Member Function Description
---------------------------

.. _class_PacketPeerStream_set_stream_peer:

- void  **set_stream_peer**  **(** :ref:`StreamPeer<class_streampeer>` peer  **)**

Set the StreamPeer object to be wrapped


