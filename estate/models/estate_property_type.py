from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"

    name = fields.Char(string="Name", required=True)

    _sql_constraints = [
        ("name_unique", "UNIQUE (name)", "The name must be unique."),
    ]
