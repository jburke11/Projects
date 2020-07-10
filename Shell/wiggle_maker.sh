#!/bin/bash
#PBS -l nodes=1 :ppn=1
module load python3
cd /data/run/jburke/potato_rna_seq_bams/hisat2_mapping/PE_files
python3 clean.py $file
echo $file
