#!/bin/bash

module load SRAToolkit
module load cutadapt
module load FastQC
module load copper.soft
module load HISAT2
module load SAMTools

while getopts ":i:r:c" opt; do
  case $opt in
    i) sra = $OPTARG ;;
    r) wget -O reference$sra.fa $OPTARG;;
    c) clean = true ;;
    \?) echo "[-i for sra id] [-r for reference genome url] [-c for optional cleanup]";;
  esac
done

prefetch $sra
fastq-dump --split-files --split-spot -F $sra
fastqc $sra*
cutadapt -g AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCACNNNNNNATCTCGTATGCCGTCTTCTGCTTG -G CAAGCAGAAGACGGCATACGAGATNNNNNNGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT \
-A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT -f fastq -n 2 -m 100 -q 10 -j 4 -o $sra.R1.fastq -p $sra.R2.fastq $sra*.fastq  > cutadaptlog.txt
fastqc $sra.*
hisat2-build -f $sra.fa $sra.reference
hisat2 -x $sra -1 $sra.R1.fastq -2 $sra.R2.fastq  -q | samtools view -b | samtools sort -O bam -o $sra.sorted.bam
samtools index $sra.sorted.bam
samtools idxstats $sra.sorted.bam > idxstats.txt
samtools flagstat $sra.sorted.bam > flagstats.txt

if [ clean = true ]
then
    rm -i reference*
    rm -i *.fastq
  fi

module unload SRAToolkit
module unload cutadapt
module unload FastQC
module unload copper.soft
module unload HISAT2
module unload SAMTools
exit 0 