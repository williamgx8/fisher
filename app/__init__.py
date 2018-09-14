from flask import Flask

from app.models.book import db
from app.web import web
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    db.create_all(app=app)

    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    app.register_blueprint(web)
