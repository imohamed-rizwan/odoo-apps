# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Odoo 14 Invoice PDF Reports ',
    'version': '14.0.1',
    'category': 'Invoicing Management',
    'description': 'Create an Invoice Report by taking input of Start Date and End Date from wizard Based on Date, Multiple pdf pages will be printed in single pdf. Only invoice that are Posted and Paid be printed.',
    'summary': 'Invoice PDF Reports for Odoo 14',
    'sequence': '10',
    'author': 'Mohamed Rizwan, Odoo SA',
    'license': 'LGPL-3',
    'maintainer': 'Mohamed Rizwan',
    'support': 'iamrizwan45@gmail.com',
    'website': 'mohamed.co.in',
    'depends': ['account','base'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'wizard/report_wiz.xml',
        'report/report.xml',
        'report/report_invoice.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/icon.png'],
    'qweb': [],

}
