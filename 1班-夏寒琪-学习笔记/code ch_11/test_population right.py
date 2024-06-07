import unittest
from city_function import city_country
class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
     name=city_country('Shanghai','China','5000000')
     self.assertEqual(name,'Shanghai,China,5000000')
unittest.main()