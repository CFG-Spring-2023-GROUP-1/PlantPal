"""Calendar feature that reminds user of when to water and fertilise their plants"""
import datetime


def describe_needs(plant_name, water_frequency, days):
    """Describes how often the plant needs watering"""
    print(f"A {plant_name.title()} needs watering {water_frequency} (every {days} days).")


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


def last_water(plant_name):
    last_watered = input(f"When did you last water your {plant_name}")
    # convert this to datetime format
    return last_watered


def days_since_watered(last_watered):
    """A count that shows how many days it's been since the plant was last watered"""
    last_date = last_watered
    now = datetime.datetime.now()
    days_lapsed = last_watered - now
    print(f"It's been {days_lapsed.days} days since you last watered me.")


def date_to_water(plant_name, last_watered):
    """Tells user the date they should next water their plant"""
    water_due = last_watered + datetime.timedelta(days=14)  # Need to make this input in relation to function days
    water_due = water_due.strftime("%A, %d/%m/%y")
    print(f"You should next water your {plant_name.title()} on {water_due}.")


plant_name = "monstera"  # Get this and water_frequency from DB - how?
water_frequency = "regularly"
last_watered = datetime.datetime.now()


describe_needs(plant_name, water_frequency, days_between_watering(water_frequency))
days_since_watered(last_watered)
date_to_water("monstera", last_watered)







