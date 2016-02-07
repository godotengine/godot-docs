.. _class_GrooveJoint2D:

GrooveJoint2D
=============

Inherits: :ref:`Joint2D<class_joint2d>`
---------------------------------------

Category: Core
--------------

Brief Description
-----------------

Groove constraint for 2D physics.

Member Functions
----------------

+----------------------------+------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_length<class_GrooveJoint2D_set_length>`  **(** :ref:`float<class_float>` length  **)**                 |
+----------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`  | :ref:`get_length<class_GrooveJoint2D_get_length>`  **(** **)** const                                             |
+----------------------------+------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_initial_offset<class_GrooveJoint2D_set_initial_offset>`  **(** :ref:`float<class_float>` offset  **)** |
+----------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`  | :ref:`get_initial_offset<class_GrooveJoint2D_get_initial_offset>`  **(** **)** const                             |
+----------------------------+------------------------------------------------------------------------------------------------------------------+

Description
-----------

Groove constraint for 2D physics. This is useful for making a body "slide" through a segment placed in another.

Member Function Description
---------------------------

.. _class_GrooveJoint2D_set_length:

- void  **set_length**  **(** :ref:`float<class_float>` length  **)**

Set the length of the groove.

.. _class_GrooveJoint2D_get_length:

- :ref:`float<class_float>`  **get_length**  **(** **)** const

Return the length of the groove.

.. _class_GrooveJoint2D_set_initial_offset:

- void  **set_initial_offset**  **(** :ref:`float<class_float>` offset  **)**

Set the initial offset of the groove on body A.

.. _class_GrooveJoint2D_get_initial_offset:

- :ref:`float<class_float>`  **get_initial_offset**  **(** **)** const

Set the final offset of the groove on body A.


