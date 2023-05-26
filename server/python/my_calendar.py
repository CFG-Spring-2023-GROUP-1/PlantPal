import my_calendar_functions
import datetime
import calendar
from python_sql_connector import connect_to_plantpal_db

connection = connect_to_plantpal_db('PlantPal')

query = """
SELECT p.CommonNames, pd.Watering
FROM Plants p
INNER JOIN PlantDetails pd
ON p.PlantID = pd.PlantID
"""

my_plants_data = my_calendar_functions.read_query(connection, query)


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
            self.days += 2
        elif self.water_frequency_split == "daily":
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

        overdue = []
        my_plants = []
        watering_order = []
        watering_dates = {}

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

        my_calendar_functions.watering_summary(overdue, watering_order, watering_dates)


WateringCalendar.run()






