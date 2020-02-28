#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:35:14 2020

@author: burkej24
"""

fp = open("/Users/burkej24/Desktop/De/genes.count_tracking", "r")
new1= open ("/Users/burkej24/Desktop/DESeq.csv", "w")

for line in fp :
    list1 = line.rstrip().split()
    if list1[0] == "tracking_id" :
        print(list1[0] , ',' , list1[1] , ',' , list1[6], ',' , list1[11], file=new1)
    else:
         print(list1[0] , ',' , int(float(list1[1])) , ',' , int(float(list1[6])), ',' , int(float(list1[11])), file=new1)
print ('\n', file=new1)
fp.close()    
new1.close()