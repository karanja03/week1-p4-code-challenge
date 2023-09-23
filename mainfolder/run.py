from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from api.model import db
from flask_sqlalchemy import SQLAlchemy
from api.routes import Get_EachRestaurants, Post_RestaurantPizza, Get_Pizzas,Get_Restaurants, Delete_Restaurants




app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzarestaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.__init__(app)
migrate=Migrate(app, db)
api=Api(app)

# import the routes
# from api import routes

api.add_resource(Get_EachRestaurants,'/restaurants/<string:id>')
api.add_resource(Post_RestaurantPizza,'/restaurants_pizza/<string:id>')
api.add_resource(Get_Pizzas,'/pizza')
api.add_resource(Get_Restaurants,'/restaurants')
api.add_resource(Delete_Restaurants,'/restaurants/<string:id>')




with app.app_context():
    db.create_all()
if __name__=="__main__":
    app.run(debug=True, port=5555)
