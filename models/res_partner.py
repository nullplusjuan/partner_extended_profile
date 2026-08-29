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
