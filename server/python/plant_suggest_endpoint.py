from flask import Blueprint, Flask, jsonify, request
from plant_suggest_response import get_recommendations_data
from plant_suggest_filter import get_plant_data_url
import requests

plant_suggestions_blueprint = Blueprint('plant_suggestions', __name__)


@plant_suggestions_blueprint.route('/home', methods=['GET'])
def welcome_endpoint():
    return jsonify("Welcome to PlantPal!")


@plant_suggestions_blueprint.route('/suggestion', methods=['POST'])
def get_recommendations_endpoint():

    user_input = request.json
    plants = user_input['plants']

    # Call the get_recommendations_data function with the input parameters
    recommendations_data = get_recommendations_data(plants)
    if not recommendations_data:
        response = {
            "message": "No recommended plants found."
        }
    else:
        formatted_data = []
        for recommendation in recommendations_data:
            formatted_recommendation = {
                "recommendation_number": recommendation["recommendation_number"],
                "common_name": recommendation["common_name"],
                "image_url": recommendation["image_url"]
            }
            formatted_data.append(formatted_recommendation)
        
        response = {
            "message": "This is the suggestion response",
            "data": formatted_data
        }
    return jsonify(response), 200


@plant_suggestions_blueprint.route('/filter', methods=['POST'])
def get_plant_filter_endpoint():

    user_input = request.get_json()
    sunlight = user_input.get('sunlight')
    low_maintenance = user_input.get('low_maintenance')
    preference = user_input.get('preference')

    url = get_plant_data_url(sunlight, low_maintenance, preference)

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data), 200
    else:
        return jsonify({"error": "Unable to fetch data"}), response.status_code
