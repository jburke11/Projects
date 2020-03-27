#!/bin/bash
module load MultiQC

while getopts "d:s:h" opt; do
  case $opt in
    s) sra_file=$OPTARG;;
    d) if [$OPTARG];
        then
        cd $OPTARG
      fi;;
    h) echo "[-d for full parent directory name (default is .)] [-s for list of sra directories][-h for help]"
       exit 0
  esac
done
mkdir qc_stats
touch qc_stats/summaries_postcut_fail.txt
touch qc_stats/summaries_precut_fail.txt
multiqc -l $sra_file -o qc_stats

cd summaries_precut

for file in *summary*; do
  echo "Number of fails in $file :" >> ../qc_stats/summaries_precut_fail.txt
  grep -c 'FAIL' $file >> ../qc_stats/summaries_precut_fail.txt
done
cd ../summaries_postcut

for file in *summary*; do
  echo "Number of fails in $file :" >> ../qc_stats/summaries_postcut_fail.txt
  grep -c 'FAIL' $file >> ../qc_stats/summaries_postcut_fail.txt
done
