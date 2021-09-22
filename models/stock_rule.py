# -*- coding: utf-8 -*-

from odoo import models, fields


class StockRule(models.Model):
    
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
        whout_vals = super(StockRule, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values)
        whout_vals.update({
            'po_so_note_line': values.get('so_line'),
        })
        return whout_vals