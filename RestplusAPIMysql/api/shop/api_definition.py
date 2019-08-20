from flask_restplus import fields
from api.myapi import api

product = api.model('Product', {
    'id': fields.Integer(readOnly=True, description='The identifier of the product'),
    'name': fields.String(required=True, description='Product name'),
})

city = api.model('City', {
    'id': fields.Integer(readOnly=True, description='The identifier of the city'),
    'name': fields.String(required=True, description='City name'),
})

cidade = api.model('Cidade', {
    'idcidade': fields.Integer(readOnly=True, description='The identifier of the city'),
    'nome': fields.String(required=True, description='City name'),
})

pesquisa = api.model('Pesquisa', {
    'idpesquisa': fields.Integer(readOnly=True, description='The identifier'),
    'nome': fields.String(required=True, description='Name'),
})

historico = api.model('Historico', {
    'idhistorico': fields.Integer(required=True, description='Chave primaria historico'),
    'idcidade': fields.Integer(required=True, description='Indicador da cidade'),
    'idindicador': fields.Integer(required=True, description='Indicador do indicador de pesquisa'),
    'ano': fields.Integer(required=True, description='Ano da pesquisa'),
    'nome': fields.String(required=True, description='Valor da pesquisa'),
})


indicador = api.model('Indicador', {
    'idindicador': fields.Integer(readOnly=True, description='The identifier'),
    'indicador': fields.String(required=True, description='Name'),
})

category = api.model('Product category', {
    'id': fields.Integer(readOnly=True, description='The identifier of the category'),
    'name': fields.String(required=True, description='Category name'),
})

pagination = api.model('One page of item', {
    'page': fields.Integer(description='Current page'),
    'pages': fields.Integer(description='Total pages'),
    'items_per_page': fields.Integer(description='Items per page'),
    'total_items': fields.Integer(description='Total amount of items')
})

page_with_products = api.inherit('Page with products', pagination, {
    'items': fields.List(fields.Nested(product))
})

page_with_cities = api.inherit('Page with cities', pagination, {
    'items': fields.List(fields.Nested(city))
})

page_with_cidades = api.inherit('Page with cities', pagination, {
    'items': fields.List(fields.Nested(cidade))
})

page_with_pesquisas = api.inherit('Page with pesquisas', pagination, {
    'items': fields.List(fields.Nested(pesquisa))
})

page_with_indicadores = api.inherit('Page with indicadores', pagination, {
    'items': fields.List(fields.Nested(indicador))
})

page_with_historicos = api.inherit('Page with indicadores', pagination, {
    'items': fields.List(fields.Nested(historico))
})