from flask import Blueprint
from controllers.greeting_controller import hello

greeting_blueprint = Blueprint('greeting', __name__)

greeting_blueprint.route('/<string:name>', methods=['GET'])(hello)
