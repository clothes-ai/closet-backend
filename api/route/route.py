#routes package (blueprints)
##Blueprints: Flask routing is setup by using the application instance as decorator on your route functions. This forces you to declare all the routes in the same file as the app instance. This is not maintainable in a larger flask app with many routes
##The way to break up routes into separate files is to use Flask blueprints. If your Flask app is api based then you can match files names to resources. Therefore, you would have a user.py file in a routes directory that contains all routes related to the user and this can be extended to other resources. Blueprints are a great way to organize your routes and a must use for large applications.
##When a user visit URL he will be redirected to the specific page. The router is the address to which the user will be redirected. For example, if the user wants to visit the clothes page then he will type http://localhost:5000/clothes
## When flask generates a URL from an endpoint it will link the view function with a blueprint.


from flask import Blueprint
# from controller.clothesController import index, create, insert, delete,  read, update
from api.controller.clothesController import index, create, insert, delete,  read, update

blueprint = Blueprint('clothes', __name__)

blueprint.route('/', methods=['GET'])(index) #/clothes/
blueprint.route('/create', methods=['GET'])(create) #/clothes/create
blueprint.route('/insert', methods=['GET'])(insert) #/clothes/insert
blueprint.route('/delete', methods=['DELETE'])(delete)
blueprint.route('/read', methods=['GET'])(read)
blueprint.route('/update', methods=['GET'])(update)