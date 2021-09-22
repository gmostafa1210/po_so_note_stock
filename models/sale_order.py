# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    so_note = fields.Char(string='SO Note')

    def action_confirm(self):
        if self._get_forbidden_state_confirm() & set(self.mapped('state')):
            raise UserError(_(
                'It is not allowed to confirm an order in the following states: %s'
            ) % (', '.join(self._get_forbidden_state_confirm())))

        for order in self.filtered(lambda order: order.partner_id not in order.message_partner_ids):
            order.message_subscribe([order.partner_id.id])
        self.write(self._prepare_confirmation_values())

        context = self._context.copy()
        context.pop('default_name', None)

        self.with_context(context)._action_confirm()
        if self.env.user.has_group('sale.group_auto_done_setting'):
            self.action_done()

        picking = self.env['stock.picking'].search([('origin', '=', self.name)])
        if picking:
            picking.po_so_note = self.so_note

        return True


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    so_line = fields.Char(string='SO Line')

    def _prepare_procurement_values(self, group_id=False):
        whout_vals = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        whout_vals.update({
            'so_line': self.so_line
        })
        return whout_vals