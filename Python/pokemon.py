# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:31:17 2019

@author: joema
"""

"""
    Project 11
    creates move and pokemon classes for proj11.py
"""

from random import randint


#DO NOT CHANGE THIS!!!
# =============================================================================
is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'}, 
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'}, 
                           'electric': {'water', 'flying'}, 
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock', 'steel'}, 
                           'fire': {'bug', 'grass', 'ice', 'steel'}, 
                           'flying': {'bug', 'fighting', 'grass'}, 
                           'ghost': {'ghost', 'psychic'}, 
                           'grass': {'water', 'ground', 'rock'}, 
                           'ground': {'electric', 'fire', 'poison', 'rock', 'steel'}, 
                           'ice': {'dragon', 'flying', 'grass', 'ground'}, 
                           'normal': set(), 
                           'poison': {'fairy', 'grass'}, 
                           'psychic': {'fighting', 'poison'}, 
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost','poison','steel'}, 
                            'dragon': {'steel'}, 
                            'dark': {'dark', 'fairy', 'fighting'},
                            'electric': {'dragon', 'electric', 'grass'},
                            'fairy': {'fire', 'poison', 'steel'},
                            'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'}, 
                            'fire': {'dragon', 'fire', 'rock', 'water'}, 
                            'flying': {'electric', 'rock', 'steel'}, 
                            'ghost': {'dark'}, 
                            'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'}, 
                            'ground': {'bug','grass'}, 
                            'ice': {'fire', 'ice', 'steel', 'water'}, 
                            'normal': {'rock', 'steel'}, 
                            'poison': {'ghost', 'ground', 'poison', 'rock'}, 
                            'psychic': {'psychic', 'steel'}, 
                            'rock': {'fighting', 'ground', 'steel'}, 
                            'steel': {'electric', 'fire', 'steel', 'water'},
                            'water': {'dragon','grass', 'ice'}
                            }

no_effect_dictionary = {'electric': {'ground'}, 
                        'dragon': {'fairy'},
                        'fighting': {'ghost'}, 
                        'ghost': {'normal', 'psychic'}, 
                        'ground': {'flying'}, 
                        'normal': {'ghost'}, 
                        'poison': {'steel'},
                        'psychic': {'dark'}, 
                        
                        'bug': set(), 'dark': set(), 'fairy': set(),'fire': set(), 
                        'flying': set(), 'grass': set(), 'ice': set(), 
                        'rock': set(), 'steel': set(), 'water': set()
                        }

#Dictionaries that determine element advantages and disadvantages
# =============================================================================

class Move(object):
    def __init__(self, name = "", element = "normal", power = 20, accuracy = 80,
                 attack_type = 2):
        """ Initialize attributes of the Move object """
        
        self.name = name
        self.element = element
        self.power = power
        
        self.accuracy = accuracy
        self.attack_type = attack_type  #attack_type is 1, 2 or 3 
        # 1 - status moves, 2 - physical attacks, 3 - special attacks
        
    def __str__(self):
            
        '''
            returns name of move
        '''        
        return self.name

    def __repr__(self):
        '''
            returns name of move for printing to console
        '''
        return self.__str__()
    
    def get_name(self):
        '''
            returns name of move
        '''
        return self.name
    
    def get_element(self):
        '''
            returns element of move
        '''
        return self.element
    
    def get_power(self):
        '''
            returns power of move
        '''
        return self.power
    
    def get_accuracy(self):
        '''
            returns accuracy of move
        '''
        return self.accuracy
    
    def get_attack_type(self):
        '''
            returns type of attack of move
        '''
        return self.attack_type

    def __eq__(self,m):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == m.get_name() and self.element == m.get_element() and\
                self.power == m.get_power() and self.accuracy == m.get_accuracy() and\
                self.attack_type == m.get_attack_type()
        
        
class Pokemon(object):
    def __init__(self, name = "", element1 = "normal", element2 = "", moves = None,
                 hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10):
        ''' initializes attributes of the Pokemon object '''
        
        self.name = name
        self.element1 = element1
        self.element2 = element2
        
        self.hp = hp
        self.patt = patt
        self.pdef = pdef
        self.satt = satt
        self.sdef = sdef
        
        self.moves = moves
        
        try:
            if len(moves) > 4:
                self.moves = moves[:4]
                
        except TypeError: #For Nonetype
            self.moves = list()

    def __eq__(self,p):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == p.name and \
            self.element1 == p.element1 and \
            self.element2 == p.element2 and \
            self.hp == p.hp and \
            self.patt == p.patt and \
            self.pdef == p.pdef and \
            self.satt == p.satt and \
            self.sdef == p.sdef and \
            self.moves == p.moves

    def __str__(self):
        '''
            returns all attributes of pokemon instance as string
        '''
        moves = ""
        for item in self.moves:
            moves += "{:<15s}".format(item.__str__())
        return "{:<15s}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}\n{:<15s}{:<15s}\n{:<15s}".format(self.name, self.hp, self.patt, self.pdef, self.satt, self.sdef, self.element1, self.element2, moves)

    def __repr__(self):
        '''
           returns string method for printing to console
        '''
        return self.__str__()


    def get_name(self):
        '''
            returns name of pokemon
        '''
        return self.name
    
    def get_element1(self):
        '''
           returns first element of pokemon
        '''
        return self.element1
    
    def get_element2(self):
        '''
            returns 2nd element of pokemon
        '''
        return self.element2
    
    def get_hp(self):
        '''
            returns hp of pokemon
        '''
        return self.hp
    
    def get_patt(self):
        '''
            returns patt
        '''
        return self.patt

    def get_pdef(self):
        '''
            returns pdef
        '''
        return self.pdef

    def get_satt(self):
        '''
            returns satt
        '''
        return self.satt

    def get_sdef(self):
        '''
            returns sdef
        '''
        return self.sdef
    
    def get_moves(self):
        '''
            returns list of moves of pokemon
        '''
        return self.moves

    def get_number_moves(self):
        '''
            returns # of moves 
        '''
        return len(self.moves)

    def choose(self,index):
        '''
            returns a specific move
        '''
        try:
            return self.moves[index]
        except IndexError:
            return None

        
    def show_move_elements(self):
        '''
            shows elements for each move
        '''
        elements = ""
        for moves in self.moves:
            elements += "{:>15s}".format(moves.get_element())
        return elements

    def show_move_power(self):
        '''
            shows power of each move
        '''
        power = ""
        for moves in self.moves:
            power += "{:>15d}".format(moves.get_power())

    def show_move_accuracy(self):
        '''
            shows accuracy of each move
        '''
        accuracy = ""
        for moves in self.moves:
            accuracy += "{:>15d}".format(moves.get_accuracy())
        
        
    def add_move(self, move):
        '''
            adds a move to a pokemons move list
        '''
        if len(self.moves) <= 3:
            self.moves.append(move)
            
        
    def attack(self, move, opponent):
        '''
            attack method used for pokemon battle
        '''
    
        if move.get_attack_type() == 2:
            damage = ((((move.power)*(self.patt / opponent.pdef) * (20)) / 50) + 2)
        elif move.get_attack_type() == 3:
            damage = ((((move.power)*(self.satt / opponent.sdef) * (20)) / 50) + 2)
        else:
            print("Invalid attack_type, turn skipped.")
            return None
        accuracy = randint(1,100)
    
        if accuracy > move.get_accuracy():
            print ("Move missed!")
            damage = 0
            return None
        modifier = 1
        if opponent.element1 in is_effective_dictionary[move.element]:
            modifier = modifier * 2
        elif opponent.element1 in not_effective_dictionary[move.element]:
            modifier = modifier * (1/2)
        elif opponent.element1 in no_effect_dictionary[move.element]:
            damage = 0
        if opponent.element2 in is_effective_dictionary[move.element]:
            modifier = modifier * 2
        elif opponent.element2 in not_effective_dictionary[move.element]:
            modifier = modifier * (1/2)
        elif opponent.element2 in no_effect_dictionary[move.element]:
            print("No effect!")
            damage = 0
           
        
        if modifier > 1:
            print("It's super effective!!!!")
        elif modifier < 1:
            print( "Not very effective...")
        if move.element == self.element1:
            modifier = modifier * 1.5
        if move.element == self.element2:
            modifier = modifier * 1.5
        
        damage = int(damage * modifier)
        opponent.subtract_hp(damage)
        
            
        
    def subtract_hp(self,damage):
        '''
           subtracts a certain hp from a desired pokemon
        '''
        self.hp = self.hp - damage
        if self.hp <= 0 :
            self.hp = 0