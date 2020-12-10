#!/bin/bash

SPECROOTDIR=~/michael/spec2017
GEM5OPT=~/michael/gem5/build/X86/gem5.opt
SPEC17CFG=~/michael/gem5/configs/sys-emu/config-files/spec17_config.py
SIMOPTIONS='--fast-forward=10000000 
            --maxinsts=300000000 
            --cpu-type=TimingSimpleCPU 
            --caches 
            --l2cache 
            --l2_size=1024 
            --l3cache'
 
######################################################################

BENCHMARK="lbm_r"
OUTDIR=~/michael/gem5/configs/sys-emu/l3cache


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

