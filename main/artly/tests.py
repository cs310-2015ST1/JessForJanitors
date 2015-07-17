from django.test import TestCase
from parsertester import parseart


class ParserTests(TestCase):

    def test_parser(self):
        kml = open('testing.kml', 'r')
        testlist = parseart(kml)
        self.assertTrue(len(testlist) == 2)
        self.assertEqual(testlist[0].name, "Royal Sweet Diamond")
        self.assertEqual(testlist[1].name, "Machina Metronoma (South Cambie neighbourhood)")


