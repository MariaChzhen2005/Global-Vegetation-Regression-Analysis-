# creates a plot for one of the .nc maps

from netCDF4 import Dataset as nc
import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from scipy.io import netcdf

file1 = nc(r'/Users/mariachzhen/Desktop/AVHRR-Data/2015/AVHRR-20150613_c20170409085632.nc', 'r')

long1 = file1.variables['longitude'][:]
lat1 = file1.variables['latitude'][:]
time1 = file1.variables['time'][:]
NDVI1 = file1.variables['NDVI'][:]
mean_NDVI1 = np.mean(NDVI1, axis=0)

ax = plt.axes(projection=ccrs.PlateCarree())
plt.contourf(long1,lat1,mean_NDVI1,cmap='RdYlBu_r',transform=ccrs.PlateCarree())
ax.set_extent([500, -500, -250, 250])
ax.coastlines(resolution='110m')
ax.gridlines(draw_labels=True)
plt.legend(loc="upper left")
plt.grid()
plt.show()
