#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:26:40 2019

@author: burkej24
"""

fp = open("fruits_veggies.txt", "r")
for line in fp:
    line1 = line.rstrip()
    list1 = line1.split()
    plu_code = str(list1[3])
    name = list1[0]
    data = (name, plu_code)
    print("\t".join(data))
