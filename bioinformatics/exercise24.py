#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:55:39 2019

@author: burkej24
"""
from Bio import SeqIO, SeqRecord, Seq
seq_dict = {}
seq_dict = SeqIO.to_dict(SeqIO.parse("maize_protein_sequences.fasta", "fasta"))

for ids, records in seq_dict.items():
    print(ids)
    print()
    print(len(records.seq))
    print()