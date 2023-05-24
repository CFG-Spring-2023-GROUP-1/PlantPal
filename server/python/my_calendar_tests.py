from unittest import TestCase, main
import my_calendar_functions


class TestDaysBetween(TestCase):
    def test_days_between_watering(self):
        # Test with different water frequencies
        self.assertEqual(my_calendar_functions.days_between_watering("frequently"), 1)
        self.assertEqual(my_calendar_functions.days_between_watering("regularly"), 7)
        self.assertEqual(my_calendar_functions.days_between_watering("infrequently"), 14)

    def test_describe_needs(self):
        # Test the description output
        self.assertEqual(
            my_calendar_functions.describe_needs("Monstera", "regularly", 1),
            "Your Monstera needs watering regularly (every 1 days).")



