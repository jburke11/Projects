#!/bin/bash
module load SRAToolkit
module load cutadapt
module load FastQC
module load copper.soft
module load HISAT2
module load SAMTools




hisat2-build -f reference.fa reference
echo "reference built"

fastq-dump --split-files --split-spot -F -Z $sra | cutadapt -g AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCACNNNNNNATCTCGTATGCCGTCTTCTGCTTG -G CAAGCAGAAGACGGCATACGAGATNNNNNNGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT -f fastq -n 2 -m 100 -q 10 -j 4 -o output.R1.fastq -p output.R2.fastq - 2> cutadaptlog.txt | hisat2 -x reference -1 output.R1.fastq -2 output.R2.fastq  -q | samtools view -b | samtools sort -O bam -o sorted.bam

fastqc $sra*
echo "quality control 1 done"

fastqc output*
echo "quality control 2 done"

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
