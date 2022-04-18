#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 08:27:40 2022
Coordinates of analyzed areas:
    1. South Africa - (-25.5, 26)
    2. Iran - (31, 54)
    3. Australia - (-24, 134)
    4. Argentina - (-33, -64)
    5. Brazil - (-5.5, -56.8)
    6. Canada, Ontario (48.9, -81.6)
    7. Alberta, Canada and Central US - (51.9, -110.2)
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
    plt.title('Annual precipitation (cm) in ' + country)
    plt.ylim(ymin=30, ymax=60)
    plt.show()
    print("y = " + str(m)+"x + " + str(b))


# South Africa
# y = -0.2806017113296059x + 44.231211984126986
# years = [42.046352777777784, 49.82700769230769, 45.01945085470086, 42.20623205128205, 35.5016344017094, 58.747424145299156, 47.849582478632485, 33.65025277777778, 30.94635683760684, 41.77611880341881, 33.40569764957265, 49.69573632478633, 31.785548931623936, 36.040110897435895, 47.06536431623931, 43.25187777777778, 53.26694102564103, 34.781468376068375, 33.98516474358974, 40.46159166666667]
# Iran
# y = -0.2462157334168479x + 15.80755024724364
# years = [16.283586820507157, 19.27990205550035, 15.23674528909499, 13.381309806411247, 15.48023421110743, 12.368086838909132, 11.44096762172905, 12.53875294431563, 13.848496788855766, 18.457067507636822, 12.902321408855029, 15.70062543704685, 11.615559557984616, 8.011343896065659, 15.230791560855325, 6.37869994663428, 12.420442751462957, 15.171046336167239, 11.36305941996982, 12.260975396562513]
# Australia
# y = -0.18013341077051612x + 24.02026374847374
# years = [23.347958547008545, 12.679423931623933, 27.708596367521373, 23.895199145299145, 24.536616025641028, 42.40906944444445, 36.25927670940171, 10.640979273504273, 19.102071794871797, 17.600354914529913, 17.237982905982907, 16.963269871794875, 18.02097264957265, 14.899520726495727, 16.419329914529914, 37.605302991452994, 32.19960341880341, 18.128241452991453, 14.557863461538462, 21.968293376068377]
# Argentina
# y = -0.13403144335196815x + 58.63106445970693
# years = [46.065442094017094, 55.331491239316236, 57.21719358974359, 59.00528012820512, 61.923004700854705, 66.66002393162393, 73.39788461538461, 69.84658311965812, 54.22005192307692, 53.44099294871795, 53.152290384615384, 54.4797108974359, 58.95780982905983, 49.0599920940171, 49.66635384615385, 51.4250155982906, 51.37196282051283, 68.30105982905984, 47.84922136752137, 65.78395000000002]
# Brazil
# y = 0.8780811000257038x + 173.20499789377288
# years = [176.47732457264962, 176.85226175213677, 177.5481837606838, 162.87870213675214, 184.9285653846154, 196.2914873931624, 168.75842414529916, 176.48230876068376, 165.04625064102564, 173.82863931623933, 180.93395427350427, 185.0272267094017, 178.32967649572652, 206.44810042735043, 184.25437991452992, 176.7839967948718, 190.87307243589743, 182.02880384615386, 201.0176918803419, 186.14631623931626]
# Ontario, Canada
# y = 0.46859084997773714x + 67.54430249224772
# years = [73.23756788645395, 70.68457285756425, 64.70663140041295, 62.46061869935627, 78.13472424652542, 62.11303528360489, 79.2505561050093, 71.41284181805564, 68.27579446671179, 74.24355555844741, 68.39904069717004, 70.65699252164559, 74.72777575347457, 75.26317344229868, 69.86027731507991, 65.38375865389621, 66.90464924609165, 64.66210352575781, 85.71297130116427, 93.82767056200441]
# Alberta, Canada and the Central US
# 
# years = [38.28539230769231, 38.66931367521367, 36.16085277777778, 37.889087606837606, 34.19497841880342, 32.194048076923075, 25.022753632478636, 31.75858974358975, 33.72118461538462, 38.22452457264958, 40.124700000000004, 34.77513076923077, 36.49706388888889, 33.67227564102564, 31.974633760683766, 44.01254294871795, 39.06179380341881, 38.51879465811967, 37.868042307692306, 38.798051923076926]
# Europe
# years = [55.10757222222223, 56.62911837606838, 55.5960826923077, 62.41747136752138, 59.823716452991455, 49.89352115384616, 61.951342735042736, 54.366084188034186, 43.457879273504275, 57.38424038461538, 59.807319871794874, 54.96260576923077, 59.611524358974364, 56.95374166666666, 60.265430341880354, 75.51117094017094, 43.72149102564103, 51.40445534188034, 58.62312542735042, 61.199968162393176]
# Southern Asia
# years = [44.45706217948718, 44.18788824786325, 40.14551047008547, 50.26636965811966, 47.20401666666667, 44.95032799145299, 43.65963397435898, 40.504375, 48.13977457264958, 47.55850747863248, 49.77613760683761, 40.844971794871796, 44.57815833333334, 46.03122777777778, 47.64790128205128, 47.12901004273504, 47.258726709401714, 51.73551474358974, 44.93427115384616, 47.67134294871796]


annual_analysis_TC()
# change_axis_range()
# 


