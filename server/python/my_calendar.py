import my_calendar_functions
import datetime
import calendar
import mysql.connector
from main import ask_disease


def create_server_connection(host_name, user_name, user_password, db_name):
        """Establishes server connection with SQL database"""
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


def read_query(connection, query):
        """Method to make a query to the database"""
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as err:
            print(f"Error: '{err}'")


class Plant:
    """Plant class that each of the user's plants will be an instance of (using the API for info)"""
    def __init__(self, name, water_frequency):
        self.name = name
        self.water_frequency = water_frequency.lower()
        self.days = 0
        # self.disease = ask_disease(plant_data)


    def describe_needs(self):
        """Describes how often the plant needs watering"""
        return f"Your {self.name.title()} needs {self.water_frequency.lower()}. Watering is recommended every {self.days} days"

    def days_between_watering(self):
        """Turns watering information from the API into a number"""
        self.water_frequency_split = self.water_frequency.split(" ")

        if "regular" in self.water_frequency_split or "regularly" in self.water_frequency_split:
            self.days += 1
        elif self.water_frequency == "weekly":
            self.days += 7
        elif self.water_frequency == "infrequently":
            self.days += 14
        else:
            self.days += 3

        return self.days


class WateringCalendar:
    """Main class which runs the calendar feature"""
    @staticmethod
    def run():
        """Main method that runs the watering calendar feature"""
        connection = create_server_connection("127.0.0.1", "root", "Dylan28megan", "PlantPal")

        query = """
        SELECT p.CommonNames, pd.Watering
        FROM Plants p
        INNER JOIN PlantDetails pd
        ON p.PlantID = pd.PlantID
        """

        my_plants_data = read_query(connection, query)

        watering_order = []
        watering_dates = {}
        overdue = []

        my_plants = []  # Create instances of plant class using DB
        for plant_data in my_plants_data:
            plant_name = plant_data[0]
            water_frequency = plant_data[1]
            plant = Plant(plant_name, water_frequency)
            my_plants.append(plant)

        print("Welcome to the PlantPal calendar")
        print(f'Today is {datetime.datetime.today().strftime("%A %dth %B %Y")}')
        print("")

        print(calendar.month(datetime.datetime.today().year, datetime.datetime.today().month))

        for plant in my_plants:
            days = plant.days_between_watering()
            print(plant.describe_needs())

            last_watered = my_calendar_functions.last_water(plant.name)

            days_since_watered = my_calendar_functions.days_since_watered(last_watered, days)

            if days_since_watered == "overdue":
                print("Watering is overdue! Please water ASAP")
                print("-------")
                overdue.append(plant.name)
                continue
            else:
                watering_order.append(plant)
                watering_dates[plant] = my_calendar_functions.date_to_water(plant.name, last_watered, days)

            # if plant.disease:
            #     my_calendar_functions.disease_treatments(plant.disease)

            print(my_calendar_functions.date_to_water(plant.name, last_watered, days))
            print("-------")
            # my_calendar_functions.disease_treatments(user_input_disease)

        print("Summary")
        for plant in overdue:
            if plant:
                print("Water these plants now:")
                print(f"- {plant}")
            else:
                pass
        print("Next watering dates:")
        for index, plant in enumerate(watering_order, start=1):
            full_string = watering_dates[plant]
            watering_date = full_string.split(" on ")[-1]
            print(f"{index}. {plant.name.title()} - {watering_date}")



### Add any additional features here that will run after main info about plants


WateringCalendar.run()


# Do they want to search for a specific plant in their list or show all?





