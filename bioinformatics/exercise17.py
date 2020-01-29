#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:35:41 2019

@author: burkej24
"""

fp = open("maize_protein_sequences.fasta" , "r")

for line in fp:
    line1 = line.rstrip()
    if ">" in line1:
        print(line1)
        header = True
    elif header == True:
        print(line1)
        header = False
    else:
        pass