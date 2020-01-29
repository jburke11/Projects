# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:37:30 2019

@author: joema
"""
in_file = open ("scores.txt" , "r")
datalist = []
data = []
exams = []
examlist = []
print ("{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}".format("Name", "Exam1", "Exam2", "Exam3", "Exam4", "Mean"))
for ch in (in_file) :
    a = ch.split()
    names = a[0] + " " + a[1]
    exams = (a[2:6])
    examlist = [int(i) for i in exams]
    examsum = int(a[2])+ int(a[3]) + int(a[4]) + int (a[5])
    personal_avg = (examsum/ 4)
    data1 = names, exams , personal_avg
    data.append(data1)
data.sort()

avgs1 = []
avgs2 = []
avgs3 = []
avgs4 = []

for lst in data:
    print ("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(lst[0], int (lst[1][0]), int (lst[1][1]), int (lst[1][2]), int (lst[1][3]), lst[2]))
    avgs1.append(int (lst[1][0]))
    avgs2.append(int (lst[1][1]))
    avgs3.append(int (lst[1][2]))
    avgs4.append(int (lst[1][3]))
    avg1mean = sum(avgs1)/len(avgs1)
    avg2mean = sum(avgs2)/len(avgs2)
    avg3mean = sum(avgs3)/len(avgs3)
    avg4mean = sum (avgs4)/ len (avgs4)
print ("{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format("Exam Mean" , avg1mean, avg2mean, avg3mean, avg4mean))
in_file.close()