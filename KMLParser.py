import lxml
import zipfile
import urllib
from pykml import parser
import xml.etree.ElementTree as ElementTree
from test.test_xml_etree import getchildren


url = 'http://data.vancouver.ca/download/kml/public_art_individual_locations.kmz'
filename = 'public_art_individual_locations.kml'

fileobject, _ = urllib.urlretrieve(url)
kmz = zipfile.ZipFile(fileobject, 'r')
kml = kmz.open(filename, 'r')
content = kml.read()
# print content

root = ElementTree.fromstring(content)
allplacemarks = root[0][4].findall('{http://earth.google.com/kml/2.2}Placemark')
print allplacemarks
for child in allplacemarks:
    name = child.findall('{http://earth.google.com/kml/2.2}name')
    print name

# root = parser.fromstring(content)
# folder = root.Document.Folder
# print folder.tag
# 
# for Placemark in folder:
#     print folder.Placemark.description.text
#     print folder.Placemark.ExtendedData.SchemaData.SimpleData.text
#     print folder.Placemark.Point.coordinates.text

# url, _ = urllib.urlretrieve('http://data.vancouver.ca/download/kml/public_art_individual_locations.kmz')
# filename = 'public_art_individual_locations.kml'
# 
# kmz = zipfile.ZipFile(url, 'r')
# kml = kmz.open(filename, 'r')
# content = kml.read()
# root = parser.parse(content).getroot()

# for item in doc.iterfind('Document/Folder/Placemark'):
#     name = item.findtext('name')
#     coordinates = item.iterfind('Point/coordinates')
#     
#     print(name)
#     print(coordinates)
#     print()

# kml = kmz.open(filename, 'r')
# content = kml.read()
# print content

# http://stackoverflow.com/questions/6861323/download-and-unzip-file-with-python
# http://programmingadvent.blogspot.ca/2013/06/kmzkml-file-parsing-with-python.html
# http://www.tutorialspoint.com/python/python_xml_processing.htm

# class PlacemarkHandler(xml.sax.handler.ContentHandler):
#     def __init__(self):
#         self.inName = False # handle XML parser events
#         self.inPlacemark = False
#         self.mapping = {} 
#         self.buffer = ""
#         self.name_tag = ""
#          
#     def startElement(self, name, attributes):
#         if name == "Placemark": # on start Placemark tag
#             self.inPlacemark = True
#             self.buffer = "" 
#         if self.inPlacemark:
#             if name == "name": # on start name tag
#                 self.inName = True # save name text to follow
#              
#     def characters(self, data):
#         if self.inPlacemark: # on text within tag
#             self.buffer += data # save text if in title
#              
#     def endElement(self, name):
#         self.buffer = self.buffer.strip('\n\t')
#          
#         if name == "Placemark":
#             self.inPlacemark = False
#             self.name_tag = "" #clear current name
#          
#         elif name == "name" and self.inPlacemark:
#             self.inName = False # on end title tag            
#             self.name_tag = self.buffer.strip()
#             self.mapping[self.name_tag] = {}
#         elif self.inPlacemark:
#             if name in self.mapping[self.name_tag]:
#                 self.mapping[self.name_tag][name] += self.buffer
#             else:
#                 self.mapping[self.name_tag][name] = self.buffer
#         self.buffer = ""
# 
# if __name__ == '__main__':
#     parser = xml.sax.make_parser()
#     handler = PlacemarkHandler()
#     parser.setContentHandler(handler)
#     parser.parse(kml)
#     kmz.close()
#     outstr = build_table(handler.mapping)
#     out_filename = filename[:-3] + "csv" #output filename same as input plus .csv
#     f = open(out_filename, "w")
#     f.write(outstr)
#     f.close()
#     print outstr