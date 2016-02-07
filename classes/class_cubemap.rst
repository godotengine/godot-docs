.. _class_CubeMap:

CubeMap
=======

Inherits: :ref:`Resource<class_resource>`
-----------------------------------------

Category: Core
--------------

Brief Description
-----------------



Member Functions
----------------

+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`      | :ref:`get_width<class_CubeMap_get_width>`  **(** **)** const                                                              |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`      | :ref:`get_height<class_CubeMap_get_height>`  **(** **)** const                                                            |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`RID<class_rid>`      | :ref:`get_rid<class_CubeMap_get_rid>`  **(** **)** const                                                                  |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_flags<class_CubeMap_set_flags>`  **(** :ref:`int<class_int>` flags  **)**                                       |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`      | :ref:`get_flags<class_CubeMap_get_flags>`  **(** **)** const                                                              |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_side<class_CubeMap_set_side>`  **(** :ref:`int<class_int>` side, :ref:`Image<class_image>` image  **)**         |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`Image<class_image>`  | :ref:`get_side<class_CubeMap_get_side>`  **(** :ref:`int<class_int>` side  **)** const                                    |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_storage<class_CubeMap_set_storage>`  **(** :ref:`int<class_int>` mode  **)**                                    |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`      | :ref:`get_storage<class_CubeMap_get_storage>`  **(** **)** const                                                          |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_lossy_storage_quality<class_CubeMap_set_lossy_storage_quality>`  **(** :ref:`float<class_float>` quality  **)** |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`  | :ref:`get_lossy_storage_quality<class_CubeMap_get_lossy_storage_quality>`  **(** **)** const                              |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

- **STORAGE_RAW** = **0**
- **STORAGE_COMPRESS_LOSSY** = **1**
- **STORAGE_COMPRESS_LOSSLESS** = **2**
- **SIDE_LEFT** = **0**
- **SIDE_RIGHT** = **1**
- **SIDE_BOTTOM** = **2**
- **SIDE_TOP** = **3**
- **SIDE_FRONT** = **4**
- **SIDE_BACK** = **5**
- **FLAG_MIPMAPS** = **1**
- **FLAG_REPEAT** = **2**
- **FLAG_FILTER** = **4**
- **FLAGS_DEFAULT** = **7**

Member Function Description
---------------------------

.. _class_CubeMap_get_width:

- :ref:`int<class_int>`  **get_width**  **(** **)** const

.. _class_CubeMap_get_height:

- :ref:`int<class_int>`  **get_height**  **(** **)** const

.. _class_CubeMap_get_rid:

- :ref:`RID<class_rid>`  **get_rid**  **(** **)** const

.. _class_CubeMap_set_flags:

- void  **set_flags**  **(** :ref:`int<class_int>` flags  **)**

.. _class_CubeMap_get_flags:

- :ref:`int<class_int>`  **get_flags**  **(** **)** const

.. _class_CubeMap_set_side:

- void  **set_side**  **(** :ref:`int<class_int>` side, :ref:`Image<class_image>` image  **)**

.. _class_CubeMap_get_side:

- :ref:`Image<class_image>`  **get_side**  **(** :ref:`int<class_int>` side  **)** const

.. _class_CubeMap_set_storage:

- void  **set_storage**  **(** :ref:`int<class_int>` mode  **)**

.. _class_CubeMap_get_storage:

- :ref:`int<class_int>`  **get_storage**  **(** **)** const

.. _class_CubeMap_set_lossy_storage_quality:

- void  **set_lossy_storage_quality**  **(** :ref:`float<class_float>` quality  **)**

.. _class_CubeMap_get_lossy_storage_quality:

- :ref:`float<class_float>`  **get_lossy_storage_quality**  **(** **)** const


