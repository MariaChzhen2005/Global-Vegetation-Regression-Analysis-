import os

from netCDF4 import Dataset as nc
import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import cartopy.crs as ccrs
from scipy.io import netcdf
from cartopy.mpl.ticker import (LongitudeFormatter, LatitudeFormatter,
                                LatitudeLocator)

year = 2014 # start year for iteration
years = {}

while year!=2015:
    cur_dir = os.chdir('/Users/mariachzhen/Desktop/AVHRR-Data/'+str(year))
    print("in first loop")
    years[str(year)] = []
    for file_name in range(len(os.listdir(os.curdir))):
        print("in second loop")
        file = nc(r'/Users/mariachzhen/Desktop/AVHRR-Data/'+str(year)+'/'+os.listdir(os.curdir)[file_name], 'r')
        long = file.variables['longitude'][:]
        lat = file.variables['latitude'][:]
        time = file.variables['time'][:]
        NDVI = file.variables['NDVI'][:]
        mean_NDVI = np.mean(NDVI, axis=0)
        
        northafr_lat = 26.0198 #N
        northafr_long = 32.2778 #E
        northafr_NDVI_list = []
        
        sqdiff_na_long = (long - northafr_long)**2
        sqdiff_na_lat = (lat - northafr_lat)**2
        min_index_long = sqdiff_na_long.argmin()
        min_index_lat = sqdiff_na_lat.argmin()
        
        for i in range(min_index_long-40,min_index_long+40):
            # print(mean_NDVI1[min_index_lat, i])
            northafr_NDVI_list.append(mean_NDVI[min_index_lat, i])
            
        northafr_maxNDVI = max(northafr_NDVI_list)
        
        years[str(year)].append(northafr_maxNDVI)
        print(years[str(year)])
        print(str(year))
        
    year +=1

# following code is bugged
months = {}
for j in range(0,13):
    months[str(j)] = []
    for year_item in years.items():
        for item in year_item:
            print(type(item))
            if type(item) == list:
                month_list=item
                for i in range(len(month_list)):
                    if i==j:
                        months[str(j)].append(month_list[i])
    j+=1

# Create a map representation
# ax = plt.axes(projection=ccrs.PlateCarree())
# plt.contourf(long,lat,mean_NDVI,cmap='RdYlBu_r',transform=ccrs.PlateCarree())
# ax.set_extent([500, -500, -250, 250])
# ax.coastlines(resolution='1200m')
# ax.gridlines(draw_labels=True)
# plt.legend(loc="upper left")
# plt.grid()
# plt.show()
