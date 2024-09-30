from odoo import models, fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"

    property_id = fields.Many2one(comodel_name="estate.property", string="Property")
    price = fields.Float(string="Price", digits=(12, 3))
    status = fields.Selection(string="Status", selection=[
        ("accepted", "Accepted"),
        ("refused", "Refused"),
    ], copy=False)
    partner_id = fields.Many2one(comodel_name="res.partner", string="Partner")