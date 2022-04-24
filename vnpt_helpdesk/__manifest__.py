# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'VNPT: Helpdesk',
    'version': '1.0',
    'summary': 'VNPT: Helpdesk',
    'description': """
VNPT Helpdesk
""",
    'website': ' ',
    'depends': [],

    'data': [
        'security/ir.model.access.csv',

        'views/bptd_location_views.xml',
        'views/menuitems.xml',
    ],
    'assets': {
        'web.assets_backend': [

        ],
    },

    'installable': True,
    'auto_install': True,
    'license': 'OEEL-1',
}
