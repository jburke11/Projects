#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:15:16 2019

@author: burkej24
"""

fp = open("/Users/burkej24/Desktop/genes.count_tracking", "r")
new1= open ("/Users/burkej24/Desktop/SRR11012008.csv", "w")

for line in fp :
    list1 = line.rstrip().split()
    if list1[0] == "tracking_id" :
        print(list1[0] , ',' , list1[1] , ',' , list1[6], file=new1)
    elif list1[0][0] != 'L' :
        pass
    else:
         print(list1[0] , ',' , int(float(list1[1])) , ',' , int(float(list1[6])), file=new1)
fp.close()    
new1.close()