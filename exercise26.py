#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 09:53:12 2019

@author: burkej24
"""

import random
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
new_seqlist = []
for record in SeqIO.parse("maize_protein_sequences.fasta", "fasta"):
    record.seq = record.seq[0:50]
    new = SeqRecord(record.seq, id= "new id" + " " + str(random.randint(0,1000)), description = record.id + "first 50" )
    new_seqlist.append(new)
SeqIO.write(new_seqlist, "first50", "fasta")