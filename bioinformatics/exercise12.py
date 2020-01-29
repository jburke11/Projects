#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:15:26 2019

@author: burkej24
"""

names = open("plu_codes_and_fruit_veggie_names.txt", "r")
prices = open("plu_codes_and_fruit_veggie_prices.txt", "r")
colors = open("plu_codes_and_fruit_veggie_colors.txt", "r")
out_file = open("red_under_0.2", "w")

dictnames = {}
dictprices = {}
dictcolors = {}
for line in colors:
    line1 = line.rstrip()
    list1 = line1.split()
    dictcolors[list1[0]] = list1[1]
for line in names:
    line1 = line.rstrip()
    list1 = line1.split()
    dictnames[list1[0]] = list1[1]
for line in prices:
    line1 = line.rstrip()
    list1 = line1.split()
    dictprices[list1[0]] = list1[1]

for code, price in dictprices.items():
    number = price.strip("$")
    if float(number) > 0.20:
        if dictcolors[code] == "red":
            print (dictnames[code], dictprices[code], file=out_file)
        else:
            pass
    else:
        pass




        
