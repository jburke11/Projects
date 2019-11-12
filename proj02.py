# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:56:47 2019

@author: joema
"""

# Project 2 
# Car rentals
# Display prompt and ask to continue 
# Go into loop
#ask for information regarding rental
#calculate miles traveled and cost depending on each rental type 
# print summary of calculations
# print thank you
#

print ("\nWelcome to car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BDW) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" ) 


while "Y" == str (input ("\nWould you like to continue (Y/N)? " )) :                #if the user says yes then enter the loop
    classification = str ( input ("\nCustomer code (BDW): "))
    while classification != "B" and classification != "D" and classification != "W" :
        print ("*** Invalid customer code. Try again. ***")                             # In case a wrong code is entered 
        classification = str ( input ("Customer code (BDW):  "))
    else :
        days = int ( input ("\nNumber of days:"))                                   # ask for rental information
        odometer_start = int ( input ("\nOdometer reading at the start:"))
        odometer_end = int ( input ("\nOdometer reading at the end:   "))  
    if classification == "B":
        if odometer_end < odometer_start :                                  # if code B then enter if else statements
            miles_drivenB = round ((0.1 * ((1000000 + odometer_end ) - odometer_start)) , 1)  # if odometer resets 
        else :
            miles_drivenB = round (0.1 *  (odometer_end - odometer_start) , 1) 
        cost = round (float ((40 * days + (0.25 * (miles_drivenB)))) , 2)
        print ("\nCustomer summary:")
        print ("\n\tclassification code:" , classification,)                    # print calculations and restart loop
        print ("\n\trental period (days):" , days) 
        print ("\n\todometer reading at start:" , odometer_start)
        print ("\n\todometer reading at end:  " , odometer_end)
        print ("\n\tnumber of miles driven:" , miles_drivenB)
        print ("\n\tamount due: $", cost)
    elif classification == "D" :
        if odometer_end < odometer_start :
            miles_drivenD = round ((0.1 * ((1000000 + odometer_end ) - odometer_start)) , 1)        # code D if else statements
        else :
            miles_drivenD = round (0.1 *  (odometer_end - odometer_start) , 1) 
        if (miles_drivenD / days) < 100 :
            cost = float ((60 * days))
        else :
            cost = round (float (((60 * days) + (((miles_drivenD) - (100 * days)) * 0.25))) ,2)         # if average miles is over the requirement
        print ("Customer summary:")
        print ("\tclassification code:" , classification,)
        print ("\trental period (days):" , days)                            # print calculations and restart loop
        print ("\todometer reading at start:" , odometer_start)
        print ("\todometer reading at end:  " , odometer_end)
        print ("\tnumber of miles driven: " , miles_drivenD)
        print ("\tamount due: $" , cost)
    elif classification == "W" :
        if odometer_end < odometer_start :                          # Code w if else statements
            miles_drivenW = round ((0.1 * ((1000000 + odometer_end ) - odometer_start)) , 1)
        else :
            miles_drivenW = round (0.1 *  (odometer_end - odometer_start) , 1)
        weeks = days / 7
        if days % weeks != 0 :                              
            weeks = int ((days / 7)) + 1                        # round up weeks
        else :  
            weeks = int (days / 7) 
        if (miles_drivenW / weeks) <= 900 :                 # calculations for 3 different scenarios 
            cost = round ( float (190 * weeks) , 2)
        elif (900 < (miles_drivenW / weeks) <= 1500) :
            cost = round ( float ( (weeks * 190) + (100 * weeks) ) , 2)
        else :
            cost = round ( float ((weeks * 190) + (weeks * 200) + (0.25 * ((miles_drivenW / weeks - 1500) * weeks))) , 2)
        print ("Customer summary:")
        print ("\tclassification code:" , classification,)
        print ("\trental period (days):" , days) 
        print ("\todometer reading at start:" , odometer_start)
        print ("\todometer reading at end:  " , odometer_end)
        print ("\tnumber of miles driven: " , miles_drivenW)
        print ("\tamount due: $" , cost)
    else :                  
        break

print ("Thank you for your loyalty.")   # print once the loop is over
        
            
            
        
        
            
    
    
