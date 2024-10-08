from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag Model"

    name = fields.Char(string="Name", required=True)

    _sql_constraints = [
        ("name_unique", "UNIQUE (name)", "The name must be unique."),
    ]
