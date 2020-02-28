#!/bin/bash
cufflinks -I 5000 -g reference.gff sra's

touch assembly_list.txt

cuffmerge -p 2 assembly_list
