# Installation #

---


To get started you need to install both :
  * The connector module for OpenERP. Use the OpenERP module manager to load the zip file you'll find [here](http://code.google.com/p/magento-openerp-smile-synchro/downloads/list)

  * The connector extension for Magento you'll install using Magento Connect Utility. The extension key is to be found on [here in the Magento Connect repository ](http://www.magentocommerce.com/extension/446/smile-openerp-synchro). See installation video in flash, in the [download section](http://code.google.com/p/magento-openerp-smile-synchro/downloads/list).

/!\ Since v 0.9.9 you have to move the Smile\_OpenERPSync.xml file,
from magento/app/code/local/Smile/OpenERPSync/etc/modules
to magento/app/etc/modules, and refresh your magento cache

(Both plugins are actually bundled in the OpenERP module you can download [here](http://code.google.com/p/magento-openerp-smile-synchro/downloads/list). Both modules are also on [SCM here ](http://code.google.com/p/magento-openerp-smile-synchro/source/checkout).



# Initial Configuration #

---


![http://img221.imageshack.us/img221/9238/openerpscreenshot001rm2.png](http://img221.imageshack.us/img221/9238/openerpscreenshot001rm2.png)
_magento interface_

You need to configure the website, shop, category, and tax class in OpenERP Client
and Magento Back office.

## _-Website_ ##

> On OpenERP, you need to configure a website Name & Url, the
> magento\_id must be set to one.
> The URL must point a the base of your Magento website; usually this means http://localhost/magento/ . The trailing slash is currently mandatory.

> ![http://img221.imageshack.us/img221/282/openerpscreenshot003et5.png](http://img221.imageshack.us/img221/282/openerpscreenshot003et5.png)

> Since 0.9.7
> You now have to configure API username and password you have to create on Magento backoffice through System > Webservices > Users and Roles (create a roles with enough right, eventually all, and create a user affected to that role). Otherwise you could just get a "Invalid api path" error message in your OpenERP server logs while synchronizing.
see the following screencast:

&lt;wiki:gadget url="http://hosting.gmodules.com/ig/gadgets/file/118008740609451236976/openerp1.xml" border="0" width="430" height="350"/&gt;



## _-Shop_ ##

> You must configure a shop with the magento\_id set to one,
> a price list and a warehouse must be defined for the shop. Ideally in the future we will map each OpenERP shop to a Magento store.

> ![http://img66.imageshack.us/img66/9836/openerpscreenshot002xv4.png](http://img66.imageshack.us/img66/9836/openerpscreenshot002xv4.png)

see following screencast:
&lt;wiki:gadget url="http://hosting.gmodules.com/ig/gadgets/file/118008740609451236976/openerp2.xml" border="0" width="430" height="350"/&gt;


## _-Category_ ##

> Categories are now automatically exported !

## _Tax Class_ ##

> You can synchronize Taxes on the products :
> When you assign taxes, such as VAT, to a product in OpenERP, you can
> also assign it a tax class id in Magento.
> Then tax class can be applied on the products in Magento.

> ![http://img65.imageshack.us/img65/5547/openerpscreenshot003vr5.png](http://img65.imageshack.us/img65/5547/openerpscreenshot003vr5.png)

> You can get the Tax class id, the same way you get the categories,
> > via SQL request:

```
        SELECT 'class_id'
        FROM `tax_class`
        WHERE 'class_name'='Tax Class name"
```


> /!\ Warning
> In Magento > System > Configuration > Sales  > Tax > Calculation
> > Or prior to Magento 1.1.4  Magento > Configuration > Sales > Sales > Tax Calculation

> you must set :

> _Catalog prices include tax_, to **No**

> _Apply Tax after Discount_, to **Yes**



> ![http://img80.imageshack.us/img80/5977/openerpscreenshot001yu2.png](http://img80.imageshack.us/img80/5977/openerpscreenshot001yu2.png)

## _-Discount_ ##

> To ensure discount calculation you must change the precision in your database
> (with for instance PGAdmin III) of the "discount" field, in the "sale\_order" table
> you can set it to the numeric(16, 4) instead of numeric(16, 2)

> ![http://img112.imageshack.us/img112/7955/magentoopenerproundingmh4.png](http://img112.imageshack.us/img112/7955/magentoopenerproundingmh4.png)

## _-Type and Attribute_ ##

> Type and Attibute are now automatically setted to the default
> values.



# Category and Products synchronization #

---


> The "Categories" and "Product" wizards will import or/and update the
> categories and products of your OpenERP catalog to Magento Catalog.

> You can prevent a category or a product to be exported by setting the "exportable"
> field to False on a product (set on True by default).

> ![http://img67.imageshack.us/img67/3578/openerpscreenshot004qe1.png](http://img67.imageshack.us/img67/3578/openerpscreenshot004qe1.png)

> Added synchronize per item on products and categories.
> You can now synchronize :
> > - On the main menu, all you items
> > - On a tree view, the selected items
> > - On a form view, the current item

> Also, when you save an item, it is automatically updated on Magento


# Sale orders synchronization #

---


## _-Import_ ##

> The "import" wizard will import Magento orders to OpenERP
> it will also create a partner with the customer information
> (if he is not already known) and save his address.

## _-Correct_ ##

> In the case you import a sale order with a product defined in Magento
> and not known by OpenERP, it will be incomplete, the field "has error" will take
> the value of 1.
> You can still correct the order by registering the product in OpenERP
> and set the Magento id in OpenERP, to the same as the one in Magento, then
> the "correct" wizard will allow you to correct sale order.

## _-Update_ ##

> the "update" wizard will update the state of the order in Magento
> for the different states to draft from done.

![http://img66.imageshack.us/img66/9176/openerpscreenshot005nn8.png](http://img66.imageshack.us/img66/9176/openerpscreenshot005nn8.png)

![http://img227.imageshack.us/img227/3866/openerpscreenshot006vc9.png](http://img227.imageshack.us/img227/3866/openerpscreenshot006vc9.png)

# Sale orders push #

---


From Charles Galpin branch :
You can now enable sale order push from Magento, sales will be pushed in OpenERP
when created.

You have to configure on Magento System>Configuration>Sales>OpenERP Sync

-> set to Enable
-> set the URL to your openerp server, the database name, and ident for a user
with enough rights.

![http://img227.imageshack.us/my.php?image=openerpscreenshot004ha0.png](http://img227.imageshack.us/my.php?image=openerpscreenshot004ha0.png)

# Overall demo #

---


(click on fullscreen view)

&lt;wiki:gadget url="http://hosting.gmodules.com/ig/gadgets/file/118008740609451236976/helloworld.xml" border="0" width="430" height="350"/&gt;