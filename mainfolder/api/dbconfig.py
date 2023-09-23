from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db= SQLAlchemy()

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzarestaurants.db'

migrate=Migrate(app, db)

api=Api(app)

# import the routes
from api import routes