import flask
from flask import Flask, jsonify, request
# Import the os package
import os

# Import the openai package
import openai


from api.route.route import blueprint

#  The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix='/clothes')


@app.route("/test")
def hello():
    return "test"

