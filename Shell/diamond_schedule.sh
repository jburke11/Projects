#!/bin/bash
#PBS -l nodes=1:ppn=20
#PBS -m abe
#PBS -N diamond
#PBS -M burkej24@msu.edu
module load copper.soft
module load diamond
cd /data/run/jburke
diamond blastp -p 20 -d uniref100.db.dmnd --query DM_pep.fa.gz -o diamond_results_title.txt -f 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore salltitles qcovhsp scovhsp    
