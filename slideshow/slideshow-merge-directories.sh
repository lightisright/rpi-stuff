#!/bin/bash

# ==================================================
# Photo directories merging script 
# ==================================================
# Status : sid / testing
# Date / Author : 2015-01-04 / XCO
# ==================================================

ROOT=/home/gzav/img
DIRS=$1
DEST=$2

# create destiation directory
echo "Create destiation directory $ROOT/$DEST"
#mkdir "$ROOT/$DEST"

# list each source directory
for $DIR in $DIRS; do

  # move each source directory file into destination directory
  # prepend filename with source directory name + "_"
  for $FILE in ls -1 $DIR; do
    echo "Move $ROOT/$DIR/$FILE source file into $ROOT/$DEST/${DIR}_${FILE}"
    #mv "$ROOT/$DIR/$FILE" "$ROOT/$DEST/${DIR}_${FILE}"
  done

  # delete empty source directory
  echo "Remove source directory $DIR"
  #rmdir "$DIR"
done


