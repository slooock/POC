from flask import request
from api.myapi import api
from flask_restplus import Resource
from api.shop.api_definition import page_with_pesquisas, pesquisa
from api.shop.parsers import pagination_parser as pagination
from database.dtos import Pesquisa
from flask_restplus import Namespace

from database import db as database

namespace = Namespace('pesquisas/', description='Pesquisas do IBGE')

@namespace.route('/')
class Offer(Resource):

    @api.expect(pagination)
    @api.marshal_with(page_with_pesquisas)
    def get(self):
        args = pagination.parse_args(request)
        page = args.get('page', 1)
        items_per_page = args.get('items_per_page', 10)
        pesquisas = Pesquisa.query.paginate(page, items_per_page, error_out=False)
        return pesquisas

@namespace.route('id/<int:id>')
@api.response(404, 'There is no pesquisa with this ID yet.')
class PesquisaItem(Resource):
	@api.marshal_with(pesquisa)
	def get(self, id):
		return Pesquisa.query.filter_by(idpesquisa = id).first()
	








