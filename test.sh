#!/bin/bash
'
module load SRAToolkit
module load cutadapt
module load FastQC
module load copper.soft
module load HISAT2
module load SAMTools
'
while getopts ":i:r:c" opt; do
  case $opt in
    i) ssr=$OPTARG
       echo $ssr ;;
    r) wget -O reference$ssr.fa $OPTARG;;
    c) clean= 1 ;;
    \?) echo "[-i for ssr id] [-r for reference genome url] [-c for optional cleanup]";;
  esac
done
echo "done"

hisat2-build -f reference$ssr.fa reference$ssr


fastq-dump --split-files --split-spot -F -Z $sra | cutadapt -g AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCACNNNNNNATCTCGTATGCCGTCTTCTGCTTG -G CAAGCAGAAGACGGCATACGAGATNNNNNNGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT \
-f fastq -n 2 -m 100 -q 10 -j 4 -o output.R1.fastq -p output.R2.fastq - 2> cutadaptlog.txt | hisat2 -x reference -1 output.R1.fastq -2 output.R2.fastq  -q | samtools view -b | samtools sort -O bam -o sorted.bam
