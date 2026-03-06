# -*- coding: utf-8 -*-
# Part of Protek Enerji. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class Website(models.Model):
    _inherit = 'website'

    protek_shop_login_required = fields.Boolean(
        string='Shop Login Required',
        default=True,
        help='Require users to login before accessing the shop'
    )

    protek_primary_color = fields.Char(
        string='Primary Color',
        default='#e31e24',
        help='Primary brand color for Protek Enerji'
    )

    protek_secondary_color = fields.Char(
        string='Secondary Color',
        default='#1a1a2e',
        help='Secondary brand color for Protek Enerji'
    )

