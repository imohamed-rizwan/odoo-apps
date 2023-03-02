
from odoo import api,fields,models,_

class ProductTemplate(models.Model):
    _inherit="product.template"

    
    minimum_quantity = fields.Float(string='Minimum Quantity',help="This field display minimum order qunatity")  
    