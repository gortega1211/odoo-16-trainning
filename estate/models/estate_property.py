from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property description"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="date availability")
    expected_price = fields.Float(string="Expected Price", digits=(12, 3))
    selling_price = fields.Float(string="selling Price", digits=(12, 3))
    bedrooms = fields.Integer(string="BedRooms")
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(string="Garden Orientation",selection=[
        ("north","North"),
        ("south", "south"),
        ("east","east"),
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


