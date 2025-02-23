from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    email = fields.String(required=True)
    address = fields.String()
    address_verified = fields.Boolean(dump_only=True)
    profile_visibility = fields.String()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class UserProfileSchema(UserSchema):
    items = fields.Nested('ItemSchema', many=True, dump_only=True)
    requests = fields.Nested('RequestSchema', many=True, dump_only=True)
