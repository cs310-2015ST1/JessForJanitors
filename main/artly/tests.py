from django.test import TestCase
from populateartly import parseart


class ParserTests(TestCase):

    def test_parser(self):
        filename = 'testing.kml'
        kml = open(filename, 'r')
        doc = kml.read()
        testlist = parseart(doc)
        self.assertEqual(testlist.len, 2)