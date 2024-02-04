import os
from flask import Flask, request, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
import uuid
from resources.shop import blueprint as shop_blueprint
from resources.product import blueprint as product_blueprint
from db import db
import models

app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['API_TITLE'] = 'Shop REST API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.3'
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = 'bene'

jwt = JWTManager(app)

db.init_app(app)

api = Api(app)

with app.app_context():
    db.create_all()

api.register_blueprint(shop_blueprint)
api.register_blueprint(product_blueprint)