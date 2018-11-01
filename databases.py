from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name, price, quantity, description, seller):
  new_product= Product(
    name=name,
    price=price,
    quantity=quantity,
    description=description,
    seller=seller)
  session.add(new_product)
  session.commit()
  

def update_product(id, name, price):
  update_product = session.query(
       Product).filter_by(
       id=id).first()
  update_product.name = name
  update_product.price = price
  session.commit()


def delete_product(id):
  session.query(Product).filter_by(
    id=id).delete()
  session.commit()


def get_product(id):
  pass
