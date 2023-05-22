import requests
# to load .env
from dotenv import load_dotenv
import os
from python_sql_connector import add_plant, get_all_myplants, remove_plant

# Load variables from .env file
load_dotenv()

api_key = os.getenv("RAPID_API_KEY")
base_url = os.getenv("RAPID_API_URL")

load_dotenv()

user_input_plant = input('Please enter a house plant by common name or latin name,'
                         'or enter "My Plants" to view your plant collection.')

# Haven't started on the remove_plant logic in this file yet
# plant_name = input("Enter the name of a plant to remove it from your collection: ")

if user_input_plant == 'My Plants':
    get_all_myplants()

host = 'house-plants2.p.rapidapi.com'
url = f"{base_url}search"
querystring = {"query": user_input_plant}
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": host
}

response = requests.get(url, headers=headers, params=querystring)

full_data = response.json()
plant_id = full_data[0]['refIndex']
data = full_data[0]['item']


def replace_none(stat):
    if stat is None:
        return 'N/A'
    else:
        return stat


plant_data = {
    'latin_name': data.get('Latin name', 'N/A'),
    'common_name': ', '.join(data.get('Common name', [])),
    'light_level': replace_none(data.get('Light tolered')),
    'watering': data.get('Watering', 'N/A'),
    'climate': data.get('Climat', 'N/A'),
    'max_temp': data.get('Temperature max', {}),
    'min_temp': data.get('Temperature min', {}),
    'growth_speed': data.get('Growth', 'N/A'),
    'common_diseases': replace_none(data.get("Disease")),
    'image': data.get('Img', 'N/A')
}

def ask_disease(plant_data):
    if plant_data['common_diseases'] == 'N/A':
        return
    else:
        user_input_disease = input(f'Does your plant currently have any disease? Choose from: {plant_data["common_diseases"]}')
        return user_input_disease

ask_disease(plant_data)

def display_from_user_input(plant_data):
    return print(
        f'Latin name: {plant_data["latin_name"]}\n'
        f'Common name(s): {plant_data["common_name"]}\n'
        f'Ideal light: {plant_data["light_level"]}\n'
        f'Watering: {plant_data["watering"]}\n'
        f'Climate type: {plant_data["climate"]}\n'
        f'Max temperature: F:{plant_data["max_temp"]["F"]}, C:{plant_data["max_temp"]["C"]}\n'
        f'Min temperature: F:{plant_data["min_temp"]["F"]}, C:{plant_data["min_temp"]["C"]}\n'
        f'Growth speed: {plant_data["growth_speed"]}\n'
        f'Common diseases: {plant_data["common_diseases"]}\n'
        f'Image: {plant_data["image"]}\n'
        )

display_from_user_input(plant_data)

def ask_add_plant(data, plant_id):
    add_plant_question = input(f'Would you like to add {user_input_plant} to your My plants collection? Please enter "y" for yes, or "n" for no')
    if add_plant_question == 'n':
        print(f'{user_input_plant} was not added')
    elif add_plant_question == 'y':
        add_plant(data, plant_id)
    return data, plant_id


ask_add_plant(data, plant_id)
