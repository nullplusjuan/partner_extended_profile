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
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class PartnerIdentityType(models.Model):
    _name = "res.partner.identity.type"
    _description = "Partner Identity Document Type"
    _order = "sequence, name"

    name = fields.Char(required=True, translate=True)
    code = fields.Char(required=True, index=True)
    sequence = fields.Integer(default=10)
    country_id = fields.Many2one(
        "res.country",
        string="Country",
        help="Leave blank for an identity type that is not country-specific.",
    )
    active = fields.Boolean(default=True)
    notes = fields.Text()

    _sql_constraints = [
        ("partner_identity_type_code_uniq", "unique(code)", "Identity type codes must be unique."),
    ]


class PartnerIdentityDocument(models.Model):
    _name = "res.partner.identity.document"
    _description = "Partner Identity Document"
    _order = "id desc"

    partner_id = fields.Many2one(
        "res.partner",
        required=True,
        ondelete="cascade",
        index=True,
    )
    identity_type_id = fields.Many2one(
        "res.partner.identity.type",
        string="ID Type",
        required=True,
        ondelete="restrict",
        index=True,
    )
    number = fields.Char(string="ID Number", required=True, index=True)
    document_copy = fields.Binary(
        string="Copy of ID",
        attachment=True,
    )
    document_filename = fields.Char(string="Filename")
    notes = fields.Text()
    active = fields.Boolean(default=True)

    @api.constrains("partner_id", "identity_type_id", "number")
    def _check_unique_partner_identity(self):
        for record in self:
            if not record.partner_id or not record.identity_type_id or not record.number:
                continue
            duplicate = self.search_count([
                ("id", "!=", record.id),
                ("partner_id", "=", record.partner_id.id),
                ("identity_type_id", "=", record.identity_type_id.id),
                ("number", "=", record.number),
            ])
            if duplicate:
                raise ValidationError(
                    "This partner already has an identity document with the same type and number."
                )
