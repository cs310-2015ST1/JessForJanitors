import xml.etree.ElementTree as ET
from artinfo import ArtInfo


def parseart(kml):
    tree = ET.parse(kml)
    root = tree.getroot()

    artlist = []

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
            artlist.append(ArtInfo(name, lat, lon, url))

    return artlist
