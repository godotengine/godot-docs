.. _doc_android_in_app_purchases:

Android in-app purchases
========================

Godot offers a first-party ``GodotGooglePlayBilling`` Android plugin compatible with Godot 4.2+ which uses the `Google Play Billing library <https://developer.android.com/google/play/billing>`_.


Usage
-----

Getting started
~~~~~~~~~~~~~~~

Make sure you have enabled and successfully set up :ref:`Android Gradle Builds <doc_android_gradle_build>`.
Follow the installation instructions on the ``GodotGooglePlayBilling`` `github page <https://github.com/godotengine/godot-google-play-billing>`__.


Initialize the plugin
~~~~~~~~~~~~~~~~~~~~~

To use the ``GodotGooglePlayBilling`` API:

1. Access the ``BillingClient``.
2. Connect to its signals to receive billing results.
3. Call ``start_connection``.

Initialization example:

::

    var billing_client: BillingClient
    func _ready():
        billing_client = BillingClient.new()
        billing_client.connected.connect(_on_connected) # No params
        billing_client.disconnected.connect(_on_disconnected) # No params
        billing_client.connect_error.connect(_on_connect_error) # response_code: int, debug_message: String
        billing_client.query_product_details_response.connect(_on_query_product_details_response) # response: Dictionary
        billing_client.query_purchases_response.connect(_on_query_purchases_response) # response: Dictionary
        billing_client.on_purchase_updated.connect(_on_purchase_updated) # response: Dictionary
        billing_client.consume_purchase_response.connect(_on_consume_purchase_response) # response: Dictionary
        billing_client.acknowledge_purchase_response.connect(_on_acknowledge_purchase_response) # response: Dictionary

        billing_client.start_connection()

The API must be in a connected state prior to use. The ``connected`` signal is sent
when the connection process succeeds. You can also use ``is_ready()`` to determine if the plugin
is ready for use. The ``get_connection_state()`` function returns the current connection state
of the plugin. 

Return values for ``get_connection_state()``:

::

    # Matches BillingClient.ConnectionState in the Play Billing Library.
    # Access in your script as: BillingClient.ConnectionState.CONNECTED
    enum ConnectionState {
    	DISCONNECTED, # This client was not yet connected to billing service or was already closed.
    	CONNECTING, # This client is currently in process of connecting to billing service.
    	CONNECTED, # This client is currently connected to billing service.
    	CLOSED, # This client was already closed and shouldn't be used again.
    }


Query available items
~~~~~~~~~~~~~~~~~~~~~

Once the API has connected, query product IDs using `query_product_details()`. You must successfully complete
a product details query before calling the ``purchase()``, ``purchase_subscription()``, or ``update_subscription()`` functions,
or they will return an error. ``query_product_details()`` takes two parameters: an array
of product ID strings and the type of product being queried.
The product type should be ``BillingClient.ProductType.INAPP`` for normal in-app purchases or ``BillingClient.ProductType.SUBS`` for subscriptions.
The ID strings in the array should match the product IDs defined in the Google Play Console entry
for your app.

Example use of ``query_product_details()``:

::

    func _on_connected():
      billing_client.query_product_details(["my_iap_item"], BillingClient.ProductType.INAPP) # BillingClient.ProductType.SUBS for subscriptions.

    func _on_query_product_details_response(query_result: Dictionary):
        if query_result.response_code == BillingClient.BillingResponseCode.OK:
            print("Product details query success")
            for available_product in query_result.product_details:
                print(available_product)
        else:
            print("Product details query failed")
            print("response_code: ", query_result.response_code, "debug_message: ", query_result.debug_message)


Query user purchases
~~~~~~~~~~~~~~~~~~~~

To retrieve a user's purchases, call the ``query_purchases()`` function passing
a product type to query. The product type should be
``BillingClient.ProductType.INAPP`` for normal in-app purchases or ``BillingClient.ProductType.SUBS`` for subscriptions.
The ``query_purchases_response`` signal is sent with the result.
The signal has a single parameter: a :ref:`Dictionary <class_Dictionary>` with
a response code and either an array of purchases or a debug message.
Only active subscriptions and non-consumed one-time purchases are
included in the purchase array.

Example use of ``query_purchases()``:

::

    func _query_purchases():
        billing_client.query_purchases(BillingClient.ProductType.INAPP) # Or BillingClient.ProductType.SUBS for subscriptions.

    func _on_query_purchases_response(query_result: Dictionary):
        if query_result.response_code == BillingClient.BillingResponseCode.OK:
            print("Purchase query success")
            for purchase in query_result.purchases:
                _process_purchase(purchase)
        else:
            print("Purchase query failed")
            print("response_code: ", query_result.response_code, "debug_message: ", query_result.debug_message)


Purchase an item
~~~~~~~~~~~~~~~~

To launch the billing flow for an item: Use ``purchase()`` for in-app products, passing the product ID string.
Use ``purchase_subscription()`` for subscriptions, passing the product ID and base plan ID. You may also optionally provide an offer ID.

For both ``purchase()`` and ``purchase_subscription()``, you can optionally pass a boolean to indicate whether
offers are `personallised <https://developer.android.com/google/play/billing/integrate#personalized-price>`_

Reminder: you **must** query the product details for an item before you can
pass it to ``purchase()``.
This method returns a dictionary indicating whether the billing flow was successfully launched.
It includes a response code and either an array of purchases or a debug message.

Example use of ``purchase()``:

::

    var result = billing_client.purchase("my_iap_item")
    if result.response_code == BillingClient.BillingResponseCode.OK:
        print("Billing flow launch success")
    else:
        print("Billing flow launch failed")
        print("response_code: ", result.response_code, "debug_message: ", result.debug_message)


The result of the purchase will be sent through the ``on_purchases_updated`` signal.

::

    func _on_purchases_updated(result: Dictionary):
        if result.response_code == BillingClient.BillingResponseCode.OK:
            print("Purchase update received")
            for purchase in result.purchases:
                _process_purchase(purchase)
        else:
            print("Purchase update error")
            print("response_code: ", result.response_code, "debug_message: ", result.debug_message)


Processing a purchase item
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``query_purchases_response`` and ``on_purchases_updated`` signals provide an array
of purchases in :ref:`Dictionary <class_Dictionary>` format. The purchase Dictionary
includes keys that map to values of the Google Play Billing
`Purchase <https://developer.android.com/reference/com/android/billingclient/api/Purchase>`_ class.

Purchase fields:

::

    order_id: String
    purchase_token: String
    package_name: String
    purchase_state: int
    purchase_time: int (milliseconds since the epoch (Jan 1, 1970))
    original_json: String
    is_acknowledged: bool
    is_auto_renewing: bool
    quantity: int
    signature: String
    product_ids: PackedStringArray


Check purchase state
~~~~~~~~~~~~~~~~~~~~

Check the ``purchase_state`` value of a purchase to determine if a
purchase was completed or is still pending.

PurchaseState values:

::

    # Matches Purchase.PurchaseState in the Play Billing Library
    # Access in your script as: BillingClient.PurchaseState.PURCHASED
    enum PurchaseState {
        UNSPECIFIED,
        PURCHASED,
        PENDING,
    }


If a purchase is in a ``PENDING`` state, you should not award the contents of the
purchase or do any further processing of the purchase until it reaches the
``PURCHASED`` state. If you have a store interface, you may wish to display
information about pending purchases needing to be completed in the Google Play Store.
For more details on pending purchases, see
`Handling pending transactions <https://developer.android.com/google/play/billing/integrate#pending>`_
in the Google Play Billing Library documentation.


Consumables
~~~~~~~~~~~

If your in-app item is not a one-time purchase but a consumable item (e.g. coins) which can be purchased
multiple times, you can consume an item by calling ``consume_purchase()`` passing
the ``purchase_token`` value from the purchase dictionary.
Calling ``consume_purchase()`` automatically acknowledges a purchase.
Consuming a product allows the user to purchase it again, it will no longer appear
in subsequent ``query_purchases()`` calls unless it is repurchased.

Example use of ``consume_purchase()``:

::

    func _process_purchase(purchase):
        if "my_consumable_iap_item" in purchase.product_ids and purchase.purchase_state == BillingClient.PurchaseState.PURCHASED:
            # Add code to store payment so we can reconcile the purchase token
            # in the completion callback against the original purchase
            billing_client.consume_purchase(purchase.purchase_token)

    func _on_consume_purchase_response(result: Dictionary):
        if result.response_code == BillingClient.BillingResponseCode.OK:
            print("Consume purchase success")
            _handle_purchase_token(result.token, true)
        else:
            print("Consume purchase failed")
            print("response_code: ", result.response_code, "debug_message: ", result.debug_message, "purchase_token: ", result.token)

    # Find the product associated with the purchase token and award the
    # product if successful
    func _handle_purchase_token(purchase_token, purchase_successful):
        # check/award logic, remove purchase from tracking list


Acknowledging purchases
~~~~~~~~~~~~~~~~~~~~~~~

If your in-app item is a one-time purchase, you must acknowledge the purchase by
calling the ``acknowledge_purchase()`` function, passing the ``purchase_token``
value from the purchase dictionary. If you do not acknowledge a purchase within
three days, the user automatically receives a refund, and Google Play revokes the purchase.
If you are calling ``comsume_purchase()`` it automatically acknowledges the purchase and
you do not need to call ``acknowledge_purchase()``.

Example use of ``acknowledge_purchase()``:

::

    func _process_purchase(purchase):
        if "my_one_time_iap_item" in purchase.product_ids and \
                purchase.purchase_state == BillingClient.PurchaseState.PURCHASED and \
                not purchase.is_acknowledged:
            # Add code to store payment so we can reconcile the purchase token
            # in the completion callback against the original purchase
            billing_client.acknowledge_purchase(purchase.purchase_token)

    func _on_acknowledge_purchase_response(result: Dictionary):
        if result.response_code == BillingClient.BillingResponseCode.OK:
            print("Acknowledge purchase success")
            _handle_purchase_token(result.token, true)
        else:
            print("Acknowledge purchase failed")
            print("response_code: ", result.response_code, "debug_message: ", result.debug_message, "purchase_token: ", result.token)

    # Find the product associated with the purchase token and award the
    # product if successful
    func _handle_purchase_token(purchase_token, purchase_successful):
        # check/award logic, remove purchase from tracking list


Subscriptions
~~~~~~~~~~~~~

Subscriptions work mostly like regular in-app items. Use ``BillingClient.ProductType.SUBS`` as the second
argument to ``query_product_details()`` to get subscription details. Pass ``BillingClient.ProductType.SUBS``
to ``query_purchases()`` to get subscription purchase details.

You can check ``is_auto_renewing`` in the a subscription purchase
returned from ``query_purchases()`` to see if a user has cancelled an
auto-renewing subscription.

You need to acknowledge new subscription purchases, but not automatic
subscription renewals.

If you support upgrading or downgrading between different subscription levels,
you should use ``update_subscription()`` to use the subscription update flow to
change an active subscription. Like ``purchase()``, results are returned by the
``on_purchases_updated`` signal.
These are the parameters of ``update_subscription()``:

1. old_purchase_token: The purchase token of the currently active subscription
2. replacement_mode: The replacement mode to apply to the subscription
3. product_id: The product ID of the new subscription to switch to
4. base_plan_id: The base plan ID of the target subscription
5. offer_id: The offer ID under the base plan (optional)
6. is_offer_personalized: Whether to enable personalized pricing (optional)

The replacement modes values are defined as:

::

    # Access in your script as: BillingClient.ReplacementMode.WITH_TIME_PRORATION
    enum ReplacementMode {
    	# Unknown...
    	UNKNOWN_REPLACEMENT_MODE = 0,

    	# The new plan takes effect immediately, and the remaining time will be prorated and credited to the user.
    	# Note: This is the default behavior.
    	WITH_TIME_PRORATION = 1,

    	# The new plan takes effect immediately, and the billing cycle remains the same.
    	CHARGE_PRORATED_PRICE = 2,

    	# The new plan takes effect immediately, and the new price will be charged on next recurrence time.
    	WITHOUT_PRORATION = 3,

    	# Replacement takes effect immediately, and the user is charged full price of new plan and
    	# is given a full billing cycle of subscription, plus remaining prorated time from the old plan.
    	CHARGE_FULL_PRICE = 5,

    	# The new purchase takes effect immediately, the new plan will take effect when the old item expires.
    	DEFERRED = 6,
    }


Default behavior is ``WITH_TIME_PRORATION``.

Example use of ``update_subscription``:

::

    billing_client.update_subscription(_active_subscription_purchase.purchase_token, \
                        BillingClient.ReplacementMode.WITH_TIME_PRORATION, "new_sub_product_id", "base_plan_id")

