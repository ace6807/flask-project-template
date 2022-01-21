from flask import Flask
from app.main import blueprint as main_blueprint
from config import Config

def create_app(config: Config):
    app = Flask(__name__)
    app.config.from_object(config)    
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app:Flask):
    pass

def register_blueprints(app: Flask):
    app.register_blueprint(main_blueprint)
