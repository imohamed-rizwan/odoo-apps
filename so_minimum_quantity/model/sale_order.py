
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, Warning


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        for lines in self:
            if lines.product_id.minimum_quantity:
                lines.product_uom_qty = lines.product_id.minimum_quantity
        return res

    @api.onchange('product_uom_qty')
    def product_qty_change(self):
        for lines in self:
            product = lines.product_id
            minimum_order_qty = product.minimum_quantity
            if minimum_order_qty and (lines.product_uom_qty < minimum_order_qty):
                print(minimum_order_qty, '===minimum_order_qty===')
                message = _('Minimum order quantity of the product %s is %s.') % \
                    (product.name, str(minimum_order_qty))
                warning_mess = {
                    'title': _('Minimum quantity criteria!'),
                    'message': message
                }
                return {'warning': warning_mess}
            pass
