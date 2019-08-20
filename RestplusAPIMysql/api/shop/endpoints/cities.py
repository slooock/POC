from flask import request
from api.myapi import api
from flask_restplus import Resource
from api.shop.api_definition import page_with_cities, city
from api.shop.parsers import pagination_parser as pagination
from flask_restplus import Namespace
from database.dtos import City
from api.shop.domain_logic import create_city

from database import db as database

namespace = Namespace('shop/cities/', description='cities of brazil')

@namespace.route('/')
class Offer(Resource):
	
	@api.expect(pagination)
	@api.marshal_with(page_with_cities)
	def get(self):
		args = pagination.parse_args(request)
		page = args.get('page', 1)
		items_per_page = args.get('items_per_page', 10)
		cities = City.query.paginate(page, items_per_page, error_out=False)
		return cities


	@api.expect(city)
	def post(self):
		create_city(request.json)
		return None, 200

