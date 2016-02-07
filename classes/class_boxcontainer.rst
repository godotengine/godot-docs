.. _class_BoxContainer:

BoxContainer
============

**Inherits:** :ref:`Container<class_container>`

**Category:** Core

Base class for Box containers.

Member Functions
----------------

+------------------------+------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`  | :ref:`get_alignment<class_BoxContainer_get_alignment>`  **(** **)** const                            |
+------------------------+------------------------------------------------------------------------------------------------------+
| void                   | :ref:`set_alignment<class_BoxContainer_set_alignment>`  **(** :ref:`int<class_int>` alignment  **)** |
+------------------------+------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

- **ALIGN_BEGIN** = **0**
- **ALIGN_CENTER** = **1**
- **ALIGN_END** = **2**

Description
-----------

Base class for Box containers. It arranges children controls vertically or horizontally, and rearranges them automatically when their minimum size changes.

Member Function Description
---------------------------

.. _class_BoxContainer_get_alignment:

- :ref:`int<class_int>`  **get_alignment**  **(** **)** const

.. _class_BoxContainer_set_alignment:

- void  **set_alignment**  **(** :ref:`int<class_int>` alignment  **)**


