from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from api.model import db
from flask_sqlalchemy import SQLAlchemy





app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzarestaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.__init__(app)
migrate=Migrate(app, db)
api=Api(app)

# import the routes
# from api import routes
with app.app_context():
    db.create_all()
if __name__=="__main__":
    app.run(debug=True, port=5555)
