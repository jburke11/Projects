#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:58:54 2019

@author: burkej24
"""

names = open("plu_codes_and_fruit_veggie_names.txt", "r")
prices = open("plu_codes_and_fruit_veggie_prices.txt", "r")
out_file = open("newfile", "w")
dictnames = {}
dictprices = {}

for line in names:
    line1 = line.rstrip()
    list1 = line1.split()
    dictnames[list1[0]] = list1[1]
for line in prices:
    line1 = line.rstrip()
    list1 = line1.split()
    dictprices[list1[0]] = list1[1]
for keys in dictnames:
    print(dictprices[keys], file=out_file)
out_file.close()