# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:45:44 2019

@author: joema
"""
##########################################
# project 8
#   initialize functions recieve scrabble input data
#   use scrabble data to do calculations
#   integrate functions into main function to determine the best moves
#
#
#
#
#
#
#
###########################################

import itertools
from operator import itemgetter
SCORE_DICT = {"a": 1, "b": 3, "c":3, "d": 2, "e":1, "f": 4, "g":2, "h":4, "i":1, "j":8, "k":5, "l":1, \
              "m":3, "n":1, "o":1, "p":3, "q":10, "r":1, "s":1, "t":1, "u":1, "v":4, "w":4, "x":8, "y":4, "z":10}

def open_file():   # prompts for file and opens file
   while True:
        try:
            file = input("Input word file: ")      # ask for filename
            fp = open(file,  encoding="ISO-8859-1") 
            break
        except FileNotFoundError:
            print ("Error: file not found.") # if not found then print statement and repeat
            continue
   return fp

def read_file(fp): # creates a dictionary of words in the word file
    fp.seek(0)
    word_dict = {}
    for line in fp:
        word = line.rstrip()
        if len(word) >= 3 and "-" not in word and "'" not in word: # ensures that only words are being added to dict
            word_dict[word.lower()] = 1
    return word_dict

def calculate_score(rack,word):
    score = 0
    if len(rack) == 7 and len(word) == 7 or len(rack) == 7 and len(word) == 8: # gives bonus if the entire rack is used
        score += 50
    for letter in word:
        score += SCORE_DICT[letter.lower()]  # uses scores from scores dict and adds to overall score
    return score

def generate_combinations(rack,placed_tile): # creates combinations of characters and adds them to a set
    combinations = []
    newcombo = []
    for word in itertools.combinations(rack + placed_tile.lower(),3):
        combinations.append(word)
    for word in itertools.combinations(rack + placed_tile.lower(),4):
        combinations.append(word)
    for word in itertools.combinations(rack + placed_tile.lower(),5):
        combinations.append(word)
    for word in itertools.combinations(rack + placed_tile.lower(),6):
        combinations.append(word)
    for word in itertools.combinations(rack + placed_tile.lower(),7):
        combinations.append(word)
    for word in itertools.combinations(rack + placed_tile.lower(),8):
        combinations.append(word)
    if not placed_tile:
        return set(combinations) # if placed tile is empty add all combinations to set
    else:
        for word in combinations:
            if placed_tile.lower() not in word:  # ensures placed tile is in the word
                pass
            else:
                newcombo.append(word)
        return set(newcombo)

def generate_words(combo,scrabble_words_dict):     # gets words from combinations
    set1 = set()
    for w in itertools.permutations(combo):
        string = "".join(list(w))  
        if string not in scrabble_words_dict:   # checks that possible words are in the dict
            pass
        else:
            set1.add(string) # if they are in the dict then add them to the set
    return set1

def generate_words_with_scores(rack,placed_tile,scrabble_words_dict): # uses a variety of functions to return word and score values
    dictscore = {}
    combinations = generate_combinations(rack, placed_tile)
    for combo in combinations: 
        words = generate_words(combo, scrabble_words_dict)
        for word in words:
            dictscore[word] = calculate_score(rack,word)
    return dictscore

def sort_words(word_dic):
    scorelist = []
    lengthlist = []
    for word, score in word_dic.items(): # takes the word dict and splits it up to add to lists
        items = (word, score, len(word))
        scorelist.append(items)
        lengthlist.append(items)
    score = sorted(scorelist, key=itemgetter(0)) # sorts the 2 different lists
    scores = sorted(score, key=itemgetter(1,2), reverse=True)
    lengths = sorted(scores, key=itemgetter(2), reverse=True)
    return scores, lengths
    
    

def display_words(word_list,specifier): # prints top 5 based on length and score
    
    if specifier == "score":
        i = 0
        if len(word_list) < 5: # if the list is less than 5
            print("{:>6s}  -  {:s}".format("Score", "Word"))
            for item in word_list:
                print("{:>6d}  -  {:s}".format(item[1], item[0]))
        else:
            print("{:>6s}  -  {:s}".format("Score", "Word")) # prints top 5 based on score
            for word in word_list:
                if i == 5 : # counter to count top 5
                    break
                else:
                    print("{:>6d}  -  {:s}".format(word[1], word[0]))
                    i +=1
                
    elif specifier == "length": # same as the score portion but prints top 5 on length
        i = 0
        if len(word_list) < 5:
            print("{:>6s}  -  {:s}".format("Length", "Word"))
            for item in word_list:
                print("{:>6d}  -  {:s}".format(item[2], item[0]))
        else:
            print("{:>6s}  -  {:s}".format("Length", "Word"))
            for word in word_list:
                if i == 5 :
                    break
                else:
                    print("{:>6d}  -  {:s}".format(word[2], word[0]))
                i +=1
def main():
    print ("Scrabble Tool")
    choice = input("Would you like to enter an example (y/n): ")
    while choice.lower() == "y": # enters loop if choice is yes
        fp = open_file()
        word_dict = read_file(fp)
        rack = input( "Input the rack (2-7chars): ")
        while True:
            i = 0
            for item in rack:
                if not item.isalpha() or len(rack) < 2 or len(rack) > 7: # checks every element in the rack to determine if it is useable
                    print ("Error: only characters and 2-7 of them. Try again.")
                    rack = input( "Input the rack (2-7chars): ")
                    break
                else:
                    i += 1 # counts successful passes
                    pass
            if len(rack) == i : # if the loop passes through all the characters in the string it is viable
                break
            else:
                pass
        placed = input ("Input tiles on board (enter for none): ")
        while True: # same logic as the loop before
            i = 0 
            if placed == "":
                break
            else:
                for tile in placed:
                    if not tile.isalpha(): 
                        print ("Error: tiles must be characters or empty")
                        placed = input( "Input tiles on board (enter for none): ")
                        break
                    else:
                        i += 1
                        pass
                if len(placed) == i :
                    break
                else:
                    pass
        words_possible = {}
        for tile in placed: # iterates through placed tiles to get words
            words_possible.update(generate_words_with_scores(rack, tile, word_dict))
        if not placed: # if the placed tile is empty string
            words_possible.update(generate_words_with_scores(rack, placed, word_dict))
        scores, length = sort_words(words_possible)
        print ("Word choices sorted by Score") # prints different statements
        display_words(scores, "score")
        print("Word choices sorted by Length")
        display_words(length, "length")
        choice = input("Do you want to enter another example (y/n): ")  # asks to continue
    print ("Thank you for playing the game") # prints once choice is n
        


if __name__ == "__main__":
    main()
