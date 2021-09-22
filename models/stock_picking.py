# -*- coding: utf-8 -*-

from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    po_so_note = fields.Char(string='PO/SO Note')
    po_so_note_line = fields.Char(string='PO/SO Line')