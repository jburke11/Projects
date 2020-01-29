# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:43:12 2019

@author: joema
"""


##
## Demonstrate some of the operations of the Pet classes
##

import pets

def main():
    
    try:

        # Hamster
        A = pets.Pet( "Hamster" )
        print( A )       
        
        # Dog named Fido who chases Cats
        B = pets.Dog( "Fido" )
        print( B )

        # Cat named Fluffy who hates everything
        C = pets.Cat( "Fluffy", "everything" )
        print( C )

    except pets.PetError:
        
        print( "Got a pet error." )

main()