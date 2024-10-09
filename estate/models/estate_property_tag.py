from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag Model"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="Color", default=1)

    _sql_constraints = [
        ("name_unique", "UNIQUE (name)", "The name must be unique."),
    ]
