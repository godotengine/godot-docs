.. _doc_making_calls_to_a_rest_api:

Making calls to a REST API
==========================

For the sake of example, we will create a simple UI with a button, that when pressed, it will start the request to the specified URL. To make the request, we will make use of the HTTPRequest node.

Preparing scene
---------------

Create a new empty scene, add a CanvasLayer as the root node, and add an script to it. Then add two child nodes to it; a Button, and an HTTPRequest node. You will need to connect the following signals to the CanvasLayer script.

- Button.pressed: When the button is pressed, we will start the request.
- HTTPRequest.request_completed: When the request is completed, we will get the requested data as an argument.

.. image:: img/rest_api_scene.png

Scripting
---------
This is all the code we need to make it work. The URL, is an online RestAPI mocker; it returns a json string, which we will then parse to get access to the data.

::

    extends CanvasLayer

    func _ready():
    	pass

    func _on_Button_pressed():
    	$HTTPRequest.request("http://www.mocky.io/v2/5185415ba171ea3a00704eed")

    func _on_HTTPRequest_request_completed( result, response_code, headers, body ):
    	var json = JSON.parse(body.get_string_from_utf8())
    	print(json.result)

With this, you should see ``(hello:world)`` printed on the console; hello being a key, and world being a value, both of them strings.
