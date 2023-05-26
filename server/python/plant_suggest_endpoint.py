from flask import Flask, jsonify, request
from plant_suggest_response import get_recommendations_data, plant_data
from plant_suggest_filter import house_plants_api
app = Flask(__name__)

@app.route('/sugguestion', methods=['POST'])
def get_recommendations_endpoint():
    # Retrieve data from the request payload
    user_input = request.json

    # Extract the input parameters from the user_input
    plants = user_input['plants']

    # Call the get_recommendations_data function with the input parameters
    recommendations_data = get_recommendations_data(plants)

     # Return the response as JSON
    response = {
        "message": "This is the sugguestion response"
    }

    # Return the recommendations data as JSON response
    return jsonify(recommendations_data)



if __name__ == '__main__':
    app.run()