#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:56:47 2022
@author: mariachzhen
Annual analysis of selected areas.
Coordinates of analyzed areas:
    1. South Africa - (-25.5, 26)
    2. Iran - (31, 54)
    3. Australia - (-24, 134)
    4. South of South America - (-33, -64)
    5. North of South America, Brazil - (-5.5, -56.8)
    6. Canada, Ontario (48.9, -81.6)
    7. Canada, Alberta and Central US - (51.9, -110.2)
    8. Europe - (49, 21)
    9. South Asia - (33.5, 98.7)
"""
import os
from netCDF4 import Dataset as nc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

years = {}
years_max = {}
year_means = []
year_max_means = []

months = {}
filled_month = {} # key: string month. values: list that will be getting filled during iterations
def annual_analysis():
    # input values to customize function
    print("Enter starting year: ")
    year = input()
    print("Enter final year: ")
    end_year = input()
    print("Enter location latitude (-90 to 90) - South to North: ")
    loc_lat = input()
    print("Enter location latitude (-180 to 180) - West to East: ")
    loc_long = input()
    while year!=end_year:
        cur_dir = os.chdir('/Users/mariachzhen/Desktop/AVHRR-Data/'+str(year))
        print("in first loop")
        years[str(year)] = []
        years_max[str(year)] = []
        for file_name in range(1, len(sorted(os.listdir(os.curdir)))):
            print("in second loop")
            file = nc(r'/Users/mariachzhen/Desktop/AVHRR-Data/'+str(year)+'/'+sorted(os.listdir(os.curdir))[file_name], 'r')
            # print(sorted(os.listdir(os.curdir))[file_name])
            long = file.variables['longitude'][:]
            lat = file.variables['latitude'][:]
            NDVI = file.variables['NDVI'][:]
            mean_NDVI = np.mean(NDVI, axis=0)
            
            NDVI_list = []
            
            sqdiff_na_long = (long - loc_long)**2
            sqdiff_na_lat = (lat - loc_lat)**2
            min_index_long = sqdiff_na_long.argmin()
            min_index_lat = sqdiff_na_lat.argmin()
            
            for i in range(min_index_long-130,min_index_long+130):
                # print(mean_NDVI1[min_index_lat, i])
                for j in range(min_index_lat-75, min_index_lat+75):
                    NDVI_list.append(mean_NDVI[j, i])
            
            NDVI_list = np.ma.compressed(NDVI_list)
            if len(NDVI_list) > 5:
                northafr_maxNDVI = max(NDVI_list)
            
            avgNDVI = np.average(NDVI_list)
            
            # inserts avgNDVI in region for each of the 33 days
            years[str(year)].append(avgNDVI)
            years[str(year)] = [x for x in years[str(year)] if pd.notnull(x)]
            print(years[str(year)])
            years_max[str(year)].append(northafr_maxNDVI)
            years_max[str(year)] = [x for x in years_max[str(year)] if pd.notnull(x)]
            print("max values: ")
            print(years_max[str(year)])
            
            
            print(str(year))
            
        year_max_mean = np.mean(years_max[str(year)])
        year_max_means.append(year_max_mean)
        print("Max value mean: " + str(year_max_means))
        year_mean = np.mean(years[str(year)])
        year_means.append(year_mean)
        print("Year mean: " + str(year_means))
        year +=1

def change_axis_range():
    x=year_max_means
    plt.plot(x, 'o')
    plt.title('Annual NDVI maximum values')
    plt.ylim(ymin=0.5,ymax=1)
    plt.show()
