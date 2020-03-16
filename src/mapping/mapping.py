from cartopy import *
from matplotlib import cm
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from numpy import *
from cv2 import *

fig = plt.figure()
src = crs.Orthographic()
ax = plt.axes(projection=src)
ax.gridlines()
ax.set_global()


nx, ny  = 20,20
x       = linspace(*src.x_limits, nx)
y       = linspace(*src.y_limits, ny)
A, B, C = 2.972e-6,-0.484e-6,-0.361e-6
omega   = (A + (B * sin(deg2rad(y))**2) + (C*sin(deg2rad(y))**4)) * 10**6
z = [omega*ones(nx)] * ny

print(z)
print(omega)
cs = ax.contour(x, y,z, cmap=cm.PuBu_r)

cbar = fig.colorbar(cs)
plt.show()
