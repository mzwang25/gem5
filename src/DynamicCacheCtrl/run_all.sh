#!/bin/bash

######################################################################
BENCHMARKS=(\
    perlbench_r \
    gcc_r \
    mcf_r \
    cactuBSSN_r \
    namd_r \
    parest_r \
    povray_r \
    lbm_r \
    omnetpp_r \
    wrf_r \
)

OUTDIR=$1
MAXINST=$2
 
######################################################################

 if [ ! $# -eq 2 ];
 then
    echo "./run_all <OUTDIR> <MAXINST>"
    exit 1
 fi



######################################################################

for B in ${BENCHMARKS[@]} 
do
    ./run_gem5_spec17_benchmark.sh $B ${OUTDIR}/${B} $MAXINST &
done
