from odoo import models, fields, api
from odoo.exceptions import UserError

from datetime import timedelta

import logging

_logger = logging.getLogger(__name__)

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"
    _order = 'id desc'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From", copy=False, default=fields.Date.today() + timedelta(days=90))
    expected_price = fields.Float(string="Expected Price", digits=(12, 3), required=True)
    selling_price = fields.Float(string="Selling Price", digits=(12, 3), readonly=True, copy=False)
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(string="Garden Orientation", selection=[
        ("north", "North"),
        ("south", "South"),
        ("east", "East"),
        ("west", "West"),
    ])
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(string="State", default="new", selection=[
        ("new", "New"),
        ("received", "Offer Received"),
        ("accepted", "Offer Accepted"),
        ("sold", "Sold"),
        ("cancel", "Cancel"),
    ], required=True, copy=False)
    property_type_id = fields.Many2one(comodel_name="estate.property.type", string="Property Type")
    buyer_id = fields.Many2one(comodel_name="res.partner", string="Buyer", copy=False)
    salesman_id = fields.Many2one(comodel_name="res.users", string="Salesman", default=lambda self: self.env.user)
    tag_ids = fields.Many2many(comodel_name="estate.property.tag", string="Property Tags")
    offer_ids = fields.One2many(comodel_name="estate.property.offer", inverse_name="property_id", string="Offers")
    total_area = fields.Integer(string="Total Area", compute="_compute_total_area")
    best_price = fields.Float(string="Best Price", digits=(12, 3), compute="_compute_best_price")

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price')) if record.offer_ids else 0.0

    @api.onchange("garden")
    def _onchange_garden(self):
        self.garden_area = 10 if self.garden else 0
        self.garden_orientation = "north" if self.garden else False

        # if not self.garden:
        #     return {
        #         'warning': {
        #             'title': "Warning",
        #             'message': f'The property: {self.name}, doesn\'t have a garden!'
        #         }
        #     }

    def sold_property(self):
        for record in self:
            if record.state == "cancel":
                raise UserError("Canceled properties can't be sold.")
            record.state = "sold"
        return True

    def cancel_property(self):
        for record in self:
            if record.state == "sold":
                raise UserError("Solded properties can't be cancel.")
            record.state = "cancel"
        return True
