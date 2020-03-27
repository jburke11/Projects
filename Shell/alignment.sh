#!/bin/bash
module load copper.soft
module load HISAT2
module load SAMTools
while getopts "s:r:d:h" opt; do   #fetches command line arguments and creates neccesary vars
  case $opt in
    s) sra_input=$OPTARG;;
    r) wget -O reference.fa $OPTARG
       hisat2-build -f reference.fa reference;;
    d) cd $OPTARG;;
    h) echo "[-i for list of sra directories] [-r for reference genome url] [-d for full path to directory of sra directories (default is .)][-h for help]"
        exit 0;;
  esac
done

while read line
  do
  sra=$line
  cp reference* $sra
  cd $sra
  echo "analysis of $sra started"
  hisat2 -x reference -1 $sra.R1.fastq -2 $sra.R2.fastq  -q --dta-cufflinks | samtools view -b -@ 2  | samtools sort -@ 2 -O bam -o $sra.sorted.bam
  samtools index $sra.sorted.bam
  echo "indexing of $sra complete"
  samtools idxstats $sra.sorted.bam > $sra.idxstats.txt
  echo "idxstats of $sra complete"
  samtools flagstat $sra.sorted.bam > $sra.flagstats.txt
  echo "flagstats of $sra complete"
  echo "analysis of $sra is completed"
  cd ..
done < $sra_input

echo "alignment completed"
exit 0
