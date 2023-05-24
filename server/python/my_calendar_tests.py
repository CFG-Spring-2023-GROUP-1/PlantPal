from unittest import TestCase, main
import my_calendar_functions, my_calendar
import datetime

### UPDATE TO REFLECT ADJUSTMENTS TO OOP


class MyCalendarTests(TestCase):
    def test_days_between_watering(self):
        """Test days between watering with different seasons"""
        self.assertEqual(my_calendar_functions.days_between_watering("frequently"), 1)
        self.assertEqual(my_calendar_functions.days_between_watering("regularly"), 7)
        self.assertEqual(my_calendar_functions.days_between_watering("infrequently"), 14)

    def test_describe_needs(self):
        """Test description is accurate"""
        self.assertEqual(
            my_calendar_functions.describe_needs("Monstera", "regularly", 1),
            "Your Monstera needs watering regularly during the (every 1 days).")

    # def test_last_water(self):


    # def test_days_since_watered(self):


    def test_date_to_water(self):
        """Tests date calculated to water next.  Uses an example date for testing"""
        water_due = datetime.datetime(2023, 5, 27)
        water_due = water_due.strftime("%A, %d/%m/%y")
        self.assertEqual(
            my_calendar_functions.date_to_water("Monstera", datetime.datetime(2023, 5, 20), 7),
            (f"You should next water your Monstera on {water_due}.")
        )


