#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:15:12 2019

@author: burkej24
"""

from Bio import SeqIO, SeqRecord, Seq
for seq_record in SeqIO.parse("maize_protein_sequences.fasta", "fasta"):
    print(seq_record.id)
    print(len(seq_record.seq))
    print(seq_record.description)
    print(seq_record.seq)
    print()
