import zipfile
import urllib
import xml.etree.ElementTree as ET
#from test.test_xml_etree import getchildren
import os
from django.http import HttpResponse
import django
from artly.models import ArtInstallation

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()



# To return number of installations in database
num_installations = 0

# Had to put an x in here for it to work
def populate(x):

    url = 'http://data.vancouver.ca/download/kml/public_art_individual_locations.kmz'
    filename = 'public_art_individual_locations.kml'

    fileobject, _ = urllib.urlretrieve(url)
    kmz = zipfile.ZipFile(fileobject, 'r')
    kml = kmz.open(filename, 'r')
    tree = ET.parse(kml)
    root = tree.getroot()

    simple_data_tag = "{http://earth.google.com/kml/2.2}SimpleData"
    coordinates_tag = "{http://earth.google.com/kml/2.2}coordinates"

    placemark = root[0][4]

    for placemark_child in placemark.iter():
        if placemark_child.tag == simple_data_tag:
            if placemark_child.get('name') == 'TITLE':
                name = placemark_child.text
            if placemark_child.get('name') == 'URL_LINK':
                url = placemark_child.text[9:-6]
        if placemark_child.tag == coordinates_tag:
            coordinates = placemark_child.text
            first_comma = coordinates.find(',')
            second_comma = coordinates.find(',',first_comma+1)
            lon = coordinates[0:first_comma]
            lat = coordinates[first_comma+1:second_comma]
            add_art(name, lat, lon, url)


    global num_installations
    response = "Success! Welcome to the Artly Art Installation Databse, population: " + str(num_installations)
    num_installations = 0
    return HttpResponse(response)

    # Print out what we have added to the user.
    for c in ArtInstallation.objects.all():
        print "- {0}".format(str(c))

def add_art(name, lat, lon, url):
    # add 1 to number of installations added
    global num_installations
    num_installations += 1
    a = ArtInstallation.objects.get_or_create(name=name, url=url, lat=lat, lon=lon)[0]
    return a

# Code below is not needed for button implementation
if __name__ == '__main__':
    print "Starting Artly population script..."
    populate()
