"""Calendar feature that reminds user of when to water and fertilise their plants"""

import datetime

# The API doesn't appear to show fertilising.  would this be monthly or something?
# Do I need to find a way to order these in time order - print to a file? Or frontend


plant_name = "" # Common name from DB (Plants)
water_frequency = ""  # Watering from DB (Plant details)
days = 0
last_watered = ""


def describe_needs(plant_name, water_frequency, water_days):
    """Describes how often the plant needs watering"""
    print(f"A {plant_name} needs watering {water_frequency} (every {water_days} days).")

describe_needs("mostera", "frequently", days)


def last_water(plant_name):
    last_watered = input(f"When did you last water your {plant_name}")
    return last_watered


def days_since_watered(last_watered):
    """A count that shows how many days it's been since the plant was last watered"""
    last_date = last_watered
    now = datetime.datetime.now()
    days_lapsed = last_watered - now
    print(f"It's been {days_lapsed.days} days since you last watered me.")


def date_to_water(last_watered):
    """Tells user the date they should next water their plant"""
    last_watered = last_watered
    water_due = last_watered + datetime.timedelta(days=14)  # Need to make this input in relation to function days
    water_due = water_due.strftime("%A, %d/%m/%y")
    print(f"You should next water your {plant_name} on {water_due}.")


def days_between_watering(water_frequency):
    """Turns to string value from the API into an integer"""
    days = 0
    if water_frequency == "frequently":
        days += 1
    elif water_frequency == "regularly":
        days += 7
    elif water_frequency == "infrequently":
        days += 14

    return days


# Need to access list/dictionary of users plants to and get watering data??
# my_plants = []
# for plant in my_plants:
#     my_plants += plant







