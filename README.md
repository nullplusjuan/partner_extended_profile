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

## License

Copyright © 2026 Joshua D

Radio Operators is free software licensed under the GNU Affero General Public License, version 3 or, at your option, any later version.

You may use, study, modify, and redistribute this software under the terms of that license.

Because this software is distributed under the GNU AGPL, modified versions remain subject to the license's copyleft requirements, including the provisions applicable when modified software is used to provide functionality over a network.

See the `LICENSE` file for the complete license terms.

SPDX-License-Identifier: AGPL-3.0-or-later