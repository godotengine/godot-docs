.. _doc_android_in_app_purchases:

Android in-app purchases
========================

Godot offers a first-party ``GodotGooglePlayBilling`` Android plugin since Godot 3.2.2.
The new plugin uses the `Google Play Billing library <https://developer.android.com/google/play/billing>`__
instead of the now deprecated AIDL IAP implementation.

If you learn better by looking at an example, you can find the demo project
`here <https://github.com/godotengine/godot-demo-projects/tree/3.5/mobile/android_iap>`__.


Migrating from Godot 3.2.1 and lower (GodotPaymentsV3)
------------------------------------------------------

The new ``GodotGooglePlayBilling`` API is not compatible with its predecessor ``GodotPaymentsV3``.

Changes
*******

- You need to enable the Custom Build option in your Android export settings and install
  the ``GodotGooglePlayBilling`` plugin manually (see below for details)
- All purchases have to be acknowledged by your app. This is a
  `requirement from Google <https://developer.android.com/google/play/billing/integrate#process>`__.
  Purchases that are not acknowledged by your app will be refunded.
- Support for subscriptions
- Signals (no polling or callback objects)


Usage
-----

Getting started
***************

If not already done, make sure you have enabled and successfully set up :ref:`Android Custom Builds <doc_android_custom_build>`.
Grab the``GodotGooglePlayBilling`` plugin binary and config from the `releases page <https://github.com/godotengine/godot-google-play-billing/releases>`__
and put both into `res://android/plugins`.
The plugin should now show up in the Android export settings, where you can enable it.


Getting started
***************

To use the ``GodotGooglePlayBilling`` API you first have to get the ``GodotGooglePlayBilling``
singleton and start the connection:

::

    var payment

    func _ready():
        if Engine.has_singleton("GodotGooglePlayBilling"):
            payment = Engine.get_singleton("GodotGooglePlayBilling")

            # These are all signals supported by the API
            # You can drop some of these based on your needs
            payment.connect("connected", self, "_on_connected") # No params
            payment.connect("disconnected", self, "_on_disconnected") # No params
            payment.connect("connect_error", self, "_on_connect_error") # Response ID (int), Debug message (string)
            payment.connect("purchases_updated", self, "_on_purchases_updated") # Purchases (Dictionary[])
            payment.connect("purchase_error", self, "_on_purchase_error") # Response ID (int), Debug message (string)
            payment.connect("sku_details_query_completed", self, "_on_sku_details_query_completed") # SKUs (Dictionary[])
            payment.connect("sku_details_query_error", self, "_on_sku_details_query_error") # Response ID (int), Debug message (string), Queried SKUs (string[])
            payment.connect("purchase_acknowledged", self, "_on_purchase_acknowledged") # Purchase token (string)
            payment.connect("purchase_acknowledgement_error", self, "_on_purchase_acknowledgement_error") # Response ID (int), Debug message (string), Purchase token (string)
            payment.connect("purchase_consumed", self, "_on_purchase_consumed") # Purchase token (string)
            payment.connect("purchase_consumption_error", self, "_on_purchase_consumption_error") # Response ID (int), Debug message (string), Purchase token (string)

            payment.startConnection()
        else:
            print("Android IAP support is not enabled. Make sure you have enabled 'Custom Build' and the GodotGooglePlayBilling plugin in your Android export settings! IAP will not work.")

All API methods only work if the API is connected. You can use ``payment.isReady()`` to check the connection status.


Querying available items
************************

As soon as the API is connected, you can query SKUs using ``querySkuDetails``.

Full example:

::

    func _on_connected():
      payment.querySkuDetails(["my_iap_item"], "inapp") # "subs" for subscriptions

    func _on_sku_details_query_completed(sku_details):
      for available_sku in sku_details:
        print(available_sku)


Purchase an item
****************

To initiate the purchase flow for an item, call ``purchase``.
You **must** query the SKU details for an item before you can
initiate the purchase flow for it.

::

    payment.purchase("my_iap_item")

Then, wait for the ``_on_purchases_updated`` callback and handle the purchase result:

::

    func _on_purchases_updated(purchases):
        for purchase in purchases:
            if purchase.purchase_state == 1: # 1 means "purchased", see https://developer.android.com/reference/com/android/billingclient/api/Purchase.PurchaseState#constants_1
                # enable_premium(purchase.sku) # unlock paid content, add coins, save token on server, etc. (you have to implement enable_premium yourself)
                if not purchase.is_acknowledged:                                        
                    payment.acknowledgePurchase(purchase.purchase_token) # call if non-consumable product
                    if purchase.sku in list_of_consumable_products:
                        payment.consumePurchase(purchase.purchase_token) # call if consumable product


Check if the user purchased an item
***********************************

To get all purchases, call ``queryPurchases``. Unlike most of the other functions, ``queryPurchases`` is
a synchronous operation and returns a :ref:`Dictionary <class_Dictionary>` with a status code
and either an array of purchases or an error message. Only active subscriptions and non-consumed one-time purchases are returned.

Full example:

::

    var query = payment.queryPurchases("inapp") # Or "subs" for subscriptions
    if query.status == OK:
        for purchase in query.purchases:
            if purchase.sku == "my_iap_item" and purchase.purchase_state == 1:
                # enable_premium(purchase.sku) # unlock paid content, save token on server, etc.
                if !purchase.is_acknowledged:
                    payment.acknowledgePurchase(purchase.purchase_token)
                    # Or wait for the _on_purchase_acknowledged callback before giving the user what they bought


Consumables
***********

If your in-app item is not a one-time purchase but a consumable item (e.g. coins) which can be purchased
multiple times, you can consume an item by calling ``consumePurchase`` with a purchase token.
Call ``queryPurchases`` to get the purchase token. Calling ``consumePurchase`` automatically
acknowledges a purchase.
Consuming a product allows the user to purchase it again, and removes it from appearing in subsequent ``queryPurchases`` calls.

::

    var query = payment.queryPurchases("inapp") # Or "subs" for subscriptions
    if query.status == OK:
        for purchase in query.purchases:
            if purchase.sku == "my_consumable_iap_item" and purchase.purchase_state == 1:
                # enable_premium(purchase.sku) # add coins, save token on server, etc.
                payment.consumePurchase(purchase.purchase_token)
                # Or wait for the _on_purchase_consumed callback before giving the user what they bought

Subscriptions
*************

Subscriptions don't work much different from regular in-app items. Just use ``"subs"`` as second
argument to ``querySkuDetails`` to get subscription details.
Check ``is_auto_renewing`` in the results of ``queryPurchases()`` to see if a
user has cancelled an auto-renewing subscription
