from flask import Flask

from app.web import web
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    app.register_blueprint(web)
