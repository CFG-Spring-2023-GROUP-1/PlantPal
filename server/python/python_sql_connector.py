import mysql.connector
import json
from connect_to_db import get_sql_connection as connect_to_plantpal_db


# GET ALL MY PLANTS RECORDS
def get_all_myplants():
    try:
        db_connection = connect_to_plantpal_db()
        cur = db_connection.cursor()

        cur.execute('SELECT * FROM PlantDetails')
        result = cur.fetchall()
        cur.close()
        return result
    except mysql.connector.Error as err:
        print('Error. Unable to retrieve My Plants:', err)
    finally:
        if db_connection:
            db_connection.close()


# # ADD TO MY PLANTS

def add_plant(data, plant_id, user_input_disease):
    try:
        db_connection = connect_to_plantpal_db()
        cur = db_connection.cursor()
        print('connected to PlantPal')

        insert_qry = "INSERT INTO PlantDetails (PlantId, Category, LatinName, CommonNames, " \
                     "LightLevel, Watering, Climate, MaxTemp, MinTemp, GrowthSpeed, CommonDiseases, " \
                     "CurrentDisease, LeafColour, BloomingSeason, Perfume, ColourOfBloom, Image) VALUES" \
                     "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        common_names_str = ', '.join(data['Common name'])
        leaf_colour_str = ', '.join(data['Color of leaf'])

        cur.execute(insert_qry, (plant_id, data['Categories'], data['Latin name'], common_names_str, data['Light tolered'], data['Watering'],
                                 data['Climat'], json.dumps(data['Temperature max']), json.dumps(
                                     data['Temperature min']), data['Growth'],
                                 data['Disease'], user_input_disease, leaf_colour_str, data[
                                     'Blooming season'], data['Perfume'], data['Color of blooms'],
                                 data['Img']))

        db_connection.commit()
        print(
            f"You've added {'/'.join(data['Common name'])} ({data['Latin name']}) to your plant collection!")
        cur.close()
    except mysql.connector.Error as err:
        print(f'Error. Unable to add {data["Latin name"]}:', err)
    finally:
        if db_connection:
            db_connection.close()


# REMOVE PLANT FROM MY PLANTS

def remove_plant(plant_name):
    try:
        db_connection = connect_to_plantpal_db()
        cur = db_connection.cursor()

        cur.execute(
            'DELETE FROM PlantDetails WHERE LatinName = %s', (plant_name,))
        db_connection.commit()

        if cur.rowcount > 0:
            print(f'{plant_name} has been removed from My Plants')
        else:
            print(f'{plant_name} not found')
        cur.close()
    except mysql.connector.Error as err:
        print(f'Error. Unable to remove {plant_name}:', err)
    finally:
        if db_connection:
            db_connection.close()
