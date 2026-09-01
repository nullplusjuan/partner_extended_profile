# Copyright 2026 Joshua D
# SPDX-License-Identifier: AGPL-3.0-or-later
{
    "name": "Partner Extended Profile",
    "version": "18.0.5.0.0",
    "summary": "Reusable personal, contact and identity profile fields for Odoo contacts",
    "author": "Quadrintin Solutions",
    "category": "Contacts",
    "license": "AGPL-3",
    "depends": ["contacts"],
    "data": [
        "security/ir.model.access.csv",
        "views/partner_identity_views.xml",
        "views/res_partner_views.xml",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "application": False,
}
