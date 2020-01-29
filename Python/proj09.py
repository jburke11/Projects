# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:04:45 2019

@author: joema
"""
"""
    SOURCE HEADER GOES HERE!
"""
#   Project 9
#   build all functions 
#   define main function
#   ask for user input 
#   use functions to perform work on data input
#
#
#
#

import csv
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

def open_file(message):   # prompts for file and opens file
   while True:
       try:
            file = input(message)      # ask for filename
            if not file: 
                fp = open("breachdata.csv", encoding="utf8")
                reader = csv.reader(fp)
            else:
                fp = open(file, encoding="utf8") 
                reader = csv.reader(fp)
            break
       except FileNotFoundError:
            print ('[ - ] File not found. Try again.') # if not found then print statement and repeat
            continue
   return reader

    
def build_dict(reader): # creates breach dictionary 
    large_dict = {}
    next(reader,None) # skips the header line
    for line in reader:
        try:
            entity_dict = {}    # seperates data points
            year_dict = {}
            list1 = line
            entity = list1[0]
            records_lost = int(list1[2].replace(",", "").replace('"', ""))
            year = int(list1[3])
            story = list1[4]
            sector = list1[5]
            method = list1[6]
            sources = list1[11].split(",")
            if not entity or not int(year) or not story or not sector or not method or not sources: # if item is empty
                pass
            if "" in sources: # if an empty string pass
                pass
            else:
                data_tuple = (records_lost, year,story,  sources)
                entity_dict[entity] = data_tuple
                year_dict[year] = (sector, method)  # create dictionary of dictionaries
                if entity not in large_dict.keys():
                    large_dict[entity] = [(entity_dict, year_dict)]
                else:
                    large_dict[entity].append((entity_dict, year_dict))
        except ValueError:
            pass # if year can't be int
    return (large_dict)
def top_rec_lost_by_entity(dictionary):
    temp_dict = {}
    temp_list = []
    for x,y in dictionary.items():  # creates keys and values
        for entity in y:
            if x in temp_dict:
                temp_dict[x] += entity[0][x][0] # creates dictionary of entity rec values
            else:
                temp_dict[x] = entity[0][x][0]
    
    for x , y in temp_dict.items(): # gets values from dictionary and creates and sorts list
        temp_list.append((x,y))
    temp_list.sort(key=itemgetter(1,0), reverse = True)
    if len(temp_list) <= 10:
        return temp_list
    else:
        return temp_list[0:10]

def records_lost_by_year(dictionary):
   temp_dict = {}
   temp_list = []
   for x,y in dictionary.items():
       for entity in y:
           if entity[0][x][1] in temp_dict: # same logic as last function but with years
               temp_dict[entity[0][x][1]] += entity[0][x][0]
           else:
               temp_dict[entity[0][x][1]] = entity[0][x][0]
   for x , y in temp_dict.items():
       temp_list.append((x,y))
   temp_list.sort(key=itemgetter(1,0), reverse = True)
   return temp_list
    


def top_methods_by_sector(dictionary): 
    methods_dict = {}
    for x,y in dictionary.items():
        for entity in y:
            for year, methods in entity[1].items(): # takes the second dict from original dict
                if methods[0] not in methods_dict:
                    methods_dict[methods[0]] = {}   # initialize dict 
                if methods[1] not in methods_dict[methods[0]]:
                    methods_dict[methods[0]][methods[1]] = 1    # initialize count
                else :
                    methods_dict[methods[0]][methods[1]] += 1 # add 1 for every occurance
    return methods_dict
    pass

        
def top_rec_lost_plot(names,records):
    ''' Plots a bargraph pertaining to
        the cybersecurity breaches data '''
        
    y_pos = np.arange(len(names))

    plt.bar(y_pos, records, align='center', alpha=0.5,
            color='blue',edgecolor='black')
    plt.xticks(y_pos, names, rotation=90)
    plt.ylabel('#Records lost')
    plt.title('Cybersecurity Breaches',fontsize=20)
    plt.show()
    
def top_methods_by_sector_plot(methods_list):
    ''' Plots the top methods used to compromise
        the security of a sector '''
    methods = [] ; quantities = []
    for tup in methods_list:
        methods.append(tup[0])
        quantities.append(tup[1])
    labels = methods
    sizes = quantities
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    plt.pie(sizes, labels=labels, colors = colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    
    plt.axis('equal')
    plt.show()
    
def main():
    BANNER = '''
    
                 _,.-------.,_
             ,;~'             '~;, 
           ,;                     ;,
          ;                         ;
         ,'                         ',
        ,;                           ;,
        ; ;      .           .      ; ;
        | ;   ______       ______   ; | 
        |  `/~"     ~" . "~     "~\'  |
        |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
         |   |        }:{        |   | 
         |   l       / | \       !   |
         .~  (__,.--" .^. "--.,__)  ~. 
         |     ---;' / | \ `;---     |  
          \__.       \/^\/       .__/  
           V| \                 / |V  
            | |T~\___!___!___/~T| |  
            | |`IIII_I_I_I_IIII'| |  
            |  \,III I I I III,/  |  
             \   `~~~~~~~~~~'    /
               \   .       .   /
                 \.    ^    ./   
                   ^~~~^~~~^ 
                   
           
           ~~Cybersecurity Breaches~~        
                   @amirootyet    
                
    '''
    
    print(BANNER)
    
    MENU = '''  
[ 1 ] Most records lost by entities
[ 2 ] Records lost by year
[ 3 ] Top methods per sector
[ 4 ] Search stories
[ 5 ] Exit

[ ? ] Choice: '''
    file = ""
    choice = ""
    while True: # loop for menu
        print(MENU)
        choice = input()
        if choice == "5":   # break if choice is 5
            print ("[ + ] Done. Exiting now...")
            break
        while choice not in "12345":
            print ('[ - ] Incorrect input. Try again.')
            print(MENU)
            choice = input()
        if choice == "5":
            print ("[ + ] Done. Exiting now...")    
            break
        message = "[ ? ] Enter the file name: "
        if file:
            pass
        else:   
            file = open_file(message)
            breach = build_dict(file)
        if choice == "1":
            print("[ + ] Most records lost by entities...")
            i = 0 # creates counter
            recs = top_rec_lost_by_entity(breach)
            print ("-"*45)
            for items in recs:
                i += 1
                print ("[ {:2d} ] | {:15.10s} | {:10d}".format(i , items[0], items[1])) # prints count with rec and entity
                if i != len(recs): # ensures - is not printed after the last line
                    print  ("-"*45)
                else:
                    pass
            plot = input("[ ? ] Plot (y/n)? ")
            if plot.lower() == "y":
                names = []
                recs = []
                for items in recs: # creates list for plotting
                    names.append(items[0])
                    recs.append(items[1])
                top_rec_lost_plot(names,recs)
            else:
                pass
        
        elif choice == "2":
            print("[ + ] Most records lost in a year...") # same as function before but with year data
            i = 0
            recs = records_lost_by_year(breach)
            print ("-"*45)
            for items in recs:
                i += 1
                print ("[ {:2d} ] | {:15.10s} | {:10d}".format(i , str(items[0]), items[1]))
                if i != len(recs):
                    print  ("-"*45)
                else:
                    pass
            plot = input("[ ? ] Plot (y/n)? ")
            if plot.lower() == "y":
                years = []
                recs = []
                for items in recs:
                    years.append(items[0])
                    recs.append(items[1])
                top_rec_lost_plot(years,recs)
            else:
                pass
        
        elif choice == "3":
            list1 = []
            keys = []
            i = 0
            sector = top_methods_by_sector(breach)
            print("[ + ] Loaded sector data.")
            for items in sector.keys(): # creates list of the keys to sort and display
                keys.append(items)
            keys.sort()
            print (" ".join(keys)) # displays list with a space
            sec = input("[ ? ] Sector (case sensitive)? ")
            while sec not in sector: # checks to see if sector is in dict
                print ("[ - ] Invalid sector name. Try again.") 
                sec = input("[ ? ] Sector (case sensitive)? ")
            print("[ + ] Top methods in sector {}".format(sec))
            for method, count in sector[sec].items(): # creates a list to sort and return
                list1.append((method, count)) 
            list1.sort(key=itemgetter(1), reverse=True)
            for items in list1:
                i += 1
                print  ("-"*45)
                print ("[ {:2d} ] | {:15.10s} | {:10d}".format(i, items[0], items[1]))
            plot = input("[ ? ] Plot (y/n)? ")
            if plot.lower() == "y":
                top_methods_by_sector_plot(list1)
            else:
                pass
        
        elif choice == "4":
            list_story = [] # creates list of stories 
            i = 0 # creates counter
            entity = input("[ ? ] Name of the entity (case sensitive)? ")
            while entity not in breach: # checks for entity
                print("[ - ] Entity not found. Try again.")
                entity = input("[ ? ] Name of the entity (case sensitive)? ")
            for values in breach[entity]: # appends stories to list
                list_story.append((values[0][entity][2]))
            print("[ + ] Found {} stories:".format(len(list_story))) # gets num of stories
            for stories in list_story:
                i += 1 # add to counter
                print("[ + ] Story {}: {:10s}".format(i, stories)) # print counter and story
        
if __name__ == "__main__":
     main()
