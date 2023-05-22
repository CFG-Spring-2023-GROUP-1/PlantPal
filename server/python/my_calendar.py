import datetime
import calendar
import my_calendar_functions
import mysql.connector


# Connect to the PlantPal MySQL database
def create_server_connection(host_name, user_name, user_password, db_name):
    """Establish server connection"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
    except Exception as err:
        print(f"Server Error: '{err}'")

    return connection

connection = create_server_connection("127.0.0.1", "root", "Dylan28megan", "PlantPal")

def read_query(connection, query):
    """Function to make a query"""
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as err:
        print(f"Error: '{err}'")

query = """
SELECT p.CommonNames, pd.Watering
FROM Plants p
INNER JOIN PlantDetails pd
ON p.PlantID = pd.PlantID
"""

my_plants = read_query(connection, query)


today_date = datetime.datetime.now()
today_date = today_date.strftime("%A, %d/%m/%y")

print("Welcome to the calendar")
print(f"Today is {today_date}") # format
yy = 2023
mm = 5
print(calendar.month(yy, mm))  # change this to reflect true month


# a while loop for whilst theres plants?
for plant in my_plants:
    plant_name = plant[0]
    water_frequency = "frequently"  ## Need to edit this function to work out wording

    days = my_calendar_functions.days_between_watering(water_frequency)
    my_calendar_functions.describe_needs(plant_name, water_frequency, days)

    last_watered = my_calendar_functions.last_water(plant_name)
    my_calendar_functions.days_since_watered(last_watered)

    my_calendar_functions.date_to_water(plant_name, last_watered, days)




# Make a to do list for what needs doing next?
# diseases



# Do they want to search for a specific plant in their list or show all?
# Maybe do a summary list of plant name and next water date




