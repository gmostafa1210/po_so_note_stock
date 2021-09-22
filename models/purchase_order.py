# -*- coding: utf-8 -*-

from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    po_note = fields.Char(string='PO Note')

    def _prepare_picking(self):
        whout_vals = super(PurchaseOrder, self)._prepare_picking()
        whout_vals.update({
            'po_so_note': self.po_note,
        })
        return whout_vals


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    po_line = fields.Char(string='PO Line')

    def _prepare_stock_move_vals(self, picking, price_unit, product_uom_qty, product_uom):
        whout_vals = super(PurchaseOrderLine, self)._prepare_stock_move_vals(picking, price_unit, product_uom_qty, product_uom)
        whout_vals.update({
            'po_so_note_line': self.po_line,
        })
        return whout_vals