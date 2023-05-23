from dotenv import load_dotenv # to load .env
import os, json


def house_plants_api():

    load_dotenv() # Load variables from .env file
    perenual_api_key = os.getenv("PERENUAL_API_KEY")
    base_URL= 'https://perenual.com/api/species-list?page=1&key=' + perenual_api_key
    return base_URL


def filter_sunlight(url,sunlight):

    if sunlight in ['full_shade', 'part_shade', 'sun-part_shade', 'full_sun']:
        return url+ '&sunlight=' + sunlight
    elif sunlight == '' or sunlight == None:
        return url
    else:
        print('Please enter a valid sunlight level: full_shade, part_shade, sun-part_shade, full_sun')
        

def low_maintanance(url,user_input):

    if isinstance(user_input, bool):
        if user_input == True:
            return url+ '&watering=minimum'
        elif user_input == False:
            return url 
        
    else:
        raise ValueError("Invalid input. Expected a boolean value.")
    
def preference(url,user_preference):

    preference_type = [
        "Palm",
        "Orchid",
        "Aglaonema",
        "Ficus elastica",
        "Dracaena"
    ]

    if user_preference in preference_type:
        return url + '&q=' + user_preference
    elif user_preference == '' or user_preference == None:
        return url




def filter_air_purifying(api_data,user_input):

    if isinstance(user_input, bool):
        if user_input is False:
            return api_data
        elif user_input == True:

            air_purify_plants = {
                "Abies alba", #this is for testing purposes
                "Dypsis lutescens",
                "Chlorophytum comosum",
                "Epipremnum aureum",
                "Anthurium andraeanum",
                "Chamaedorea seifrizii",
                "Chamaedorea elegans",
                "Dracaena marginata",
                "Dracaena fragrans",
                "Ficus benjamina",
                "Chrysanthemum morifolium",
                "Ficus elastica",
                "Dendrobium",
                "Dieffenbachia",
                "Aloe vera",
                "Dracaena fragrans",
                "Boston fern",
                "Hedera helix",
                "Spathiphyllum",
                "Rhapis excelsa",
                "Sansevieria trifasciata",
                "Philodendron bipinnatifidum",
                "Gerbera jamesonii",
                "Phalaenopsis",
                "Musa acuminata"
            }

            matched_items = []

            for plant in api_data['data']:
                scientific_name = plant['scientific_name']
                if isinstance(scientific_name, list):
                    if any(name in scientific_name for name in air_purify_plants):
                        matched_items.append(plant)
                else:
                    if scientific_name in air_purify_plants:
                        matched_items.append(plant)

            # Print the matched items
            if matched_items:
                return matched_items
            else:
                print("None of the plant names exist in the JSON data.")
        
    else:
        raise ValueError("Invalid input. Expected a boolean value.")

