# Recipe API

## The Problem

In todays world many people are becoming more concerned about the quality and nutrional value of there food. Food prepared commercially are often full of additives, preservatives and ingredients that many people refuse or cannot eat, such as those with allergies or dietary requirments. As a result, homemade meals are increasing in popularity as they hold a better control of what ingredients go into them and how nutritious they can be. 

Creating healthy and nutritous homemade meals can be challenging for many reasons, such as, lack of knowledge, recipe management, nutrional tracking and finding recipes. Most people are unsure of their nutrional needs and its hard to keep track of those said nutrients and recipes that follow along with them, and for those who are just starting out in their healthy lifestyle, its hard to find sites where people have shared their recipes for free.

## The Goal

The goal of this recipe API is to address these challenges by providing a clear solution for managing homemade recipes and heres how:

1. Centralized Recipe Management
    the recipe API allows user to create, read, update and delete food recipes in a centralized database, this helps simplify the process of having multiple recipes and allowing ease of access and modifications.

2. Nutritional Information Integretion
    each ingredient will have a detailed nutrional information such as calories, protien and fat. This allows users to track and meet their nutrional requirements

3. Ingredient Management
    Users can manage a database of ingredients, including adding new ingredients, update existing ones and specifying nutritional content. This allows users to accurately measure and include many ingredients into their recipes

4. Public and Private Recipes
    Users can mark recipes as public or private. This allows users to access a wide range of recipes shared by other users. Private recipes will remain accessible only to the creator, maintaining privacy

5. Search and Discover Recipes
    The API allows user to search for recipes by name or ingredients allowing for an ease of access for those with specific dietary requirements or preferences

6. User Authentication and Profile Management
    The APi supports user registration and authentication, which allows users to create and manage their profiles. this ensures that users data is secure and personalized

Overall, the Recipe API has a structured, effecint and user friendly solution to the problem which allows better nutrion and overall health.

# ERD

Below is the approved ERD design that the recipe API will be following

![ERD Diagram](/docs:/Images/RecipeAPI_ERD_design.png)

# Trello Board

Below is my Kanban board, which i used Trello to create. It shows each card discription and shows progress that was made throughout the project

![Trello Board](/docs:/Images/1.png)

![Trello Board](/docs:/Images/2.png)

![Trello Board](/docs:/Images/3.png)

![Trello Board](/docs:/Images/4.png)

![Trello Board](/docs:/Images/5.png)

![Trello Board](/docs:/Images/0.png)

![Trello Board](/doc:/Images/6.png)

![Trello Board](/docs:/Images/7.png)

![Trello Board](/docs:/Images/8.png)

![Trello Board](/docs:/Images/9.png)

![Trello Board](/docs:/Images/10.png)

![Trello Board](/docs:/Images/11.png)


# Third Party Services, Packages, and Dependancies

The Recipe API uses several third party services, packages and dependancies to allow it to run effectively and effeciently. Below is a list with explanations of their roles and benefits.

1. Flask
    - Flask is a lightweight WSGI web application framework in Python. its job is to create the web server and handle the HTTP requests and responses. it is the foundation of the API endpoints. its beneficial for the API as its easy to use, flexible and modular and has extensive documentation and a large support community

2. SQLAlchemy
    - SQLAlchemy is an SQL toolkit and Object-Relational Mapping (ORM) library for python. its job is to interact with the database in an object-oriented manner.SQLAlchemy allows for the definition of database models (tables) as Python classes and provides methods to query and manipulate data.its beneficial for the API as it simplifies the database interactions and reduces the boilerplate code. it also provides a high level ORM and supports multiple database backends

3. Flask-SQLAlchemy
    - Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy. its role is to intergrate SQLAlchemy with Flask which helps benefit the setup and usage of SQLAlchemy with Flask by simplifying it. it also adds useful helpers and tools to flasks core.

4. Marshmallow
    - Marshmallow is a library used for object serialization and deserialization, input validation and data transformation. its job is to serialize python objects to JSON and deserialize JSON to python objects.its benefits include highly customizable hooks and extension points, it simplifies data serialization and validation and intergrates well with SQLAlchemy.

5. marshmallow-sqlalchemy
    - Marshmallow-sqlalchemy is an intergration library that combines SQLAlchemy models to Marshmallow Schemas. its role is to provide automatic generation of Marshmallows schemas based on SQLAlchemy models which allows for better and easier serializations and deserializations of database records. its beneficial as it reduces boilerplate code by automatically generating schemas and ensures consistancy between database models and API schemas

6. Werkzueg
    - Werkzeug is a WSGI web application library which is used by Flask as its underlying library that handles HTTP requests and responses. its benefits include, providing robust tools for handling WSGI requests, support advanced features such as URL routing and request/response management and its well intergrated with Flask and other WSGI-compliant frameworks

7. SQLite
    - SQLite is a C-language library that provides a lightweight, disk based database and doesn't require a seperate server process. it is the API's main database engine and uses it to store users data, recipes, ingredients and the relationships between them


The third party services, packages and dependancies allow the API to follow the best practices in web development, including secure password storage, data validation, and effecient database management.


# Benefits and Drawbacks of SQLite

### Benefits
SQLite is and easy to set up and use database as it does not require a seperate server process which allows for a simply deployment. it is also self contained, lightweight and requires no configuration or administration which benefits small to medium sized applications. since its light weight, it also provides great performance for read heavy operations and small to medium sized datasets. one of its biggest benefits is that its cross platform, between Windows, macOS, Linux and Android, and its FREE!

### Drawbacks
SQLite uses a simplified locking mechanism that may not handle high levels of concurrent write operations as many other advanced database systems have, this also leads into its scalability, as it is more suitable for small to medium sized  applications and wont be able to scale well with larger apllications. SQLite also doesn't prove some of the functions found in some of the bigger database systems such as stored procedures and user defined functions. SQLite also doesn't provide the same level of backup, recovery and security as some othe database sytems provide.

In summary, SQLite is a good choice for the Recipe API due to its simplicity, ease of use and lightweight nature. it is well suited for small to medium applications, however, for more larger ones, PostgreSQL or MySQL might be more appropriate.


# ORM in The Recipe API

Features of SQLAlchemy
Object-Relational Mapping (ORM):
Allows developers to use Python classes and objects to interact with the database instead of writing raw SQL queries.
Schema Definition:
Define database tables as Python classes with attributes representing columns, making it easy to understand and manage.
Relationships:
Easily define relationships between tables (e.g., one-to-many, many-to-one) using foreign keys and relationship functions.
Query Building:
Construct complex queries using Python code, making data retrieval and manipulation straightforward.
Transactions:
Supports transactions to ensure data integrity by grouping multiple database operations into a single unit of work.
Session Management:
Manages database connections and operations within a transactional context using sessions.
Flexibility:
Supports multiple database systems (e.g., SQLite, PostgreSQL, MySQL), allowing easy switching between them.
Performance:
Includes features like lazy loading and query caching to optimize database interactions.
Purpose of SQLAlchemy
Simplify Database Interactions: Provides a high-level, Pythonic interface to the database, making it easier to work with and maintain.
Abstract Complexity: Hides the complexity of SQL and database management, allowing developers to focus on application logic.
Functionalities of SQLAlchemy in This App
Defining Models:
Models like User, Recipe, Ingredient, and RecipeIngredient are defined as Python classes, representing database tables.

    ```class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    profile_image = db.Column(db.String(255), nullable=True)
    recipes = db.relationship('Recipe', backref='user', lazy=True)```

Creating and Managing the Database Schema:
Automatically generates the necessary SQL commands to create tables and relationships.

    ``` db.create_all() ```

Querying the Database:
Provides an easy way to query data. For example, fetching all public recipes:

    ``` public_recipes = Recipe.query.filter_by(is_public=True).all() ```

Managing Transactions:
Ensures all database operations are executed within a transactional context to maintain data integrity.

    ``` new_user = User(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit() ```

Handling Relationships:
Easily navigate between related objects. For example, accessing the recipes created by a user:

    ```user.recipes```

Example of Relationships
Here’s an example of defining and using relationships:

    ```class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_name = db.Column(db.String(100), nullable=False)
    recipe_method = db.Column(db.Text, nullable=False)
    is_public = db.Column(db.Boolean, default=False)
    ingredients = db.relationship('RecipeIngredient', backref='recipe', lazy=True)```

    ```class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False)```

    # Querying related objects
    recipe = Recipe.query.first()
    for ingredient in recipe.ingredients:
    print(ingredient.ingredient_id, ingredient.quantity, ingredient.unit)


### Conclusion
SQLAlchemy makes working with databases in Python easier by allowing you to use Python objects to represent database tables and relationships. It simplifies database queries, ensures data integrity with transactions, and optimizes performance. This makes your code more readable, maintainable, and efficient.


# Implemented Models
User Model
Represents the users of the application.
Attributes:
id: Primary key, unique identifier for each user.
first_name: User's first name.
last_name: User's last name.
email: User's email address, unique.
password_hash: Hashed password for security.
date_created: Timestamp of when the user was created.
profile_image: URL or path to the user's profile image.
Relationships:
recipes: One-to-many relationship with the Recipe model. A user can create multiple recipes.

    ```class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    profile_image = db.Column(db.String(255), nullable=True)
    recipes = db.relationship('Recipe', backref='user', lazy=True) ```

2. Recipe Model

    Represents recipes created by users.
    Attributes:
    id: Primary key, unique identifier for each recipe.
    user_id: Foreign key, links to the user who created the recipe.
    recipe_name: Name of the recipe.
    recipe_method: Detailed method or instructions for the recipe.
    is_public: Boolean flag indicating if the recipe is public.

Relationships:
user: Many-to-one relationship with the User model. A recipe is created by one user.
    ingredients: One-to-many relationship with the RecipeIngredient model. A recipe can have multiple ingredients.

    class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_name = db.Column(db.String(100), nullable=False)
    recipe_method = db.Column(db.Text, nullable=False)
    is_public = db.Column(db.Boolean, default=False)
    ingredients = db.relationship('RecipeIngredient', backref='recipe', lazy=True)


3. Ingredient Model
Represents ingredients that can be used in recipes.

Attributes:
id: Primary key, unique identifier for each ingredient.
ingredient_name: Name of the ingredient.
description: Description of the ingredient.
ingredient_category: Category of the ingredient (e.g., vegetable, meat).
calories: Caloric value of the ingredient.
protein: Protein content of the ingredient.
fat: Fat content of the ingredient.

Relationships:
recipes: One-to-many relationship with the RecipeIngredient model. An ingredient can be used in multiple recipes.

    ```class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    ingredient_category = db.Column(db.String(50), nullable=True)
    calories = db.Column(db.Integer, nullable=True)
    protein = db.Column(db.Integer, nullable=True)
    fat = db.Column(db.Integer, nullable=True)
    recipes = db.relationship('RecipeIngredient', backref='ingredient', lazy=True)

RecipeIngredient Model
Represents the association between recipes and ingredients, including the quantity and unit of each ingredient used in a recipe.

Attributes:
id: Primary key, unique identifier for each record.
recipe_id: Foreign key, links to the recipe.
ingredient_id: Foreign key, links to the ingredient.
quantity: Quantity of the ingredient used in the recipe.
unit: Unit of measurement for the quantity (e.g., grams, cups).

Relationships:
recipe: Many-to-one relationship with the Recipe model. A recipe ingredient is associated with one recipe.
ingredient: Many-to-one relationship with the Ingredient model. A recipe ingredient is associated with one ingredient.

    ```class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False)```


# How Relationships Aid Database Implementation
Data Integrity:
The use of foreign keys ensures that relationships between tables are maintained. For example, each recipe must be associated with a valid user, and each ingredient in a recipe must be linked to an existing ingredient.
Simplified Queries:
Relationships allow for simplified and more readable queries. For example, accessing all recipes created by a user or all ingredients in a recipe can be done through relationship attributes rather than complex join operations.

    ```user = User.query.get(user_id)
        user_recipes = user.recipes

    recipe = Recipe.query.get(recipe_id)
    recipe_ingredients = recipe.ingredients

Efficient Data Retrieval:
Relationships enable efficient data retrieval by leveraging SQLAlchemy's lazy loading and eager loading strategies. This allows related data to be fetched only when needed, reducing unnecessary database queries.

Consistency in Data Handling:
By defining relationships at the model level, the application ensures consistency in how data is handled and accessed. This makes the codebase more maintainable and less prone to errors.

Flexibility and Extensibility:
The defined relationships provide a flexible foundation for extending the database schema in the future. For example, adding new features like comments on recipes or ratings can be done without disrupting the existing schema.

Example: Adding a New Ingredient to a Recipe
Here’s an example of how the relationships help in adding a new ingredient to a recipe:

Assume we have recipe_id and ingredient_id, and quantity and unit are provided by the user

    ```recipe_ingredient = RecipeIngredient(
    recipe_id=recipe_id,
    ingredient_id=ingredient_id,
    quantity=data['quantity'],
    unit=data['unit']
    )
    db.session.add(recipe_ingredient)
    db.session.commit()```

Retrieve the recipe with its ingredients

    ```recipe = Recipe.query.get(recipe_id)
    for ingredient in recipe.ingredients:
    print(f"Ingredient ID: {ingredient.ingredient_id}, Quantity: {ingredient.quantity}, Unit: {ingredient.unit}")```

In this example, the relationships between Recipe, Ingredient, and RecipeIngredient allow us to easily manage and retrieve the ingredients associated with a recipe. This demonstrates how the relationships streamline database operations and enhance the overall functionality of the application.



# How to use Recipe API

# Installation

## Prerequisites:
    
    - Python3
    - Bash
    - Git
    - Pip

1. Open a terminal and navigate to a directory you'd like to clone the repository to.

2. Clone the GitHub repository via SSH:
    ```git clone git@github.com:Noah-Morgan2/T2A2.git```
or via HTTPS:
    ```git clone https://github.com/Noah-Morgan2/T2A2.git```

3. Navigate to the src/ directory in the cloned repository
    ``` cd T2A2/src/```

4. Create a virtual environment and activate it

macOS:
    ```python3 -m venv venv```
    ```source venv/bin.activate```

Windows:
    ```python3 -m venv venv```
    ```venv/Scripts/activiate```

5. Install Dependancies
    ```pip3 install -r requirements.txt```

6. Set up database
    ```python3
    >>> from app import db
    >>> db.create_all()
    >>> exit()```

7. run the application
    ```Flask run```


1. Register a New User

HTTP Verb: POST

Path: /register

Required Body Data:
    
   ```{ "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "password": "securepassword" }```
        
Response:

Success (201):
    
        ```{
        "message": "User registered successfully"
        }```

Failure (400):

        ```{
    "error": "Email already exists"
        }```

Failure (500):

        ```{
        "error": "Internal server error message"
     }```

2. Login a User

HTTP Verb: POST

Path: /login

    Required Body Data:
    ```{
    "email": "john.doe@example.com",
    "password": "securepassword"
    }```

Response:

Success (200):

       ``` {
    "message": "Login successful",
    "user_id": 1
    }```

Failure(401):

        ```{
    "message": "Invalid credentials"
    }```

Failure(500):

        ```{
    "error": "Internal server error message"
    }```
3. Create a New Recipe

HTTP Verb: POST

Path: /recipe

Required Body Data:

    ```{
    "user_id": 1,
    "recipe_name": "Spaghetti Carbonara",
    "recipe_method": "Cook pasta, add sauce",
    "is_public": true
    }```

Response:

Success (201):
    ```{
    "message": "Recipe created successfully",
    "recipe_id": 1
    }```

Failure(500):
    ```{
    "error": "Internal server error message"
    }```

4. Create a New Ingredient

HTTP Verb: POST

Path: /ingredient

Required Body Data:

    ```{
    "ingredient_name": "Tomato",
    "description": "A red juicy fruit",
    "ingredient_category": "Vegetable",
    "calories": 18,
    "protein": 1,
    "fat": 0
    }```

Response:

Success (201):
    ```{
    "message": "Ingredient added successfully",
    "ingredient_id": 1
    }```

Failure (500):
    ```{
    "error": "Internal server error message"
    }```

5. Add an Ingredient to a Recipe

HTTP Verb: POST

Path: /recipe/<int:recipe_id>/ingredients

Required Body Data:

    ```{
    "ingredient_id": 1,
    "quantity": 100,
    "unit": "grams"
    }```

Response:

Success (201):

    ```{
    "message": "Ingredient added to recipe"
    }```

Failure (500):
    ```{
    "error": "Internal server error message"
    }```

6. Retrieve Public Recipes

HTTP Verb: GET

Path: /public_recipes

Required Body Data: None

Response:

Success (200):
        ```[
        {
           "id": 1,
           "user_id": 1,
          "recipe_name": "Spaghetti Carbonara",
         "recipe_method": "Cook pasta, add sauce"
        }
    ]```

Failure (500):

    ```{
    "error": "Internal server error message"
    }```

7. Search Recipes by Name

HTTP Verb: GET

Path: /search_recipes

Required Query Parameter:

recipe_name: The name of the recipe to search for.

Example Request:

    /search_recipes?recipe_name=Spaghetti

Response:

Success (200):
     ```[
        {
            "id": 1,
            "user_id": 1,
            "recipe_name": "Spaghetti Carbonara",
            "recipe_method": "Cook pasta, add sauce",
         "is_public": true
        }
    ]```

Failure (400):
    ```{
        "error": "Recipe name is required"
    }```

Failure (500):
        ```{
        "error": "Internal server error message"
    }```

8. Search Ingredients by Name

HTTP Verb: GET

Path: /search_ingredients

Required Query Parameter:

ingredient_name: The name of the ingredient to search for.

Example Request:

    /search_ingredients?ingredient_name=Tomato

Response:

Success (200):
        ```[
     {
         "id": 1,
         "ingredient_name": "Tomato",
            "description": "A red juicy fruit",
            "ingredient_category": "Vegetable",
            "calories": 18,
         "protein": 1,
         "fat": 0
     }
    ]```

Failure (400):
        ```{
        "error": "Ingredient name is required"
    }```

Failure (500):
    ```{
        "error": "Internal server error message"
    }```







