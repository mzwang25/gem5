# Copyright (c) 2012-2013 ARM Limited
# All rights reserved.
#
# The license below extends only to copyright in the software and shall
# not be construed as granting a license to any other intellectual
# property including but not limited to intellectual property relating
# to a hardware implementation of the functionality of the software
# licensed hereunder.  You may use the software subject to the license
# terms below provided that you ensure that this notice is replicated
# unmodified and in its entirety in all distributions of the software,
# modified or unmodified, in source code or in binary form.
#
# Copyright (c) 2006-2008 The Regents of The University of Michigan
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Simple test script
#
# "m5 test.py"

from __future__ import print_function
from __future__ import absolute_import

import optparse
import sys
import os

import m5
from m5.defines import buildEnv
from m5.objects import *
from m5.params import NULL
from m5.util import addToPath, fatal, warn

import spec17_benchmarks

addToPath("/home/nanoproj/michael/gem5/configs")

from ruby import Ruby

from common import Options
from common import Simulation
from common import CacheConfig
from common import CpuConfig
from common import ObjectList
from common import MemConfig
from common.FileSystemConfig import config_filesystem
from common.Caches import *
from common.cpu2000 import *

def get_processes(options):
    """Interprets provided options and returns a list of processes"""

    multiprocesses = []
    inputs = []
    outputs = []
    errouts = []
    pargs = []

    workloads = options.cmd.split(';')
    if options.input != "":
        inputs = options.input.split(';')
    if options.output != "":
        outputs = options.output.split(';')
    if options.errout != "":
        errouts = options.errout.split(';')
    if options.options != "":
        pargs = options.options.split(';')

    idx = 0
    for wrkld in workloads:
        process = Process(pid = 100 + idx)
        process.executable = wrkld
        process.cwd = os.getcwd()

        if options.env:
            with open(options.env, 'r') as f:
                process.env = [line.rstrip() for line in f]

        if len(pargs) > idx:
            process.cmd = [wrkld] + pargs[idx].split()
        else:
            process.cmd = [wrkld]

        if len(inputs) > idx:
            process.input = inputs[idx]
        if len(outputs) > idx:
            process.output = outputs[idx]
        if len(errouts) > idx:
            process.errout = errouts[idx]

        multiprocesses.append(process)
        idx += 1

    if options.smt:
        assert(options.cpu_type == "DerivO3CPU")
        return multiprocesses, idx
    else:
        return multiprocesses, 1


parser = optparse.OptionParser()
Options.addCommonOptions(parser)
Options.addSEOptions(parser)

# Benchmark options here
parser.add_option("-b", "--benchmark", type="string", default="", help="The SPEC benchmark to be loaded.")
parser.add_option("--benchmark_stdout", type="string", default="", help="Absolute path for benchmark's stdout")
parser.add_option("--benchmark_stderr", type="string", default="", help="Absolute path for benchmark's stderr")


if '--ruby' in sys.argv:
    Ruby.define_options(parser)

(options, args) = parser.parse_args()

if args:
    print("Error: script doesn't take any positional arguments")
    sys.exit(1)

multiprocesses = []
numThreads = 1

# Parsing Benchmark to use
if options.benchmark:
    print("Selected SPEC_CPU2017 Benchmark")
    if(options.benchmark == '500.perlbench_r'):
        print("--> 500.perlbench_r")
        process = spec17_benchmarks.perlbench_r
    elif(options.benchmark == '502.gcc_r'):
        print("--> 502.gcc_r")
        process = spec17_benchmarks.gcc_r
    elif(options.benchmark == '503.bwaves_r'):
        print("--> 503.bwaves_r")
        process = spec17_benchmarks.bwaves_r
    elif(options.benchmark == '505.mcf_r'):
        print("--> 505.mcf_r")
        process = spec17_benchmarks.mcf_r
    elif(options.benchmark == '507.cactuBSSN_r'):
        print("--> 507.cactuBSSN_r")
        process = spec17_benchmarks.cactuBSSN_r
    elif(options.benchmark == '508.namd_r'):
        print("--> 508.namd_r")
        process = spec17_benchmarks.namd_r
    elif(options.benchmark == '510.parest_r'):
        print("--> 510.parest_r")
        process = spec17_benchmarks.parest_r
    elif(options.benchmark == '511.povray_r'):
        print("--> 511.povray_r")
        process = spec17_benchmarks.povray_r
    elif(options.benchmark == '519.lbm_r'):
        print("--> 519.lbm_r")
        process = spec17_benchmarks.lbm_r
    elif(options.benchmark == '520.omnetpp_r'):
        print("--> 520.omnetpp_r")
        process = spec17_benchmarks.omnetpp_r
    elif(options.benchmark == '521.wrf_r'):
        print("--> 521.wrf_r")
        process = spec17_benchmarks.wrf_r
    elif(options.benchmark == '523.xalancbmk_r'):
        print("--> 523.xalancbmk_r")
        process = spec17_benchmarks.xalancbmk_r
    elif(options.benchmark == '525.x264_r'):
        print("--> 525.x264_r")
        process = spec17_benchmarks.x264_r
    elif(options.benchmark == '526.blender_r'):
        print("--> 526.blender_r")
        process = spec17_benchmarks.blender_r
    elif(options.benchmark == '527.cam4_r'):
        print("--> 527.cam4_r")
        process = spec17_benchmarks.cam4_r
    elif(options.benchmark == '531.deepsjeng_r'):
        print("--> 531.deepsjeng_r")
        process = spec17_benchmarks.deepsjeng_r
    elif(options.benchmark == '538.imagick_r'):
        print("--> 538.imagick_r")
        process = spec17_benchmarks.imagick_r
    elif(options.benchmark == '541.leela_r'):
        print("--> 541.leela_r")
        process = spec17_benchmarks.leela_r
    elif(options.benchmark == '544.nab_r'):
        print("--> 544.nab_r")
        process = spec17_benchmarks.nab_r
    elif(options.benchmark == '548.exchange2_r'):
        print("--> 548.exchange2_r")
        process = spec17_benchmarks.exchange2_r
    elif(options.benchmark == '554.roms_r'):
        print("--> 554.roms_r")
        process = spec17_benchmarks.roms_r
    elif(options.benchmark == '557.xz_r'):
        print("--> 557.xz_r")
        process = spec17_benchmarks.xz_r
    elif(options.benchmark == '600.perlbench_s'):
        print("--> 600.perlbench_s")
        process = spec17_benchmarks.perlbench_s
    elif(options.benchmark == '602.gcc_s'):
        print("--> 602.gcc_s")
        process = spec17_benchmarks.gcc_s
    elif(options.benchmark == '603.bwaves_s'):
        print("--> 603.bwaves_s")
        process = spec17_benchmarks.bwaves_s
    elif(options.benchmark == '605.mcf_s'):
        print("--> 605.mcf_s")
        process = spec17_benchmarks.mcf_s
    elif(options.benchmark == '607.cactuBSSN_s'):
        print("--> 607.cactuBSSN_s")
        process = spec17_benchmarks.cactuBSSN_s
    elif(options.benchmark == '619.lbm_s'):
        print("--> 619.lbm_s")
        process = spec17_benchmarks.lbm_s
    elif(options.benchmark == '620.omnetpp_s'):
        print("--> 620.omnetpp_s")
        process = spec17_benchmarks.omnetpp_s
    elif(options.benchmark == '621.wrf_s'):
        print("--> 621.wrf_s")
        process = spec17_benchmarks.wrf_s
    elif(options.benchmark == '623.xalancbmk_s'):
        print("--> 623.xalancbmk_s")
        process = spec17_benchmarks.xalancbmk_s
    elif(options.benchmark == '625.x264_s'):
        print("--> 625.x264_s")
        process = spec17_benchmarks.x264_s
    elif(options.benchmark == '627.cam4_s'):
        print("--> 627.cam4_s")
        process = spec17_benchmarks.cam4_s
    elif(options.benchmark == '628.pop2_s'):
        print("--> 628.pop2_s")
        process = spec17_benchmarks.pop2_s
    elif(options.benchmark == '631.deepsjeng_s'):
        print("--> 631.deepsjeng_s")
        process = spec17_benchmarks.deepsjeng_s
    elif(options.benchmark == '638.imagick_s'):
        print("--> 638.imagick_s")
        process = spec17_benchmarks.imagick_s
    elif(options.benchmark == '641.leela_s'):
        print("--> 641.leela_s")
        process = spec17_benchmarks.leela_s
    elif(options.benchmark == '644.nab_s'):
        print("--> 644.nab_s")
        process = spec17_benchmarks.nab_s
    elif(options.benchmark == '648.exchange2_s'):
        print("--> 648.exchange2_s")
        process = spec17_benchmarks.exchange2_s
    elif(options.benchmark == '649.fotonik3d_s'):
        print("--> 649.fotonik3d_s")
        process = spec17_benchmarks.fotonik3d_s
    elif(options.benchmark == '654.roms_s'):
        print("--> 654.roms_s")
        process = spec17_benchmarks.roms_s
    elif(options.benchmark == '657.xz_s'):
        print("--> 657.xz_s")
        process = spec17_benchmarks.xz_s
    elif(options.benchmark == '996.specrand_fs'):
        print("--> 996.specrand_fs")
        process = spec17_benchmarks.specrand_fs
    elif(options.benchmark == '997.specrand_fr'):
        print("--> 997.specrand_fr")
        process = spec17_benchmarks.specrand_fr
    elif(options.benchmark == '998.specrand_is'):
        print("--> 998.specrand_is")
        process = spec17_benchmarks.specrand_is
    elif(options.benchmark == '999.specrand_ir'):
        print("--> 999.specrand_ir")
        process = spec17_benchmarks.specrand_ir
    else:
        print("--> Invalid Benchmark Name Exiting.")
        sys.exit(1)
else:
    print("Need --benchmark switch to specify SPEC CPU2017 workload")
    sys.exit(1)


(CPUClass, test_mem_mode, FutureClass) = Simulation.setCPUClass(options)
CPUClass.numThreads = numThreads

# Check -- do not allow SMT with multiple CPUs
if options.smt and options.num_cpus > 1:
    fatal("You cannot use SMT with multiple CPUs!")

np = options.num_cpus
system = System(cpu = [CPUClass(cpu_id=i) for i in range(np)],
                mem_mode = test_mem_mode,
                mem_ranges = [AddrRange(options.mem_size)],
                cache_line_size = options.cacheline_size,
                workload = NULL)

if numThreads > 1:
    system.multi_thread = True

# Create a top-level voltage domain
system.voltage_domain = VoltageDomain(voltage = options.sys_voltage)

# Create a source clock for the system and set the clock period
system.clk_domain = SrcClockDomain(clock =  options.sys_clock,
                                   voltage_domain = system.voltage_domain)

# Create a CPU voltage domain
system.cpu_voltage_domain = VoltageDomain()

# Create a separate clock domain for the CPUs
system.cpu_clk_domain = SrcClockDomain(clock = options.cpu_clock,
                                       voltage_domain =
                                       system.cpu_voltage_domain)

# If elastic tracing is enabled, then configure the cpu and attach the elastic
# trace probe
if options.elastic_trace_en:
    CpuConfig.config_etrace(CPUClass, system.cpu, options)

# All cpus belong to a common cpu_clk_domain, therefore running at a common
# frequency.
for cpu in system.cpu:
    cpu.clk_domain = system.cpu_clk_domain

if ObjectList.is_kvm_cpu(CPUClass) or ObjectList.is_kvm_cpu(FutureClass):
    if buildEnv['TARGET_ISA'] == 'x86':
        system.kvm_vm = KvmVM()
        for process in multiprocesses:
            process.useArchPT = True
            process.kvmInSE = True
    else:
        fatal("KvmCPU can only be used in SE mode with x86")

# Sanity check
if options.simpoint_profile:
    if not ObjectList.is_noncaching_cpu(CPUClass):
        fatal("SimPoint/BPProbe should be done with an atomic cpu")
    if np > 1:
        fatal("SimPoint generation not supported with more than one CPUs")

# Assign Workload here
for i in range(np):
    system.cpu[i].workload = process
    system.cpu[i].createThreads()
    print("process: " + str(process.cmd) + "\n")

if options.ruby:
    Ruby.create_system(options, False, system)
    assert(options.num_cpus == len(system.ruby._cpu_ports))

    system.ruby.clk_domain = SrcClockDomain(clock = options.ruby_clock,
                                        voltage_domain = system.voltage_domain)
    for i in range(np):
        ruby_port = system.ruby._cpu_ports[i]

        # Create the interrupt controller and connect its ports to Ruby
        # Note that the interrupt controller is always present but only
        # in x86 does it have message ports that need to be connected
        system.cpu[i].createInterruptController()

        # Connect the cpu's cache ports to Ruby
        system.cpu[i].icache_port = ruby_port.slave
        system.cpu[i].dcache_port = ruby_port.slave
        if buildEnv['TARGET_ISA'] == 'x86':
            system.cpu[i].interrupts[0].pio = ruby_port.master
            system.cpu[i].interrupts[0].int_master = ruby_port.slave
            system.cpu[i].interrupts[0].int_slave = ruby_p2rt.master
            system.cpu[i].itb.walker.port = ruby_port.slave
            system.cpu[i].dtb.walker.port = ruby_port.slave
else:
    MemClass = Simulation.setMemClass(options)
    system.membus = SystemXBar()
    system.system_port = system.membus.slave
    CacheConfig.config_cache(options, system)
    MemConfig.config_mem(options, system)
    config_filesystem(system, options)

if options.wait_gdb:
    for cpu in system.cpu:
        cpu.wait_for_remote_gdb = True

root = Root(full_system = False, system = system)
Simulation.run(options, root, system, FutureClass)
