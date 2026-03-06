# -*- coding: utf-8 -*-
# Part of Protek Enerji. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class ProtekEnerjiWebsiteSale(WebsiteSale):
    """
    Override Website Sale controller to enforce login requirement
    and restrict access to shopping functionality only.
    """

    @http.route(['/shop', '/shop/page/<int:page>'], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        """Override shop to require login"""
        if request.env.user._is_public():
            return request.render('protekenerji.protek_shop_login_required')
        return super(ProtekEnerjiWebsiteSale, self).shop(page=page, category=category, search=search,
                           min_price=min_price, max_price=max_price, ppg=ppg, **post)

    @http.route(['/shop/<model("product.template"):product>'], type='http', auth="public", website=True, sitemap=True)
    def product(self, product, category='', search='', **kwargs):
        """Override product page to require login"""
        if request.env.user._is_public():
            return request.render('protekenerji.protek_shop_login_required')
        return super(ProtekEnerjiWebsiteSale, self).product(product=product, category=category, search=search, **kwargs)

    @http.route(['/shop/cart'], type='http', auth="public", website=True, sitemap=False)
    def cart(self, access_token=None, revive='', **post):
        """Override cart to require login"""
        if request.env.user._is_public():
            return request.render('protekenerji.protek_shop_login_required')
        return super(ProtekEnerjiWebsiteSale, self).cart(access_token=access_token, revive=revive, **post)


class ProtekEnerjiHome(http.Controller):
    """Controller for Protek Enerji custom pages"""

    @http.route(['/protek', '/protek/home'], type='http', auth='public', website=True)
    def protek_home(self, **kw):
        """Protek Enerji Home Page - accessible to public"""
        return request.render('protekenerji.protek_home_page', {
            'page_name': 'protek_home',
        })

    @http.route(['/protek/about'], type='http', auth='public', website=True)
    def protek_about(self, **kw):
        """About Protek Enerji Page"""
        return request.render('protekenerji.protek_about_page', {
            'page_name': 'protek_about',
        })

    @http.route(['/protek/gdpr'], type='http', auth='public', website=True)
    def protek_gdpr(self, **kw):
        """GDPR Privacy Policy Page"""
        return request.render('protekenerji.protek_gdpr_page', {
            'page_name': 'protek_gdpr',
        })

    @http.route(['/protek/contact'], type='http', auth='public', website=True)
    def protek_contact(self, **kw):
        """Contact Page"""
        return request.render('protekenerji.protek_contact_page', {
            'page_name': 'protek_contact',
        })

    @http.route(['/contactus'], type='http', auth='public', website=True)
    def contactus(self, **kw):
        """Override default Contact Us page with Protek Enerji contact info"""
        return request.render('protekenerji.protek_contact_page', {
            'page_name': 'contactus',
        })

