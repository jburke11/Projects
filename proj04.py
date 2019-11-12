# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:20:10 2019

@author: joema
"""
################################################
# Project 4
#   Define all functions 
#   integrate all functions into main()
#   ask for input on which calculation to perform
#   perform desired calculations until told to stop
#
#
#
#
#################################################
import math
EPSILON = 1.0e-7

def display_options():                                                  # menu function from strings.py
    ''' This function displays the menu of options'''

    MENU = '''\nPlease choose one of the options below:
              A. Display the value of the sum of the first N natural numbers. 
              B. Display the approximate value of e.
              C. Display the approximate value of the hyperbolic sine of X.
              D. Display the approximate value of the hyperbolic cosine of X.
              M. Display the menu of options.
              X. Exit from the program.'''
       
    print(MENU)
def sum_natural(N):         # define sum of natural numbers, use for loop and range to add desired numbers
  n = str (N)
  Sum = 0
  if n.isdigit() == False:
     print ("\n\tError: N was not a valid natural number. [{}]".format(N))
     return None
  q = int (n)
  if q <= 0 :
     print ("\n\tError: N was not a valid natural number. [{}]".format(N))
     return None
  else:
     for i in range (1,q+1):
       Sum += i
  return Sum
             

def approximate_euler():        # define euler function return euler rounded to 10 decimal places
    e = 0
    f = 0
    for i in range (0, 1000):
        f = (1/(math.factorial(i)))
        if f < 1.0e-7:
            break
        else:
            e += f
    e = round (e, 10)
    return e


def float_check (num):      # float check function from lab 4 
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


def approximate_sinh(x):        # define sin function and return rounded to 10 decimal places
    sin = 0
    if float_check(x) == False:
        return print ("\n\tError: X was not a valid float. [{}]".format(x))
    else:
        x = float (x)
        for i in range (0, 1000):       # arbritrary range stops when a is less than the desired epsilon
            a = (x**(2*i+1))/ (math.factorial(2*i+1))
            if a < 1.0e-7:
                break
            else:
                sin += a
    s = round (sin, 10)
    return s
        
        
           
def approximate_cosh(x):    # define sin function and return rounded to 10 decimal places
    cos = 0
    if float_check(x) == False:
        return print ("\n\tError: X was not a valid float. [{}]".format(x))
    else:
        x = float (x)
        for i in range (0, 1000):           # arbritrary range stops when a is less than the desired epsilon
            a = (x**(2*i))/ (math.factorial(2*i))
            if a < 1.0e-7:
                break
            else:
                cos += a
    cos = float (round (cos, 10))
    return float (cos)

def main():                     # define main function with other functions nested inside
    display_options()
    while True:
        option = input ("\n\tEnter option: ")       # while loop for calculations
        opt = option.lower()
        if opt == "a":          # option a calculations makes sure x is a digit then performs calculation and prints value
            N = input ("\nEnter N: ")
            n = str(N)
            if n.isdigit() == False:
                print ("\n\tError: N was not a valid natural number. [{}]".format(N))
            elif n.isdigit() == True :
                n = int (n)
                if n <= 0 :
                    print ("\n\tError: N was not a valid natural number. [{}]".format(N))  
                else: 
                    print ("\n\tThe sum:  {}".format(sum_natural(N)))
            continue
        
        elif opt == "b":        # calls euler function and compares to pythons e
            print (""" \n\tApproximation: {:.10f}
\tMath module:   {:.10f}
\tdifference:    {:.10f}""".format(approximate_euler(), math.e, (math.e - approximate_euler())))
        elif opt == "c":        # option c if input is a float then convert it to a float and perform calculation
            x = input ("\n\tEnter X: ") 
            if float_check(x) == True:
                X = float (x)
                print ("""\tApproximation: {:.10f}
\tMath module:   {:.10f} 
\tdifference:    {:.10f}""".format(float(approximate_sinh(X)), float (math.sinh(X)), float ((math.sinh(X) - approximate_sinh(X)))))
            else:
                print ("\n\tError: X was not a valid float. [{}]".format(x))
            continue
        elif opt == "d":        # option d basically the same as option c
            x = input ("\n\tEnter X: ")
            if float_check (x) == True :
                X = float (x)
                print ("""\tApproximation: {:.10f}
\tMath module:   {:.10f} 
\tdifference:    {:.10f}""".format(float (approximate_cosh(X)), float (math.cosh(X)), float ((math.cosh(X) - approximate_cosh(X)))))
            else:
                print ("\n\tError: X was not a valid float. [{}]".format(x))
            continue
        elif opt == "m":        # option m calls menu function
            display_options()
            continue
        elif opt == "x":        # x terminates the loop and prints goodbye statement
            print ("Hope to see you again.")
            break
        else:       # if input is not in the menu
            print ("\nError:  unrecognized option [{}]".format(option.upper()))
            display_options()
            continue

if __name__ == "__main__": 
    main()    
    




    
        