from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"
    _order = "sequence, name"

    name = fields.Char(string="Name", required=True)
    property_ids = fields.One2many(comodel_name="estate.property", inverse_name="property_type_id", string="Properties")
    sequence = fields.Integer(string="Sequence", default=1, help="Used to order property types. Lower is better.")

    _sql_constraints = [
        ("name_unique", "UNIQUE (name)", "The name must be unique."),
    ]
