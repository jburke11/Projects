# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:25:01 2019

@author: joema
"""

rods_flt = round (float ( input ("Input rods: ")) , 3) 
print ("You input", rods_flt, "rods")

print ("Conversions")
meters_flt = round ((rods_flt * 5.0292) , 3)
print ("Meters:" , meters_flt)
furlongs_flt = round ((rods_flt / 40) , 3)
print ("Furlongs:" , furlongs_flt)
miles_flt = round ((rods_flt * 5.0292 / 1609.34) , 3)
print ("Miles:" , miles_flt )
feet = round ((rods_flt * 5.0292 / 0.3048), 3)
print ("Feet:" , feet)
walking_time = round ((((rods_flt * 5.0292 / 1609.34) / 3.1 ) * 60) , 3)
print ("Minutes to walk" , walking_time)
print ("rods:" , rods_flt)
