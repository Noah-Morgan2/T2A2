from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from datetime import datetime
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    profile_image = db.Column(db.String(200))
    recipes = db.relationship('Recipe', backref='user', lazy=True)


# Define the Recipe model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_name = db.Column(db.String(100), nullable=False)
    recipe_method = db.Column(db.String, nullable=False)
    is_public = db.Column(db.Boolean, default=False)
    ingredients = db.relationship('RecipeIngredient', backref='recipe', lazy=True)


# Define the Ingredient model
class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String)
    ingredient_category = db.Column(db.String(50))
    calories = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    recipes = db.relationship('RecipeIngredient', backref='ingredient', lazy=True)


# Define the RecipeIngredient model
class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False)


# Define Marshmallow schemas for serialization and validation
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


class RecipeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Recipe
        load_instance = True


class IngredientSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Ingredient
        load_instance = True


class RecipeIngredientSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RecipeIngredient
        load_instance = True


# Initialize schemas
user_schema = UserSchema()
recipe_schema = RecipeSchema()
ingredient_schema = IngredientSchema()
recipe_ingredient_schema = RecipeIngredientSchema()


# Error handling
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = jsonify(code=e.code, name=e.name, description=e.description).data
    response.content_type = "application/json"
    return response


@app.errorhandler(Exception)
def handle_generic_exception(e):
    response = jsonify(code=500, name="Internal Server Error", description=str(e))
    response.status_code = 500
    return response


# User routes
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        user = user_schema.load(data)
        db.session.add(user)
        db.session.commit()
        return user_schema.jsonify(user), 201
    except Exception as e:
        return handle_generic_exception(e)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return user_schema.jsonify(user)


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    try:
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.email = data['email']
        user.password_hash = data['password_hash']
        user.profile_image = data.get('profile_image')
        db.session.commit()
        return user_schema.jsonify(user)
    except Exception as e:
        return handle_generic_exception(e)


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    except Exception as e:
        return handle_generic_exception(e)


# Recipe routes
@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    try:
        recipe = recipe_schema.load(data)
        db.session.add(recipe)
        db.session.commit()
        return recipe_schema.jsonify(recipe), 201
    except Exception as e:
        return handle_generic_exception(e)


@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return recipe_schema.jsonify(recipe)


@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    data = request.get_json()
    try:
        recipe.recipe_name = data['recipe_name']
        recipe.recipe_method = data['recipe_method']
        recipe.is_public = data.get('is_public', recipe.is_public)
        db.session.commit()
        return recipe_schema.jsonify(recipe)
    except Exception as e:
        return handle_generic_exception(e)


@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    try:
        db.session.delete(recipe)
        db.session.commit()
        return jsonify({'message': 'Recipe deleted successfully'})
    except Exception as e:
        return handle_generic_exception(e)


@app.route('/recipes', methods=['GET'])
def list_recipes():
    recipes = Recipe.query.all()
    return jsonify(recipe_schema.dump(recipes, many=True))


# Ingredient routes
@app.route('/ingredients', methods=['POST'])
def create_ingredient():
    data = request.get_json()
    try:
        ingredient = ingredient_schema.load(data)
        db.session.add(ingredient)
        db.session.commit()
        return ingredient_schema.jsonify(ingredient), 201
    except Exception as e:
        return handle_generic_exception(e)


@app.route('/ingredients/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id):
    ingredient = Ingredient.query.get_or_404(ingredient_id)
    return ingredient_schema.jsonify(ingredient)


@app.route('/ingredients/<int:ingredient_id>', methods=['PUT'])
def update_ingredient(ingredient_id):
    ingredient = Ingredient.query.get_or_404(ingredient_id)
    data = request.get_json()
    try:
        ingredient.ingredient_name = data['ingredient_name']
        ingredient.description = data.get('description')
        ingredient.ingredient_category = data.get('ingredient_category')
        ingredient.calories = data.get('calories')
        ingredient.protein = data.get('protein')
        ingredient.fat = data.get('fat')
        db.session.commit()
        return ingredient_schema.jsonify(ingredient)
    except Exception as e:
        return handle_generic_exception(e)


@app.route('/ingredients/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient(ingredient_id):
    ingredient = Ingredient.query.get_or_404(ingredient_id)
    try:
        db.session.delete(ingredient)
        db.session.commit()
        return jsonify({'message': 'Ingredient deleted successfully'})
    except Exception as e:
        return handle_generic_exception(e)


@app.route('/ingredients', methods=['GET'])
def list_ingredients():
    ingredients = Ingredient.query.all()
    return jsonify(ingredient_schema.dump(ingredients, many=True))


# Recipe-Ingredient routes
@app.route('/recipes/<int:recipe_id>/ingredients', methods=['POST'])
def add_ingredient_to_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    data = request.get_json()
    try:
        recipe_ingredient = recipe_ingredient_schema.load(data)
        recipe_ingredient.recipe_id = recipe_id
        db.session.add(recipe_ingredient)
        db.session.commit()
        return recipe_ingredient_schema.jsonify(recipe_ingredient), 201
    except Exception as e:
        return handle_generic_exception(e)


@app.route('/recipes/<int:recipe_id>/ingredients/<int:ingredient_id>', methods=['PUT'])
def update_ingredient_in_recipe(recipe_id, ingredient_id):
    recipe_ingredient = RecipeIngredient.query.filter_by(
        recipe_id=recipe_id, ingredient_id=ingredient_id).first_or_404()
    data = request.get_json()
    try:
        recipe_ingredient.quantity = data['quantity']
        recipe_ingredient.unit = data['unit']
        db.session.commit()
        return recipe_ingredient_schema.jsonify(recipe_ingredient)
    except Exception as e:
        return handle_generic_exception(e)


@app.route('/recipes/<int:recipe_id>/ingredients/<int:ingredient_id>', methods=['DELETE'])
def remove_ingredient_from_recipe(recipe_id, ingredient_id):
    recipe_ingredient = RecipeIngredient.query.filter_by(
        recipe_id=recipe_id, ingredient_id=ingredient_id).first_or_404()
    try:
        db.session.delete(recipe_ingredient)
        db.session.commit()
        return jsonify({'message': 'Ingredient removed from recipe successfully'})
    except Exception as e:
        return handle_generic_exception(e)


@app.route('/public/recipes', methods=['GET'])
def list_public_recipes():
    recipes = Recipe.query.filter_by(is_public=True).all()
    return jsonify(recipe_schema.dump(recipes, many=True))


@app.route('/search/recipes', methods=['GET'])
def search_recipes():
    query = request.args.get('query')
    recipes = Recipe.query.filter(
        Recipe.recipe_name.like(f'%{query}%')).all()
    return jsonify(recipe_schema.dump(recipes, many=True))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
