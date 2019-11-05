from flask import request
from api.myapi import api
from flask_restplus import Resource
from api.shop.api_definition import page_with_historicos, historico
from api.shop.parsers import pagination_parser as pagination
from database.dtos import Historico
from flask_restplus import Namespace
from database.dtos import Cidade

from database import db as database

namespace = Namespace('historicos/', description='Historico do IBGE')

@namespace.route('/')
class Offer(Resource):

    @api.expect(pagination)
    @api.marshal_with(page_with_historicos)
    def get(self):
        args = pagination.parse_args(request)
        page = args.get('page', 1)
        items_per_page = args.get('items_per_page', 10)
        historicos = Historico.query.paginate(page, items_per_page, error_out=False)
        return historicos        

@namespace.route('NomeCidade/<string:nomeCidade>')
@api.response(404, 'There is no historico with this Name yet.')
class historicoCidadeNome(Resource):

    @api.expect(pagination)
    @api.marshal_with(page_with_historicos)
    def get(self, nomeCidade):
        args = pagination.parse_args(request)
        page = args.get('page', 1)
        items_per_page = args.get('items_per_page', 10)

        cidade = Cidade.query.filter_by(nome = nomeCidade).first()

        historico = Historico.query.filter_by(idcidade = cidade.idcidade).paginate(page, items_per_page, error_out=False)

        return historico


@namespace.route('idCidade/<string:idCidade>')
@api.response(404, 'There is no historico with this Name yet.')
class historicoCidadeId(Resource):

    @api.expect(pagination)
    @api.marshal_with(page_with_historicos)
    def get(self, idCidade):
        args = pagination.parse_args(request)
        page = args.get('page', 1)
        items_per_page = args.get('items_per_page', 10)

        
        cidade = Cidade.query.filter_by(idcidade = idCidade).first()

        historico = Historico.query.filter_by(idcidade = cidade.idcidade).paginate(page, items_per_page, error_out=False)

        return historico

'''
@namespace.route('id/<int:id>')
@api.response(404, 'There is no cidade with this ID yet.')
class PesquisaItem(Resource):
	@api.marshal_with(historico)
	def get(self, id):
		return Historico.query.filter_by(idhistorico= id).first()
'''		