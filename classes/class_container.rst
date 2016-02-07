.. _class_Container:

Container
=========

Inherits: :ref:`Control<class_control>`
---------------------------------------

Category: Core
--------------

Brief Description
-----------------

Base node for containers.

Member Functions
----------------

+-------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void  | :ref:`queue_sort<class_Container_queue_sort>`  **(** **)**                                                                                    |
+-------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void  | :ref:`fit_child_in_rect<class_Container_fit_child_in_rect>`  **(** :ref:`Control<class_control>` child, :ref:`Rect2<class_rect2>` rect  **)** |
+-------+-----------------------------------------------------------------------------------------------------------------------------------------------+

Signals
-------

-  **sort_children**  **(** **)**

Numeric Constants
-----------------

- **NOTIFICATION_SORT_CHILDREN** = **50** --- Notification for when sorting the children, it must be obeyed immediately.

Description
-----------

Base node for conainers. A :ref:`Container<class_container>` contains other controls and automatically arranges them in a certain way.

A Control can inherit this to reate custom container classes.

Member Function Description
---------------------------

.. _class_Container_queue_sort:

- void  **queue_sort**  **(** **)**

Queue resort of the contained children. This is called automatically anyway, but can be called upon request.

.. _class_Container_fit_child_in_rect:

- void  **fit_child_in_rect**  **(** :ref:`Control<class_control>` child, :ref:`Rect2<class_rect2>` rect  **)**

Fit a child control in a given rect. This is mainly a helper for creating custom container classes.


