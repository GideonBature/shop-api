from flask import request, jsonify
import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import products
from schemas import ProductSchema, ProductUpdateSchema

blueprint = Blueprint('product', __name__, description='Operations on Products')

@blueprint.route('/product/<product_id>')
class Product(MethodView):
    @blueprint.response(200, ProductSchema)
    def get(self, product_id):
        try:
        # Attempt to retrieve the product details using the product_id as the key
            return jsonify(products[product_id])
        except KeyError:
        # Return a message and status code 404 if the product is not found
            return jsonify({"message": "Product not found"}), 404


    @blueprint.arguments(ProductUpdateSchema)
    @blueprint.response(200, ProductSchema)
    def put(self, product_data, product_id):
         # Get the product data from the request JSON
        product_data = request.json
    
        try:
        # Attempt to update the product using the product_id as the key
        # |= merge the dictionaries
            products[product_id] |= product_data
            return jsonify(products[product_id])
        except KeyError:
        # Return a message and status code 404 if the product is not found
            return jsonify({"message": "Product not found"}), 404


    def delete(self, product_id):
        try:
        # Attempt to delete the product using the product_id as the key
            del products[product_id]
            return jsonify({"message": "Product deleted successfully"})
        except KeyError:
        # Return a message and status code 404 if the product is not found
            return jsonify({"message": "Product not found"}), 404

@blueprint.route('/product')
class ProductList(MethodView):
    @blueprint.response(200, ProductSchema(many=True))
    def get(self):
        return jsonify(list(products.values()))
    
    @blueprint.arguments(ProductSchema)
    @blueprint.response(201, ProductSchema)
    def post(self, new_product):

        product_data = request.json
        product_id = uuid.uuid4().hex

        for product in products.values():
            if product_data['name'] == product['name']:
                abort(400, message="Product already exists")


        product = {**product_data, 'id': product_id}
        products[product_id] = product
        return product
