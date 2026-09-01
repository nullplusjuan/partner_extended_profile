# Copyright 2026 Joshua D
# SPDX-License-Identifier: AGPL-3.0-or-later
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    birth_date = fields.Date(string="Date of Birth")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other / Prefer not to say")],
        string="Gender",
    )
    mobile2 = fields.Char(string="Alternate Mobile")
    phone_work = fields.Char(string="Work Phone")
    employer = fields.Char(string="Place of Employment")
    employer_partner_id = fields.Many2one(
        "res.partner",
        string="Employer Contact",
        ondelete="set null",
        domain="[('is_company', '=', True)]",
        help="Company/contact record representing this person's employer.",
    )
    marital_status = fields.Selection(
        [("single", "Single"), ("married", "Married"), ("common_law", "Common Law"), ("other", "Other")],
        string="Marital Status",
    )
    identity_document_ids = fields.One2many(
        "res.partner.identity.document", "partner_id", string="Identification Documents"
    )

    @api.constrains("birth_date")
    def _check_birth_date(self):
        for partner in self.filtered("birth_date"):
            if partner.birth_date >= fields.Date.context_today(partner):
                raise ValidationError(_("Date of Birth must be before today."))
