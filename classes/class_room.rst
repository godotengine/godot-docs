.. _class_Room:

Room
====

Inherits: :ref:`VisualInstance<class_visualinstance>`
-----------------------------------------------------

Category: Core
--------------

Brief Description
-----------------

Room data resource.

Member Functions
----------------

+--------------------------+---------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`set_room<class_Room_set_room>`  **(** :ref:`Room<class_room>` room  **)**                               |
+--------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`Room<class_room>`  | :ref:`get_room<class_Room_get_room>`  **(** **)** const                                                       |
+--------------------------+---------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`compute_room_from_subtree<class_Room_compute_room_from_subtree>`  **(** **)**                           |
+--------------------------+---------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`set_simulate_acoustics<class_Room_set_simulate_acoustics>`  **(** :ref:`bool<class_bool>` enable  **)** |
+--------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_simulating_acoustics<class_Room_is_simulating_acoustics>`  **(** **)** const                         |
+--------------------------+---------------------------------------------------------------------------------------------------------------+

Description
-----------

Room contains the data to define the bounds of a scene (using a BSP Tree). It is instanced by a :ref:`RoomInstance<class_roominstance>` node to create rooms. See that class documentation for more information about rooms.

Member Function Description
---------------------------

.. _class_Room_set_room:

- void  **set_room**  **(** :ref:`Room<class_room>` room  **)**

.. _class_Room_get_room:

- :ref:`Room<class_room>`  **get_room**  **(** **)** const

.. _class_Room_compute_room_from_subtree:

- void  **compute_room_from_subtree**  **(** **)**

.. _class_Room_set_simulate_acoustics:

- void  **set_simulate_acoustics**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Room_is_simulating_acoustics:

- :ref:`bool<class_bool>`  **is_simulating_acoustics**  **(** **)** const


