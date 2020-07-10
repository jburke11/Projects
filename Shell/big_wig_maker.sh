#!/bin/bash
#PBS -l nodes=1 :ppn=1
cd /data/run/jburke/potato_rna_seq_bams/hisat2_mapping/SE_files
./wigToBigWig $file chrom.sizes ${file}.bw
