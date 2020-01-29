# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:15:52 2019

@author: joema
"""
import csv
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']

def read_file(fp):
    fp.seek(0)
    list1 = []
    reader = csv.reader(fp)
    next(reader,None) 
    next(reader,None) 
    next(reader,None) 
    next(reader,None) 
    for line in reader:
        if "" in line:
            pass
        else:
            list1.append(line)
    return list1  # temoprary return value so main runs

def get_totals(list1):
    list2 =[]
    for line in list1:
        if line[0] == "U.S.":
            n = line[1]
            us = int (n.replace(",", ""))
        else:
            num = (line[1])
            number = num.replace(",", "")
            number1 = int (number.replace("<", ""))
            list2.append (number1)
    a = sum (list2)
    return us, a  # temoprary return value so main runs

def get_industry_counts(list1):
    list2 =[]
    construction = 0
    manufacturing = 0 
    buisness = 0
    leisure = 0
    agriculture = 0 
    for line in list1 :
        if line[0] == "U.S.":
            pass
        else:
            list2.append(line[9])
    for line in list2:
        if line == "Construction":
            construction += 1
        elif line == "Manufacturing":
            manufacturing += 1
        elif line == "Business services":
            buisness += 1
        elif line == "Leisure/hospitality":
            leisure += 1
        elif line == "Agriculture":
            agriculture += 1
    totals = []
    totals.append(["Construction", construction])  
    totals.append(["Manufacturing", manufacturing])
    totals.append(["Business services", buisness])
    totals.append(["Leisure/hospitality", leisure])
    totals.append(["Agriculture", agriculture])
    backwards = sorted(totals, key = itemgetter(1)) 
    return backwards[-1::-1]

def get_largest_states(list1):
    list2 =[]
    us = list1[0][2]
    usa = float (us.replace("%", ""))
    for line in list1:
        lin = float (line[2].replace("%", ""))
        if lin > usa:
            state = line[0]
            
            list2.append(state)
        else:
            continue
    print (list2)
        
    return list2  # temoprary return value so main runs

def main():    
    fp = open("immigration.csv")
    L = read_file(fp)
    
    us_pop,total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))
      
