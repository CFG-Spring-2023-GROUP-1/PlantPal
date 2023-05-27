import json, requests
from .plant_suggest_filter import filter_sunlight, low_maintanance, preference, house_plants_api, filter_air_purifying

"""
Fuction Requirements

Allow the user to search for plants (using the Perenual API) to find 
recommendations for plants that might fit their requirements (e.g. little 
sunlight, air purifying etc), preferences (e.g. palms, orchids) and lifestyle (e.g. low maintenance).

"""

def get_user_input():
    print('Welcome to the plant suggestion tool. Please answer the following questions to find your perfect plant match.')
    input_sunlight = input('How much sunlight does your home get? (full_shade, part_shade, sun-part_shade, full_sun): ')
    input_low_maintenance = input('Do you want a low maintenance plant? (True/False): ')
    input_low_maintenance = bool(input_low_maintenance)
    input_preference = input('Do you have a preference for a certain type of plant? (Palm, Orchid, Aglaonema, Ficus elastica, Dracaena): ')
    input_air_purifying = input('Do you want an air purifying plant? (True/False): ')
    input_air_purifying = bool(input_air_purifying)
    return input_sunlight, input_low_maintenance, input_preference, input_air_purifying

def print_recommendations(plants):
    if plants:
        for i, plant in enumerate(plants[:3], 1):
            print(f"Recommendation {i}: {plant['common_name']}, {plant['default_image']['small_url']}")

    else:
        print("No plants found with the given filter.")

def print_plant_data(plant_query_url):

    headers = {'Authorization': house_plants_api()}  # Create headers dictionary
    response = requests.get(plant_query_url, headers=headers)
   
    data = response.json()
    # filter out plants with id > 3000 because only premium users can access them
    filtered_data = [plant for plant in data['data'] if plant['id'] <= 3000] 
    print_recommendations(filtered_data)


def plant_data(plant_query_url):
    headers = {'Authorization': house_plants_api()}  # Create headers dictionary
    response = requests.get(plant_query_url, headers=headers)   
    data = response.json()
    return data


def get_recommendations_data(plants):
    if plants:
        recommendations = []
        for i, plant in enumerate(plants[:3], 1):
            recommendation = {
                "recommendation_number": i,
                "common_name": plant["common_name"],
                "image_url": plant["default_image"]["small_url"]
            }
            recommendations.append(recommendation)

        return json.dumps(recommendations)
    else:
        return json.dumps([])



"""User input"""
# input_sunlight, input_low_maintenance, input_preference, input_air_purifying = get_user_input()
# query_url = filter_sunlight(house_plants_api(), input_sunlight)
# query_url = low_maintanance(query_url, input_low_maintenance)
# query_url = preference(query_url, input_preference)
# print_plant_data(query_url)


# result_list = filter_air_purifying(plant_data(query_url),input_air_purifying)
# print_recommendations(result_list)
# print(get_recommendations_data(result_list))


# print(plant_data(house_plants_api()))






