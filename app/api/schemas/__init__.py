from marshmallow import Schema, fields

class PaginationSchema(Schema):
    page = fields.Integer()
    per_page = fields.Integer()
    total = fields.Integer()
    pages = fields.Integer()
