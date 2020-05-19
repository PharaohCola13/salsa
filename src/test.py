import matplotlib.pyplot as plt

from sunpy.net import Fido, attrs
import sunpy.map
from sunpy.io.file_tools import read_file


timerange = attrs.Time('2002/05/24 11:06', '2002/05/24 11:07')
instrument = attrs.Instrument('LASCO')
detector = attrs.Detector('C3')
result = Fido.search(timerange, instrument)

print("Test")
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
