from marshmallow import Schema, fields

class RequestSchema(Schema):
    id = fields.Integer(dump_only=True)
    item_id = fields.Integer(required=True)
    requester_id = fields.Integer(dump_only=True)
    status = fields.String(dump_only=True)
    request_period = fields.Integer(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    
    # Nested relationships
    item = fields.Nested('ItemSchema', dump_only=True)
    requester = fields.Nested('UserSchema', dump_only=True)
