#!/bin/bash
module load SRAToolkit
module load cutadapt
module load FastQC
module load copper.soft
module load HISAT2
module load SAMTools

echo "input SRA id: "
read sra

prefetch $sra
echo "sra files downloaded"

fastq-dump --split-files --split-spot -F $sra
echo "fastqdump done"

fastqc $sra*
echo "quality control 1 done"

cutadapt -g AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCACNNNNNNATCTCGTATGCCGTCTTCTGCTTG -G CAAGCAGAAGACGGCATACGAGATNNNNNNGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT -f fastq -n 2 -m 100 -q 10 -j 4 -o output.R1.fastq -p output.R2.fastq $sra*.fastq  > cutadaptlog.txt
echo "cutadapt done"

fastqc output*
echo "quality control 2 done"

echo "moving to HISAT"

echo "enter reference genome url"
read url
wget -O reference.fa $url

echo "entering HISAT"
hisat2-build -f reference.fa reference
echo "reference built"

hisat2 -x reference -1 output.R1.fastq -2 output.R2.fastq  -q | samtools view -b | samtools sort -O bam -o sorted.bam # sam file never created ;)
samtools index sorted.bam
samtools idxstats sorted.bam > idxstats.txt
samtools flagstat sorted.bam > flagstats.txt
echo "Done"

echo "Do you want to clean up files? (y/n)"
read option

if [ $option = "y" ]; then
    rm -i reference*
    rm -i *.fastq
    echo "Done"
else
  echo "Done"
fi
module unload SRAToolkit
module unload cutadapt
module unload FastQC
module unload copper.soft
module unload HISAT2
module unload SAMTools
exit 0
