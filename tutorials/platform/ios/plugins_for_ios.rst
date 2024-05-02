:article_outdated: True

.. _doc_plugins_for_ios:

Plugins for iOS
===============

Godot provides StoreKit, GameCenter, iCloud services and other plugins.
They are using same model of asynchronous calls explained below.

ARKit and Camera access are also provided as plugins.

Latest updates, documentation and source code can be found at `Godot iOS plugins repository <https://github.com/godotengine/godot-ios-plugins>`_

Accessing plugin singletons
---------------------------

To access plugin functionality, you first need to check that the plugin is
exported and available by calling the `Engine.has_singleton()` function, which
returns a registered singleton.

Here's an example of how to do this in GDScript:

::

    var in_app_store
    var game_center

    func _ready():
        if Engine.has_singleton("InAppStore"):
            in_app_store = Engine.get_singleton("InAppStore")
        else:
            print("iOS IAP plugin is not available on this platform.")

        if Engine.has_singleton("GameCenter"):
            game_center = Engine.get_singleton("GameCenter")
        else:
            print("iOS Game Center plugin is not available on this platform.")


Asynchronous methods
--------------------

When requesting an asynchronous operation, the method will look like
this:

::

    Error purchase(Variant params);

The parameter will usually be a Dictionary, with the information
necessary to make the request, and the call will have two phases. First,
the method will immediately return an Error value. If the Error is not
'OK', the call operation is completed, with an error probably caused
locally (no internet connection, API incorrectly configured, etc). If
the error value is 'OK', a response event will be produced and added to
the 'pending events' queue. Example:

::

    func on_purchase_pressed():
        var result = in_app_store.purchase({ "product_id": "my_product" })
        if result == OK:
            animation.play("busy") # show the "waiting for response" animation
        else:
            show_error()

    # put this on a 1 second timer or something
    func check_events():
        while in_app_store.get_pending_event_count() > 0:
            var event = in_app_store.pop_pending_event()
            if event.type == "purchase":
                if event.result == "ok":
                    show_success(event.product_id)
                else:
                    show_error()

Remember that when a call returns OK, the API will *always* produce an
event through the pending_event interface, even if it's an error, or a
network timeout, etc. You should be able to, for example, safely block
the interface waiting for a reply from the server. If any of the APIs
don't behave this way it should be treated as a bug.

The pending event interface consists of two methods:

-  ``get_pending_event_count()``
   Returns the number of pending events on the queue.

-  ``Variant pop_pending_event()``
   Pops the first event from the queue and returns it.

Store Kit
---------

Implemented in `Godot iOS InAppStore plugin <https://github.com/godotengine/godot-ios-plugins/blob/master/plugins/inappstore/in_app_store.mm>`_.

The Store Kit API is accessible through the ``InAppStore`` singleton.
It is initialized automatically.

The following methods are available and documented below:

::

    Error purchase(Variant params)
    Error request_product_info(Variant params)
    Error restore_purchases()
    void set_auto_finish_transaction(bool enable)
    void finish_transaction(String product_id)

 and the pending events interface:

 ::

    int get_pending_event_count()
    Variant pop_pending_event()

``purchase``
~~~~~~~~~~~~

Purchases a product ID through the Store Kit API. You have to call ``finish_transaction(product_id)`` once you
receive a successful response or call ``set_auto_finish_transaction(true)`` prior to calling ``purchase()``.
These two methods ensure the transaction is completed.

Parameters
^^^^^^^^^^

Takes a dictionary as a parameter, with one field, ``product_id``, a
string with your product ID. Example:

::

    var result = in_app_store.purchase({ "product_id": "my_product" })

Response event
^^^^^^^^^^^^^^

The response event will be a dictionary with the following fields:

On error:

::

    {
      "type": "purchase",
      "result": "error",
      "product_id": "the product ID requested",
    }

On success:

::

    {
      "type": "purchase",
      "result": "ok",
      "product_id": "the product ID requested",
    }

``request_product_info``
~~~~~~~~~~~~~~~~~~~~~~~~

Requests the product info on a list of product IDs.

Parameters
^^^^^^^^^^

Takes a dictionary as a parameter, with a single ``product_ids`` key to which a
string array of product IDs is assigned. Example:

::

    var result = in_app_store.request_product_info({ "product_ids": ["my_product1", "my_product2"] })

Response event
^^^^^^^^^^^^^^

The response event will be a dictionary with the following fields:

::

    {
      "type": "product_info",
      "result": "ok",
      "invalid_ids": [ list of requested IDs that were invalid ],
      "ids": [ list of IDs that were valid ],
      "titles": [ list of valid product titles (corresponds with list of valid IDs) ],
      "descriptions": [ list of valid product descriptions ],
      "prices": [ list of valid product prices ],
      "localized_prices": [ list of valid product localized prices ],
    }

``restore_purchases``
~~~~~~~~~~~~~~~~~~~~~

Restores previously made purchases on user's account. This will create
response events for each previously purchased product ID.

Response event
^^^^^^^^^^^^^^

The response events will be dictionaries with the following fields:

::

    {
      "type": "restore",
      "result": "ok",
      "product_id": "product ID of restored purchase",
    }

``set_auto_finish_transaction``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If set to ``true``, once a purchase is successful, your purchase will be
finalized automatically. Call this method prior to calling ``purchase()``.

Parameters
^^^^^^^^^^

Takes a boolean as a parameter which specifies if purchases should be
automatically finalized. Example:

::

    in_app_store.set_auto_finish_transaction(true)

``finish_transaction``
~~~~~~~~~~~~~~~~~~~~~~

If you don't want transactions to be automatically finalized, call this
method after you receive a successful purchase response.


Parameters
^^^^^^^^^^

Takes a string ``product_id`` as an argument. ``product_id`` specifies what product to
finalize the purchase on. Example:

::

    in_app_store.finish_transaction("my_product1")

Game Center
-----------

Implemented in `Godot iOS GameCenter plugin <https://github.com/godotengine/godot-ios-plugins/blob/master/plugins/gamecenter/game_center.mm>`_.

The Game Center API is available through the ``GameCenter`` singleton. It
has the following methods:

::

    Error authenticate()
    bool is_authenticated()
    Error post_score(Variant score)
    Error award_achievement(Variant params)
    void reset_achievements()
    void request_achievements()
    void request_achievement_descriptions()
    Error show_game_center(Variant params)
    Error request_identity_verification_signature()

and the pending events interface:

::

    int get_pending_event_count()
    Variant pop_pending_event()

``authenticate``
~~~~~~~~~~~~~~~~

Authenticates a user in Game Center.

Response event
^^^^^^^^^^^^^^

The response event will be a dictionary with the following fields:

On error:

::

    {
      "type": "authentication",
      "result": "error",
      "error_code": the value from NSError::code,
      "error_description": the value from NSError::localizedDescription,
    }

On success:

::

    {
      "type": "authentication",
      "result": "ok",
      "player_id": the value from GKLocalPlayer::playerID,
    }

``post_score``
~~~~~~~~~~~~~~

Posts a score to a Game Center leaderboard.

Parameters
^^^^^^^^^^

Takes a dictionary as a parameter, with two fields:

-  ``score`` a float number
-  ``category`` a string with the category name

Example:

::

    var result = game_center.post_score({ "score": 100, "category": "my_leaderboard", })

Response event
^^^^^^^^^^^^^^

The response event will be a dictionary with the following fields:

On error:

::

    {
      "type": "post_score",
      "result": "error",
      "error_code": the value from NSError::code,
      "error_description": the value from NSError::localizedDescription,
    }

On success:

::

    {
      "type": "post_score",
      "result": "ok",
    }

``award_achievement``
~~~~~~~~~~~~~~~~~~~~~

Modifies the progress of a Game Center achievement.

Parameters
^^^^^^^^^^

Takes a Dictionary as a parameter, with 3 fields:

-  ``name`` (string) the achievement name
-  ``progress`` (float) the achievement progress from 0.0 to 100.0
   (passed to ``GKAchievement::percentComplete``)
-  ``show_completion_banner`` (bool) whether Game Center should display
   an achievement banner at the top of the screen

Example:

::

    var result = award_achievement({ "name": "hard_mode_completed", "progress": 6.1 })

Response event
^^^^^^^^^^^^^^

The response event will be a dictionary with the following fields:

On error:

::

    {
      "type": "award_achievement",
      "result": "error",
      "error_code": the error code taken from NSError::code,
    }

On success:

::

    {
      "type": "award_achievement",
      "result": "ok",
    }

``reset_achievements``
~~~~~~~~~~~~~~~~~~~~~~

Clears all Game Center achievements. The function takes no parameters.

Response event
^^^^^^^^^^^^^^

The response event will be a dictionary with the following fields:

On error:

::

    {
      "type": "reset_achievements",
      "result": "error",
      "error_code": the value from NSError::code,
    }

On success:

::

    {
      "type": "reset_achievements",
      "result": "ok",
    }

``request_achievements``
~~~~~~~~~~~~~~~~~~~~~~~~

Request all the Game Center achievements the player has made progress
on. The function takes no parameters.

Response event
^^^^^^^^^^^^^^

The response event will be a dictionary with the following fields:

On error:

::

    {
      "type": "achievements",
      "result": "error",
      "error_code": the value from NSError::code,
    }

On success:

::

    {
      "type": "achievements",
      "result": "ok",
      "names": [ list of the name of each achievement ],
      "progress": [ list of the progress made on each achievement ],
    }

``request_achievement_descriptions``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request the descriptions of all existing Game Center achievements
regardless of progress. The function takes no parameters.

Response event
^^^^^^^^^^^^^^

The response event will be a dictionary with the following fields:

On error:

::

    {
      "type": "achievement_descriptions",
      "result": "error",
      "error_code": the value from NSError::code,
    }

On success:

::

    {
      "type": "achievement_descriptions",
      "result": "ok",
      "names": [ list of the name of each achievement ],
      "titles": [ list of the title of each achievement ],
      "unachieved_descriptions": [ list of the description of each achievement when it is unachieved ],
      "achieved_descriptions": [ list of the description of each achievement when it is achieved ],
      "maximum_points": [ list of the points earned by completing each achievement ],
      "hidden": [ list of booleans indicating whether each achievement is initially visible ],
      "replayable": [ list of booleans indicating whether each achievement can be earned more than once ],
    }

``show_game_center``
~~~~~~~~~~~~~~~~~~~~

Displays the built in Game Center overlay showing leaderboards,
achievements, and challenges.

Parameters
^^^^^^^^^^

Takes a Dictionary as a parameter, with two fields:

-  ``view`` (string) (optional) the name of the view to present. Accepts
   "default", "leaderboards", "achievements", or "challenges". Defaults
   to "default".
-  ``leaderboard_name`` (string) (optional) the name of the leaderboard
   to present. Only used when "view" is "leaderboards" (or "default" is
   configured to show leaderboards). If not specified, Game Center will
   display the aggregate leaderboard.

Examples:

::

    var result = show_game_center({ "view": "leaderboards", "leaderboard_name": "best_time_leaderboard" })
    var result = show_game_center({ "view": "achievements" })

Response event
^^^^^^^^^^^^^^

The response event will be a dictionary with the following fields:

On close:

::

    {
      "type": "show_game_center",
      "result": "ok",
    }
