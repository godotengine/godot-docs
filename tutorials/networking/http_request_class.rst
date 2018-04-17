.. _doc_http_request_class:

Making HTTP requests
====================

The :ref:`HTTPRequest <class_HTTPRequest>` node is the easiest way to make HTTP requests in Godot.
It is backed by the more low-level :ref:`HTTPClient <class_HTTPClient>`, for which a tutorial is available :ref:`here <doc_http_client_class>`.

For the sake of this example, we will create a simple UI with a button, that when pressed will start the HTTP request to the specified URL.

Preparing scene
---------------

Create a new empty scene, add a CanvasLayer as the root node and add an script to it. Then add two child nodes to it: a Button and an HTTPRequest node. You will need to connect the following signals to the CanvasLayer script:

- Button.pressed: When the button is pressed, we will start the request.
- HTTPRequest.request_completed: When the request is completed, we will get the requested data as an argument.

.. image:: img/rest_api_scene.png

Scripting
---------

Below is all the code we need to make it work. The URL points to an online API mocker; it returns a pre-defined JSON string, which we will then parse to get access to the data.

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

For more information on parsing JSON, see the class references for :ref:`JSON <class_JSON>` and :ref:`JSONParseResult <class_JSONParseResult>`.

Note that you may want to check whether the ``result`` equals ``RESULT_SUCCESS`` and whether a JSON parsing error occurred, see the JSON class reference and :ref:`HTTPRequest <class_HTTPRequest>` for more.

Sending data to server
----------------------

Until now we have limited ourselves to requesting data from a server. But what if you need to send data to the server? Here is a common way of doing it:

::

    func _make_post_request(url, data_to_send, use_ssl):
        # Convert data to json string:
        var query = JSON.print(data_to_send)
        # Add 'Content-Type' header:
        var headers = ["Content-Type: application/json"]
        $HTTPRequest.request(url, headers, use_ssl, HTTPClient.METHOD_POST, query)        

