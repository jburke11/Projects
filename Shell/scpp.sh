while getopts ":mlh" opt; do   #fetches command line arguments and creates neccesary vars
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
    h) echo "[-m for mudhen to local] [-l for  local to mudhen] [-h for help]"
        exit 1;;
  esac
done
