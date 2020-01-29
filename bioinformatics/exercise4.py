#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:24:59 2019

@author: burkej24
"""

fp = open("fruits_veggies.txt", "r")
listred = []
for line in fp:
    line1 = line.rstrip()
    list1 = line1.split()
    if "red" in list1[1]:
        listred.append(list1)
for redfood in listred:
    print (redfood[0])