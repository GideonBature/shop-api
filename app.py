from flask import Flask, request, jsonify
import uuid
from db import shops, products

app = Flask(__name__)


@app.route('/shop', methods=['POST'])
def create_shops():
    """
    Create a new shop based on the data provided in the request.
    
    Returns:
    dict: The created shop data including a unique id.
    """
    # Extract shop data from the request
    shop_data = request.json
    
    # Generate a unique id for the shop
    shop_id = uuid.uuid4().hex
    
    # Create the shop dictionary including the generated id
    shop = {**shop_data, 'id': shop_id}
    
    # Store the shop in the collection using the generated id as key
    shops[shop_id] = shop
    
    # Return the created shop data
    return shop


@app.route('/shop')
def get_shops():
    """
    Get a list of all shops.
    
    Returns:
        dict: A dictionary containing a list of all shops.
    """
    return jsonify({"shops": list(shops.values())})


@app.route('/shop/<shop_id>')
def get_shop(shop_id):
    """
    Get a shop by its ID.

    Args:
        shop_id (str): The ID of the shop to retrieve.

    Returns:
        dict: The details of the shop with the specified ID.
    """
    try:
        # Attempt to retrieve the shop details using the shop_id as the key
        return jsonify(shops[shop_id])
    except KeyError:
        # Return a message and status code 404 if the shop is not found
        return jsonify({"message": "Shop not found"}), 404
    

@app.route('/shop/<shop_id>', methods=['DELETE'])
def delete_shop(shop_id):
    """
    Delete a shop by its ID.

    Args:
        shop_id (str): The ID of the product to delete.

    Returns:
        dict: A message indicating that the product was deleted.
    """
    try:
        # Attempt to delete the product using the product_id as the key
        del shops[shop_id]
        return jsonify({"message": "Product deleted successfully"})
    except KeyError:
        # Return a message and status code 404 if the product is not found
        return jsonify({"message": "Shop not found"}), 404
    

@app.route('/product', methods=['POST'])
def create_products():
    """
    Create a new product for a specific shop.

    Parameters:
        shop_id (str): The id of the shop.
            Required to be passed in the request's JSON data.

    Returns:
        dict: The created product.
    """
    # Get the new product data from the request's JSON
    new_product = request.json

    # Check if the shop_id exists in the shops dictionary
    if new_product['shop_id'] not in shops:
        return {"message": "Shop not found"}, 404

    # Generate a unique product id
    product_id = uuid.uuid4().hex

    # Add the new product to the products dictionary with the generated product id
    products[product_id] = new_product

    # Return the created product
    return new_product


@app.route('/product')
def get_products():
    """
    Endpoint to get a list of all products.

    Returns:
        dict: A dictionary containing a list of all products.
    """
    return jsonify({"products": list(products.values())})


@app.route('/product/<product_id>')
def get_product(product_id):
    """
    Get the details of a product by its ID.

    Args:
        product_id (str): The ID of the product to retrieve.

    Returns:
        dict: The details of the product with the specified ID.
    """
    try:
        # Attempt to retrieve the product details using the product_id as the key
        return jsonify(products[product_id])
    except KeyError:
        # Return a message and status code 404 if the product is not found
        return jsonify({"message": "Product not found"}), 404
    

@app.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update the details of a product by its ID.

    Args:
        product_id (str): The ID of the product to update.

    Returns:
        dict: The updated product details.
    """
    # Get the product data from the request JSON
    product_data = request.json
    
    # Check if the required fields are present in the product data
    if 'price' not in product_data or 'name' not in product_data:
        return jsonify({"message": "Missing required fields"}), 400
    
    try:
        # Attempt to update the product using the product_id as the key
        # |= merge the dictionaries
        products[product_id] |= product_data
        return jsonify(products[product_id])
    except KeyError:
        # Return a message and status code 404 if the product is not found
        return jsonify({"message": "Product not found"}), 404


@app.route('/product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete a product by its ID.

    Args:
        product_id (str): The ID of the product to delete.

    Returns:
        dict: A message indicating that the product was deleted.
    """
    try:
        # Attempt to delete the product using the product_id as the key
        del products[product_id]
        return jsonify({"message": "Product deleted successfully"})
    except KeyError:
        # Return a message and status code 404 if the product is not found
        return jsonify({"message": "Product not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)