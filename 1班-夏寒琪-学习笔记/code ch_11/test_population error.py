import unittest
from city_function import city_country
class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
     name=city_country('Shanghai','China')
     self.assertEqual(name,'Shanghai,China')
unittest.main()