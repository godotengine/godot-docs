.. _doc_unit_testing:

Unit testing
============

Godot Engine allows to write unit tests directly in C++. The engine integrates
the `doctest <https://github.com/doctest/doctest>`_ unit testing framework which
gives ability to write test suites and test cases next to production code, but
since the tests in Godot go through a different ``main`` entry point, the tests
reside in a dedicated ``tests/`` directory instead, which is located at the root
of the engine source code.

Platform and target support
---------------------------

C++ unit tests can be run on Linux, macOS, and Windows operating systems.

Tests can only be run with editor ``tools`` enabled, which means that export
templates cannot be tested currently.

Running tests
-------------

Before tests can be actually run, the engine must be compiled with the ``tests``
build option enabled (and any other build option you typically use), as the
tests are not compiled as part of the engine by default:

.. code-block:: shell

    scons tests=yes

Once the build is done, run the tests with a ``--test`` command-line option:

.. code-block:: shell

    ./bin/<godot_binary> --test

The test run can be configured with the various doctest-specific command-line
options. To retrieve the full list of supported options, run the ``--test``
command with the ``--help`` option:

.. code-block:: shell

    ./bin/<godot_binary> --test --help

Any other options and arguments after the ``--test`` command are treated as
arguments for doctest.

.. note::

    Tests are compiled automatically if you use the ``dev_mode=yes`` SCons option.
    ``dev_mode=yes`` is recommended if you plan on contributing to the engine
    development as it will automatically treat compilation warnings as errors.
    The continuous integration system will fail if any compilation warnings are
    detected, so you should strive to fix all warnings before opening a pull
    request.

Filtering tests
~~~~~~~~~~~~~~~

By default, all tests are run if you don't supply any extra arguments after the
``--test`` command. But if you're writing new tests or would like to see the
successful assertions output coming from those tests for debugging purposes, you
can run the tests of interest with the various filtering options provided by
doctest.

The wildcard syntax ``*`` is supported for matching any number of characters in
test suites, test cases, and source file names:

+--------------------+---------------+------------------------+
| **Filter options** | **Shorthand** | **Examples**           |
+--------------------+---------------+------------------------+
| ``--test-suite``   | ``-ts``       | ``-ts="*[GDScript]*"`` |
+--------------------+---------------+------------------------+
| ``--test-case``    | ``-tc``       | ``-tc="*[String]*"``   |
+--------------------+---------------+------------------------+
| ``--source-file``  | ``-sf``       | ``-sf="*test_color*"`` |
+--------------------+---------------+------------------------+

For instance, to run only the ``String`` unit tests, run:

.. code-block:: shell

    ./bin/<godot_binary> --test --test-case="*[String]*"

Successful assertions output can be enabled with the ``--success`` (``-s``)
option, and can be combined with any combination of filtering options above,
for instance:

.. code-block:: shell

    ./bin/<godot_binary> --test --source-file="*test_color*" --success

Specific tests can be skipped with corresponding ``-exclude`` options. As of
now, some tests include random stress tests which take a while to execute. In
order to skip those kind of tests, run the following command:

.. code-block:: shell

    ./bin/<godot_binary> --test --test-case-exclude="*[Stress]*"

Writing tests
-------------

Test suites represent C++ header files which must be included as part of the
main test entry point in ``tests/test_main.cpp``. Most test suites are located
directly under ``tests/`` directory.

All header files are prefixed with ``test_``, and this is a naming convention
which the Godot build system relies on to detect tests throughout the engine.

Here's a minimal working test suite with a single test case written:

.. code-block:: cpp

    #pragma once

    #include "tests/test_macros.h"

    namespace TestString {

    TEST_CASE("[String] Hello World!") {
        String hello = "Hello World!";
        CHECK(hello == "Hello World!");
    }

    } // namespace TestString

.. note::
    You can quickly generate new tests using the ``create_test.py`` script found in the ``tests/`` directory.
    This script automatically creates a new test file with the required boilerplate code in the appropriate location.
    It's also able to automatically include the new header in ``tests/test_main.cpp`` using invasive mode (``-i`` flag).
    To view usage instructions, run the script with the ``-h`` flag.

The ``tests/test_macros.h`` header encapsulates everything which is needed for
writing C++ unit tests in Godot. It includes doctest assertion and logging
macros such as ``CHECK`` as seen above, and of course the definitions for
writing test cases themselves.

.. seealso::

    `tests/test_macros.h <https://github.com/godotengine/godot/blob/master/tests/test_macros.h>`_
    source code for currently implemented macros and aliases for them.

Test cases are created using ``TEST_CASE`` function-like macro. Each test case
must have a brief description written in parentheses, optionally including
custom tags which allow to filter the tests at runtime, such as ``[String]``,
``[Stress]`` etc.

Test cases are written in a dedicated namespace. This is not required, but
allows to prevent naming collisions for when other static helper functions are
written to accommodate the repeating testing procedures such as populating
common test data for each test, or writing parameterized tests.

Godot supports writing tests per C++ module. For instructions on how to write
module tests, refer to :ref:`doc_custom_module_unit_tests`.

Subcases
~~~~~~~~

In situations where you have a common setup for several test cases with only slight variations, subcases can be very helpful. Here's an example:

.. code-block:: cpp

    TEST_CASE("[SceneTree][Node] Testing node operations with a very simple scene tree") {
        // ... common setup (e.g. creating a scene tree with a few nodes)
        SUBCASE("Move node to specific index") {
            // ... setup and checks for moving a node
        }
        SUBCASE("Remove node at specific index") {
            // ... setup and checks for removing a node
        }
    }

Each ``SUBCASE`` causes the ``TEST_CASE`` to be executed from the beginning.
Subcases can be nested to an arbitrary depth, but it is advised to limit nesting to no more than one level deep.

Assertions
~~~~~~~~~~

A list of all commonly used assertions used throughout the Godot tests, sorted
by severity.

+-------------------+----------------------------------------------------------------------------------------------------------------------------------+
| **Assertion**     | **Description**                                                                                                                  |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``REQUIRE``       | Test if condition holds true. Fails the entire test immediately if the condition does not hold true.                             |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``REQUIRE_FALSE`` | Test if condition does not hold true. Fails the entire test immediately if the condition holds true.                             |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``CHECK``         | Test if condition holds true. Marks the test run as failing, but allow to run other assertions.                                  |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``CHECK_FALSE``   | Test if condition does not hold true. Marks the test run as failing, but allow to run other assertions.                          |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``WARN``          | Test if condition holds true. Does not fail the test under any circumstance, but logs a warning if something does not hold true. |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``WARN_FALSE``    | Test if condition does not hold true. Does not fail the test under any circumstance, but logs a warning if something holds true. |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------+

All of the above assertions have corresponding ``*_MESSAGE`` macros, which allow
to print optional message with rationale of what should happen.

Prefer to use ``CHECK`` for self-explanatory assertions and ``CHECK_MESSAGE``
for more complex ones if you think that it deserves a better explanation.

.. seealso::

    `doctest: Assertion macros <https://github.com/doctest/doctest/blob/master/doc/markdown/assertions.md>`_.

Logging
~~~~~~~

The test output is handled by doctest itself, and does not rely on Godot
printing or logging functionality at all, so it's recommended to use dedicated
macros which allow to log test output in a format written by doctest.

+----------------+-----------------------------------------------------------------------------------------------------------+
| **Macro**      | **Description**                                                                                           |
+----------------+-----------------------------------------------------------------------------------------------------------+
| ``MESSAGE``    | Prints a message.                                                                                         |
+----------------+-----------------------------------------------------------------------------------------------------------+
| ``FAIL_CHECK`` | Marks the test as failing, but continue the execution. Can be wrapped in conditionals for complex checks. |
+----------------+-----------------------------------------------------------------------------------------------------------+
| ``FAIL``       | Fails the test immediately. Can be wrapped in conditionals for complex checks.                            |
+----------------+-----------------------------------------------------------------------------------------------------------+

Different reporters can be chosen at runtime. For instance, here's how the
output can be redirected to an XML file:

.. code-block:: shell

    ./bin/<godot_binary> --test --source-file="*test_validate*" --success --reporters=xml --out=doctest.txt

.. seealso::

    `doctest: Logging macros <https://github.com/doctest/doctest/blob/master/doc/markdown/logging.md>`_.

Testing failure paths
~~~~~~~~~~~~~~~~~~~~~

Sometimes, it's not always feasible to test for an *expected* result. With the
Godot development philosophy of that the engine should not crash and should
gracefully recover whenever a non-fatal error occurs, it's important to check
that those failure paths are indeed safe to execute without crashing the engine.

*Unexpected* behavior can be tested in the same way as anything else. The only
problem this creates is that the error printing shall unnecessarily pollute the
test output with errors coming from the engine itself (even if the end result is
successful).

To alleviate this problem, use ``ERR_PRINT_OFF`` and ``ERR_PRINT_ON`` macros
directly within test cases to temporarily disable the error output coming from
the engine, for instance:

.. code-block:: cpp

    TEST_CASE("[Color] Constructor methods") {
        ERR_PRINT_OFF;
        Color html_invalid = Color::html("invalid");
        ERR_PRINT_ON; // Don't forget to re-enable!

        CHECK_MESSAGE(html_invalid.is_equal_approx(Color()),
            "Invalid HTML notation should result in a Color with the default values.");
    }

Special tags in test case names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These tags can be added to the test case name to modify or extend the test environment:

+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Tag**            | **Description**                                                                                                                                                      |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``[SceneTree]``    | Required for test cases that rely on a scene tree with MessageQueue to be available. It also enables a mock rendering server and :ref:`ThemeDB<class_ThemeDB>`.      |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``[Editor]``       | Like ``[SceneTree]``, but with additional editor-related infrastructure available, such as :ref:`EditorSettings<class_EditorSettings>`.                              |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``[Audio]``        | Initializes the :ref:`AudioServer<class_AudioServer>` using a mock audio driver.                                                                                     |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``[Navigation2D]`` | Creates the default 2D navigation server and makes it available for testing.                                                                                         |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``[Navigation3D]`` | Creates the default 3D navigation server and makes it available for testing.                                                                                         |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

You can use them together to combine multiple test environment extensions.

Testing signals
~~~~~~~~~~~~~~~

The following macros can be use to test signals:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Macro
     - Description
   * - ``SIGNAL_WATCH(object, "signal_name")``
     - Starts watching the specified signal on the given object.
   * - ``SIGNAL_UNWATCH(object, "signal_name")``
     - Stops watching the specified signal on the given object.
   * - ``SIGNAL_CHECK("signal_name", Vector<Vector<Variant>>)``
     - Checks the arguments of all fired signals. The outer vector contains each fired signal, while the inner vector contains the list of arguments for that signal. The order of signals is significant.
   * - ``SIGNAL_CHECK_FALSE("signal_name")``
     - Checks if the specified signal was not fired.
   * - ``SIGNAL_DISCARD("signal_name")``
     - Discards all records of the specified signal.

Below is an example demonstrating the use of these macros:

.. code-block:: cpp

    //...
    SUBCASE("[Timer] Timer process timeout signal must be emitted") {
        SIGNAL_WATCH(test_timer, SNAME("timeout"));
        test_timer->start(0.1);

        SceneTree::get_singleton()->process(0.2);

        Array signal_args;
        signal_args.push_back(Array());

        SIGNAL_CHECK(SNAME("timeout"), signal_args);

        SIGNAL_UNWATCH(test_timer, SNAME("timeout"));
    }
    //...

Test tools
----------

Test tools are advanced methods which allow you to run arbitrary procedures to
facilitate the process of manual testing and debugging the engine internals.

These tools can be run by supplying the name of a tool after the ``--test``
command-line option. For instance, the GDScript module implements and registers
several tools to help the debugging of the tokenizer, parser, and compiler:

.. code-block:: shell

    ./bin/<godot_binary> --test gdscript-tokenizer test.gd
    ./bin/<godot_binary> --test gdscript-parser test.gd
    ./bin/<godot_binary> --test gdscript-compiler test.gd

If any such tool is detected, then the rest of the unit tests are skipped.

Test tools can be registered anywhere throughout the engine as the registering
mechanism closely resembles of what doctest provides while registering test
cases using dynamic initialization technique, but usually these can be
registered at corresponding ``register_types.cpp`` sources (per module or core).

Here's an example of how GDScript registers test tools in
``modules/gdscript/register_types.cpp``:

.. code-block:: cpp

    #ifdef TESTS_ENABLED
    void test_tokenizer() {
        TestGDScript::test(TestGDScript::TestType::TEST_TOKENIZER);
    }

    void test_parser() {
        TestGDScript::test(TestGDScript::TestType::TEST_PARSER);
    }

    void test_compiler() {
        TestGDScript::test(TestGDScript::TestType::TEST_COMPILER);
    }

    REGISTER_TEST_COMMAND("gdscript-tokenizer", &test_tokenizer);
    REGISTER_TEST_COMMAND("gdscript-parser", &test_parser);
    REGISTER_TEST_COMMAND("gdscript-compiler", &test_compiler);
    #endif

The custom command-line parsing can be performed by a test tool itself with the
help of OS :ref:`get_cmdline_args<class_OS_method_get_cmdline_args>` method.

Integration tests for GDScript
------------------------------

Godot uses doctest to prevent regressions in GDScript during development. There
are several types of test scripts which can be written:

- tests for expected errors;
- tests for warnings;
- tests for features.

Therefore, the process of writing integration tests for GDScript is the following:

1. Pick a type of a test script you'd like to write, and create a new GDScript
   file under the ``modules/gdscript/tests/scripts`` directory within
   corresponding sub-directory.

2. Write GDScript code. The test script must have a function called ``test()``
   which takes no arguments. Such function will be called by the test runner.
   The test should not have any dependency unless it's part of the test too.
   Global classes (using ``class_name``) are registered before the runner
   starts, so those should work if needed.

   Here's an example test script:

   ::

        func test():
            if true # Missing colon here.
                print("true")

3. Change directory to the Godot source repository root.

   .. code-block:: shell

       cd godot

4. Generate ``*.out`` files to update the expected results from the output:

   .. code-block:: shell

       bin/<godot_binary> --gdscript-generate-tests modules/gdscript/tests/scripts

You may add the ``--print-filenames`` option to see filenames as their test
outputs are generated. If you are working on a new feature that is causing
hard crashes, you can use this option to quickly find which test file causes
the crash and debug from there.

5. Run GDScript tests with:

   .. code-block:: shell

       ./bin/<godot_binary> --test --test-suite="*GDScript*"

This also accepts the ``--print-filenames`` option (see above).

If no errors are printed and everything goes well, you're done!

.. warning::

    Make sure the output does have the expected values before submitting a pull
    request. If ``--gdscript-generate-tests`` produces ``*.out`` files which are
    unrelated to newly added tests, you should revert those files back and
    only commit ``*.out`` files for new tests.

.. note::

    The GDScript test runner is meant for testing the GDScript implementation,
    not for testing user scripts nor testing the engine using scripts. We
    recommend writing new tests for already resolved
    `issues related to GDScript at GitHub <https://github.com/godotengine/godot/issues?q=is%3Aissue+label%3Atopic%3Agdscript+is%3Aclosed>`_,
    or writing tests for currently working features.

.. note::

    If your test case requires that there is no ``test()``
    function present inside the script file,
    you can disable the runtime section of the test by naming the script file so that it matches the pattern ``*.notest.gd``.
    For example, "test_empty_file.notest.gd".
