# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:30:20 2019

@author: joema
"""

"""
Project 11
    creates lists of pokemon and move instances
    integrate all functions into main function
    users play the game until they quit 
    game ends and closing message is printed
    
    
"""
import csv
from random import randint
from random import seed
from copy import deepcopy
from pokemon import Pokemon
from pokemon import Move

seed(1) #Set the seed so that the same events always happen


#DO NOT CHANGE THIS!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock", 
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric", 
                   "psychic", "ice", "dragon", "dark", "fairy"]

#Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================
 
def read_file_moves(fp):  
    '''
        takes file pointer and makes csv reader
        iterates through reader and creates list of valid move instances
    '''
    moves_file = csv.reader(fp)
    move_objects = []
    next(moves_file, None)
    for line in moves_file:
        if line[2] != "1":
        
            pass
        elif line[9] == "1":
            
            pass
        elif line[4] == "" or not line[4]:
           
            pass
        elif line[6] == "" or not line[6]:
            
            pass
        
        else:
            move_object = Move(line[1], element_id_list[int(line[3])], int(line[4]), int(line[6]), int(line[9]))
            move_objects.append(move_object)
    return move_objects
        


def read_file_pokemon(fp):
    '''
        takes file pointer and makes csv reader
        iterates through reader and creates list of pokemon instances
    '''
    pokemon_file = csv.reader(fp) 
    pokemon_objects = []
    ids = set()
    next(pokemon_file,None)
    for line in pokemon_file:
        if line[3] != "":
            element2 = line[3].lower()
        else:
            element2 = ""
        if line[11] != "1":
            pass
        elif line[0] in ids:
            pass
        else:
            ids.add(line[0])
            pokemon = Pokemon((line[1].lower()), line[2].lower(), element2, None, int(line[5]), int(line[6]), \
                              int(line[7]), int(line[8]), int(line[9]))
            pokemon_objects.append(pokemon)
    return pokemon_objects
        

def choose_pokemon(choice,pokemon_list):
    '''
        takes integer input and returns pokemon at that index
    '''
    pokemon = ""
    try:
        num = int(choice)
        num -= 1
        pokemon = deepcopy(pokemon_list[num])
        return pokemon
    except ValueError:
        for items in pokemon_list:
            if choice == items.name:
                pokemon = deepcopy(items)
                return pokemon
            else:
                pass
    except IndexError:
        return None
    if pokemon == "":
        return None

def add_moves(pokemon,moves_list):
    '''
        adds moves to pokemon
    '''
    move = moves_list[randint(0, len(moves_list) - 1)]
    pokemon.add_move(move)
    for i in range(0,201):
        more_moves = []
        more_moves.append(moves_list[randint(0, (len(moves_list) - 1))])
        for move in more_moves:
            if move not in pokemon.moves:
                if move.element == pokemon.element1 or move.element == pokemon.element2:
                    pokemon.add_move(move)
                    continue
                else:
                    pass
            else:
                pass
        if len(pokemon.moves) == 4:
            return True
    return False
        
    

def turn (player_num, player_pokemon, opponent_pokemon):
    '''
        gives menu of possible moves and choices
        executes move
    '''
    print("Player {}'s turn".format(player_num))
    print(player_pokemon)
    while True:
        print ("Show options: 'show ele', 'show pow', 'show acc'")
        index = input("Select an attack between 1 and {} or show option or 'q': ".format(len(player_pokemon.moves)))
        if index.isdigit():
            index = int(index) - 1
            print("selected move: {}".format(player_pokemon.moves[index]))
            print()
            print("{} hp before:{}".format(opponent_pokemon.name, opponent_pokemon.hp))
            player_pokemon.attack(player_pokemon.moves[index], opponent_pokemon)
            print("{} hp after:{}".format(opponent_pokemon.name, opponent_pokemon.hp))
            print()
            if player_num == 1 and opponent_pokemon.hp == 0:
                print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(2,1))
                return False
            elif player_num == 2 and opponent_pokemon.hp == 0:
                print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(1,2))
                return False
            else:
                return True
        elif index.lower() == "show ele":
            ele = ""
            for moves in player_pokemon.moves:
                ele += "{:<15s}".format(moves.element)
            print (ele)
        elif index.lower() == "show pow":
            power = ""
            for moves in player_pokemon.moves:
                power += "{:<15d}".format(moves.power)
            print(power)
        elif index.lower() == "show acc":
            acc = ""
            for moves in player_pokemon.moves:
                acc += "{:<15d}".format(moves.accuracy)
            print (acc)
        elif index.lower() == "q":
            if int(player_num) == 1:
                print("Player {} quits, Player {} has won the pokemon battle!".format(1,2))
                return False
            else:
                print("Player {} quits, Player {} has won the pokemon battle!".format(2,1))
                return False
        else:
            print("Invalid input")
            

def main():
    """ 
    opens both move and pokemon files, creates player1 and player2 pokemon
    loops through the game until 1 pokemon faints and asks to restart 
    once players are done loop breaks and closing message is printed
    """
    fp = open("moves.csv", encoding="utf8") # opens csv files as readers
    moves_list = read_file_moves(fp)
    fp = open("pokemon.csv", encoding="utf8")
    pokemon_list = read_file_pokemon(fp)
    usr_inp = input("Would you like to have a pokemon battle? ").lower()
    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower() 
    if usr_inp != 'y':
        print("Well that's a shame, goodbye")
        return
    else:
        while True:
            pok = input("Player {}, choose a pokemon by name or index: ".format(1))
            pokemon1 = choose_pokemon(pok.lower(), pokemon_list)
            while not pokemon1:
                pok = input("Invalid option, choose a pokemon by name or index: ")
                pokemon1 = choose_pokemon(pok.lower(), pokemon_list)
            print("pokemon{}:".format(1))
            print(pokemon1)
            valid1 = add_moves(pokemon1, moves_list)
            if not valid1:
                print("Insufficient moves; choose a different pokemon.")
                pok = input("Player {}, choose a pokemon by name or index: ".format(1))
                pokemon1 = choose_pokemon(pok.lower(), pokemon_list)
                while not pokemon1:
                    pok = input("Invalid option, choose a pokemon by name or index: ")
                    pokemon1 = choose_pokemon(pok.lower(), pokemon_list)
                
                
            pok = input("Player {}, choose a pokemon by name or index: ".format(2))
            pokemon2 = choose_pokemon(pok.lower(), pokemon_list)
            while not pokemon2:
                pok = input("Invalid option, choose a pokemon by name or index: ")
                pokemon2 = choose_pokemon(pok.lower(), pokemon_list)
            print("pokemon{}:".format(2))
            print(pokemon2)
            valid2 = add_moves(pokemon2, moves_list)
            if not valid2:
                print("Insufficient moves; choose a different pokemon.")
                pok = input("Player {}, choose a pokemon by name or index: ".format(2))
                pokemon2 = choose_pokemon(pok.lower(), pokemon_list)
                while not pokemon2:
                    pok = input("Invalid option, choose a pokemon by name or index: ")
                    pokemon2 = choose_pokemon(pok.lower(), pokemon_list)
    
            start_player = 1
            valid = True
            while valid:
                if start_player % 2 != 0:
                    hp1 = pokemon1.hp 
                    valid = turn(1, pokemon1, pokemon2)
                    start_player += 1
                    hp2 = pokemon1.hp
                else:
                   valid = turn(2, pokemon2, pokemon1)
                   start_player += 1
                   if hp1 == hp2 and pokemon2.hp != 0 and hp2 != 0 and hp1 != 0 and valid != False:
                       print("Player 1 hp after: {}".format(pokemon1.hp))
                       print("Player 2 hp after: {}".format(pokemon2.hp))
            choice = input("Battle over, would you like to have another? ")
            while choice.lower() != "n" and choice.lower() != "y" and choice.lower() != "q":
                choice = input("Invalid option! Please enter a valid choice: ")
            if choice.lower() == "y":
                continue 
            elif choice.lower() == "q" or choice.lower() == "n":
                print("Well that's a shame, goodbye")
                break
        
    
if __name__ == "__main__":
    main()