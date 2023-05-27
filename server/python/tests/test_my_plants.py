import unittest
from unittest.mock import patch
import sys
sys.path.append("../")
from my_plants_main import remove_from_my_plants, replace_none, display_my_plants, display_from_user_input, search_plant


class TestMainFunctions(unittest.TestCase):
    def test_replace_none(self):
        self.assertEqual(replace_none(None), 'N/A')
        self.assertEqual(replace_none('Cycas revoluta'), 'Cycas revoluta')

    def test_display_from_user_input(self):
        plant_data = {
            "latin_name": "Agave attenuata",
            "common_name": "Dragon-tree Agave, Century plant",
            "light_level": "Strong light ( 21,500 to 3,200 lux/2000 to 300 fc)",
            "watering": "Must dry between watering & Water only when dry",
            "climate": "Arid Tropical",
            "max_temp": {"F": 95, "C": 35},
            "min_temp": {"F": 41, "C": 5},
            "growth_speed": "Slow",
            "common_diseases": "N/A",
            "image": "http://www.tropicopia.com/house-plant/thumbnails/5443.jpg"
        }

        expected = (
            "Latin name: Agave attenuata\n"
            "Common name(s): Dragon-tree Agave, Century plant\n"
            "Ideal light: Strong light ( 21,500 to 3,200 lux/2000 to 300 fc)\n"
            "Watering: Must dry between watering & Water only when dry\n"
            "Climate type: Arid Tropical\n"
            "Max temperature: F:95, C:35\n"
            "Min temperature: F:41, C:5\n"
            "Growth speed: Slow\n"
            "Common diseases: N/A\n"
            "Image: http://www.tropicopia.com/house-plant/thumbnails/5443.jpg\n"
        )

        self.assertEqual(display_from_user_input(plant_data), expected)

    def test_display_myplants_empty(self):
        with patch('my_plants_main.get_all_myplants', return_value=[]):
            with patch('builtins.print') as mock_print:
                display_my_plants()
        mock_print.assert_called_with("Your plant collection is empty.")

        # @patch('main.input', side_effect=['Monstera deliciosa', 'y'])
        # @patch('main.remove_plant')
        # def test_remove_from_my_plants(self, mock_remove_plant, _):
        #     mock_plants = [
        #         (8, 'Bromeliad', 'Guzmenia', 'Guzmania'),
        #         (157, 'Philodendron', 'Monstera deliciosa', 'Splitleaf Philodendron, Mexican Breadfruit'),
        #         (275, 'Hanging', 'Chlorophytum comosum', 'Spider plant')
        #     ]
        #     remove_from_my_plants(mock_plants)
        #     mock_remove_plant.assert_called_once_with('Monstera deliciosa')


if __name__ == '__main__':
    unittest.main()
