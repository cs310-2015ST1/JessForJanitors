import unittest
from populateartly import parseArt


class ParserTests(unittest.TestCase):

    def test_Parser(self):
        filename = 'testing.kml'
        kml = open(filename, 'r')
        doc = kml.read()
        testlist = parseArt(doc)
        self.assertEqual(testlist.len, 2)

