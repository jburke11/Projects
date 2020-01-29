# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:04:45 2019

@author: joema
"""
################################
# import addons
# define all functions
#   choose a file, read the file, do operation on the file
# integrate all functions into main 
# ask for input 
#output desired values
#
#
#
#
#
#
##################################


import csv
from operator import itemgetter

PROMPT = '''
Choose
         (1) Top sites by country
         (2) Search by web site name
         (3) Top sites by views
         (q) Quit
         
Choice: '''

         
def open_file():
    while True:
        try:
            file = input("Input a filename: ")      # ask for filename
            fp = open(file,  encoding="ISO-8859-1") # if not found then print statement and repeat
            break
        except FileNotFoundError:
            print ("Error: file not found.")
            continue
    return fp


def read_file(fp):  # reads the file starting from the 2nd line 
    fp.seek(0)
    reader = csv.reader(fp)
    next(reader, None)
    list1 = []
    for line in reader:
        try:        # try statement ensures there are no empty or n/a cells 
            country_rank = int (line[0])
            website = line[1]           # finds and appends all the desired indicies
            page_views = (line[5])
            views = page_views.replace(" ", "")
            v = int (views)         
            country = line[30]
            t_rank = line[14]
            traffic_rank = t_rank.replace(" ", "") 
            tuple1 = country_rank , website, int (traffic_rank), v, country
            list1.append(tuple1)
        except ValueError:  # if the row has n/a in the desired cell skip it
            continue
    b = sorted (list1, key=itemgetter(0,4)) # sort the list 
    return b

def remove_duplicate_sites(list1):  #removes duplicate sites
    websites = []
    duplicates_removed = []
    for line in list1:
        list1 = (line[1].split(".",1)) # 2 lines get just the website name without prefix or suffix
        list2 = list1[1].split(".") 
        site = list2[0] #append the website to a list
        if site not in websites:
            websites.append(site)   # if the website has not been seen before than append it to the new list
            duplicates_removed.append(line)
        else:
            continue # otherwise skip it
    a = sorted(duplicates_removed, key=itemgetter(0, 1)) # sort the new list
    return a
    
def top_sites_per_country(list1 ,country):
   list2 = []
   for line in list1:
       if line[4] == country:   # gets all the values for a specific country
           list2.append(line)
       else:
           continue 
   list2.sort(key=itemgetter(0)) # sorts items in a specific country
   return list2[0:20] # return the top 20

def top_sites_per_views(list1):
   a = sorted(list1, key=itemgetter(3), reverse = True) # sort the list by page views
   b = remove_duplicate_sites(a) 
   b.sort(key=itemgetter(3), reverse = True) # remove duplicates and sort again
   return b[0:20] # print top 20
def main():
    print ("----- Web Data -----")
    list1 = read_file(open_file()) # opens and reads file
    options = "123qQ" # possible menu choices
    while True: # main loop
        print (PROMPT)
        choice = input ()
        while choice not in options:    # loop to get right choice
            print ("Incorrect input. Try again.")
            print (PROMPT)
            choice = input()
        if choice == "1": # top 20 by country
            print ("--------- Top 20 by Country -----------")
            country = input ("Country: ")
            print ("{:30s} {:>15s}{:>30s}".format("Website", "Traffic Rank", "Average Daily Page Views"))
            topsites = top_sites_per_country(list1, country)
            for line in topsites: # get website, rank, and views data from each line 
                website = line[1]
                rank = line[2]
                views = line[3]
                print ("{:30s} {:>15d}{:>30,d}".format(website, int(rank), int(views))) # print that information
                continue
        elif choice == "2":
            keyword = input("Search: ")
            print("{:^50s}".format("Websites Matching Query"))
            websites = []
            for line in list1: # list of websites
                website = line[1]
                if keyword.lower() in website:
                    websites.append(website) # if the keyword is in a website append that website to a list
            if len(websites) > 0: # if there is more than 0 items then print the websites
                for line in websites:
                    print (line) # print each website in the list
            else:
                print ("None found") # if the list has no items than there were no websites found
            continue
                
                
        elif choice == "3":
            print ("--------- Top 20 by Page View -----------")
            print ("{:30s} {:>15s}".format("Website",  "Ave Daily Page Views"))
            for line in top_sites_per_views(list1): # get and print site and view data
                site = line[1] 
                views = line[3]
                print ("{:30s} {:>20,d}".format(site, views))
            continue
        elif choice == "q" or choice == "Q": # option to quit the loop
            break
            
if __name__ == "__main__":
     main()
