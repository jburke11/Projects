#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:15:16 2019

@author: burkej24
"""

fp = open("Artificial_population_genotype_data.txt", "r")


for line in fp :
    list1 = line.rstrip().split()
    if list1[2] == "A" :
        print ("\t".join(list1))
    elif list1[2] == "B" :
        list2 = list1[0:2] + ["A" for B in list1[2] if line] + ["B" for A in list1[3] if line] + ["B" if ch == "A" else "A" for ch in list1[4:] if ch]
        print ("\t".join(list2))
    else:
        print ("               ", "\t".join(list1))
