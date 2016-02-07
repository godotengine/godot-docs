.. _class_StyleBoxTexture:

StyleBoxTexture
===============

Inherits: :ref:`StyleBox<class_stylebox>`
-----------------------------------------

Category: Core
--------------

Brief Description
-----------------

Texture Based 3x3 scale style.

Member Functions
----------------

+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_texture<class_StyleBoxTexture_set_texture>`  **(** :ref:`Texture<class_texture>` texture  **)**                                              |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Texture<class_texture>`  | :ref:`get_texture<class_StyleBoxTexture_get_texture>`  **(** **)** const                                                                               |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_margin_size<class_StyleBoxTexture_set_margin_size>`  **(** :ref:`int<class_int>` margin, :ref:`float<class_float>` size  **)**               |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_margin_size<class_StyleBoxTexture_get_margin_size>`  **(** :ref:`int<class_int>` margin  **)** const                                         |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_expand_margin_size<class_StyleBoxTexture_set_expand_margin_size>`  **(** :ref:`int<class_int>` margin, :ref:`float<class_float>` size  **)** |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_expand_margin_size<class_StyleBoxTexture_get_expand_margin_size>`  **(** :ref:`int<class_int>` margin  **)** const                           |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_draw_center<class_StyleBoxTexture_set_draw_center>`  **(** :ref:`bool<class_bool>` enable  **)**                                             |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`get_draw_center<class_StyleBoxTexture_get_draw_center>`  **(** **)** const                                                                       |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

Texture Based 3x3 scale style. This stylebox performs a 3x3 scaling of a texture, where only the center cell is fully stretched. This allows for the easy creation of bordered styles.

Member Function Description
---------------------------

.. _class_StyleBoxTexture_set_texture:

- void  **set_texture**  **(** :ref:`Texture<class_texture>` texture  **)**

.. _class_StyleBoxTexture_get_texture:

- :ref:`Texture<class_texture>`  **get_texture**  **(** **)** const

.. _class_StyleBoxTexture_set_margin_size:

- void  **set_margin_size**  **(** :ref:`int<class_int>` margin, :ref:`float<class_float>` size  **)**

.. _class_StyleBoxTexture_get_margin_size:

- :ref:`float<class_float>`  **get_margin_size**  **(** :ref:`int<class_int>` margin  **)** const

.. _class_StyleBoxTexture_set_expand_margin_size:

- void  **set_expand_margin_size**  **(** :ref:`int<class_int>` margin, :ref:`float<class_float>` size  **)**

.. _class_StyleBoxTexture_get_expand_margin_size:

- :ref:`float<class_float>`  **get_expand_margin_size**  **(** :ref:`int<class_int>` margin  **)** const

.. _class_StyleBoxTexture_set_draw_center:

- void  **set_draw_center**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_StyleBoxTexture_get_draw_center:

- :ref:`bool<class_bool>`  **get_draw_center**  **(** **)** const


