import unittest
from unittest import TestCase, main
import my_calendar_functions
from my_calendar import Plant, WateringCalendar
import datetime

class PlantTests(TestCase):
    def test_describe_needs(self):
        plant = Plant("cactus", "regularly")
        plant.days = 7
        expected_output = "Your Cactus needs regularly. Watering is recommended every 7 days"
        self.assertEqual(plant.describe_needs(), expected_output)

    def test_days_between_watering(self):
        """Test days between watering with different seasons"""
        plant1 = Plant("Rose", "weekly")
        plant2 = Plant("Lily", "regularly")
        plant3 = Plant("Cactus", "infrequently")
        plant4 = Plant("Orchid", "sporadically")

        self.assertEqual(plant1.days_between_watering(), 7)
        self.assertEqual(plant2.days_between_watering(), 1)
        self.assertEqual(plant3.days_between_watering(), 14)
        self.assertEqual(plant4.days_between_watering(), 3)


class TestMyCalendarFunctions(TestCase):
    def test_date_to_water(self):
     """Tests date calculated to water next.  Uses an example date for testing"""
     water_due = datetime.datetime(2023, 5, 27)
     water_due = water_due.strftime("%A %dth %B %Y")
     self.assertEqual(
         my_calendar_functions.date_to_water("Monstera", datetime.datetime(2023, 5, 20), 7),
         (f"You should next water your Monstera on {water_due}."))



    # def test_last_water(self):


    # def test_days_since_watered(self):


    # def test_date_to_water(self):
    #     """Tests date calculated to water next.  Uses an example date for testing"""
    #     water_due = datetime.datetime(2023, 5, 27)
    #     water_due = water_due.strftime("%A, %d/%m/%y")
    #     self.assertEqual(
    #         my_calendar_functions.date_to_water("Monstera", datetime.datetime(2023, 5, 20), 7),
    #         (f"You should next water your Monstera on {water_due}.")
    #     )

if __name__ == '__main__':
    unittest.main()
