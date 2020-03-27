#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -m abe
#PBS -N sra_prefetch/dump
#PBS -M burkej24@msu.edu
module load FastQC
module load cutadapt

while getopts "d:s:h" opt; do
  case $opt in
    d)  cd $OPTARG ;;
    s)  sra_input=$OPTARG
        if [ -a $sra_input ];
          then
            multi=true
        else
          sra=$sra_input
          multi=false
        fi;;
    h) echo "[-d for directory of sra id's (default is .)] [-s for list of sra accessions or sra id] [-h for help]"
       exit 0
  esac
done
mkdir summaries_precut
mkdir summaries_postcut
while read line
  do
    sra=$line
    cd $sra
    fastqc ${sra}_1.fastq ${sra}_2.fastq
    unzip ${sra}_1_fastqc.zip
    unzip ${sra}_2_fastqc.zip
    rm *.zip
    cd ${sra}_1_fastqc
    mv summary.txt ../../summaries_precut/$sra.summary.1
    cd ..
    cd ${sra}_2_fastqc
    mv summary.txt ../../summaries_precut/$sra.summary.2
    cd ..
    cutadapt -g AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCACNNNNNNATCTCGTATGCCGTCTTCTGCTTG -G CAAGCAGAAGACGGCATACGAGATNNNNNNGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT \
    -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT -f fastq -n 2 -m 100 -q 10 -j 4 -o $sra.R1.fastq -p $sra.R2.fastq $sra*.fastq  > $sra.cutadaptlog.txt
    fastqc $sra.R1.fastq $sra.R2.fastq
    unzip ${sra}.R1_fastqc.zip
    unzip ${sra}.R2_fastqc.zip
    rm *.zip
    cd ${sra}.R1_fastqc
    mv summary.txt ../../summaries_postcut/$sra.summary.1
    cd ..
    cd ${sra}.R2_fastqc
    mv summary.txt ../../summaries_postcut/$sra.summary.2
    cd ..
  if [ -e ${sra}_1_fastqc.html ] && [ -e ${sra}_2_fastqc.html ] && [ -e ${sra}.R1_fastqc.html ] && [ -e ${sra}.R2_fastqc.html ];
    then
      cd ..
      continue
  else
    echo "error processing $sra"
    exit 1
    fi
  done < $sra_input
  if [ -d summaries_precut ] && [ -d summaries_postcut ];
  then
  echo "all fastq analyzed"
  exit 0
else
  echo "summary directories not created"
  exit 1
fi
exit 0
