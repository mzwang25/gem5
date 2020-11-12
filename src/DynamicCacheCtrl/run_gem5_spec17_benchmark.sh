#!/bin/bash

SPECROOTDIR=~/michael/spec2017
GEM5OPT=~/michael/gem5/build/X86/gem5.opt
SPEC17CFG=~/michael/gem5/src/DynamicCacheCtrl/test.py
SIMOPTIONS='--fast-forward=1000000 --at-instruction --maxinsts=500000000 --caches --l2cache'
 
######################################################################

BENCHMARK=$1
OUTDIR=$2
MAXINST=$3

#Check proper number of arguments
if [ ! $# -eq 3 ];
then
    echo "run_gem5_spec17_benchmarks.sh <BENCHMARK> <OUTDIR>"
    echo "! OUTDIR should be a absolute path like ~/michael/outdir"
    echo "  or the directory will end up in a weird location"
    exit 1
fi

# Set up enviorment
cd ${SPECROOTDIR}
source shrc

# Go to executable of that benchmark
go $BENCHMARK > /dev/null
ACTUALBENCHNAME=`basename "$PWD"`
echo "Found Benchmark: $ACTUALBENCHNAME" 
echo

# Attemt to enter into the run directory
{
    cd ./run/run*
} ||
{
    echo "Error: Benchmark $ACTUALBENCHNAME has not been built yet"
    exit
}

# Run gem5
${GEM5OPT} --outdir=${OUTDIR} --debug-flags=DynamicCacheCtrl ${SPEC17CFG} ${ACTUALBENCHNAME} ${MAXINST}

