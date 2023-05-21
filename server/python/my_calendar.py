import datetime
import calendar
import my_calendar_functions

today_date = datetime.datetime.now()  # format this

print("Welcome to the calendar")
print(f"Today is {today_date}")
yy = 2023
mm = 5
print(calendar.month(yy, mm))  # change this to reflect true month


# Make a to do list for what needs doing next?

my_plants = []  # is this a dictionary or list - need to fill with data from DB

# Do they want to search for a specific plant in their list or show all?
# Maybe do a summary list of plant name and next water date

for plant in my_plants:
    plant_name = ""
    water_frequency = ""

    days = my_calendar_functions.days_between_watering(water_frequency)

    my_calendar_functions.days_between_watering(plant_name, water_frequency, days)

    last_watered = my_calendar_functions.last_water(plant_name)
    my_calendar_functions.days_since_watered(last_watered)

    my_calendar_functions.date_to_water(plant_name, last_watered, days)


