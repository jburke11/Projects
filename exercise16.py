#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:19:09 2019

@author: burkej24
"""

fp = open("maize_protein_sequences.fasta" , "r")
import re

for line in fp:
    line1 = line.rstrip()
    header = re.match("^>.*glycosyl+", line1)
    group = re.match("groups", line1)
    if header and not group:
        print(line1)
