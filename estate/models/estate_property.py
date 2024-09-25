from odoo import models, fields

from datetime import timedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Model Estate Property"
    _order = 'id desc'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="PostCode")
    date_availability = fields.Date(string="Date Availability", copy=False, default=fields.Date.today() + timedelta(days=90))
    expected_price = fields.Float(string="Expected Price", digits=(12, 3), required=True)
    selling_price = fields.Float(string="Selling Price", digits=(12, 3), readonly=True, copy=False)
    bedrooms = fields.Integer(string="BedRooms", default=2)
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
