import zipfile
import urllib
import xml.etree.ElementTree as ET
#from test.test_xml_etree import getchildren


url = 'http://data.vancouver.ca/download/kml/public_art_individual_locations.kmz'
filename = 'public_art_individual_locations.kml'

fileobject, _ = urllib.urlretrieve(url)
kmz = zipfile.ZipFile(fileobject, 'r')
kml = kmz.open(filename, 'r')
tree = ET.parse("testing.kml")
root = tree.getroot()

placemark_tag = "{http://earth.google.com/kml/2.2}Placemark"
simple_data_tag = "{http://earth.google.com/kml/2.2}SimpleData"
description_tag = "{http://earth.google.com/kml/2.2}description"
coordinates_tag = "{http://earth.google.com/kml/2.2}coordinates"

placemark = root[0][4]

print placemark.tag

for placemark_child in placemark.iter():
    print placemark_child

for placemark_child in placemark.iter():
    if placemark_child.tag == simple_data_tag:
        if placemark_child.get('name') == 'TITLE':
            print placemark_child.text
        if placemark_child.get('name') == 'URL_LINK':
            print placemark_child.text
    if placemark_child.tag == coordinates_tag:
        print "Coordinates: " + placemark_child.text
