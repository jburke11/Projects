# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:20:10 2019

@author: joema
"""
data_o = open("data.txt", "r")
x = 0
y = 0
minimum = 10e10
maximum= 0
minimumh = 10e10
maximumh= 0
minimumw = 10e10
maximumw = 0
BM = 0
print ("{:<12s}{:<12s}{:<12s}{:<12s}".format("Name", "Height(m) ", "Weight(kg)", "BMI")) 
for i,ch in enumerate (data_o):
    if i == 0 :
        continue
    else:
        names = ch[:6]
        height = float (ch[12:16])
        x += height
        if height < minimumh:
            minimum_h = height
            minimumh
        if height > maximumh :
            maximum_h = height
            maximumh = height
        weight = float (ch[24:29])
        y += weight
        if weight < minimumw:
            minimum_w = weight
            minimumw = weight
        if weight > maximumw:
            maximum_w = weight
            maximumw = weight
        BMI = weight / height ** 2
        BM += BMI
        if BMI < minimum:
            minb = BMI
            minimum = BMI
        if BMI > maximum:
            maxb = BMI
            maximum = BMI
        print ("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(names, height, weight, BMI))       
        if i == 8:
            avgbmi = BM / i
            avg_weight = y / i       
            avg_height = x/i
            print ("\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average", avg_height, avg_weight, avgbmi))
            print ("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max", maximum_h, maximum_w, maxb))
            print ("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min", minimum_h, minimum_w, minb))
data_o.close()
        