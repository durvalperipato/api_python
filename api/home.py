# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


class HomeApi(Resource):
    """
    Flask-resftul resource for returning db.meal collection.
    :Example:
    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config
    # Create flask app, config, and resftul api, then add MealApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(MealApi, '/meal/<meal_id>')
    """

    def get(self) -> Response:
        """
        GET response method for single documents in meal collection.
        :return: JSON object
        """
        output = "Hello Api"
        return jsonify({'result': output})