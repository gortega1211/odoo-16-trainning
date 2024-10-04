from odoo import models, fields, api
from odoo.exceptions import UserError

from datetime import timedelta

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
    validity = fields.Integer(string="Validity", default=7)
    date_deadline = fields.Date(string="Date Deadline", compute="_compute_date_deadline", inverse="_inverse_validity")

    @api.depends("validity")
    def _compute_date_deadline(self):
        for record in self:
            create_date = record.create_date.date() if record.create_date else fields.Date.today()
            record.date_deadline = create_date + timedelta(days=record.validity)

    def _inverse_validity(self):
        for record in self:
            validity_timedelta = record.date_deadline - record.create_date.date()
            record.validity = validity_timedelta.days

    def accept_offer(self):
        for record in self:
            if record.property_id.state == "sold":
                raise UserError("This property has already been sold!")
            if record.property_id.state == "cancel":
                raise UserError("This property is canceled!")
            record.property_id.buyer_id = record.partner_id
            record.property_id.selling_price = record.price
            record.property_id.state = "sold"
            record.status = "accepted"
        return True

    def refuse_offer(self):
        for record in self:
            record.status = "refused"
        return True