#!/bin/bash
#PBS -l nodes=1 :ppn=1
module load SAMTools
cd /data/run/jburke/potato_rna_seq_bams/hisat2_mapping/PE_files
samtools mpileup -o ${file}.pile ${file}
echo $file
