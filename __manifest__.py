# -*- coding: utf-8 -*-

{
    'name' : 'PO/SO to Stock',
    'version' : '1.1',
    'summary': 'PO/SO to stock summary.',
    'sequence': 1,
    'description': 'PO/SO to stock description.',
    'depends' : ['base', 'purchase', 'purchase_stock', 'sale_management', 'sale'],
    'data': [
        'views/purchase_order_view.xml',
        'views/sale_order_view.xml',
        'views/stock_picking_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
