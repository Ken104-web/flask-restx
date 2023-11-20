from flask import Flask
from .extensions import api, db , migrate
from .routes import ns

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'


    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)


    api.add_namespace(ns)

    return app