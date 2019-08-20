from database.db import db

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))

	def __init__(self, name):
		self.name = name


class City(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))

	def __init__(self, name):
		self.name = name


class Cidade(db.Model):
	idcidade = db.Column(db.Integer,primary_key=True,autoincrement=False,  nullable=False,unique=True)
	nome = db.Column(db.String(100))

	def __init__(self, idcidade, nome):
		self.idcidade = idcidade
		self.nome = nome

class Pesquisa(db.Model):
	idpesquisa = db.Column(db.Integer,primary_key=True,autoincrement=False,  nullable=False,unique=True)
	nome = db.Column(db.String(100))

	def __init__(self, idpesquisa, nome):
		self.idpesquisa = idpesquisa
		self.nome = nome

class Indicador(db.Model):
	idindicador = db.Column(db.Integer,primary_key=True,autoincrement=False,  nullable=False,unique=True)
	indicador = db.Column(db.String(200))

	def __init__(self, idindicador, indicador):
		self.idindicador = idindicador
		self.indicador = indicador

class Historico(db.Model):
	idhistorico = db.Column(db.Integer, primary_key=True, autoincrement=False,  nullable=False,unique=False)
	idcidade = db.Column(db.Integer, primary_key=False, autoincrement=False,  nullable=False,unique=False)
	idindicador = db.Column(db.Integer, primary_key=False, autoincrement=False,  nullable=False,unique=False)
	ano = db.Column(db.Integer, primary_key=False, autoincrement=False,  nullable=False,unique=False)
	valor = db.Column(db.String(200))

	def __init__(self,idcidade,idindicador,ano,valor):
		self.idcidade = idcidade
		self.idindicador = idindicador
		self.ano = ano
		self.valor = valor		