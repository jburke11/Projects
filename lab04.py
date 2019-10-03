# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:20:10 2019

@author: joema
"""
def leap_year (year1):
    year = int (year1)
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def rotate (s, n):
    if len (s) == 0 or len(s) == 1:
        return s 
    else:
        x = str((s[len(s) - n:] + s[0:len(s) - n]))
        return x


def digit_count (num):  
    num1 = str(num)
    odd = "13579"
    even = "2468"
    zero = "0"
    decimal = "."
    new = 0
    x = 0
    y = 0
    z = 0
    if decimal not in num1:
        for i , ch in enumerate (num1):
            if ch in zero :
                x += 1 
            elif ch in odd :
                y += 1
            elif ch in even :
                z += 1
    else:
        for i , ch in enumerate (num1):
            if decimal in ch :
                new2 = str(num1 [0:i])
        new = str (new2)
        for a , b in enumerate (new):
            if b in zero :
                x += 1 
            elif b in odd :
                y += 1
            elif b in even :
                z += 1
    return (z , y , x)


def float_check (num):
    num1 = str(num)
    decimal = "."
    ex = "e"
    x = 0
    for i , ch in enumerate (num1):
        if decimal in ch:
            x += 1
    if x > 1 :
        return False
    elif ex in num1 :
        return False
    elif x == 1 :
        return True
    elif num1.isdigit() == False :
        return False
    else:
        return True
    
            
    
    
    



        


    
        