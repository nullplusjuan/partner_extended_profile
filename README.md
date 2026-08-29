# Partner Extended Profile

Reusable Odoo 18 `res.partner` fields for personal/contact information that is not specific to REACT or any other organization.

Fields added:

- `birth_date`
- `gender`
- `mobile2`
- `phone_work`
- `employer`
- `marital_status`

On first installation, the module safely copies values from the previous `react_*` columns when those legacy columns exist. Existing generic values take precedence and are never overwritten by the migration hook.
