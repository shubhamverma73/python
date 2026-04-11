from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Int(required=True)
    role = fields.Str(required=True)
    content = fields.Str(required=True)

class ItemResponseSchema(Schema):
    status = fields.Int()
    message = fields.Str()
    data = fields.Raw()