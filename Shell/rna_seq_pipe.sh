#!/bin/bash


function load_modules {   #load all required modules
module load SRAToolkit
module load cutadapt
module load FastQC
module load copper.soft
module load HISAT2
module load SAMTools
}

function pipeline {  # main pipe for data analysis
prefetch $sra
fastq-dump --split-files --split-spot -F $sra
fastqc $sra*
cutadapt -g AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCACNNNNNNATCTCGTATGCCGTCTTCTGCTTG -G CAAGCAGAAGACGGCATACGAGATNNNNNNGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT \
-A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT -f fastq -n 2 -m 100 -q 10 -j 4 -o $sra.R1.fastq -p $sra.R2.fastq $sra*.fastq  > $sra.cutadaptlog.txt
fastqc $sra.R*
hisat2-build -f reference$sra.fa $sra.reference
hisat2 -x $sra.reference -1 $sra.R1.fastq -2 $sra.R2.fastq  -q | samtools view -b -@ 2| samtools sort -@ 2 -O bam -o $sra.sorted.bam
samtools index $sra.sorted.bam
samtools idxstats $sra.sorted.bam > $sra.idxstats.txt
samtools flagstat $sra.sorted.bam > $sra.flagstats.txt
}

function unload_modules {   # unloads all modules used
module unload SRAToolkit
module unload cutadapt
module unload FastQC
module unload copper.soft
module unload HISAT2
module unload SAMTools
}

load_modules
clean=false
while getopts ":i:r:ch" opt; do   #fetches command line arguments and creates neccesary vars
  case $opt in
    i) sra_input=$OPTARG
        if [ -a $sra_input ];
        then
        multi=true
      else
        sra=$sra_input
        multi=false
      fi;;
    r) wget -O reference.fa $OPTARG;;
    c) clean=true ;;
    h) echo "[-i for sra id/sra id file] [-r for reference genome url] [-c for optional cleanup]"
        exit 1;;
  esac
done

if [ $multi = true ];     # processes multiple sra's by reading in file
then
  while read line
  do
    sra=$line
    mkdir $sra
    cd $sra
    cp ../reference.fa reference$sra.fa
    pipeline
    cd ..
  done < $sra_input

else          # does pipe with only 1 sra
  sra=$sra_input
  mkdir $sra
  cd $sra
  cp ../reference.fa reference$sra.fa
  pipeline
fi

if [ $clean = true ];   #cleans up files
then
    rm -i reference*
    rm -i *.fastq
  fi

unload_modules  #unload files
exit 0    # done
