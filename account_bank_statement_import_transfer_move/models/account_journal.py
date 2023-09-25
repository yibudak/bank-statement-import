# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountJournal(models.Model):

    _inherit = "account.journal"

    transfer_line = fields.Boolean(
        string="Add balance Line",
        help="Generate balance line on total of bank statemen import",
    )