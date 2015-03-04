#!/bin/bash

# pour stopper le diaporama
killall fbi

# choose which diectory to display
IMGDIR="/home/gzav/img"
RDMDIR="/home/gzav/img"
NBDIR=$(ls -1d $IMGDIR/* | wc -l)
#echo "NB DIR = $NBDIR"
#NBDIR=$((NBDIR+1))
#echo "NB DIR = $NBDIR"
RDM=$((RANDOM%${NBDIR}))
#echo "RDM = $RDM - $((RANDOM))"
j=0; 
for i in `ls -1d $IMGDIR/*`; 
do 
  if [ $j -eq $RDM ]; 
  then 
    echo "Display image directory $j/$NBDIR : $i";
    RDMDIR=$i
    break;
  fi; 
  j=$((j+1)); 
done;


# démarrage du diaporama
nohup fbi -T 2 -noverbose --autodown -t 6 $RDMDIR/* > /dev/null
#nohup fbi -T 2 -m 1280x1024-60 -noverbose --autodown -u -t 6 /home/gzav/img/* > /dev/null

