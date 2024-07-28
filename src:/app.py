from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    profile_image = db.Column(db.String(255), nullable=True)
    recipes = db.relationship('Recipe', backref='user', lazy=True)



class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_name = db.Column(db.String(100), nullable=False)
    recipe_method = db.Column(db.Text, nullable=False)
    is_public = db.Column(db.Boolean, default=False)
    ingredients = db.relationship('RecipeIngredient', backref='recipe', lazy=True)



class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    ingredient_category = db.Column(db.String(50), nullable=True)
    calories = db.Column(db.Integer, nullable=True)
    protein = db.Column(db.Integer, nullable=True)
    fat = db.Column(db.Integer, nullable=True)
    recipes = db.relationship('RecipeIngredient', backref='ingredient', lazy=True)



class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False)


# Create tables
db.create_all()


class UserSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)


class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)


class RecipeSchema(Schema):
    user_id = fields.Integer(required=True)
    recipe_name = fields.String(required=True)
    recipe_method = fields.String(required=True)
    is_public = fields.Boolean()


class IngredientSchema(Schema):
    ingredient_name = fields.String(required=True)
    description = fields.String()
    ingredient_category = fields.String()
    calories = fields.Integer()
    protein = fields.Integer()
    fat = fields.Integer()


class RecipeIngredientSchema(Schema):
    ingredient_id = fields.Integer(required=True)
    quantity = fields.Float(required=True)
    unit = fields.String(required=True)


@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify({'error': e.messages}), 400


@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        # Validate the input data
        UserSchema().load(data)
        # Hash the password
        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password_hash=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already exists'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        # Validate the input data
        LoginSchema().load(data)
        user = User.query.filter_by(email=data['email']).first()
        if user and check_password_hash(user.password_hash, data['password']):
            return jsonify({'message': 'Login successful', 'user_id': user.id})
        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/recipe', methods=['POST'])
def create_recipe():
    try:
        data = request.json
        # Validate the input data
        RecipeSchema().load(data)
        new_recipe = Recipe(
            user_id=data['user_id'],
            recipe_name=data['recipe_name'],
            recipe_method=data['recipe_method'],
            is_public=data.get('is_public', False)
        )
        db.session.add(new_recipe)
        db.session.commit()
        return jsonify({'message': 'Recipe created successfully', 'recipe_id': new_recipe.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/ingredient', methods=['POST'])
def create_ingredient():
    try:
        data = request.json
        # Validate the input data
        IngredientSchema().load(data)
        new_ingredient = Ingredient(
            ingredient_name=data['ingredient_name'],
            description=data.get('description'),
            ingredient_category=data.get('ingredient_category'),
            calories=data.get('calories'),
            protein=data.get('protein'),
            fat=data.get('fat')
        )
        db.session.add(new_ingredient)
        db.session.commit()
        return jsonify({'message': 'Ingredient added successfully', 'ingredient_id': new_ingredient.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/recipe/<int:recipe_id>/ingredients', methods=['POST'])
def add_ingredient_to_recipe(recipe_id):
    try:
        data = request.json
        # Validate the input data
        RecipeIngredientSchema().load(data)
        new_recipe_ingredient = RecipeIngredient(
            recipe_id=recipe_id,
            ingredient_id=data['ingredient_id'],
            quantity=data['quantity'],
            unit=data['unit']
        )
        db.session.add(new_recipe_ingredient)
        db.session.commit()
        return jsonify({'message': 'Ingredient added to recipe'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/public_recipes', methods=['GET'])
def get_public_recipes():
    try:
        # Query to get all public recipes
        public_recipes = Recipe.query.filter_by(is_public=True).all()
        result = []
        for recipe in public_recipes:
            result.append({
                'id': recipe.id,
                'user_id': recipe.user_id,
                'recipe_name': recipe.recipe_name,
                'recipe_method': recipe.recipe_method
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/search_recipes', methods=['GET'])
def search_recipes():
    try:
        recipe_name = request.args.get('recipe_name')
        if not recipe_name:
            return jsonify({'error': 'Recipe name is required'}), 400
        recipes = Recipe.query.filter(Recipe.recipe_name.ilike(f'%{recipe_name}%')).all()
        result = []
        for recipe in recipes:
            result.append({
                'id': recipe.id,
                'user_id': recipe.user_id,
                'recipe_name': recipe.recipe_name,
                'recipe_method': recipe.recipe_method,
                'is_public': recipe.is_public
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/search_ingredients', methods=['GET'])
def search_ingredients():
    try:
        ingredient_name = request.args.get('ingredient_name')
        if not ingredient_name:
            return jsonify({'error': 'Ingredient name is required'}), 400
        ingredients = Ingredient.query.filter(Ingredient.ingredient_name.ilike(f'%{ingredient_name}%')).all()
        result = []
        for ingredient in ingredients:
            result.append({
                'id': ingredient.id,
                'ingredient_name': ingredient.ingredient_name,
                'description': ingredient.description,
                'ingredient_category': ingredient.ingredient_category,
                'calories': ingredient.calories,
                'protein': ingredient.protein,
                'fat': ingredient.fat
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
