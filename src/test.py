import matplotlib.pyplot as plt

from sunpy.net import Fido, attrs as a
import sunpy.map
from sunpy.io.file_tools import read_file

import matplotlib.pyplot as plt
from reproject import reproject_interp

import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS

import sunpy.data.sample
def test1():
    timerange = a.Time('2019/05/02 00:00', '2019/05/02 00:01')
    instrument = a.Instrument('LASCO')
    detector = a.Detector('C1')
    result = Fido.search(timerange, instrument)

    print(result)

    downloaded_files = Fido.fetch(result)
    print(downloaded_files)

    data, header = read_file(downloaded_files[0])[0]

    # Add the missing meta information to the header
    header['CUNIT1'] = 'arcsec'
    header['CUNIT2'] = 'arcsec'

    lascomap = sunpy.map.Map(data, header)
    fig = plt.figure()
    lascomap.plot()
    plt.show()

def test2():
    aia_map = sunpy.map.Map(sunpy.data.sample.AIA_193_IMAGE)

    fig = plt.figure()
    ax = plt.subplot(projection=aia_map)
    aia_map.plot(ax)
    plt.show()
test2()
