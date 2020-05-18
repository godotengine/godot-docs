.. _doc_custom_visualscript_nodes:

Custom VisualScript nodes
=========================

Custom nodes are written in GDScript and can then be used in VisualScript.
This is useful for offloading complex code to GDScript and reusing it.

Creating a custom node
----------------------

Create a new script that extends :ref:`class_VisualScriptCustomNode` and put a ``tool`` keyword at the top. This is needed for the script to run in the editor.

There are some functions that can be implemented to set parameters of the custom node.
Only add functions that are needed, a ``_has_input_sequence_port`` function is not necessary if it should return ``false`` for example.

The most important part of a custom node is the ``_step`` function. The logic of the node is defined there.

The ``inputs`` parameter holds the value of the input ports.

The ``outputs`` parameter is an array where the indices represent the output port ids. It can be modified to set the values of the output ports.

``start_mode`` can be checked to see if it is the first time ``_step`` is called.

``working_mem`` is persistent each ``_step`` call. It can be used to store information.

If you want to throw an error, for example if the input types are incorrect, you can return the error message as a string.
When everything goes right, return the id of the sequence port which should be called next. If your custom node doesn't have any, just return 0.


Example:

::

    tool
    extends VisualScriptCustomNode

    # The name of the custom node as it appears in the search.
    func _get_caption():
        return "Get Input Direction 2D"

    func _get_category():
        return "Input"

    # The text displayed after the input port / sequence arrow.
    func _get_text():
        return ""

    func _get_input_value_port_count():
        return 0

    # The types of the inputs per index starting from 0.
    func _get_input_value_port_type(idx):
        return TYPE_OBJECT

    func _get_output_value_port_count():
        return 1

    # The types of outputs per index starting from 0.
    func _get_output_value_port_type(idx):
        return TYPE_VECTOR2

    # The text displayed before each output node per index.
    func _get_output_value_port_name(idx):
        return "Direction"

    func _has_input_sequence_port():
        return true

    # The number of output sequence ports to use
    # (has to be at least one if you have an input sequence port).
    func _get_output_sequence_port_count():
        return 1

    func _step(inputs, outputs, start_mode, working_mem):
        # start_mode can be checked to see if it is the first time _step is called.
        # This is useful if you only want to do an operation once.

        # working_memory is persistent between _step calls.

        # The inputs array contains the value of the input ports.

        var x = int(Input.is_action_pressed("ui_right")) - int(Input.is_action_pressed("ui_left"))
        var y = int(Input.is_action_pressed("ui_down")) - int(Input.is_action_pressed("ui_up"))

        # The outputs array is used to set the data of the output ports.

        outputs[0] = Vector2(x, y)

        # Return the error string if an error occurred, else the id of the next sequence port.
        return 0

Using a custom node
-------------------

To use the script, add a ``CustomNode``, select it and drag your custom node script into the ``script`` property shown in the inspector.

.. image:: img/visual_script_custom_node_set_script.png

Result:

.. image:: img/visual_script_custom_node_result.png
