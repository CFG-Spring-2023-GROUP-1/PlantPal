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


# remove plant from My Plants that matches select_plant user input
def remove_from_my_plants(plants):
    select_plant = input('Enter the scientific (Latin) name of the plant you want to remove: ')
    chosen_entry = [plant for plant in plants if plant[2].lower() == select_plant.lower()]
    while not chosen_entry:
        print('Plant not found, please try again.')
        select_plant = input('Enter the scientific (Latin) name of the plant you want to remove: ')
        chosen_entry = [plant for plant in plants if plant[2].lower() == select_plant.lower()]
    remove_plant(select_plant)
    search_plant()


# Show user each plant in their collection
def display_my_plants():
    try:
        plants = get_all_myplants()
        if plants:
            print(f'My Plants:')
            for plant in plants:
                print(plant)
        elif not plants:
            print('Your plant collection is empty.')
            return
        # ask user if they want to remove any plant from displayed collection
        ask_remove_plant = input('Would you like to remove a plant from your collection? (y/n)')
        if ask_remove_plant.lower() == 'y':
            remove_from_my_plants(plants)
        elif ask_remove_plant.lower() == 'n':
            search_plant()
        else:
            raise ValueError
    except ValueError:
        print(f'Invalid input.')
        search_plant()


def replace_none(stat):
    return stat if stat is not None else 'N/A'


def display_from_user_input(plant_data):
    return (
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


# if common_diseases in plant_data is not none, ask for user input on plant disease
def ask_disease(plant_data):
    if plant_data['common_diseases'] == "N/A":
        return None
    else:
        common_diseases = plant_data['common_diseases']
        while True:
            user_input_disease = input(
                f'Does your plant currently have any disease? Choose from: {common_diseases}, or enter "none".')
            if user_input_disease.lower() == 'none':
                return False
            elif user_input_disease.lower() in common_diseases.lower():
                return user_input_disease
            else:
                print('Disease entered not found. Please try again.')


# ask user if they want to add searched for plant to My Plants
def ask_add_plant(data, plant_id, user_input_plant, user_input_disease=None):
    try:
        add_plant_question = input(f'Would you like to add {user_input_plant} '
                                   f'to your My plants collection? (y/n)')
        if add_plant_question.lower() == 'n':
            print(f'{user_input_plant} was not added')
        elif add_plant_question.lower() == 'y':
            return add_plant(data, plant_id, user_input_disease)
    except Exception as err:
        print(f"An error occurred: {err}")


# call the api with user input
def search_plant():
    while True:
        try:
            user_input_plant = input('Please enter a house plant by common name or latin name,'
                                     'or enter "My Plants" to view your plant collection.')

            if user_input_plant.lower() == 'my plants':
                display_my_plants()

            host = 'house-plants2.p.rapidapi.com'
            url = f"{base_url}search"
            querystring = {"query": user_input_plant}
            headers = {
                "X-RapidAPI-Key": api_key,
                "X-RapidAPI-Host": host}

            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()
            full_data = response.json()
            if full_data:
                plant_id = full_data[0]['refIndex']
                data = full_data[0]['item']
                if data:
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
                    print(display_from_user_input(plant_data))
                    ask_add_plant(data, plant_id, user_input_plant, user_input_disease=ask_disease(plant_data))
                else:
                    print("No plant found. Please enter a valid plant name.")
            else:
                print("Error: Failed to fetch plant data. Please try again.")
        except requests.exceptions.RequestException as err:
            print(f"Error: Failed to make the API request: {err}")
        except (KeyError, IndexError) as err:
            print(f"Error: Invalid response data: {err}")


if __name__ == '__main__':
    search_plant()
