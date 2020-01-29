# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:24:54 2019

@author: joema
"""

from operator import itemgetter

def build_map( in_file1, in_file2 ):
    in_file1.readline()
    in_file2.readline()
    data_map = {}
    #READ EACH LINE FROM FILE 1
    for line in in_file1:
        # Split the line into two words
        countries_list = line.strip().split()
            
            # Convert to Title case, discard whitespace
        continent = countries_list[0].strip().title()
        country = countries_list[1].strip().title()
            # Ignore empty strings
        if continent != "":
                # If current continent not in map, insert it 
            if continent not in data_map.keys():
                data_map[continent] = {country: []}
                
                # If country is not empty insert (continent is guaranteed to be in map)
            if country not in data_map[continent].keys():
                data_map[continent][country] = []
                
                     # If current country not in map, insert it 
                     
     #READ EACH LINE FROM FILE 2        
    for line in in_file2:

        # Split the line into two words
        cities_list = line.strip().split()
        
        # Convert to Title case, discard whitespace
        country = cities_list[0].strip().title()
        city = cities_list[1].strip().title()
        
        # Ignore empty strings
        if country != "":
            
            # insert city (country is guaranteed to be in map)
            for continent in data_map.keys():
                if country in data_map[continent]:
                    if city not in data_map[continent][country]: 
                        data_map[continent][country].append(city)
    return data_map

def display_map( data_map ):

    # Modify this code to display a sorted nested dictionary
    continents_list = sorted (data_map.keys()) #sorted list of the continent keys
    for continents in continents_list:
        print("{}:".format(continents)) #continents in continents_list
        countries_list = sorted(data_map[continents].keys()) #sorted list of the countries keys in the continents
        for countries in countries_list:
            print("{:>10s} --> ".format(countries),end = '') #countries in countries_list
            cities = sorted(data_map[continents][countries]) #sorted list of the cities
            for city in cities :
                if city != cities[-1]:#As long as not last city, add a comma and a space after the cities names
                    print('{}, '.format(city),end = '') # city in cities                      
                else:# if it is the last, don't add a comma and a space.
                    print('{}'.format(city))

def open_file():

    try:
        filename = input("Enter file name: ")
        in_file = open( filename, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file

def main():

    # YOUR CODE

    in_file1 = open_file() #Continents with countries file: continents.txt
    in_file2 = open_file() #Countries with cities file: cities.txt

    if in_file1 != None and in_file2 != None:

        data_map = build_map( in_file1, in_file2 ) # data_map is a dictionary
        display_map( data_map )
        in_file1.close()
        in_file2.close()

if __name__ == "__main__":
    main()