# -*- coding: utf-8 -*-

from odoo import models, fields


class StockMove(models.Model):  
    _inherit = 'stock.move'

    po_so_note = fields.Char(string='PO/SO Note')
    po_so_note_line = fields.Char(string='PO/SO Line')