from flask import Flask, redirect, url_for
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    jwt.init_app(app)
    db.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000"]}})

    CORS(app, supports_credentials=True)

    
    api = Api(app, version='1.0', title='ZipLink', description='ZipLink Application API')

    from app.backend.apis.v1.ZipUrl import api as link_ns

    api.add_namespace(link_ns, path='/api')

    return app