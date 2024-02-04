from flask import jsonify, request
import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import shops
from schemas import ShopSchema

blueprint = Blueprint('shop', __name__, description='Operations on Shops')

@blueprint.route('/shop/<shop_id>')
class Shop(MethodView):
    @blueprint.response(200, ShopSchema)
    def get(self, shop_id):
        try:
        # Attempt to retrieve the shop details using the shop_id as the key
            return jsonify(shops[shop_id])
        except KeyError:
            abort(404, message="Shop not found")
        

    def delete(self, shop_id):
        try:
        # Attempt to delete the product using the product_id as the key
            del shops[shop_id]
            return jsonify({"message": "Shop deleted successfully"})
        except KeyError:
            abort(404, message="Shop not found")


@blueprint.route('/shop')
class ShopList(MethodView):
    @blueprint.response(200, ShopSchema(many=True))
    def get(self):
        return jsonify(list(shops.values()))
    
    @blueprint.arguments(ShopSchema)
    @blueprint.response(201, ShopSchema)
    def post(self, shop_data):

        shop_data = request.json
        shop_id = uuid.uuid4().hex

        for shop in shops.values():
            if shop_data['name'] == shop['name']:
                abort(400, message="Shop already exists")


        shop = {**shop_data, 'id': shop_id}
        shops[shop_id] = shop
        return shop