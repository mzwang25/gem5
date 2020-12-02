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

OUTDIR=$1
MAXINST=$2
 
######################################################################

 if [ ! $# -eq 2 ];
 then
    echo "./run_all <OUTDIR> <MAXINST>"
    exit 1
 fi

######################################################################

function run_one {
	BENCHMARK=$1
	OUTDIR=$2
	MAXINST=$3
    SIZE=$4

	if [ ! $# -eq 4];
	then
		echo "run_gem5_spec17_benchmarks.sh <BENCHMARK> <OUTDIR> <MAXINST>"
		echo "! OUTDIR should be a absolute path like ~/michael/outdir"
		echo "  or the directory will end up in a weird location"
		exit 1
	fi

	cd ${SPECROOTDIR}
	source shrc

	go $BENCHMARK > /dev/null
	ACTUALBENCHNAME=`basename "$PWD"`
	echo "Found Benchmark: $ACTUALBENCHNAME"
	echo

	{
		cd ./run/run*
	} ||
	{
		echo "Error: Benchmark $ACTUALBENCHNAME has not been built yet"
		exit
	}

	#any other options to run go below
	${GEM5OPT} --outdir=${OUTDIR}/${SIZE} --debug-flags=DynamicCacheCtrl ${SPEC17CFG} \
		 -b ${ACTUALBENCHNAME} \
         -i ${MAXINST} \
         -l ${SIZE}
}


######################################################################

#for L3SIZE in 64kB 3296kB #5744kB 8192kB 10640kB
for L3SIZE in 32kB 64kB 256kB
do
for B in ${BENCHMARKS[@]} 
do
    run_one $B ${OUTDIR}/${B} $MAXINST $L3SIZE&
done
done
