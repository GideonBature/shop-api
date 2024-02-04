from flask import Flask, request, jsonify
from flask_smorest import Api
import uuid
from db import shops, products
from resources.shop import blueprint as shop_blueprint
from resources.product import blueprint as product_blueprint

app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['API_TITLE'] = 'Shop REST API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.3'
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

api = Api(app)
api.register_blueprint(shop_blueprint)
api.register_blueprint(product_blueprint)