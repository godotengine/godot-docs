.. _doc_using_godot_cpp_template:

Using the godot-cpp-template
============================

Introduction
------------

.. container:: tutorial

    .. compound:: Step 1

        Test 1

        .. container:: step-context

            .. image:: img/icu_data.png

    .. container:: comment

        Hello. This is a comment inbetween two steps.

    .. compound:: Step 2

        Test 2

        .. container:: step-context

            .. tabs::
                .. code-tab:: cpp
                    :name: intro-step2-code
                    :linenos:
                    :emphasize-lines: 1

                    #include <godot_cpp/classes/node.hpp>

                .. code-tab:: gdscript GDScript
                    :caption: src/test.gd
                    :name: intro-step2-code
                    :linenos:
                    :emphasize-lines: 1

                    func _ready():
                        print("Hello, World!")

    .. compound:: Step 3

        Test 3

        .. container:: step-context

            .. tabs::
                .. code-tab:: cpp
                    :caption: src/test.cpp
                    :name: intro-step3-code
                    :linenos:
                    :emphasize-lines: 3

                    #include <godot_cpp/classes/node.hpp>

                    using namepsace Godot;

    .. compound:: Step 4

        Test 4

        .. container:: step-context

            .. tabs::
                .. code-tab:: cpp
                    :caption: src/test.cpp
                    :name: intro-step4-code
                    :linenos:
                    :emphasize-lines: 5-6

                    #include <godot_cpp/classes/node.hpp>

                    using namepsace Godot;

                    class Test : public Node {
                    };

    .. container:: comment

        Hello again! This is another comment.

    .. compound:: Step 5

        Test 5

        .. container:: step-context

            .. tabs::
                .. code-tab:: cpp
                    :caption: src/test.cpp
                    :name: intro-step5-code
                    :linenos:
                    :emphasize-lines: 6

                    #include <godot_cpp/classes/node.hpp>

                    using namepsace Godot;

                    class Test : public Node {
                        GDCLASS(Test, Node);
                    };

    .. compound:: Step 6

        Test 6

        .. container:: step-context

            .. tabs::
                .. code-tab:: cpp
                    :caption: src/test.cpp
                    :name: intro-step6-code
                    :linenos:
                    :emphasize-lines: 8-10

                    #include <godot_cpp/classes/node.hpp>

                    using namepsace Godot;

                    class Test : public Node {
                        GDCLASS(Test, Node);

                    public:
                        Test();
                        ~Test();
                    };


Introduction 2
--------------

.. container:: tutorial

    .. compound:: Step 1

        Test 1

        .. container:: step-context

            .. image:: img/icu_data.png

    .. container:: comment

        Hello. This is a comment inbetween two steps.

    .. compound:: Step 2

        Test 2

        .. container:: step-context

            .. tabs::
                .. code-tab:: cpp
                    :name: intro-step2-code
                    :linenos:
                    :emphasize-lines: 1

                    #include <godot_cpp/classes/node.hpp>

                .. code-tab:: gdscript GDScript
                    :caption: src/test.gd
                    :name: intro2-step2-code
                    :linenos:
                    :emphasize-lines: 1

                    func _ready():
                        print("Hello, World!")

    .. compound:: Step 3

        Test 3

        .. container:: step-context

            .. tabs::
                .. code-tab:: cpp
                    :caption: src/test.cpp
                    :name: intro2-step3-code
                    :linenos:
                    :emphasize-lines: 3

                    #include <godot_cpp/classes/node.hpp>

                    using namepsace Godot;

    .. compound:: Step 4

        Test 4

        .. container:: step-context

            .. tabs::
                .. code-tab:: cpp
                    :caption: src/test.cpp
                    :name: intro2-step4-code
                    :linenos:
                    :emphasize-lines: 5-6

                    #include <godot_cpp/classes/node.hpp>

                    using namepsace Godot;

                    class Test : public Node {
                    };

    .. container:: comment

        Hello again! This is another comment.

    .. compound:: Step 5

        Test 5

        .. container:: step-context

            .. tabs::
                .. code-tab:: cpp
                    :caption: src/test.cpp
                    :name: intro2-step5-code
                    :linenos:
                    :emphasize-lines: 6

                    #include <godot_cpp/classes/node.hpp>

                    using namepsace Godot;

                    class Test : public Node {
                        GDCLASS(Test, Node);
                    };

    .. compound:: Step 6

        Test 6

        .. container:: step-context

            .. tabs::
                .. code-tab:: cpp
                    :caption: src/test.cpp
                    :name: intro2-step6-code
                    :linenos:
                    :emphasize-lines: 88

                    #include <godot_cpp/classes/node.hpp>

                    using namepsace Godot;

                    class Test : public Node {
                        GDCLASS(Test, Node);

                    public:
                        Test();
                        ~Test();
                    };

                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
                    // Hello
                    // World
