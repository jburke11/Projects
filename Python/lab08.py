# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:32:00 2019

@author: joema
"""
import string
from operator import itemgetter


def add_word( word_map, word ):

    # puts the word in the dictionary if it is not there
    if word not in word_map:
        word_map[ word ] = 0

    # if the word is in the dictionary add 1 to the frequency number
    word_map[ word ] += 1


def build_map( in_file, word_map ):

    for line in in_file:

        # splits the line in the text on whitespace
        word_list = line.split()

        for word in word_list:
            if word:
            # strip the words of punctuation and add to dictionary
                word = word.strip().strip(string.punctuation)
                add_word( word_map, word.lower())
                
            else:
                continue
        

def display_map( word_map ):

    word_list = list()

    # for the key and the item in the dictionary make a list of tuples
    for word, count in word_map.items():
        word_list.append( (word, count) )
    # sort the list of tuples on frequency number
    freq_list = sorted( word_list, key=itemgetter(0,1), reverse = True )

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():

    try:
        file = input("Input document name: ")
        in_file = open( file, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


word_map = dict()
in_file = open_file()

if in_file != None:

    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()

