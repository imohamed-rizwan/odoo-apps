# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Invoice Qweb Reports ',
    'version': '13.0',
    'author': 'Mohamed Rizwan',
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
        'wizard/report_wiz.xml',
        'report/report.xml',
        'report/report_invoice.xml',
    ],
    'support': 'iamrizwan45@gmail.com',
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
