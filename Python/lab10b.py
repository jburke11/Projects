# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:41:14 2019

@author: joema
"""

import cards

# Create the deck of cards
a =0
b = 0
the_deck = cards.Deck()
#the_deck.shuffle()
player1_hand=[]
player2_hand=[]
for i in range(5):
    player1_hand.append(the_deck.deal())
    player2_hand.append(the_deck.deal())
print ("Starting Hands")
print ("Hand1:", player1_hand)
print ("Hand2:", player2_hand)
print ()
while True:
    player1_card = player1_hand[0]
    player2_card = player2_hand[0]
    if player1_card.rank() == player2_card.rank():
        print( "Battle was", "1:", player1_card,",", "2:", player2_card,",", "Tie" )
    elif player1_card.rank() > player2_card.rank():
        print( "Battle was", "1:", "{}{}".format(player1_card, ","),"2:", "{}{}".format(player2_card, "."), "Player 1 wins battle.")
        a += 1
        player1_hand.append(player1_hand.pop(0))
        player1_hand.append(player2_hand.pop(0))
        
    else:
        print( "Battle was", "1:", "{}{}".format(player1_card, ","),"2:", "{}{}".format(player2_card, "."), "Player 2 wins battle.")
        player2_hand.append(player2_hand.pop(0))
        player2_hand.append(player1_hand.pop(0))
        b += 1
    print ("hand1:", player1_hand)
    print ("hand2:", player2_hand)
    if len(player1_hand) == 0:
        print ("Player 2 wins!!!")
        break
    elif len (player2_hand) == 0:
        print("Player 1 wins!!!")
        break
    
    choice = input("Keep Going: (Nn) to stop:")
    if choice.lower() != "n":
        continue
    else:
        if a > b:
            print ("Player 1 wins!!!")
            break
        else:
           print ("Player 2 wins!!!") 
           break