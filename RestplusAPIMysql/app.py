from flask import Flask, Blueprint
import settings
from api.myapi import api
from api.shop.endpoints.products import namespace as productsnamespace
from api.shop.endpoints.cities import namespace as citiesnamespace
from api.shop.endpoints.cidades import namespace as cidadesnamespace
from api.shop.endpoints.pesquisas import namespace as pesquisasnamespace
from api.shop.endpoints.indicadores import namespace as indicadoresnamespace
from api.shop.endpoints.historico import namespace as historiconamespace

from database.db import db

app = Flask(__name__)

def configure_app(app):
    app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_EXPANSION
    app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VAL
    app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODS


def init_app(app):
    configure_app(app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(cidadesnamespace)
    api.add_namespace(pesquisasnamespace)
    api.add_namespace(indicadoresnamespace)
    api.add_namespace(historiconamespace)
    app.register_blueprint(blueprint)

    db.init_app(app)


def main():
    init_app(app)
    app.run(debug=settings.FLASK_DEBUG, threaded=settings.FLASK_THREADED)

if __name__ == "__main__":
    main()