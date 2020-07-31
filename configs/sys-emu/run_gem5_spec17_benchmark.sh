#!/bin/bash

SPECROOTDIR=~/michael/spec2017
GEM5OPT=~/michael/gem5/build/X86/gem5.opt
SPEC17CFG=~/michael/se-sim/spec17_config.py
SIMOPTIONS='--maxinsts=100000000 --caches --l2cache --l3cache'
OUTDIR=~/michael/se-sim/l3cache

######################################################################

BENCHMARK=$1

#Check proper number of arguments
if [ ! $# -eq 1 ];
then
    echo "run_gem5_spec17_benchmarks.sh <BENCHMARK>"
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
${GEM5OPT} --outdir=${OUTDIR} ${SPEC17CFG} --benchmark ${ACTUALBENCHNAME} ${SIMOPTIONS}

