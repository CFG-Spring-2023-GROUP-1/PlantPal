import my_calendar_functions
import datetime
import calendar
from python_sql_connector import connect_to_plantpal_db

"""Main My Calendar feature"""

connection = connect_to_plantpal_db()

query = """
SELECT p.CommonNames, pd.Watering, pd.CurrentDisease
FROM Plants p
INNER JOIN PlantDetails pd
ON p.PlantID = pd.PlantID
"""

my_plants_data = my_calendar_functions.read_query(connection, query)


class Plant:
    """Plant class that each of the user's plants will be an instance of (using the API for info)"""

    def __init__(self, plant_name, water_frequency, disease):
        self.plant_name = plant_name
        self.water_frequency = water_frequency.lower()
        self.current_disease = disease
        self.days = 0

    def describe_needs(self):
        """Describes how often the plant needs watering"""
        return f"Your {self.plant_name.title()} needs {self.water_frequency.lower()}. Watering is recommended every {self.days} days"

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
            current_disease = plant_data[2]
            plant = Plant(plant_name, water_frequency, current_disease)
            my_plants.append(plant)

        print("Welcome to the PlantPal calendar")
        print(
            f'Today is {datetime.datetime.today().strftime("%A %dth %B %Y")}')
        print("")

        print(calendar.month(datetime.datetime.today().year,
              datetime.datetime.today().month))

        print("---------------")

        for plant in my_plants:
            days = plant.days_between_watering()
            print(plant.describe_needs())

            last_watered = my_calendar_functions.last_water(plant.plant_name)

            days_since_watered = my_calendar_functions.days_since_watered(
                last_watered, days)

            if days_since_watered == "overdue":
                print("Watering is overdue! Please water ASAP")
                print("---------------")
                overdue.append(plant.plant_name)
                continue
            else:
                watering_order.append(plant)
                watering_dates[plant] = my_calendar_functions.date_to_water(
                    plant.plant_name, last_watered, days)

            print(my_calendar_functions.disease_treatments(plant.current_disease))

            print(my_calendar_functions.date_to_water(
                plant.plant_name, last_watered, days))
            print("-------")

        my_calendar_functions.watering_summary(
            overdue, watering_order, watering_dates)


WateringCalendar.run()
