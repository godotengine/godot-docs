

Good bad test
=============




Doing our own thing
-------------------


.. container:: comparison-box

    .. container::

        **Do** this freaking thing. Follow the instructions pretty nicely.

        .. code-block::
            :class: code-example-good

            if (foo and bar) or not baz:
                print("condition is true")

            # Also more things here

    .. container::

        **Don't** do this other thing. It's because I really don't like it. Screw you.

        .. code-block::
            :class: code-example-bad

            if foo && bar || !baz:
                print("condition is true") # Putting more stuff here for testing purposes


-------------------------

-------------------------

Using ``table`` directive
-------------------------

.. table::
    :width: 100%
    :name: potato tomato
    :class: code-example-good

    +-------------------------------------------------+-------------------------------------------------+
    |                                                 |                                                 |
    |   **Good**                                      |   **Bad**                                       |
    |                                                 |                                                 |
    +=================================================+=================================================+
    |                                                 |                                                 |
    |.. rst-class:: code-example-good                 |.. rst-class:: code-example-bad                  |
    |                                                 |                                                 |
    |.. code-block::                                  |::                                               |
    |   :emphasize-lines: 2,3                         |                                                 |
    |                                                 |                                                 |
    |                                                 |                                                 |
    |                                                 |                                                 |
    |   # Code example 1aaaaaaaaaaaaaaaaaaaa          |   # Code example 2aaaaaaaaaaaaaaaaaaaaaaaaaaaaa |
    |   # Code example 1                              |   # Code example 2                              |
    |   # Code example 1                              |   # Code example 2                              |
    |   # Code example 1                              |   # Code example 2                              |
    |   # Code example 1                              |   # Code example 2                              |
    |                                                 |                                                 |
    +-------------------------------------------------+-------------------------------------------------+

Using ``list-table`` directive
------------------------------

.. list-table::
    :width: 100%
    :widths: auto
    :header-rows: 1

    * - Good
      - Bad
    * - .. rst-class:: code-example-good

        ::

            # Code example 1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            # Code example 1
            # Code example 1
            # Code example 1
            # Code example 1

      - .. rst-class:: code-example-bad

        ::

            # Code example 1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            # Code example 1
            # Code example 1
            # Code example 1
            # Code example 1


On master
---------


**Good**:

.. rst-class:: code-example-good

::

    if (foo and bar) or not baz:
        print("condition is true")

**Bad**:

.. rst-class:: code-example-bad

::

    if foo && bar || !baz:
        print("condition is true")


And that's it, really.
