.. _doc_handling_compatibility_breakages:

Handling compatibility breakages
================================

.. TODO: Elaborate on types of compatibility and procedure.

So you've added a new parameter to a method, changed the return type,
changed the type of a parameter, or changed its default value,
and now the automated testing is complaining about compatibility breakages?

Breaking compatibility should be avoided, but when necessary there are systems in place
to handle this in a way that makes the transition as smooth as possible.

A practical example
-------------------

.. TODO: Add example that showcases more details like original default arguments etc.

These changes are taken from `pull request #88047 <https://github.com/godotengine/godot/pull/88047>`_, which added
new pathing options to ``AStarGrid2D`` and other AStar classes.
Among other changes, these methods were modified in ``core/math/a_star_grid_2d.h``:

.. code-block:: cpp

    Vector<Vector2> get_point_path(const Vector2i &p_from, const Vector2i &p_to);
    TypedArray<Vector2i> get_id_path(const Vector2i &p_from, const Vector2i &p_to);

To:

.. code-block:: cpp

    Vector<Vector2> get_point_path(const Vector2i &p_from, const Vector2i &p_to, bool p_allow_partial_path = false);
    TypedArray<Vector2i> get_id_path(const Vector2i &p_from, const Vector2i &p_to, bool p_allow_partial_path = false);

This meant adding new compatibility method bindings to the file, which should be in the ``protected`` section of
the code, usually placed next to ``_bind_methods()``:

.. code-block:: cpp

    #ifndef DISABLE_DEPRECATED
        TypedArray<Vector2i> _get_id_path_bind_compat_88047(const Vector2i &p_from, const Vector2i &p_to);
        Vector<Vector2> _get_point_path_bind_compat_88047(const Vector2i &p_from, const Vector2i &p_to);
        static void _bind_compatibility_methods();
    #endif

They should start with an ``_`` to indicate that they are internal, and end with ``_bind_compat_`` followed by the PR number
that introduced the change (``88047`` in this example). These compatibility methods need to be implemented in a dedicated file,
like ``core/math/a_star_grid_2d.compat.inc`` in this case:

.. code-block:: cpp
    :caption: core/math/a_star_grid_2d.compat.inc

    /**************************************************************************/
    /*  a_star_grid_2d.compat.inc                                             */
    /**************************************************************************/
    /*                         This file is part of:                          */
    /*                             GODOT ENGINE                               */
    /*                        https://godotengine.org                         */
    /**************************************************************************/
    /* Copyright (c) 2014-present Godot Engine contributors (see AUTHORS.md). */
    /* Copyright (c) 2007-2014 Juan Linietsky, Ariel Manzur.                  */
    /*                                                                        */
    /* Permission is hereby granted, free of charge, to any person obtaining  */
    /* a copy of this software and associated documentation files (the        */
    /* "Software"), to deal in the Software without restriction, including    */
    /* without limitation the rights to use, copy, modify, merge, publish,    */
    /* distribute, sublicense, and/or sell copies of the Software, and to     */
    /* permit persons to whom the Software is furnished to do so, subject to  */
    /* the following conditions:                                              */
    /*                                                                        */
    /* The above copyright notice and this permission notice shall be         */
    /* included in all copies or substantial portions of the Software.        */
    /*                                                                        */
    /* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,        */
    /* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF     */
    /* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. */
    /* IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY   */
    /* CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,   */
    /* TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE      */
    /* SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                 */
    /**************************************************************************/

    #ifndef DISABLE_DEPRECATED

    #include "core/variant/typed_array.h"

    TypedArray<Vector2i> AStarGrid2D::_get_id_path_bind_compat_88047(const Vector2i &p_from_id, const Vector2i &p_to_id) {
        return get_id_path(p_from_id, p_to_id, false);
    }

    Vector<Vector2> AStarGrid2D::_get_point_path_bind_compat_88047(const Vector2i &p_from_id, const Vector2i &p_to_id) {
        return get_point_path(p_from_id, p_to_id, false);
    }

    void AStarGrid2D::_bind_compatibility_methods() {
        ClassDB::bind_compatibility_method(D_METHOD("get_id_path", "from_id", "to_id"), &AStarGrid2D::_get_id_path_bind_compat_88047);
        ClassDB::bind_compatibility_method(D_METHOD("get_point_path", "from_id", "to_id"), &AStarGrid2D::_get_point_path_bind_compat_88047);
    }

    #endif // DISABLE_DEPRECATED

Unless the change in compatibility is complex, the compatibility method should call the modified method directly,
instead of duplicating that method. Make sure to match the default arguments for that method (in the example above this would be ``false``).

This file should always be placed next to the original file, and have ``.compat.inc`` at the end instead of ``.cpp`` or ``.h``.
Next, this should be included in the ``.cpp`` file we're adding compatibility methods to, so ``core/math/a_star_grid_2d.cpp``:

.. code-block:: cpp
    :caption: core/math/a_star_grid_2d.cpp

    #include "a_star_grid_2d.h"
    #include "a_star_grid_2d.compat.inc"

    #include "core/variant/typed_array.h"

And finally, the changes reported by the API validation step should be added to the relevant validation file. Because this was
done during the development of 4.3, this would be ``misc/extension_api_validation/4.2-stable.expected`` (including changes not shown in
this example):

.. code-block:: text
    :caption: misc/extension_api_validation/4.2-stable.expected

    GH-88047
    --------
    Validate extension JSON: Error: Field 'classes/AStar2D/methods/get_id_path/arguments': size changed value in new API, from 2 to 3.
    Validate extension JSON: Error: Field 'classes/AStar2D/methods/get_point_path/arguments': size changed value in new API, from 2 to 3.
    Validate extension JSON: Error: Field 'classes/AStar3D/methods/get_id_path/arguments': size changed value in new API, from 2 to 3.
    Validate extension JSON: Error: Field 'classes/AStar3D/methods/get_point_path/arguments': size changed value in new API, from 2 to 3.
    Validate extension JSON: Error: Field 'classes/AStarGrid2D/methods/get_id_path/arguments': size changed value in new API, from 2 to 3.
    Validate extension JSON: Error: Field 'classes/AStarGrid2D/methods/get_point_path/arguments': size changed value in new API, from 2 to 3.

    Added optional "allow_partial_path" argument to get_id_path and get_point_path methods in AStar classes.
    Compatibility methods registered.

The instructions for how to add to that file are at the top of the file itself.

If you get a "Hash changed" error for a method, it means that the compatibility binding is missing or incorrect.
Such lines shouldn't be added to the ``.expected`` file, but fixed by binding the proper compatibility method.

And that's it! You might run into a bit more complicated cases, like rearranging arguments,
changing return types, etc., but this covers the basic on how to use this system.

For more information, see `pull request #76446 <https://github.com/godotengine/godot/pull/76446>`_.
