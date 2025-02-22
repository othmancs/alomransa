from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    @api.constrains('qty_done')
    def _check_qty_done(self):
        for record in self:
            if record.qty_done > record.reserved_uom_qty:
                raise ValidationError("الكمية المنفذة لا يمكن أن تكون أكبر من الكمية المحجوزة.")
class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.constrains('quantity_done')
    def _check_quantity_done(self):
        for record in self:
            if record.quantity_done > record.product_uom_qty:
                raise ValidationError("الكمية المنفذة لا يمكن أن تكون أكبر من الكمية المحجوزة.")
