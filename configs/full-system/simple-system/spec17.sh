#!/bin/sh

GEM5=/home/nanoproj/michael/gem5/build/X86/gem5.opt
KERNEL=../binaries/vmlinux-4.19.83
DISK=../disks/linux-spec17.img
CONFIG=/home/nanoproj/michael/gem5/configs/example/fs.py
CKPT=/home/nanoproj/michael/full-system-sim/simple-system/m5out
OUTDIR=./lbm519

$GEM5 -d $OUTDIR $CONFIG \
--kernel=$KERNEL \
--disk=$DISK \
--checkpoint-dir=$CKPT \
--checkpoint-restore=1 \
--maxinsts=100000000
