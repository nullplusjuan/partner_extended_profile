{
    "name": "Partner Extended Profile",
    "version": "18.0.1.0.0",
    "summary": "Reusable personal and contact profile fields for Odoo contacts",
    "author": "Quadrintin Solutions",
    "category": "Contacts",
    "license": "LGPL-3",
    "depends": ["contacts"],
    "data": [
        "views/res_partner_views.xml",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "application": False,
}
