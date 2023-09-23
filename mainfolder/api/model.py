from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import validates, relationship
import datetime
Base = declarative_base()

db = SQLAlchemy()
class Pizzas(db.Model):
    __tablename__='pizzas_table'
    
    id=db.Column(db.String(255), primary_key=True)
    name=db.Column(db.String, nullable=False)
    ingredients=db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)    
    def __repr__(self):
        return f'{self.id}, {self.name}, {self.ingredients}, {self.created_at}, {self.updated_at}'
    

class Restaurants_Pizzas(db.Model):
    __tablename__ = 'restaurants_pizzas'
    
    id=db.Column(db.String(255), primary_key=True)
    pizza_id=db.Column(db.String(255), db.ForeignKey("pizzas.id"))
    restaurant_id=db.Column(db.String(255), db.ForeignKey("restaurants.id"))
    price=db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)    
    
    restaurants= db.relationship('Restaurants', backref='parent')
    def __repr__(self):
        return f'{self.id}, {self.pizza_id}, {self.restaurant_id},{self.price}, {self.created_at}, {self.updated_at}'
    
    

class Restaurants(db.Model):
    __tablename__ = 'restaurants_table'
    
    id=db.Column(db.String(255), primary_key=True)
    name=db.Column(db.String(50), unique=True, nullable=False)
    address=db.Column(db.String, nullable=False)
    
    @validates('name')
    def validates_name(self, value):
        if len(value)>50:
            raise ValueError('Name Must be less than 50 characters')
        return value
    
    
    # price = Column(Float, CheckConstraint('price >= 1 AND price <= 30'), nullable=False)
    @validates('price')
    def validates_price(self,value):
        if( 1<=value<=30):
            return value
        raise ValueError('Please Enter a Price Range between 1-30')
    
    def __repr__(self):
        return f'{self.id}, {self.name}, {self.address}'


