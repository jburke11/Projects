while getopts ":mlqh" opt; do   #fetches command line arguments and creates neccesary vars
  case $opt in
    m) echo "input path on mudhen"
    read mudhen
    echo "input local path"
    read loc
    scp -P 45679 jburke@mudhen.plantbiology.msu.edu:$mudhen $loc ;;
    l) echo "input path on mudhen"
    read mudhen
    echo "input local path"
    read loc
    scp -P 45679 $loc jburke@mudhen.plantbiology.msu.edu:$mudhen;;
    q) scp -P 45679 /Users/burkej24/Desktop/potato_genome/*multi* jburke@mudhen.plantbiology.msu.edu:/data/run/jburke/scripts;;
    w) echo "input file name"
    read file
    scp -P 45679 $PWD:$file jburke@mudhen.plantbiology.msu.edu:/data/run/jburke/scripts;;
    h) echo "[-m for mudhen to local] [-l for  local to mudhen] [-h for help]"
        exit 1;;
  esac
done
