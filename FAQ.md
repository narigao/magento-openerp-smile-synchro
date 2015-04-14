# Can't install the Magento extension from the extension repository #
If you get an error in the Magento download manager, may be you should try to open the settings tab in the download manager and choose 'beta' instead of 'stable'. Then try again.

# Testing the Magento extension #
You can ensure that your Magento extension is properly installed by browsing the following URL with your favorite browser:
http://localhost/magento/app/code/local/Smile_OpenERP_Synchro/openerp-synchro.php

Ensure your get a welcome message with no error before the message (due to some bad interaction with Magento when testing that URL from the browser, you might need to clear your cookies before trying again).

**If you get a 404 not found error** then it might be an installation bug we are still investigating, see: http://code.google.com/p/magento-openerp-smile-synchro/issues/detail?id=11
In this case, the work around is to copy the Smile\_OpenERP\_Synchro manuall from magento/local to magento/community. Make sure it passes the test then. We are working on that issue.

# OpenERP error log while synchronizing #
if you get an error like `junk after document element`

you should log the detailed error message, so change temporarily your xmlrpc.py library file, in     def _parse\_response(self, file, sock): (close to line 1321),
add a print response statement so you get:
```
while 1:
            if sock:
                response = sock.recv(1024)
            else:
                response = file.read(1024)
		print response
```_

Then stop and restart your OpenERP server, next time you get an error you might easily investigate on what is going wrong with the PHP response from Magento (you'll get the HTML error message logged) in the OpenERP server log.


# Sale order amount precision #
If OpenERP displays order amount that seems to be trunked and differ slightly from Magento values, then you should increase the OpenERP discount field float precision inside the sale\_order\_line table. For instance, you can set it to the numeric(16, 4) instead of numeric(16, 2) with PGAdmin III. Warning, always make a database dump before altering it if you are running in production.

![http://img112.imageshack.us/img112/7955/magentoopenerproundingmh4.png](http://img112.imageshack.us/img112/7955/magentoopenerproundingmh4.png)


# Tax after or before discount #
The connector has only been successfully tested with taxes applied AFTER discounts. I think this is the default in OpenERP and I don't know how one should proceed if doing the contrary (but I'm pretty sure this can be achieved using some OpenERP module). On the contrary, It's clear that Magento is able to deal with any of the two options, so then one could alter our connector a little bit to make it work correctly with OpenERP if what you want is taxes being applied before discount. Please [let us know here](http://groups.google.com/group/magento-openerp) if you attempt such a thing.


# e-accelerator #
It looks like e-accelerator doesn't work with the Zend php docBlock based reflection system. On the contrary, the apc (easier to configure and just as fast) accelerator looks all right. When using e-accelerator, you might have issues with the XML/RPC signatures.


# Why not use only the built'in Magento webservices? #
We had trouble doing that to retrieve the sale orders and their sale order lines properly. Still, we now believe this could also be done using only the Magento native webservices API, so we should probably refactor our code to achieve that, see that RFE: http://code.google.com/p/magento-openerp-smile-synchro/issues/detail?id=6

# Security #
**The connector web services are currently exposed in an unprotected manner to the world.** This is very important you prevent anyone from connecting to the webservice page ( http://localhost/magento/app/code/community/Smile_OpenERP_Synchro/openerp-synchro.php ) by tunning your server (probably Apache). Ideally only the OpenERP server could connect to that page (same as the test page). Using Magento ACL based webservices would improve that situation a lot. Please don't hesitate to contribute such an improvement.
the Magento webservices API guidelines have just been published here:
http://www.magentocommerce.com/wiki/doc/webservices-api/custom-api

# Store id #
Currently mono Magento store is trivial to get working. Still, this should be possible to use multiple Magento store ids. Notice that in Magento you state what is the root category of every store. This way, if you you can decide which products will be available in which store by simply assigning them the proper category. Still, some improvements could certainly be made so don't hesitate to make usggestion on the [Google feedback group](http://groups.google.com/group/magento-openerp).

# You imported Magento sale orders referencing products that are not in the OpenERP catalog, what to do ? #
You'll have to create the missing products in OpenERP manually. You can find out what are those missing products by looking at the OpenERP logs when a sale order import error occurs. For each of those missing OpenERP products, you'll manually set the corresponding magento\_id in the OpenERP product form. Once you did this, you can click on the 'correct sale orders' wizard in OpenERP.