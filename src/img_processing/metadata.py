from pyexiv2 import ImageMetadata
import json, datetime
import geocoder
import pprint

fname = "./data/latest_test.jpg"


def read():
    metadata = ImageMetadata(fname)
    metadata.read()
    userdata=json.loads(metadata['Exif.Photo.UserComment'].value)
    pprint.pprint(userdata)
