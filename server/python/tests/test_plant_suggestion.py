import unittest
import os
from unittest.mock import patch
import sys
sys.path.append("../")
from plant_suggest_filter import house_plants_api, filter_sunlight, low_maintanance, preference, filter_air_purifying


class TestHousePlantsAPI(unittest.TestCase):

    @patch('plant_suggest_filter.os.getenv')
    def test_house_plants_api(self, mock_getenv):
        mock_getenv.return_value = 'test_api_key'
        expected_url = 'https://perenual.com/api/species-list?page=1&key=test_api_key'
        self.assertEqual(house_plants_api(), expected_url)


class TestHousePlantsURL(unittest.TestCase):

    def test_filter_sunlight(self):
        url = 'https://perenual.com/api/species-list?page=1&key=test_api_key'
        sunlight = 'full_sun'
        expected_url = url + '&sunlight=' + sunlight
        self.assertEqual(filter_sunlight(url, sunlight), expected_url)

    def test_low_maintanance(self):
        url = 'https://perenual.com/api/species-list?page=1&key=test_api_key'
        user_input = True
        expected_url = url + '&watering=minimum'
        self.assertEqual(low_maintanance(url, user_input), expected_url)

    def test_preference(self):
        url = 'https://perenual.com/api/species-list?page=1&key=test_api_key'
        user_preference = "Palm"
        expected_url = url + '&q=' + user_preference
        self.assertEqual(preference(url, user_preference), expected_url)

class TestAirPurifyingFilter(unittest.TestCase):

    def test_filter_air_purifying(self):
        api_data = {'data': [{'scientific_name': 'Dypsis lutescens'}, {'scientific_name': 'Other name'}]}
        user_input = True
        expected_output = [{'scientific_name': 'Dypsis lutescens'}]
        self.assertEqual(filter_air_purifying(api_data, user_input), expected_output)

    
    def test_filter_air_purifying_false(self):
        api_data = {'data': [{'scientific_name': 'Dypsis lutescens'}, {'scientific_name': 'Other name'}]}
        user_input = False
        expected_output = [{'scientific_name': 'Dypsis lutescens'}, {'scientific_name': 'Other name'}]
        actual_output = filter_air_purifying(api_data, user_input)
        self.assertEqual(actual_output, expected_output)

    def test_invalid_input(self):
        api_data = {'data': [{'scientific_name': 'Dypsis lutescens'}, {'scientific_name': 'Other name'}]}
        user_input = "invalid"
        with self.assertRaises(ValueError):
            filter_air_purifying(api_data, user_input)

if __name__ == '__main__':
    unittest.main()
