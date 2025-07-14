import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    def test_city_country_population(self):
        result = city_country("Santiago", "Chile", 5000000)
        expected = "Santiago, Chile - population 5000000"
        self.assertEqual(result, expected)

    def test_city_country_population_language(self):
        result = city_country("Santiago", "Chile", 5000000, "Spanish")
        expected = "Santiago, Chile - population 5000000, Spanish"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
