import unittest
from unittest import TestCase, main
from unittest.mock import patch
import my_calendar_functions
from my_calendar import Plant, WateringCalendar
from datetime import datetime, timedelta

"""Calendar tests"""

class PlantTests(TestCase):
    def test_describe_needs(self):
        plant = Plant("cactus", "regularly", "Overwatering")
        plant.days = 7
        expected_output = "Your Cactus needs regularly. Watering is recommended every 7 days"
        self.assertEqual(plant.describe_needs(), expected_output)

    def test_days_between_watering(self):
        """Test days between watering with different seasons"""
        plant1 = Plant("Rose", "weekly", None)
        plant2 = Plant("Lily", "regularly", "Root Rot")
        plant3 = Plant("Cactus", "infrequently", "Flies")
        plant4 = Plant("Orchid", "sporadically", "Wilting")

        self.assertEqual(plant1.days_between_watering(), 7)
        self.assertEqual(plant2.days_between_watering(), 2)
        self.assertEqual(plant3.days_between_watering(), 14)
        self.assertEqual(plant4.days_between_watering(), 3)


class CalendarTests(TestCase):
    @patch('my_calendar_functions.datetime')
    def test_date_to_water(self, mock_datetime):
        mock_datetime.return_value = datetime(2023, 5, 20)  # Mocks datetime.today()
        water_due = datetime(2023, 5, 27).strftime("%A %dth %B %Y")

        self.assertEqual(
            my_calendar_functions.date_to_water("Monstera", datetime(2023, 5, 20), 7),
            f"You should next water your Monstera on {water_due}.")
        self.assertNotEqual(my_calendar_functions.date_to_water("Rose", datetime(2023, 5, 20), 14),
            f"You should next water your Rose on {water_due}.")

    def test_days_since_watered(self):
        last_watered = datetime.today() - timedelta(days=1)
        days = 2
        expected_output = print("It's been 1 day since you last watered me")
        self.assertEqual(my_calendar_functions.days_since_watered(last_watered, days), expected_output)

    def test_days_overdue(self):
        last_watered = datetime.today() - timedelta(days=3)
        days = 2
        expected_output = "overdue"
        self.assertEqual(my_calendar_functions.days_since_watered(last_watered, days), expected_output)

    @patch('builtins.input', side_effect=['01/05/23', '05/10/22'])
    def test_last_water(self, mock_input):
        """Test last water function with different inputs"""
        plant1_name = 'Rose'
        plant2_name = 'Monstera'
        expected_date1 = datetime.strptime('01/05/23', "%d/%m/%y")
        expected_date2 = datetime.strptime('05/10/22', "%d/%m/%y")

        result1 = my_calendar_functions.last_water(plant1_name)
        result2 = my_calendar_functions.last_water(plant2_name)

        self.assertEqual(result1, expected_date1)
        self.assertEqual(result2, expected_date2)


class TestDiseaseTreatments(TestCase):
    def test_disease_none(self):
        result = my_calendar_functions.disease_treatments(None)
        self.assertEqual(result, "Your plant currently shows no sign of disease")


if __name__ == '__main__':
    unittest.main()
