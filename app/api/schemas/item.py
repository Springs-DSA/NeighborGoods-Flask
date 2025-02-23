from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String()
    tags = fields.List(fields.String())
    owner_id = fields.Integer(dump_only=True)
    available = fields.Boolean()
    can_leave_node = fields.Boolean()
    loan_period = fields.Integer()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
