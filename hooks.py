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
import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)


LEGACY_FIELD_MAP = {
    "react_birth_date": "birth_date",
    "react_gender": "gender",
    "react_mobile2": "mobile2",
    "react_phone_work": "phone_work",
    "react_employer": "employer",
    "react_marital_status": "marital_status",
}


def _column_exists(cr, table, column):
    cr.execute(
        """
        SELECT 1
          FROM information_schema.columns
         WHERE table_schema = current_schema()
           AND table_name = %s
           AND column_name = %s
        """,
        (table, column),
    )
    return bool(cr.fetchone())


def post_init_hook(env):
    """Migrate values from the former REACT-owned partner columns if present.

    This intentionally only fills empty new fields, so installing this module on a
    database where the generic profile was already maintained cannot overwrite
    newer data.
    """
    cr = env.cr
    migrated = []

    for old_column, new_column in LEGACY_FIELD_MAP.items():
        if not _column_exists(cr, "res_partner", old_column):
            continue
        if not _column_exists(cr, "res_partner", new_column):
            continue

        cr.execute(
            f"""
            UPDATE res_partner
               SET {new_column} = {old_column}
             WHERE {new_column} IS NULL
               AND {old_column} IS NOT NULL
            """
        )
        if cr.rowcount:
            migrated.append((old_column, new_column, cr.rowcount))

    if migrated:
        _logger.info("Migrated legacy REACT partner profile data: %s", migrated)
