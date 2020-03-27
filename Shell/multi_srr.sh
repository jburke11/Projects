#!/bin/bash

module load SRAToolkit
while getopts "d:s:h" opt; do
  case $opt in
    d) if [$OPTARG];
        then
	cd $OPTARG
      fi;;
    s)  sra_input=$OPTARG;;
    h) echo "[-d for full path to output directory (default is .)] [-s for list of sra accessions or sra id] [-h for help]"
       exit 1
  esac
done

declare -a id_array
i=0
while read line
do
  if [ $i != 4 ]
  then
    id_array=(${id_array[@]} $line)
    ((i+= 1))
    echo $i
  else
    qsub -v "sra_in=${id_array[*]}" /data/run/jburke/scripts/get_sra_multi.sh
    unset id_array
    ((i=0))
    echo $i
  fi
done < $sra_input

if [ $i == 0 ];
then
  echo $temp
  echo "all jobs created"
  exit 1
else
    qsub -v "sra_in=${id_array[*]}" /data/run/jburke/scripts/get_sra_multi.sh
    echo "all jobs submitted"
    exit 1
  fi
