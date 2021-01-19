#!/bin/bash

SPECROOTDIR=~/michael/spec2017
GEM5OPT=~/michael/gem5/build/X86/gem5.opt
SPEC17CFG=~/michael/gem5/src/DynamicCacheCtrl/no_dc_config.py

######################################################################
BENCHMARKS=(\
    perlbench_s \
    parest_r \
    gcc_s
)

MAXINST=$1
 
######################################################################

 if [ ! $# -eq 1 ];
 then
    echo "./run_all <MAXINST>"
    exit 1
 fi

######################################################################

for B in ${BENCHMARKS[@]} 
do
    ./run_one.sh $B $MAXINST&
done
