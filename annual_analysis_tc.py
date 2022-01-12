#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 08:27:40 2022
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
    
@author: mariachzhen
"""

import os
from netCDF4 import Dataset as nc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

years = []

variable_name=""

# variable_name = 'PDSI'
# year = 2014
# end_year = 2015
# loc_lat = -5.5
# loc_long = -56.8

print("Enter country: ")
country = input()

def annual_analysis_TC():
    
    # input values to customize function
    print("Enter variable: ")
    variable_name = input()
    print("Enter starting year: ")
    year = input()
    year = int(year)
    print("Enter final year: ")
    end_year = input()
    end_year = int(end_year)
    print("Enter location latitude (-90 to 90) - South to North: ")
    loc_lat = input()
    print("Enter location longitude (-180 to 180) - West to East: ")
    loc_long = input()
    
    while year!=end_year:
        print("in first loop")
        for file_name in range(end_year-year):
            print("in second loop")
            file = nc(r'/Users/mariachzhen/Desktop/AVHRR-Data/TerraClimate_'+variable_name+'/TerraClimate_'+variable_name+"_"+str(year)+'.nc', 'r')
            # print(sorted(os.listdir(os.curdir))[file_name])
            long = file.variables['lon'][:]
            lat = file.variables['lat'][:]
            var = file.variables[variable_name][:]
            mean_var = np.mean(var, axis=0)
            
            var_list = []
            
            sqdiff_na_long = (long - float(loc_long))**2
            sqdiff_na_lat = (lat - float(loc_lat))**2
            min_index_long = sqdiff_na_long.argmin()
            min_index_lat = sqdiff_na_lat.argmin()
            
            for i in range(min_index_long-130,min_index_long+130):
                # print(mean_var1[min_index_lat, i])
                for j in range(min_index_lat-75, min_index_lat+75):
                    var_list.append(mean_var[j, i])
            
            var_list = np.ma.compressed(var_list)
            
            
            avgvar = np.average(var_list)
            
            # inserts avgvar in region for each of the 33 days
            years.append(avgvar)
            years_good = [x for x in years if pd.notnull(x)]
            print(years_good)
            # years_max.append(northafr_maxvar)
            # years_max_good = [x for x in years_max if pd.notnull(x)]
            # print("max values: ")
            # print(years_max_good)
            
            print(year)
            year +=1
            
        # year_max_mean = np.mean(years_max[str(year)])
        # year_max_means.append(year_max_mean)
        # print("Max value mean: " + str(year_max_means))
        # year_mean = np.mean(years[str(year)])
        # year_means.append(year_mean)
        # print("Year mean: " + str(year_means))
        # year +=1

def change_axis_range():

    y=years
    x=np.arange(20)
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, y, 'o')
    plt.plot(x, m*x + b)
    plt.title('Annual PDSI values in ' + country)
    plt.ylim(ymax=1000)
    plt.show()
    print("y = " + str(m)+"x + " + str(b))

# Brazil
# years = [369.1834920299145, 231.9433132051282, 442.87746846153846, 632.7567081410257, 373.1544361752137, 176.59641995726497, 320.0468087179487, 460.4965653418804, 410.87777754273503, 203.85102395299148, 350.038840940171, 298.7451758760684, 288.8607236965812, 190.18723288461538, 147.06772222222224, 467.34972938034184, 272.71215758547004, 314.62981032051283, 106.47710049145299, 128.37979190170938]
# Iran
# years = [223.88697503772406, 39.40578263589857, 464.10925414504436, 288.96871533528395, 420.9296457160208, 612.7739010801957, 594.4245675306393, 460.68676688841043, 575.6981926502522, 357.01531140738285, 280.0787285847043, 485.3056506017445, 361.1293415084097, 608.2228684074934, 505.33339852232154, 629.6908646626919, 614.1216240891024, 558.6516634923264, 458.6241527041699, 493.4651556576865]
# Australia
years = [447.61915797008544, 557.0567638034188, 120.15070369658122, 133.75689591880342, 352.8533317735043, 10.623908803418804, 22.09030074786325, 344.55745754273505, 591.1668998931624, 393.2113701495727, 507.95198705128206, 350.46586809829057, 543.4297583547009, 595.5623191239317, 406.21853241452993, 60.035656452991454, 23.08375303418804, 292.77504504273503, 577.1067363675214, 377.2022278846154]
# South of South America

# Brazil

# Ontario, Canada

# Alberta, Canada and the Central US

# Europe

# Asia




# annual_analysis_TC()
change_axis_range()
