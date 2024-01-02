.. _doc_android_in_app_purchases:

Android in-app purchases
========================

Godot offers a first-party ``GodotGooglePlayBilling`` Android plugin compatible with Godot 4 which uses the `Google Play Billing library <https://developer.android.com/google/play/billing>`_.


Usage
-----

Getting started
***************

Make sure you have enabled and successfully set up :ref:`Android Gradle Builds <doc_android_gradle_build>`.
Follow the compiling instructions on the ``GodotGooglePlayBilling`` `github page <https://github.com/godotengine/godot-google-play-billing>`__.

Then put the files `./godot-google-play-billing/build/outputs/aar/GodotGooglePlayBilling.***.release.aar` and `./GodotGooglePlayBilling.gdap` into your project in the `res://android/plugins` folder.

The plugin should now show up in the Android export settings, where you can enable it.


Initialize the plugin
*********************

To use the ``GodotGooglePlayBilling`` API:

1. Obtain a reference to the ``GodotGooglePlayBilling`` singleton
2. Connect handlers for the plugin signals
3. Call ``startConnection``

Initialization example:

::

    var payment

    func _ready():
        if Engine.has_singleton("GodotGooglePlayBilling"):
            payment = Engine.get_singleton("GodotGooglePlayBilling")

            # These are all signals supported by the API
            # You can drop some of these based on your needs
            payment.billing_resume.connect(_on_billing_resume) # No params
            payment.connected.connect(_on_connected) # No params
            payment.disconnected.connect(_on_disconnected) # No params
            payment.connect_error.connect(_on_connect_error) # Response ID (int), Debug message (string)
            payment.price_change_acknowledged.connect(_on_price_acknowledged) # Response ID (int)
            payment.purchases_updated.connect(_on_purchases_updated) # Purchases (Dictionary[])
            payment.purchase_error.connect(_on_purchase_error) # Response ID (int), Debug message (string)
            payment.sku_details_query_completed.connect(_on_product_details_query_completed) # Products (Dictionary[])
            payment.sku_details_query_error.connect(_on_product_details_query_error) # Response ID (int), Debug message (string), Queried SKUs (string[])
            payment.purchase_acknowledged.connect(_on_purchase_acknowledged) # Purchase token (string)
            payment.purchase_acknowledgement_error.connect(_on_purchase_acknowledgement_error) # Response ID (int), Debug message (string), Purchase token (string)
            payment.purchase_consumed.connect(_on_purchase_consumed) # Purchase token (string)
            payment.purchase_consumption_error.connect(_on_purchase_consumption_error) # Response ID (int), Debug message (string), Purchase token (string)
            payment.query_purchases_response.connect(_on_query_purchases_response) # Purchases (Dictionary[])

            payment.startConnection()
        else:
            print("Android IAP support is not enabled. Make sure you have enabled 'Gradle Build' and the GodotGooglePlayBilling plugin in your Android export settings! IAP will not work.")

The API must be in a connected state prior to use. The ``connected`` signal is sent
when the connection process succeeds. You can also use ``isReady()`` to determine if the plugin
is ready for use. The ``getConnectionState()`` function returns the current connection state
of the plugin.

Return values for ``getConnectionState()``:

::

    # Matches BillingClient.ConnectionState in the Play Billing Library
    enum ConnectionState {
        DISCONNECTED, # not yet connected to billing service or was already closed
        CONNECTING, # currently in process of connecting to billing service
        CONNECTED, # currently connected to billing service
        CLOSED, # already closed and shouldn't be used again
    }


Query available items
*********************

Once the API has connected, query SKUs using ``querySkuDetails()``. You must successfully complete
a SKU query before calling the ``purchase()`` or ``queryPurchases()`` functions,
or they will return an error. ``querySkuDetails()`` takes two parameters: an array
of SKU name strings, and a string specifying the type of SKU being queried.
The SKU type string should be ``"inapp"`` for normal in-app purchases or ``"subs"`` for subscriptions.
The name strings in the array should match the SKU product ids defined in the Google Play Console entry
for your app.

Example use of ``querySkuDetails()``:

::

    func _on_connected():
      payment.querySkuDetails(["my_iap_item"], "inapp") # "subs" for subscriptions

    func _on_product_details_query_completed(product_details):
      for available_product in product_details:
        print(available_product)

    func _on_product_details_query_error(response_id, error_message, products_queried):
        print("on_product_details_query_error id:", response_id, " message: ",
                error_message, " products: ", products_queried)


Query user purchases
********************

To retrieve a user's purchases, call the ``queryPurchases()`` function passing
a string with the type of SKU to query. The SKU type string should be
``"inapp"`` for normal in-app purchases or ``"subs"`` for subscriptions.
The ``query_purchases_response`` signal is sent with the result.
The signal has a single parameter: a :ref:`Dictionary <class_Dictionary>` with
a status code and either an array of purchases or an error message.
Only active subscriptions and non-consumed one-time purchases are
included in the purchase array.

Example use of ``queryPurchases()``:

::

    func _query_purchases():
        payment.queryPurchases("inapp") # Or "subs" for subscriptions

    func _on_query_purchases_response(query_result):
        if query_result.status == OK:
            for purchase in query_result.purchases:
                _process_purchase(purchase)
        else:
            print("queryPurchases failed, response code: ",
                    query_result.response_code,
                    " debug message: ", query_result.debug_message)


You should query purchases during startup after successfully retrieving SKU details.
Since the user may make a purchase or resolve a pending transaction from
outside your app, you should recheck for purchases when resuming from the
background. To accomplish this, you can use the ``billing_resume`` signal.

Example use of ``billing_resume``:

::

    func _on_billing_resume():
        if payment.getConnectionState() == ConnectionState.CONNECTED:
            _query_purchases()


For more information on processing the purchase items returned by
``queryPurchases()``, see `Processing a purchase item`_


Purchase an item
****************

To initiate the purchase flow for an item, call ``purchase()`` passing the
product id string of the SKU you wish to purchase.
Reminder: you **must** query the SKU details for an item before you can
pass it to ``purchase()``.

Example use of ``purchase()``:

::

    payment.purchase("my_iap_item")


The payment flow will send a ``purchases_updated`` signal on success or a
``purchase_error`` signal on failure.

::

    func _on_purchases_updated(purchases):
        for purchase in purchases:
            _process_purchase(purchase)

    func _on_purchase_error(response_id, error_message):
        print("purchase_error id:", response_id, " message: ", error_message)


Processing a purchase item
**************************

The ``query_purchases_response`` and ``purchases_updated`` signals provide an array
of purchases in :ref:`Dictionary <class_Dictionary>` format. The purchase Dictionary
includes keys that map to values of the Google Play Billing
`Purchase <https://developer.android.com/reference/com/android/billingclient/api/Purchase>`_ class.

Purchase fields:

::

    dictionary.put("order_id", purchase.getOrderId());
    dictionary.put("package_name", purchase.getPackageName());
    dictionary.put("purchase_state", purchase.getPurchaseState());
    dictionary.put("purchase_time", purchase.getPurchaseTime());
    dictionary.put("purchase_token", purchase.getPurchaseToken());
    dictionary.put("quantity", purchase.getQuantity());
    dictionary.put("signature", purchase.getSignature());
    // PBL V4 replaced getSku with getSkus to support multi-sku purchases,
    // use the first entry for "sku" and generate an array for "skus"
    ArrayList<String> skus = purchase.getSkus();
    dictionary.put("sku", skus.get(0)); # Not available in plugin
    String[] skusArray = skus.toArray(new String[0]);
    dictionary.put("products", productsArray);
    dictionary.put("is_acknowledged", purchase.isAcknowledged());
    dictionary.put("is_auto_renewing", purchase.isAutoRenewing());


Check purchase state
********************

Check the ``purchase_state`` value of a purchase to determine if a
purchase was completed or is still pending.

PurchaseState values:

::

    # Matches Purchase.PurchaseState in the Play Billing Library
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
***********

If your in-app item is not a one-time purchase but a consumable item (e.g. coins) which can be purchased
multiple times, you can consume an item by calling ``consumePurchase()`` passing
the ``purchase_token`` value from the purchase dictionary.
Calling ``consumePurchase()`` automatically acknowledges a purchase.
Consuming a product allows the user to purchase it again, it will no longer appear
in subsequent ``queryPurchases()`` calls unless it is repurchased.

Example use of ``consumePurchase()``:

::

    func _process_purchase(purchase):
        if "my_consumable_iap_item" in purchase.products and purchase.purchase_state == PurchaseState.PURCHASED:
            # Add code to store payment so we can reconcile the purchase token
            # in the completion callback against the original purchase
            payment.consumePurchase(purchase.purchase_token)

    func _on_purchase_consumed(purchase_token):
        _handle_purchase_token(purchase_token, true)

    func _on_purchase_consumption_error(response_id, error_message, purchase_token):
        print("_on_purchase_consumption_error id:", response_id,
                " message: ", error_message)
        _handle_purchase_token(purchase_token, false)

    # Find the sku associated with the purchase token and award the
    # product if successful
    func _handle_purchase_token(purchase_token, purchase_successful):
        # check/award logic, remove purchase from tracking list


Acknowledging purchases
***********************

If your in-app item is a one-time purchase, you must acknowledge the purchase by
calling the ``acknowledgePurchase()`` function, passing the ``purchase_token``
value from the purchase dictionary. If you do not acknowledge a purchase within
three days, the user automatically receives a refund, and Google Play revokes the purchase.
If you are calling ``comsumePurchase()`` it automatically acknowledges the purchase and
you do not need to call ``acknowledgePurchase()``.

Example use of ``acknowledgePurchase()``:

::

    func _process_purchase(purchase):
        if "my_one_time_iap_item" in purchase.products and \
                purchase.purchase_state == PurchaseState.PURCHASED and \
                not purchase.is_acknowledged:
            # Add code to store payment so we can reconcile the purchase token
            # in the completion callback against the original purchase
            payment.acknowledgePurchase(purchase.purchase_token)

    func _on_purchase_acknowledged(purchase_token):
        _handle_purchase_token(purchase_token, true)

    func _on_purchase_acknowledgement_error(response_id, error_message, purchase_token):
        print("_on_purchase_acknowledgement_error id: ", response_id,
                " message: ", error_message)
        _handle_purchase_token(purchase_token, false)

    # Find the sku associated with the purchase token and award the
    # product if successful
    func _handle_purchase_token(purchase_token, purchase_successful):
        # check/award logic, remove purchase from tracking list


Subscriptions
*************

Subscriptions work mostly like regular in-app items. Use ``"subs"`` as the second
argument to ``querySkuDetails()`` to get subscription details. Pass ``"subs"``
to ``queryPurchases()`` to get subscription purchase details.

You can check ``is_auto_renewing`` in the a subscription purchase
returned from ``queryPurchases()`` to see if a user has cancelled an
auto-renewing subscription.

You need to acknowledge new subscription purchases, but not automatic
subscription renewals.

If you support upgrading or downgrading between different subscription levels,
you should use ``updateSubscription()`` to use the subscription update flow to
change an active subscription. Like ``purchase()``, results are returned by the
``purchases_updated`` and ``purchase_error`` signals.
There are three parameters to ``updateSubscription()``:

1. The purchase token of the currently active subscription
2. The product id string of the subscription SKU to change to
3. The proration mode to apply to the subscription.

The proration values are defined as:

::

    enum SubscriptionProrationMode {
        # Replacement takes effect immediately, and the remaining time
        # will be prorated and credited to the user.
        IMMEDIATE_WITH_TIME_PRORATION = 1,
        # Replacement takes effect immediately, and the billing cycle remains the same.
        # The price for the remaining period will be charged.
        # This option is only available for subscription upgrade.
        IMMEDIATE_AND_CHARGE_PRORATED_PRICE,
        # Replacement takes effect immediately, and the new price will be charged on
        # next recurrence time. The billing cycle stays the same.
        IMMEDIATE_WITHOUT_PRORATION,
        # Replacement takes effect when the old plan expires, and the new price
        # will be charged at the same time.
        DEFERRED,
        # Replacement takes effect immediately, and the user is charged full price
        # of new plan and is given a full billing cycle of subscription,
        # plus remaining prorated time from the old plan.
        IMMEDIATE_AND_CHARGE_FULL_PRICE,
    }


Default behavior is ``IMMEDIATE_WITH_TIME_PRORATION``.

Example use of ``updateSubscription``:

::

    payment.updateSubscription(_active_subscription_purchase.purchase_token, \
						"new_sub_sku", SubscriptionProrationMode.IMMEDIATE_WITH_TIME_PRORATION)


The ``confirmPriceChange()`` function can be used to launch price change confirmation flow
for a subscription. Pass the product id of the subscription SKU subject to the price change.
The result will be sent by the ``price_change_acknowledged`` signal.

Example use of ``confirmPriceChange()``:

::

    enum BillingResponse {SUCCESS = 0, CANCELLED = 1}

    func confirm_price_change(product_id):
        payment.confirmPriceChange(product_id)

    func _on_price_acknowledged(response_id):
        if response_id == BillingResponse.SUCCESS:
            print("price_change_accepted")
        elif response_id == BillingResponse.CANCELED:
            print("price_change_canceled")
