.. _class_Slider:

Slider
======

Inherits: :ref:`Range<class_range>`
-----------------------------------

Category: Core
--------------

Brief Description
-----------------

Base class for GUI Sliders.

Member Functions
----------------

+--------------------------+----------------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`set_ticks<class_Slider_set_ticks>`  **(** :ref:`int<class_int>` count  **)**                                   |
+--------------------------+----------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`    | :ref:`get_ticks<class_Slider_get_ticks>`  **(** **)** const                                                          |
+--------------------------+----------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`get_ticks_on_borders<class_Slider_get_ticks_on_borders>`  **(** **)** const                                    |
+--------------------------+----------------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`set_ticks_on_borders<class_Slider_set_ticks_on_borders>`  **(** :ref:`bool<class_bool>` ticks_on_border  **)** |
+--------------------------+----------------------------------------------------------------------------------------------------------------------+

Description
-----------

Base class for GUI Sliders.

Member Function Description
---------------------------

.. _class_Slider_set_ticks:

- void  **set_ticks**  **(** :ref:`int<class_int>` count  **)**

Set amount of ticks to display in slider.

.. _class_Slider_get_ticks:

- :ref:`int<class_int>`  **get_ticks**  **(** **)** const

Return amounts of ticks to display on slider.

.. _class_Slider_get_ticks_on_borders:

- :ref:`bool<class_bool>`  **get_ticks_on_borders**  **(** **)** const

Return true if ticks are visible on borders.

.. _class_Slider_set_ticks_on_borders:

- void  **set_ticks_on_borders**  **(** :ref:`bool<class_bool>` ticks_on_border  **)**

Set true if ticks are visible on borders.


