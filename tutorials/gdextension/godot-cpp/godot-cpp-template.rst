.. _doc_using_godot-cpp-template:

Using the godot-cpp-template
============================

Introduction
------------

.. container:: steps

    .. compound:: Step 1

        Test 1

        .. container:: step-context

            .. image:: img/icu_data.png

    .. compound:: Step 2

        Test 2

        .. container:: step-context

            .. code-block:: cpp
                :caption: src/test.cpp
                :name: intro-step2-code
                :linenos:
                :emphasize-lines: 1

                #include <godot_cpp/classes/node.hpp>

                using namepsace Godot;

                class Test : public Node {
                    GDCLASS(Test, Node);

                public:
                    Test();
                    ~Test();
                };
