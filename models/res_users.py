# -*- coding: utf-8 -*-
# Part of Protek Enerji. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    is_protek_customer = fields.Boolean(
        string='Protek Customer',
        default=False,
        help='Mark this user as a Protek Enerji customer with restricted portal access'
    )

    @api.model
    def _signup_create_user(self, values):
        """Override to set protek customer flag for portal signups"""
        values['is_protek_customer'] = True
        return super()._signup_create_user(values)

