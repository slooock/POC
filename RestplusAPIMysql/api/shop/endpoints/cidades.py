from flask import request
from api.myapi import api
from flask_restplus import Resource
from api.shop.api_definition import page_with_cidades, cidade
from api.shop.parsers import pagination_parser as pagination
from database.dtos import Cidade
from api.shop.domain_logic import create_product
from flask_restplus import Namespace

from database import db as database

namespace = Namespace('cidades/', description='Cities of Brazil')

@namespace.route('/')
class Offer(Resource):

    @api.expect(pagination)
    @api.marshal_with(page_with_cidades)
    def get(self):
        args = pagination.parse_args(request)
        page = args.get('page', 1)
        items_per_page = args.get('items_per_page', 10)
        cidades = Cidade.query.paginate(page, items_per_page, error_out=False)
        print(cidades)
        return cidades

    @api.expect(cidade)
    def post(self):
        create_cidade(request.json)
        return None, 200

@namespace.route('id/<int:id>')
@api.response(404, 'There is no cidade with this ID yet.')
class CidadeItem(Resource):
    @api.marshal_with(cidade)
    def get(self, id):
        return Cidade.query.filter_by(idcidade = id).first()

@namespace.route('nomeCidade/<string:nomeCidade>')
@api.response(404, 'There is no cidade with this Name yet.')
class CidadeItemNome(Resource):

    @api.marshal_with(cidade)
    def get(self, nomeCidade):
        print(Cidade.query.filter_by(nome = nomeCidade))
        return Cidade.query.filter_by(nome = nomeCidade).all()
        
	








