#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:56:19 2019

@author: burkej24
"""

fp = open("Artificial_population_genotype_data.txt", "r")
list3 =[]
for line in fp :
    list1 = line.rstrip().split()
    if list1[2] == "A" :
        list1[0] = " ".join(list1[0:2])
        list1.remove(list1[1])
        print ("\t".join(list1))
        list3.append(list1)
    elif list1[2] == "B" :
        list2 = list1[0:2] + ["A" for B in list1[2] if line] + ["B" for A in list1[3] if line] + ["B" if ch == "A" else "A" for ch in list1[4:] if ch]
        list2[0] = " ".join(list1[0:2])
        list2.remove(list1[1])
        print ("\t".join(list2))
        list3.append(list2)
    else:
        print ("               ", "\t".join(list1))
        list1.insert(0,"")
        list3.append(list1)


rez = [[list3[j][i] for j in range(len(list3))] for i in range(len(list3[0]))] 
for item in rez:
    if item == rez[0]:
        print ("  ", " ".join(item))
    else:
        print("\t".join(item))
    
 