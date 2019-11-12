########################
# Project 1
#conversions
#   prompt for an integer
#   convert to float and print 
#   convert rods in float to different units of meaure
#   round and print the converted values

 # ask for string and convert to float and print the float value
rods_flt = float ( input ("Input rods: "))
print ("You input", rods_flt, "rods.")  

print ("Conversions")

# conversions
meters_flt = (rods_flt * 5.0292)
furlongs_flt = (rods_flt / 40)
miles_flt = ((rods_flt * 5.0292) / 1609.34)
feet_flt = (((rods_flt * 5.0292) / 0.3048))
walking_time_flt = (( miles_flt / 3.1 ) * 60)

 
# print rounded conversions
print ("Meters:" , round ((meters_flt) ,3))
print ("Feet:" , round ((feet_flt) , 3))
print ("Miles:" , round ( (miles_flt) ,3))
print ("Furlongs:" , round ((furlongs_flt) ,3))
print ("Minutes to walk" , rods_flt , "rods:" , round ((walking_time_flt) ,3))

