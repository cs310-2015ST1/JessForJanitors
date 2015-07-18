import zipfile
import urllib
from test.test_xml_etree import getchildren
import os
from django.http import HttpResponse
import django
from models import ArtInstallation
from parsertester import parseart

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

# To return number of installations in database
num_installations = 0

# Had to put an x in here for it to work
def populate(x):

    id = 1

    url = 'http://data.vancouver.ca/download/kml/public_art_individual_locations.kmz'
    filename = 'public_art_individual_locations.kml'

    fileobject, _ = urllib.urlretrieve(url)
    kmz = zipfile.ZipFile(fileobject, 'r')
    kml = kmz.open(filename, 'r')
    artlist = parseart(kml)

    for art in artlist:
        add_art("loc_"+str(id), art.name, art.lat, art.lon, art.url)
        id+=1

    global num_installations
    response = "Success! Welcome to the Artly Art Installation Database, population: " + str(num_installations)
    num_installations = 0
    return HttpResponse(response)


def add_art(locationid, name, lat, lon, url):
    # add 1 to number of installations added
    twiturl = "https://twitter.com/intent/tweet?text=I+discovered+"+name+" using+this+sweet+app+called+Artly!"
    global num_installations
    num_installations += 1
    a = ArtInstallation.objects.get_or_create(locationid=locationid, name=name, url=url, lat=lat, lon=lon, twitterurl = twiturl)[0]
    return a

# Code below is not needed for button implementation
if __name__ == '__main__':
    print "Starting Artly population script..."
    populate()
