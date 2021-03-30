#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -m abe
#PBS -N htseq
#PBS -M burkej24@msu.edu
module load HTSeq
while getopts "s:d:h" opt; do   #fetches command line arguments and creates neccesary vars
  case $opt in
    s) sra_input=$OPTARG;;
    d) cd $OPTARG;;
    h) echo "[-i for list of sra directories] [-d for full path to directory of sra directories (default is .)][-h for help]"
        exit 0;;
  esac
done

declare -a id_array
while read sra
do
  id_array+=(${sra}/${sra}.sorted.bam)
done < $sra_input

htseq-count -f bam -r pos -s yes -m union -i "ID" ${id_array[$PBS_ARRAYID]} reference.gff
