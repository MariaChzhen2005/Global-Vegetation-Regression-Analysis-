#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 23:09:25 2021

@author: mariachzhen
"""

import os
from netCDF4 import Dataset as nc
import numpy as np

year = 1995
years = {}

# north africa variables -> change to south africa later

months = {}
filled_month = {} # key: string month. values: list that will be getting filled during iterations

while year!=2016:
    cur_dir = os.chdir('/Users/mariachzhen/Desktop/AVHRR-Data/'+str(year))
    print("in first loop")
    years[str(year)] = []
    for file_name in range(1, len(sorted(os.listdir(os.curdir)))):
        print("in second loop")
        file = nc(r'/Users/mariachzhen/Desktop/AVHRR-Data/'+str(year)+'/'+sorted(os.listdir(os.curdir))[file_name], 'r')
        # print(sorted(os.listdir(os.curdir))[file_name])
        long = file.variables['longitude'][:]
        lat = file.variables['latitude'][:]
        time = file.variables['time'][:]
        NDVI = file.variables['NDVI'][:]
        mean_NDVI = np.mean(NDVI, axis=0)
        
        northafr_lat = -25.5 #N
        northafr_long = 26 #E
        northafr_NDVI_list = []
        northafr_maxNDVI_list = []
        
        sqdiff_na_long = (long - northafr_long)**2
        sqdiff_na_lat = (lat - northafr_lat)**2
        min_index_long = sqdiff_na_long.argmin()
        min_index_lat = sqdiff_na_lat.argmin()
        
        for i in range(min_index_long-130,min_index_long+130):
            # print(mean_NDVI1[min_index_lat, i])
            for j in range(min_index_lat-75, min_index_lat+75):
                northafr_NDVI_list.append(mean_NDVI[j, i])
        
        northafr_NDVI_list = np.ma.compressed(northafr_NDVI_list)
        if len(northafr_NDVI_list) > 5:
            northafr_maxNDVI = max(northafr_NDVI_list)
        
        
        avgNDVI = np.average(northafr_NDVI_list)
        
        # inserts avgNDVI in region for each of the 33 days
        years[str(year)].append(avgNDVI)
        print(years[str(year)])
        print("Max: " + str(northafr_maxNDVI))
        
        print(str(year))
        
        date = file.time_coverage_start # gets netcdf attribute
        date_list = list(date)
        month = date_list[5]+date_list[6] # string month, e.g. '12'
        if month in filled_month:
            filled_month[month].append(avgNDVI)
        else:
            filled_month[month] = []
            filled_month[month].append(avgNDVI)
        # months[month] += avgNDVI
        # print(filled_month)
        
    year +=1

print(filled_month)
