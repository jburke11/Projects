#!/bin/bash

#PBS -l nodes=1 :ppn=10
#PBS joejob
#PBS -o piles.txt
cd /data/run/jburke/potato_rna_seq_bams/hisat2_mapping/PE_files

files=(/data/run/jburke/potato_rna_seq_bams/hisat2_mapping/PE_files/*.bam)
for file in "${files[@]}"; 
do
	echo $file
	qsub -v file=${file} pile.sh 
done

