#!/bin/sh

GEM5=/home/nanoproj/michael/gem5/build/X86/gem5.opt
KERNEL=../binaries/vmlinux-4.19.83
DISK=../disks/linux-spec17.img
CONFIG=/home/nanoproj/michael/gem5/configs/example/fs.py
CKPT=/home/nanoproj/michael/full-system/m5out

$GEM5 $CONFIG --kernel=$KERNEL --disk=$DISK --at-instruction
