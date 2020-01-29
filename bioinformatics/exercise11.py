#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:00:47 2019

@author: burkej24
"""

names = open("plu_codes_and_fruit_veggie_names.txt", "r")
prices = open("plu_codes_and_fruit_veggie_prices.txt", "r")
colors = open("plu_codes_and_fruit_veggie_colors.txt", "r")
out_file = open("red", "w")
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
for code, color in dictcolors.items():
    if color == "red":
        red = dictnames[code], dictprices[code]
        print ("\t".join(red), file = out_file)
        
for line in dictnames:
    veggie_info = dictnames[line], dictprices[line], dictcolors[line]
    print(veggie_info)