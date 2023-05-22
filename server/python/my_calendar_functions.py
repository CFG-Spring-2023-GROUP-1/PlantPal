"""Calendar feature that reminds user of when to water and fertilise their plants"""
from datetime import datetime, timedelta


def describe_needs(plant_name, water_frequency, days):
    """Describes how often the plant needs watering"""
    print(f"Your {plant_name.title()} needs watering {water_frequency} (every {days} days).")


def days_between_watering(water_frequency):
    """Turns watering information from the API into a number"""
    days = 0
    if water_frequency == "frequently":
        days += 1
    elif water_frequency == "regularly":
        days += 7
    elif water_frequency == "infrequently":
        days += 14

    return days


def last_water(plant_name):
    """Gets the date the user last watered their plant"""
    last_watered_string = input(f"When did you last water your {plant_name}? dd/mm/yy\n")
    last_watered = datetime.strptime(last_watered_string, "%d/%m/%y")
    return last_watered


def days_since_watered(last_watered):
    """A count that shows how many days it's been since the plant was last watered"""
    last_date = last_watered
    now = datetime.today()
    days_lapsed = now - last_date
    print(f"It's been {days_lapsed.days} days since you last watered me.")
    # need to do an if for day or days


def date_to_water(plant_name, last_watered,days):
    """Tells user the date they should next water their plant"""
    water_due = last_watered + timedelta(days)  # Need to make this input in relation to function days
    water_due = water_due.strftime("%A, %d/%m/%y")
    print(f"You should next water your {plant_name.title()} on {water_due}.")









