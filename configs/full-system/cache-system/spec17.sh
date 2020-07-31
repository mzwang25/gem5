#!/bin/sh

GEM5=/home/nanoproj/michael/gem5/build/X86/gem5.opt
KERNEL=../binaries/vmlinux-4.19.83
DISK=../disks/linux-spec17.img
CONFIG=/home/nanoproj/michael/gem5/configs/example/fs.py
CKPT=/home/nanoproj/michael/full-system/m5out

$GEM5 $CONFIG --kernel=$KERNEL --disk=$DISK \
 \
 --num-cpus=2\
 --sys-clock="2GHz"\
 --cpu-clock="2GHz"\
 --sys-voltage="1V"\
 \
 --caches\
 --cacheline_size="64"\
 \
 --l1d_size="64kB"\
 --l1i_size="32kB"\
 --l1d_assoc=8\
 --l1i_assoc=8\
 \
 --l2cache\
 --num-l2caches=1\
 --l2_size="512kB"\
 --l2_assoc=8\
 \
 --num-l3caches=1\
 --l3_size="2MB"\
 --l3_assoc=16 \
 \
 --mem-type="DDR3_2133_8x8" \
 --mem-channels=1 \
 --mem-size="8192MB" \
 --checkpoint-restore=1 \
 --maxinsts=100000000
 
