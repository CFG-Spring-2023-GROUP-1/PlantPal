import os
from dotenv import load_dotenv
import requests
# to load .env
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

api_key = os.getenv("RAPID_API_KEY")
base_url = os.getenv("RAPID_API_URL")

load_dotenv()

user_input = input('Please enter a house plant by common name or latin name.')
host = 'house-plants2.p.rapidapi.com'
url = f"{base_url}search"
querystring = {"query": user_input}
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": host
}

response = requests.get(url, headers=headers, params=querystring)
#
full_data = response.json()

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


print(
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
