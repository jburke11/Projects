#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:31:02 2019

@author: burkej24
"""

fp = open("maize_protein_sequences.fasta" , "r")
import re
for line in fp:
    line1 = line.rstrip()
    header = re.match(("^>.*glycosyl+"), line1)
    if (header):
        print (line1)
    else:
        pass