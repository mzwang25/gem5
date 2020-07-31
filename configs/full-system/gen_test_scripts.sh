#!/bin/bash

SPEC2017=~/michael/spec2017/
SPEC2017BENCH=~/michael/full-system/SPEC2017BENCH

#######################################################################

#Above: SPEC2017 is the location of the spec2017 root. SPEC2017BENCH is
#  a folder that should be copied into the root of the disk image. This 
#  script will generate that folder at SPEC2017BENCH

#######################################################################

SPEC2017BIN=$SPEC2017BENCH/bin
SCRIPTDIR=$SPEC2017BENCH/scripts

#create directories
mkdir -p $SPEC2017BENCH
cd $SPEC2017BENCH
mkdir -p $SPEC2017BIN
mkdir -p $SCRIPTDIR


#######################################################################

cd $SPEC2017
source shrc

#######################################################################
cd $SPEC2017/benchspec/CPU

for dir in `ls -d */`
do
    dir=${dir%/}

    echo "creating scripts for $dir ..."

    go $dir run > /dev/null
    cd run*


    cp * $SPEC2017BIN

    #create a script to run that executable
    specinvoke -n | grep "\.\./run_*" | sed 's,^[^/]*/,,' | sed 's,^[^/]*/,,' | while read line; do echo "./$line"; done > $SCRIPTDIR/$dir.sh

done

