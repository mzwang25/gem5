#!/bin/bash

SPECROOTDIR=~/michael/spec2017
GEM5OPT=~/michael/gem5/build/X86/gem5.opt
SPEC17CFG=~/michael/gem5/src/DynamicCacheCtrl/no_dc_config.py

######################################################################
BENCHMARKS=(\
    perlbench_r \
    gcc_r \
    bwaves_r \
    mcf_r \
    cactuBSSN_r \
    namd_r \
    parest_r \
    povray_r \
    lbm_r \
    omnetpp_r \
    xz_r \
    perlbench_s \
    gcc_s \
    bwaves_s \
    mcr_s \
    cactuBSSN_s \
    lbm_s \
    omnetpp_s \
    wrf_s \
    xalancbmk_s \
    x264_s \
    cam4_s \
    pop2_s \
    deepsjeng_s \
    imagick_s \
    leela_s \
    nab_s \
    exchange2_s \
    fotonik3d_s \
    roms_s \
    xz_s
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
