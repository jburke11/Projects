# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:07:36 2019

@author: joema
"""
data1 = open("data1.txt" , "r")
data2 = open("data2.txt", "r")
def get_dicts():
    data1.seek(0)
    data2.seek(0)
    dict1 = {}
    dict2 = {}
    for line in data1:
        list1 = line.split()
        try:
            dict1[list1[0]] = int (list1[1])
            continue
        except ValueError:
            pass
        for line in data2:
            list1 = line.split()
            try:
                dict2[list1[0]] = int (list1[1])
            except ValueError:
                pass
    return dict1, dict2
def check_names(dict1, dict2):
    newdict = {}
    newdict.update(dict1.items())
    newdict.update(dict2.items())
    set1 = set (dict1.keys())
    set2 = set (dict2.keys())
    set3 = set1 & set2
    for name in set3:
        newdict[name] = dict1.get(name) + dict2.get(name)
    
    print("{:10s} {:10s}".format("Name" , "Total"))
    
    for line in sorted (newdict):
        print("{:10s} {:<10d}".format(line, int (newdict[line])))

def main():
    dict1, dict2 = get_dicts()
    return check_names(dict1, dict2)
    
        
main()       