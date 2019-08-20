from database import db
from database.dtos import Product
from database.dtos import City

def create_product(data):
    name = data.get('name')
    product = Product(name)
    db.add(product)

def read_product(data):
    pass

def update_product(data):
    pass

def delete_product(data):
    pass

def create_city(data):
    name = data.get('name')
    city = City(name)
    db.add(city)

def read_city(data):
    pass

def update_city(data):
    pass

def delete_city(data):
    pass