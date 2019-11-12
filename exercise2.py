#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:07:10 2019

@author: burkej24
"""
fp = open("fruits_veggies.txt", "r")

for line in fp:
    line1 = line.rstrip()
    list1 = line1.split()
    print (list1[0])
