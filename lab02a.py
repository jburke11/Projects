# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:03:02 2019

@author: joema
"""


y = 0  # empty counters
o = 0
e = 0
so = 0
se = 0
t = 0
while y >= -100000 :             # start of while loop 
    y = int (input ("Input an integer (0 terminates): "))
    if y < 0 :
        continue
    elif y == 1 :   # special case for 1 counter
        o += 1 
        so += 1
        t += 1 
    elif  y % 2 == 0 and y != 0 and y > 0:     # even counter
        e += 1 
        se += y
        t += 1
    elif y % 2 != 0 and y > 0:   #odd counter
        o += 1
        so += y 
        t += 1
    else:                              # print when 0 is entered 
        print ("sum of odds:" , so)
        print ("sum of evens:" , se)
        print ("odd count:" , o)
        print ("even count:" , e)
        print ("total positive int count:" , t)
        break
         
    
    





 