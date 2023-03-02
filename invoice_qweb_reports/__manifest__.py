# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Invoice Qweb Reports ',
    'version': '14.0.1',
    'category': 'Invoicing Management',
    'author': 'Mohamed Rizwan, Odoo SA',
    'website': 'mohamed.co.in',
    'summary': """Create an invoice report by taking input of start date and end date from wizard""",
    'description': """
                Create an invoice report by taking input of start date and end date from wizard
                Based on Date, multiple pdf pages will be printed in single pdf.
                Only invoice that are Posted and Paid be printed.
                """,
    'depends': ['account','base'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'wizard/report_wiz.xml',
        'report/report.xml',
        'report/report_invoice.xml',
    ],
    'images': ['static/description/icon.png'],
    'support': 'iamrizwan45@gmail.com',
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
