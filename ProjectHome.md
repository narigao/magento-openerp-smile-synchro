# Welcome to the OpenERP / Magento connector project! #

| [![](http://openerp.com/templates/tiny/images/openlogo.jpg)](http://www.openerp.com) | [![](http://www.varien.com/_blog/images/Magento_logo_small.gif)](http://www.magentocommerce.com/) | [![](http://www.smile.fr/extension/smiledesign/design/site/images/pages/Logo_Smile_2008.png)](http://www.smile.fr) |
|:-------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|

![http://magento-openerp-smile-synchro.googlecode.com/svn/wiki/overview.png](http://magento-openerp-smile-synchro.googlecode.com/svn/wiki/overview.png)

# News #
&lt;wiki:gadget url="http://hosting.gmodules.com/ig/gadgets/file/118008740609451236976/magento-openerp-synchro.xml" border="0" width="1000" height="500" &gt;

# What is it for? #
Want to sell your OpenERP managed product catalog on the web with the professional and scalable e-commerce Magento platform? Want to add a multi-stock, production (MRP), localized accounting or outstanding CRM to your e-commerce store, want to back it with an incredibly powerful ERP? Then that synchronization module is for you.


## Warning: ##
Both Magento and OpenERP are complex open source products. Make sure you master them correctly independently before attempting any synchronization.


# Design principles of the module: #
The main module of the connector comes as an OpenERP plugin that keeps most of the business rules and settings on the powerful and extensible OpenERP platform. Magento is mostly used to for customers to enter their sale orders.

Still, as Magento has a rather sophisticated promotion and package management, one can use Magento to deal with the exact pricing rules (including shipping and taxes), the sale order is passed back to OpenERP with those Magento prices, no matter what was the original OpenERP pricing (Magento can override OpenERP prices). Taxes and discounts are properly handled.


# Main features #
  * Product catalog export from OpenERP to Magento (with common atributes but without pictures at the moment, that's our next wanted feature)
  * Product stocks updates, based on OpenERP virtual stocks (number of products in the physical stock that have not been reserved yet)
  * Category tree export, including creation and updates. Each Magento store has its own root category id, you can thus choose to where Magento store products get loaded.
  * Taxes sync (provided that you first manually set up the magento ids of the OpenERP taxes see UserManual)
  * Sale orders imports from Magento to OpenERP. Only new sale orders are imported. This process find out which customers are already in the OpenERP database or if they have a new shipping or delivery address. Only new resources are created. Sale order lines are created too. Discounts and taxes amounts are properly imported for each line so you can finally generate an invoice in OpenERP or trigger procurement, shipping or manufacturing operations according to you stocks levels.
  * Broken sale order re-import function: if for whatever reason some sale order can't be imported; for instance because it is referencing a product that is not known inside the OpenERP database (which would just be an administration error), then once you fixed the missing product, this button gives you the opportunity to re-import properly those sale orders that failed previously.
  * Minimal code and best practices coding so evolving and maintaining the code is a snap: very minimal extra OpenERP data structures and views. No extra Magento data structure nor extra view.


# Documentation #
  * See our [flash demos here](http://code.google.com/p/magento-openerp-smile-synchro/downloads/list)
  * UserManual
  * [FAQ](http://code.google.com/p/magento-openerp-smile-synchro/wiki/FAQ)


# Feedback #
Your feedback will be very appreciated, use the following links:
  * [Bug tracker](http://code.google.com/p/magento-openerp-smile-synchro/issues/list)
  * [discussion group](http://groups.google.com/group/magento-openerp)


# Support #
All the code here is free and open source. Still, you can also get paid support, by contacting us at [Smile.fr](http://www.smile.fr/index.php/pied-de-page/coordonnees).