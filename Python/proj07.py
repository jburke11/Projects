# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 21:26:52 2019

@author: joema
"""
###################################
# Project 7
# define all funcions
#   choose a file, open file, and do work based on the information the file contains
# integrate all functions into main loop
#   ask for input, send data through different functions
#    output desired information
#
#
#
###################################

import matplotlib.pyplot as plt
import csv
from operator import itemgetter

MIN_YEAR = 2009
MAX_YEAR = 2017

def open_file(prompt_str): # opens file depending on the prompt
    if prompt_str == "Enter the travel data file: ": # if the prompt is to open data file
        while True:
            try:
                file = input (prompt_str)    # use try except to check for right filename
                fp = open(file, "r", encoding = "utf-8")  
                break
            except FileNotFoundError:
                print ("File not found! Try Again!") 
                continue
    else:
        while True:         # if the prompt is for country code file
            try:
                file_codes = input (prompt_str)
                fp = open(file_codes, "r")
                break
            except FileNotFoundError:
                print ("File not found! Try Again!")  # makes sure country code file is right
                continue
    return fp # returns file pointer

def read_country_code_file(fp): # reads the country code file
    fp.seek(0)
    country_code_list = []
    reader = csv.reader(fp)
    next(reader, None)
    for line in fp:
        line.strip() # strips the white space and splits the elements at /
        codes, country = line.split("/")
        country_codes = codes, country.strip() # creates tuple
        country_code_list.append(country_codes) # appends tuple to list
    country_code_list.sort(key=itemgetter(0))
    return country_code_list # returns list of tuples

def read_travel_file(fp):
    fp.seek(0)
    total_list = []
    listyears = []
    datatemp = []
    reader = csv.reader(fp)
    next(reader, None)
    for line in reader:     # collects information from each line 
        year = int(line[0])
        country_name = line[1][:20]
        country_code = line[2]
        num_departures = int(line[3])
        num_arrivals = int(line[4])
        expenditures = float(line[5])
        receipts = float(line[6]) 
        num_departures = num_departures /1000
        num_arrivals = num_arrivals / 1000
        expenditures = expenditures /  1000000
        receipts = receipts /  1000000
        try:
            eavg = expenditures / num_departures # tries to calculate average
        except ZeroDivisionError:
            eavg = 0    # if there are no departures set avg to zero
        try: # same process for expenditures
            ravg = receipts / num_arrivals
        except ZeroDivisionError:
            ravg = 0
        data = (year, country_name, country_code, num_arrivals, num_departures,expenditures, receipts, round ((eavg * 1000) , 2), round ((ravg * 1000) ,2)) 
        if data[0] not in listyears: # makes list of tuples based on years
            datatemp = []
            listyears.append(data[0])
            datatemp.append(data)
            total_list.append(datatemp)
        else:
            datatemp.append(data)
    return total_list  # returns list of list and tuples
        

def get_country_code_data(country_code, total_list):
    country_list = []
    total_years = []
    sample_years = []
    for line in total_list:
        for data in line:
            if data[0] not in total_years:    # finds out all the years in the datasheet
                    total_years.append(data[0])
            if data[2] == country_code:  # appends the data if the country codes match
                country_list.append(data)
                if data[0] not in sample_years: # finds out how many years are in the country code subset
                    sample_years.append(data[0])
            else:
                continue
    country_list.sort(key=itemgetter(0))
    if not country_list: # if country list is empty return none
        return None
    else:
        return country_list


def display_country_data(country_list):
    total_departures = 0
    total_arrivals = 0
    total_expenditures = 0
    total_receipts = 0
    # Get the country name from the list
    country_name = country_list[0][1]
    
    # Print table title
    title = "Travel Data for {}".format(country_name)
    print("\n{:^80s}".format(title))
    
    # Table headers
    header = ['Year', 'Departures','Arrivals','Expenditures', 'Receipts']
    units = ['','(thousands)','(thousands)','(millions)','(millions)']
    
    # header string formatting
    print ("{:6s}{:>15s}{:>15s}{:>15s}{:>15s}".format(header[0], header[1], header[2], header[3], header[4]))
    print ("{:6s}{:>15s}{:>15s}{:>15s}{:>15s}".format(units[0], units[1], units[2], units[3], units[4]))
    for line in country_list: # calculates totals based on each element in the list
        year = line[0]
        departures = line[4]
        arrivals = line[3]
        expenditures = line[5]
        receipts = line[6]
        total_departures += departures
        total_arrivals += arrivals
        total_expenditures += expenditures
        total_receipts += receipts
    # Numeric values string formatting
        print ('{:<6d}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}'.format(year, departures, arrivals, expenditures, receipts))
    print ()
    print ('{:6s}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}'.format("Total", total_departures, total_arrivals, total_expenditures, total_receipts ))
    print ()
    
    
def display_year_data(year_list): # displays year data in a table
    total_departures = 0
    total_arrivals = 0
    total_expenditures = 0
    total_receipts = 0
    
    # Get the year from the list
    year = str(year_list[0][0])
    
    # Print table title
    title = "Travel Data for {:s}".format(year)
    print("\n{:^80s}".format(title))
    
    # Table headers
    header = ['Country Name', 'Departures','Arrivals','Expenditures',\
              'Receipts']
    units = ['','(thousands)','(thousands)','(millions)','(millions)']
    
    print ('{:25s}{:15s}{:15s}{:15s}{:15s}'.format(header[0], header[1], header[2], header[3], header[4]))
    print ('{:25s}{:15s}{:15s}{:15s}{:15s}'.format(units[0], units[1], units[2], units[3], units[4]))
    # header string formatting
    # '{:25s}{:15s}{:15s}{:15s}{:15s}'
    for line in year_list:  # collects information from the list
        country = line[1]
        departures = line[4]
        arrivals = line[3]
        expenditures = line[5]
        receipts = line[6]
        total_departures += departures
        total_arrivals += arrivals
        total_expenditures += expenditures
        total_receipts += receipts
    # Rows string formatting
    # '{:20s}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}'
        print ("{:20s}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}".format(country, departures, arrivals, expenditures, receipts))
    print ()
    print ("{:20s}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}".format("Total", total_departures, total_arrivals, total_expenditures, total_receipts ))
    print ()
    

def prepare_bar_plot(year_list):    # gets top 20 based on year
    expend_list = []
    receipt_list = []
    for line in year_list:  # creates two list based on country name and expenditure/ receipt data
        expend_data = line[1], line[7]  
        expend_list.append(expend_data) 
        receipt_data = line[1], line[8]
        receipt_list.append(receipt_data)
    expend_list.sort(key=itemgetter(1), reverse = True)
    receipt_list.sort(key=itemgetter(1), reverse = True)
    return expend_list[0:20], receipt_list[0:20]    
    

def prepare_line_plot(country_list):
   receipt_list = []
   expend_list =[]   
   
   for data in country_list: # gets average expenditure and receipt data
      expend_list.append(data[7])
      receipt_list.append(data[8])
           
   return expend_list, receipt_list


def plot_bar_data(expend_list, receipt_list, year):
    '''
        This function plots the the top 20 countries with the highest average
        expenditures and the top 20 countries with the highest receipts.
        
        Returns: None
    
    '''

    # prepare the columns
    countries_expend = [elem[0] for elem in expend_list]
    values_expend = [elem[1] for elem in expend_list]
    
    countries_receipt = [elem[0] for elem in receipt_list]
    values_receipt = [elem[1] for elem in receipt_list]
    
    # Average expenditures
    
    x = range(20) # top 20 countries are to be plotted.

    fig, axs = plt.subplots(2, 1,figsize=(7,10))
    title = "Top 20 countries with highest average expenditures {:4d}".format(int(year))
    axs[0].set_title(title)
    axs[0].bar(x, values_expend, width=0.4, color='b')
    axs[0].set_ylabel("Avg. Expenditures (US dollar)")
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(countries_expend , rotation='90')
    
    # Average receipt
    title = "Top 20 countries with highest average receipt  {:4s}".format(year)
    axs[1].set_title(title)
    axs[1].set_ylabel("Avg. Receipts (US dollar)")
    axs[1].bar(x, values_receipt, width=0.4, color='b')
    axs[1].set_xticks(x)
    axs[1].set_xticklabels(countries_receipt , rotation='90')
    fig.tight_layout()
    plt.show()
    
    ##comment the previous line and uncomment the following two lines when trying to pass Test 4
    fig.savefig('avg_expense_receipts.png',dpi=100)
    fig.clf()


def plot_line_data(country_code, expend_list, receipt_list):
    '''
        Plot the line plot for the expenditures and receipts for the
        country between 2009 and 2017
        
        Returns: None
    '''
    
    
    title = "Average expenditures and receipts for {} between 2009 and 2017".format(country_code)
    years = range(MIN_YEAR, MAX_YEAR+1)
    fig, axs = plt.subplots(figsize=(7,5))
    axs.set_title(title)
    axs.set_ylabel("Cost (US dollar)")
    axs.plot(years, expend_list, years, receipt_list)
    axs.legend(['Expenditures','Receipt'])

    plt.show()
    
    ##comment the previous line and uncomment the following two lines when trying to pass Test 4
    fig.savefig('line.png',dpi=100)
    fig.clf()

def main():

    
   BANNER = "\nInternational Travel Data Viewer\
   \n\nThis program reads and displays departures, arrivals, expenditures,"\
   " and receipts for international travels made between 2009 and 2017."
    
    # Prompt for option
   OPTION = "\nMenu\
   \n\t1: Display data by year\
   \n\t2: Display data by country\
   \n\t3: Display country codes\
   \n\t4: Stop the Program\
   \n\n\tEnter option number: "
    
    
   print(BANNER)
   
   fp = open_file("\nEnter the travel data file: ") # prompts to open two files
   fp_codes = open_file("\nEnter the country code file: ")
   choices = ("1234") # correct options for menu
   while True:
       choice = input(OPTION)
       while choice not in choices:    # loop to get right choice
           print ("Invalid option. Try Again!")
           choice = input(OPTION)
       if choice == "1":  
           year_list = []
           totalyears = []
           for i in range (2009, 2018): # creates list of possible years
               totalyears.append(str(i))
           year = input("Enter year: ")
           while year not in totalyears: # if the input is not in the year list
               print ("Year needs to be between 2009 and 2017. Try Again!")
               year = input("Enter year: ")
           travel_list = read_travel_file(fp)
           for line in travel_list:
               for data in line:
                   if data[0] == int (year): # gets data based on inputted year
                       year_list.append(data)
           display_year_data(year_list) # displays table
           graph = input("Do you want to plot (yes/no)?")
           if graph.lower() == "yes":
               expend_list, receipt_list = prepare_bar_plot(year_list)
               plot_bar_data(expend_list, receipt_list, year)
               continue
           else:
               continue
        
       if choice == "2" :
           code_list = []
           country_code = input("Enter country code: ")
           codes = read_country_code_file(fp_codes)
           for line in codes:
               code_list.append(line[0]) # creates list of just country codes
           while country_code.upper() not in code_list: # loop until correct country code is input
               print ("Country code is not found! Try Again!") 
               country_code = input("Enter country code: ")
                
           total_list = read_travel_file(fp)
           data = get_country_code_data(country_code.upper(), total_list)
           display_country_data(data) # displays table based on data
           graph = input("Do you want to plot (yes/no)?")
           if graph.lower() == "yes":
               expend_list, receipt_list = prepare_line_plot(data)
               plot_line_data(country_code, expend_list, receipt_list)
               continue
           else:
               continue
       if choice == "3":
           codes = read_country_code_file(fp_codes) # gets country code information
           print ("Country Code Reference")
           print ("{:15s}{:25s}".format("Country Code", "Country Name"))
           for line in codes:
               country_code = line[0] # gets code
               country = line[1] # gets country
               print ("{:15s}{:25s}".format(country_code, country)) # prints country and code in a table
           continue
       if choice == "4": # break if choice is 4
           break
        
    
    
    
   print("\nThanks for using this program!") # print statement once loop is over
if __name__ == "__main__":
    main()        
