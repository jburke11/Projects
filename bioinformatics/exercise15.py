#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:33:21 2019

@author: burkej24
"""
fp = open("maize_protein_sequences.fasta" , "r")
import re
for line in fp:
    line1 = line.rstrip()
    header = re.match("^>.*glycosyl+", line1)
    if header:
        group = re.match("groups", line1)
        if not group :
            print (line1)
        else:
            pass
    else:
        pass
