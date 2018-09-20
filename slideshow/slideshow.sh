#!/bin/bash

# kill fbi to stop display
killall fbi

# choose which directory to display
IMGDIR="/your/photos/path"

# check if a specific directory is choosen
if [ $# -eq 1 ] && [ ! -z "$1" ] && [ -d "$IMGDIR/$1" ];
then
	RDMDIR="$IMGDIR/$1"
	
# else: choose random one
else

NBDIR=$(ls -1d $IMGDIR/* | wc -l)
RDM=$((RANDOM%${NBDIR}))
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

fi;

echo "Display directory: $RDMDIR"

# start display
nohup fbi -T 2 -noverbose --autodown -t 6 $RDMDIR/* > /dev/null

# specify command
#nohup fbi -T 2 -m 1280x1024-60 -noverbose --autodown -u -t 6 /home/gzav/img/* > /dev/null


