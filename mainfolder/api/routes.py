from flask_restful import Resource
from api.model import Restaurants, Restaurants_Pizzas, Pizzas
from api.model import db
from flask import session
from flask import request


class Get_Restaurants(Resource):
    def get(self):
        all_restaurants=[]
        
        restaurants = Restaurants.query.all() 
        
        for restaurant in restaurants:
            
            restaurant_data={
                'id':restaurant.id,
                'name':restaurant.name,
                'address':restaurant.address
                
            }
            all_restaurants.append(restaurant_data)
            
        return all_restaurants
    
class Get_EachRestaurants(Resource):
    def get(self, id):
        restaurant = Restaurants.query.get(id)

        if restaurant:
            
            restaurant_data = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": []
            }

            pizzas = Pizzas.query.join(Restaurants_Pizzas).filter(
                Restaurants_Pizzas.restaurant_id == id
            ).all()

            for pizza in pizzas:
                pizza_data = {
                    "id": pizza.id,
                    "name": pizza.name,
                    "ingredients": pizza.ingredients
                }
                restaurant_data["pizzas"].append(pizza_data)

            return restaurant_data, 200  
        else:
            return {"error": "Restaurant not found"}, 404            
     
class Delete_Restaurants(Resource):
    def delete(self, id):
        restaurant = Restaurants.query.get(id)
        if restaurant:
            restaurant_pizzas = Restaurants_Pizzas.query.filter_by(restaurant_id=id).all()
            for restaurant_pizza in restaurant_pizzas:
                db.session.delete(restaurant_pizza)
                
                db.session.delete(restaurant)
                db.session.commit()
                
                return {}, 204
            else:
                

               return {"error": "Restaurant not found"}, 404
           
class Get_Pizzas(Resource):
    def get(self):
        all_pizza=[]
        
        pizzas= Pizzas.query.all()
        
        for pizza in pizzas:
            pizza_data={
            'id': pizza.id,
            'name': pizza.name ,
            'ingredients':pizza.ingredients
            }
            
            all_pizza.append(pizza_data)
        
        return all_pizza
    
class Post_RestaurantPizza(Resource):
    def post (self ):
        data= request.get_json()
        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')
        
        if not price or not pizza_id or not restaurant_id:
            return {'errors': ['[Lease enter the riht amounts]']}, 400
        
        pizza = Pizzas.query.get(pizza_id)
        restaurant = Restaurants.query.get(restaurant_id)
        
        if not pizza or not restaurant:
            return {'errors': ['Pizza or Restaurant not found']}, 404
        
        restaurant_pizza = Restaurants_Pizzas(
            price=price,
            pizza=pizza,
            restaurant=restaurant
        )
        
        db.session.add(restaurant_pizza)
        db.session.commit()
        
        pizza_data={
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
            
        }
        
        return pizza_data, 201


        
        
        
            
        
     