#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:44:44 2019

@author: burkej24
"""

fp = open("fruits_veggies.txt", "r")
out_file = open("plu_codes_and_fruit_veggie_names.txt", "w")
dict1 = {}

for line in fp:
    line1 = line.rstrip()
    list1 = line1.split()
    food = list1[0]
    plu_code = str(list1[3])
    dict1[plu_code] = food
for line in dict1.items():
    print("\t".join(line), file=out_file)
out_file.close()