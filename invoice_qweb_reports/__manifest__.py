# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Odoo 13 Invoice PDF Reports ',
    'version': '13.0.2',
    'category': 'Invoicing Management',
    'description': 'Create an Invoice Report by taking input of Start Date and End Date from wizard Based on Date, Multiple pdf pages will be printed in single pdf. Only invoice that are Posted and Paid be printed.',
    'summary': 'Invoice PDF Reports for Odoo 13',
    'sequence': '10',
    'author': 'Mohamed Rizwan, Odoo SA',
    'license': 'LGPL-3',
    'maintainer': 'Mohamed Rizwan',
    'support': 'iamrizwan45@gmail.com',
    'website': 'mohamed.co.in',
    'depends': ['account','base'],
    'demo': [],
    'data': [
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