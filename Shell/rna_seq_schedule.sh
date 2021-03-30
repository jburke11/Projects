#PBS -l nodes=1:ppn=2
#PBS -m abe
#PBS -M burkej24@msu.edu
cd /data/run/jburke

./rna_seq_pipe.sh -r http://rice.plantbiology.msu.edu/pub/data/Eukaryotic_Projects/o_sativa/annotation_dbs/pseudomolecules/version_7.0/all.dir/all.chrs.con -i SRR11282890

