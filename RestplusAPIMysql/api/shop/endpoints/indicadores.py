from flask import request
from api.myapi import api
from flask_restplus import Resource
from api.shop.api_definition import page_with_indicadores, indicador
from api.shop.parsers import pagination_parser as pagination
from database.dtos import Indicador
from flask_restplus import Namespace

from database import db as database

namespace = Namespace('indicadores/', description='Indicadores do IBGE')

@namespace.route('/')
class Offer(Resource):

    @api.expect(pagination)
    @api.marshal_with(page_with_indicadores)
    def get(self):
        args = pagination.parse_args(request)
        page = args.get('page', 1)
        items_per_page = args.get('items_per_page', 10)
        indicadores = Indicador.query.paginate(page, items_per_page, error_out=False)
        return indicadores

@namespace.route('id/<int:id>')
@api.response(404, 'There is no cidade with this ID yet.')
class IndicadorItem(Resource):
	@api.marshal_with(indicador)
	def get(self, id):
		return Indicador.query.filter_by(idindicador= id).first()