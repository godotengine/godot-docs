.. _doc_android_in_app_purchases:

Android in-app purchases
========================

Godot engine has integrated GooglePaymentsV3 module with which we can implement in-app purchases in our game.

The Godot engine demo project repository has an android-iap example project. It includes a gdscript interface for android iap.

Check the repository here https://github.com/godotengine/godot-demo-projects

Find the iap.gd script in 

::
    godot-demo-projects/misc/android_iap

Add it to the Autoload list and name it as IAP so that we can reference it anywhere in the game.

Getting the product details
---------------------------

When starting our game, we will need to get the item details from Google such as the product price, description and localized price string etc.

::
    #First listen to the sku details update callback
    IAP.connect("sku_details_complete",self,"sku_details_complete")
    #Then ask google the details for these items
    IAP.sku_details_query(["pid1","pid2"])
    
    
    #This will be called when sku details are retrieved successfully
    func sku_details_complete():
        print(IAP.sku_details) #This will print the details as JSON format, refer the format in iap.gd
        print(IAP.sku_details["pid1"].price) #print formatted localized price
