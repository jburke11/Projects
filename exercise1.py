#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:04:43 2019

@author: burkej24
"""
fp = open("fruits_veggies.txt", "r")

for line in fp:
    print (line.rstrip())
