# -*- coding: utf-8 -*-
# Part of Protek Enerji. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager


class ProtekEnerjiPortal(CustomerPortal):
    """
    Extended Portal Controller for Protek Enerji
    Provides order history and customer account management
    """

    def _prepare_home_portal_values(self, counters):
        """Add order counts to portal home"""
        values = super()._prepare_home_portal_values(counters)
        partner = request.env.user.partner_id

        if 'order_count' in counters:
            SaleOrder = request.env['sale.order']
            order_count = SaleOrder.search_count([
                ('partner_id', '=', partner.id),
                ('state', 'in', ['sale', 'done'])
            ])
            values['order_count'] = order_count

        if 'quotation_count' in counters:
            SaleOrder = request.env['sale.order']
            quotation_count = SaleOrder.search_count([
                ('partner_id', '=', partner.id),
                ('state', 'in', ['draft', 'sent'])
            ])
            values['quotation_count'] = quotation_count

        return values

    @http.route(['/my/orders', '/my/orders/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_orders(self, page=1, date_begin=None, date_end=None, sortby=None, filterby=None, **kw):
        """Display customer orders"""
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        SaleOrder = request.env['sale.order']

        domain = [
            ('partner_id', '=', partner.id),
            ('state', 'in', ['sale', 'done'])
        ]

        searchbar_sortings = {
            'date': {'label': 'Order Date', 'order': 'date_order desc'},
            'name': {'label': 'Reference', 'order': 'name'},
            'stage': {'label': 'Stage', 'order': 'state'},
        }

        searchbar_filters = {
            'all': {'label': 'All', 'domain': []},
            'sale': {'label': 'Confirmed', 'domain': [('state', '=', 'sale')]},
            'done': {'label': 'Locked', 'domain': [('state', '=', 'done')]},
        }

        if not sortby:
            sortby = 'date'
        sort_order = searchbar_sortings[sortby]['order']

        if not filterby:
            filterby = 'all'
        domain += searchbar_filters[filterby]['domain']

        if date_begin and date_end:
            domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]

        # Count for pager
        order_count = SaleOrder.search_count(domain)

        # Pager
        pager = portal_pager(
            url="/my/orders",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby, 'filterby': filterby},
            total=order_count,
            page=page,
            step=self._items_per_page
        )

        # Content according to pager
        orders = SaleOrder.search(domain, order=sort_order, limit=self._items_per_page, offset=pager['offset'])

        values.update({
            'date': date_begin,
            'orders': orders,
            'page_name': 'orders',
            'pager': pager,
            'default_url': '/my/orders',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
            'searchbar_filters': searchbar_filters,
            'filterby': filterby,
        })

        return request.render("protekenerji.portal_my_orders", values)

    @http.route(['/my/orders/<int:order_id>'], type='http', auth="user", website=True)
    def portal_order_page(self, order_id=None, access_token=None, report_type=None, download=False, **kw):
        """Display single order details"""
        try:
            order_sudo = self._document_check_access('sale.order', order_id, access_token=access_token)
        except Exception:
            return request.redirect('/my/orders')

        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=order_sudo, report_type=report_type,
                                     report_ref='sale.action_report_saleorder', download=download)

        values = self._prepare_portal_layout_values()
        values.update({
            'order': order_sudo,
            'page_name': 'order',
        })

        return request.render("protekenerji.portal_order_page", values)

    @http.route(['/my/past-orders', '/my/past-orders/page/<int:page>'], type='http', auth="user", website=True)
    def portal_past_orders(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        """Display past/completed orders"""
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        SaleOrder = request.env['sale.order']

        domain = [
            ('partner_id', '=', partner.id),
            ('state', '=', 'done'),
            ('invoice_status', '=', 'invoiced')
        ]

        searchbar_sortings = {
            'date': {'label': 'Order Date', 'order': 'date_order desc'},
            'name': {'label': 'Reference', 'order': 'name'},
            'amount': {'label': 'Total Amount', 'order': 'amount_total desc'},
        }

        if not sortby:
            sortby = 'date'
        sort_order = searchbar_sortings[sortby]['order']

        if date_begin and date_end:
            domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]

        # Count for pager
        order_count = SaleOrder.search_count(domain)

        # Pager
        pager = portal_pager(
            url="/my/past-orders",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total=order_count,
            page=page,
            step=self._items_per_page
        )

        # Content according to pager
        orders = SaleOrder.search(domain, order=sort_order, limit=self._items_per_page, offset=pager['offset'])

        values.update({
            'date': date_begin,
            'orders': orders,
            'page_name': 'past_orders',
            'pager': pager,
            'default_url': '/my/past-orders',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })

        return request.render("protekenerji.portal_past_orders", values)

