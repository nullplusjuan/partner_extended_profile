# Copyright 2026 Joshua D
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# SPDX-License-Identifier: AGPL-3.0-or-later
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    birth_date = fields.Date(string="Date of Birth")
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other / Prefer not to say"),
        ],
        string="Gender",
    )
    mobile2 = fields.Char(string="Alternate Mobile")
    phone_work = fields.Char(string="Work Phone")
    employer = fields.Char(string="Place of Employment")
    marital_status = fields.Selection(
        [
            ("single", "Single"),
            ("married", "Married"),
            ("common_law", "Common Law"),
            ("other", "Other"),
        ],
        string="Marital Status",
    )
    identity_document_ids = fields.One2many(
        "res.partner.identity.document",
        "partner_id",
        string="Identification Documents",
    )
