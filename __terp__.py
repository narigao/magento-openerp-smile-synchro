{
    "name" : "Magento Synchro Smile",
    "version" : "0.9.5",
    "author" : "Smile",
    "category" : "Interfaces/CMS & eCommerce",
    "website" : "http://code.google.com/p/magento-openerp-smile-synchro/",
    #please notice that the delivery module is only used to add attach a shipping price line
    "depends" : ["product", "stock", "sale", "account", "account_tax_include"],
    "description": """Magento OpenERP Interface - This module allows product catalog 
and sale orders synchronization between OpenERP and Magento.
This module is contributed by the Smile French IT company
( http://www.smile.fr/ )""",
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : ['magento_view.xml','magento_wizard.xml','magento_data.xml' ],
    "active": False,
    "installable": True
}
