import unittest
from city_functions import city_country
class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
     name=city_country('Shanghai','China')
     self.assertEqual(name,'Shanghai,China')
     name2=city_country('Paris','France')
     self.assertEqual(name2,'Paris,France')
unittest.main()

