#!/bin/bash
#PBS -l nodes=1:ppn=10
#PBS -N Joe_orthofinder
#PBS -m abe
#PBS -M burkej24@msu.edu

module load copper.soft OrthoFinder/2.4.0.Py3
orthofinder -f /data/run/jburke/orthofinder/peps/
