import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
# db_drop_and_create_all()

## ROUTES

@app.route('/drinks')
def get_drinks():
    drinks = [ drink.short() for drink in Drink.query.all() ]

    if len(drinks) == 0:
        abort(404)

    return jsonify({
            'success': True,
            'drinks': drinks
        }), 200

@requires_auth('get:drinks-detail')
@app.route('/drinks-detail')
def get_drinks_detail():
    drinks = [ drink.long() for drink in Drink.query.all() ]

    if len(drinks) == 0:
        abort(404)

    return jsonify({
        'success': True,
        'drinks': drinks
    }), 200

@requires_auth('post:drinks')
@app.route('/drinks', methods=['POST'])
def create_drink():
    body = request.get_json()
    title = body.get('title', None)
    recipe = json.dumps(body.get('recipe', None))

    try:
        drink = Drink(title=title, recipe=recipe)
        drink.insert()

        return jsonify({
            'success': True,
            'drinks': [drink.long()]
        }), 200

    except:
        abort(422)

@requires_auth('patch:drinks')
@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
def update_drink(drink_id):
    body = request.get_json()
    title = body.get('title', None)
    recipe = json.dumps(body.get('recipe', None))
    drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

    if drink is None:
        abort(404)
    
    try:
        drink.title = title
        drink.recipe = recipe
        drink.update()

        return jsonify({
            'success': True,
            'drinks': [drink.long()]
        }), 200

    except:
        abort(422)

@requires_auth('delete:drinks')
@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
def delete_drink(drink_id):
    drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

    if drink is None:
        abort(404)
    
    try:
        drink.delete()

        return jsonify({
            'success': True,
            'delete': drink_id
        }), 200

    except:
        abort(422)

## Error Handling
'''
Example error handling for unprocessable entity
'''
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

@app.errorhandler(404)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": 'Unathorized'
    }), 401

@app.errorhandler(AuthError)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": error.status_code,
                    "message": error.error['description']
                    }), error.status_code