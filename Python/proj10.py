# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:31:59 2019

@author: joema
"""

#######################################
# Project 10
#   define all functions to create 'aces up' game 
#   integrate all functions into 'main' to play the game
#
#
#
#
#
#######################################



import cards  # required !!!
RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
        of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def init_game(): # initializes the stock, tableau, and foundation for the game
    
    stock = cards.Deck() # creates instance of Deck class
    stock.shuffle() # shuffles deck
    foundation = []
    tableau = [[""],[""],[""],[""]]
    tableau[0] = [stock.deal()] # deals 1 card to each tableau stack
    tableau[1] = [stock.deal()]
    tableau[2] = [stock.deal()]
    tableau[3] = [stock.deal()]
 
    return (stock, tableau, foundation) 
                               
    
def deal_to_tableau( stock, tableau ):
        
    tableau[0].append(stock.deal()) # deals 1 card to each tableau stack
    tableau[1].append(stock.deal())
    tableau[2].append(stock.deal())
    tableau[3].append(stock.deal())
 
    
    return None


def display( stock, tableau, foundation ):
    '''Display the stock, tableau, and foundation.'''
    
    print("\n{:<8s}{:^13s}{:s}".format( "stock", "tableau", "  foundation"))
    
    # determine the number of rows to be printed -- determined by the most
    #           cards in any tableau column
    max_rows = 0
    for col in tableau:
        if len(col) > max_rows:
            max_rows = len(col)

    for i in range(max_rows):
        # display stock (only in first row)
        if i == 0:
            display_char = "" if stock.is_empty() else "XX"
            print("{:<8s}".format(display_char),end='')
        else:
            print("{:<8s}".format(""),end='')

        # display tableau
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print("{:4s}".format( str(col[i]) ), end='' )

        # display foundation (only in first row)
        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')

        print()

def get_option():

    option = input("\nInput an option (DFTRHQ): ") # input option
    options = option.strip().split() # creates list with the options ignores whitespace
    if not options[0].isalpha(): # 1st option will always be a letter otherwise false
        return None
    elif options[0].upper() == "D" and len(options) == 1: # this suite of statements ensures that the options
        return options                                    # are all in the correct format
    elif options[0].upper() == "F" and options[1].isnumeric() == True and len(options) == 2:
        return options
    elif options[0].upper() == "T" and len(options) != 3:
        print("Error in option: {}".format(option))
        return None
    elif options[0].upper() == "T" and options[1].isnumeric() == True and options[2].isnumeric() == True and len(options) == 3:
        return options
    elif options[0].upper() == "R" and len(options) == 1:
        return options
    elif options[0].upper() == "H" and len(options) == 1:
        return options
    elif options[0].upper() == "Q" and len(options) == 1:
        return options
    else:
        print("Error in option: {}".format(option))
        return None
            
def validate_move_to_foundation( tableau, from_col ):
    if not from_col: # if from_col is an empty value
       print("Invalid index.") 
       return False
    elif not 1 <= int(from_col) <= 4: # if from-col is not between 1 and 4
        print("Invalid index.")
        return False
    else:
        for i in range(0,4): # iterates through the columns
            if len(tableau[from_col - 1]) == 0: # if from col is empty
                return False
            elif tableau[i] == tableau[from_col - 1]: # if i equals the from col skip it 
                pass
            elif len(tableau[i]) == 0 : # if the tableau column is empty skip it
                pass
            elif tableau[from_col - 1][-1].value() == 1: # if the from col value is an ace it can't go to foundation
                return False
            elif tableau[i][-1].suit() == tableau[from_col -1][-1].suit() and tableau[i][-1].rank() > tableau[from_col - 1][-1].rank():
                return True # if the two cards have the same suit and the rank of one is larger than from col return true
            elif tableau[i][-1].suit() == tableau[from_col -1][-1].suit() and tableau[i][-1].value() == 1: # if two cards have the same suit and one is an ace
                return True
    return False
    
def move_to_foundation( tableau, foundation, from_col ):
    result = validate_move_to_foundation(tableau, from_col) # checks validity
    if result == True:
        foundation.append(tableau[from_col - 1].pop(-1)) # takes off last card from tableau and appends to foundation
    else:
        print("Error, cannot move {}.".format(tableau[from_col - 1][-1]))   


def validate_move_within_tableau( tableau, from_col, to_col ):
    
    if from_col == "": # makes sure it isn't empty
       print("Invalid index.")
       return False
    elif not 1 <= int(from_col) <= 4: # makes sure it's in the correct range
        print("Invalid index.")
        return False
    elif to_col == "":
       print("Invalid index.") 
       return False
    elif not 1 <= int(to_col) <= 4:
        print("Invalid index.")
        return False
    elif len(tableau[to_col - 1]) == 0: # checks if the to col is empty
        return True
    else:
        return False
 



def move_within_tableau( tableau, from_col, to_col ):
    result = validate_move_within_tableau(tableau, from_col, to_col) # checks validity of move
    if result: 
        tableau[to_col - 1].append(tableau[from_col - 1].pop(-1)) # takes last value from from_col and appends it to the to_col
    else:
        print("Invalid move")
  

        
def check_for_win( stock, tableau ):
    try: # makes sure there is only 1 card in each tableau spot and that they're all aces
        if len(stock) == 0 and tableau[0][0].value() == 1 and tableau[1][0].value() == 1 and tableau[2][0].value() == 1 and tableau[3][0].value() == 1 \
        and len(tableau[0]) == 1 and len(tableau[1]) == 1 and len(tableau[2]) == 1 and len(tableau[3]) == 1 :
            return True
        else:
            return False
    except IndexError: # if a col is empty
        return False

        
def main():
 
    stock, tableau, foundation = init_game()
    print( MENU )
    display( stock, tableau, foundation )

    while True:
        if check_for_win(stock, tableau) == True: # checks for win before entering another option
            print("You won!")
            break
        options = get_option()
        if not options:
            print("Invalid option.")
        elif options[0].upper() == "D": # deals to tableau
            deal_to_tableau(stock, tableau) 
        elif options[0].upper() == "F": # moves to foundation
            move_to_foundation(tableau, foundation, int(options[1]))
        elif options[0].upper() == "T": # moves within tableau
            move_within_tableau(tableau, int(options[1]), int(options[2]))
        elif options[0].upper() == "R": # restarts game
            print("=========== Restarting: new game ============")
            print(RULES)
            stock, tableau, foundation = init_game() # re initializes game
            print( MENU )
        elif options[0].upper() == "H": # prints help
            print (MENU)
        elif options[0].upper() == "Q": # breaks loop
            print("You have chosen to quit.")
            break
        else:
            print("Invalid option.")
        if check_for_win(stock, tableau) == True: # checks for win after move
            print("You won!")
            break
        display( stock, tableau, foundation) # displays hand
if __name__ == "__main__":
    main()