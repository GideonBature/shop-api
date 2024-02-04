from marshmallow import Schema, fields

class ProductSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    shop_id = fields.Str(required=True)


class ProductUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class ShopSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)