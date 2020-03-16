from pyexiv2 import ImageMetadata
import json, datetime
import geocoder
import pprint

fname = "./data/latest_test.jpg"

def write():
    g = geocoder.ip('me').latlng
    n = datetime.datetime.now()
    metadata = ImageMetadata(fname)
    metadata.read()

    userdata = {'Location': {'lat'  : g[0],
                             'long' : g[1]},
                'Time'    : str(n),
                }
    metadata['Exif.Photo.UserComment'] = json.dumps(userdata)
    metadata.write()

def read():
    metadata = ImageMetadata(fname)
    metadata.read()
    userdata=json.loads(metadata['Exif.Photo.UserComment'].value)
    pprint.pprint(userdata)
