#!/bin/bash
#PBS -l nodes=1:ppn=2
#PBS -m abe
#PBS -N sra_prefetch/dump
#PBS -M burkej24@msu.edu

module load SRAToolkit
while getopts "d:s:h" opt; do
  case $opt in
    d) if [$OPTARG];
        then
        cd $OPTARG
      fi;;
    s)  sra_in=$OPTARG;;
    h) echo "[-d for full path to output directory (default is .)] [-s for list of sra accessions or sra id] [-h for help]"
       exit 1
  esac
done

  for line in "${sra_in[@]}";
  do
    echo $line
    sra=$line
    mkdir $sra
    cd $sra
    prefetch $sra
    fastq-dump --split-files --split-spot -F $sra
  if [ -e ${sra}_1.fastq ] && [ -e ${sra}_2.fastq ];
    then
      cd ..
      continue
  else
    echo "sra file $sra not created"
    exit 0
    fi
  done
  echo "all fastq files created"
  exit
