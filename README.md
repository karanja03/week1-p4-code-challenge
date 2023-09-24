# RESTAURANT PIZZA API
The Restaurant Pizza API is a RESTful web service built using Flask-RESTful. It allows users to interact with restaurant and pizza data. Users can retrieve a list of all restaurants, get details about a specific restaurant including its associated pizzas, delete a restaurant along with its associated pizzas, and more.



## Installation

1. Clone the repository:

     git clone git@github.com:karanja03/week1-p4-code-challenge.git

2. Navigate to the project directory:
      cd /Phase4/CodeChallenges/week1-p4-code-challenge$ 

3. pip install -r requirements.txt

4. Create an SQLite database for the API

5. Apply the database migrations:

    flask db upgrade

6. Run the application

    python3 run.py


The API will be accessible at http://localhost:5555.


## USAGE

The API provides several endpoints to interact with restaurant and pizza data. You can use HTTP methods such as GET, POST, and DELETE to perform various actions.


## ENDPOINTS
GET /restaurants

Retrieve a list of all restaurants.

GET /restaurants/<id>

Retrieve details about a specific restaurant, including its associated pizzas.

DELETE /restaurants/<id>

Delete a restaurant along with its associated pizzas.

GET /pizzas

Retrieve a list of all pizzas.

POST /restaurant-pizza

Create a new entry for a pizza at a restaurant, including its price, pizza ID, and restaurant ID.

## CONTRIBUTING
Contributions are welcome! If you'd like to contribute to this project, please contact me @wambuik@gmail.com

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.
