# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:16:52 2019

@author: joema
"""

vowels = "aeiou"
while vowels == "aeiou":
    letter = str( input( "Enter a word ('quit' to quit): "))
    lowercase = letter.lower()
    if lowercase == "quit":
        break
    else:
        if lowercase[0] in vowels :
            print (lowercase + "way")
        else:
            for index , letters in enumerate (lowercase):
                if letters in vowels and lowercase[0] not in vowels :
                    print (lowercase[index:] + lowercase[0:index] + "ay")
                    break
                else :
                    continue
            else :
                print (lowercase + "ay")
        
                        
               
                   
   
    
