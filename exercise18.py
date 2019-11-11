#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:47:45 2019

@author: burkej24
"""
fp = open("maize_protein_sequences.fasta" , "r")
Genbank_format_sequences = open("Genbank_format_sequences.txt", "w")

for line in fp:
    line1 = line.rstrip()
    if ">" in line1:
        list1 = line1.split()
        list2 = list1[0].split("|")
        if "NP" in list2[3] :
            print(list1, file = Genbank_format_sequences)
        else:
            pass
    else:
        pass
Genbank_format_sequences.close()