#!/bin/bash

#PBS -l nodes=1 :ppn=10
#PBS joejob
#PBS -o wiggler.txt
cd /data/run/jburke/potato_rna_seq_bams/hisat2_mapping/SE_files

files=(/data/run/jburke/potato_rna_seq_bams/hisat2_mapping/SE_files/*.pile.wig)
for file in "${files[@]}"; 
do
        echo $file
        qsub -v file=${file} big_wig_maker.sh 
done
