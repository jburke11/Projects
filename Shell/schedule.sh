#!/bin/bash
#PBS -l nodes=1:ppn=2
#PBS -m abe
#PBS -N sra_prefetch/dump
#PBS -M burkej24@msu.edu

qsub -v "sra_input=srr.txt" /data/run/jburke/scripts/multi_srr.sh 
