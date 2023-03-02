
{
    'name': "Sales Order Minimum Quantity",
    'author': 'Mohamed Rizwan',
    'category': 'Sales',
    'summary': """Set minimum sales quantity limit on product""",
    'website': 'mohamed.co.in',
    'description': """
                Set minimum sales quantity limit on product
                """,
    'support': 'iamrizwan45@gmail.com',
    'version': '13.0',
    'depends': ['base','sale_management','product'],
    'license': 'LGPL-3',
    'data': [
            'views/view_minimum_order_quantity.xml'
           ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
