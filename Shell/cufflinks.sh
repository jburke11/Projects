#!/bin/bash
module load cufflinks

while getopts "b:g:h" opt; do   #fetches command line arguments and creates neccesary vars
  case $opt in
    b) bam_input=$OPTARG;;
    r) wget -O reference.gff $OPTARG;;
    h) echo "[-b for bam file][-g for gff file] [-h for help]"
        exit 1;;
  esac
done


cufflinks -I 5000 -g reference.gff $sra_input
echo "cufflinks done"
