# PIZZA RESTAURANT

The Restaurant API is a robust web service designed to manage restaurant and pizza-related information efficiently. This API enables users to perform various operations, including retrieving restaurant details, managing pizza data, and associating pizzas with specific restaurants. It is built using Flask, SQLAlchemy, and marshmallow-sqlalchemy.

## Installation

1. Clone this repo

git clone  https://github.com/karanja03/week1-p4-code-challenge

2. Navigate to the project directory using cd

3. Create a virtual environment (optional but recommended):
    python -m venv venv

4. Activate the virtual environment:

source venv/bin/activate

5. Install the project dependencies:
   pip install -r requirements.txt

6. Apply the database migrations
    flask db init
    flask db migrate
    flask db upgrade


# FEATURES

The Restaurant API offers the following key features:

1. Retrieve Restaurants: Get a list of all registered restaurants, including their names and addresses.

2. Retrieve Pizzas: Fetch a list of all available pizzas, complete with details like ingredients and creation/update timestamps.

3. Retrieve Specific Restaurant: Get detailed information about a specific restaurant by providing its unique ID.

4. Retrieve Specific Pizza: Get detailed information about a specific pizza by providing its unique ID.

5. Delete Restaurant: Delete a restaurant by specifying its unique ID, including all associated records.

6. Delete Pizza: Delete a pizza by specifying its unique ID, including all associated records.

7. Retrieve Restaurant-Pizza Associations: Fetch a list of all restaurant-pizza associations, including prices.

8. Create Restaurant-Pizza Association: Create a new restaurant-pizza association, specifying the pizza, restaurant, and price

## API Endpoints
The following API endpoints are available:

1. GET /restaurants: Retrieve a list of all registered restaurants.
2. GET /restaurants/int:id: Get details of a specific restaurant by its ID.
3. DELETE /restaurants/int:id: Delete a restaurant by its ID.
4. GET /pizzas: Retrieve a list of all available pizzas.
5. GET /pizzas/int:id: Get details of a specific pizza by its ID.
6. DELETE /pizzas/int:id: Delete a pizza by its ID.
7. GET /restaurantspizza: Fetch a list of restaurant-pizza associations.
8. POST /restaurantspizza: Create a new restaurant-pizza association, specifying the pizza, restaurant, and price.
9. For detailed information on how to use these endpoints, refer to the API documentation or the source code.

## Models
The Restaurant API includes three main models:

1. Restaurant: Represents a restaurant with attributes such as name and address. Restaurants can be associated with multiple pizzas.

2. Pizza: Represents a pizza with attributes such as name, ingredients, and creation/update timestamps. Pizzas can be associated with multiple restaurants.

3. RestaurantPizza: Represents the association between restaurants and pizzas, including the price. This model allows you to associate a pizza with a specific restaurant along with its price.

## Contributing
Contributions to this project are welcome! If you would like to contribute, please follow these steps:

Fork the repository on GitHub.
Create a new branch for your feature or bug fix.
Make your changes and commit them with clear and concise messages.
Push your changes to your fork.
Create a pull request to the main repository's main branch.
## License
This project is licensed under the MIT License - see the LICENSE file for details.