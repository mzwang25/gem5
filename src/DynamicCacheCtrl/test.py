###############################################################################
# Usage:
#   gem5.opt --outdir=<> 
#            --debug-flags=DynamicCacheCtrl 
#            test.py
#            <Benchmark Name>
#            <Max Instructions>
#
###############################################################################

import m5
import sys
import os
import subprocess
from m5.objects import *
from m5.util import addToPath

###############################################################################
# SPEC BENCHMARKS

addToPath("/home/nanoproj/michael/gem5/src/DynamicCacheCtrl/")
addToPath("/home/nanoproj/michael/gem5/configs/common")

from getBenchmark import getBenchmark

process = None

if len(sys.argv) == 3:
    process = getBenchmark(sys.argv[1])
else:
    print("Need benchmark argument to run")
    sys.exit(1)

###############################################################################
# Some Caches

class L1Cache(Cache):
    assoc = 1
    size = '32kB'
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20

    def __init__(self, options=None):
        super(L1Cache, self).__init__()
        pass

class L2Cache(Cache):
    assoc = 1
    size = '1024kB'
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20

    def __init__(self, options=None):
        super(L2Cache, self).__init__()
        pass

class L3Cache(Cache):
    assoc = 1
    size = '8192kB'
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20


    def __init__(self, options=None):
        super(L3Cache, self).__init__()
        pass


###############################################################################

system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

system.cpu = TimingSimpleCPU()
system.dynamic_cache = DynamicCacheCtrl()
system.dcache = L1Cache()
system.icache = L1Cache()
system.l2cache = L2Cache()
system.membus = SystemXBar()
system.l2bar = IOXBar()

# CPU 
system.cpu.icache_port = system.icache.cpu_side
system.cpu.dcache_port = system.dcache.cpu_side

system.dcache.mem_side = system.l2bar.slave
system.icache.mem_side = system.l2bar.slave

system.l2bar.master = system.l2cache.cpu_side

#=================================================================
#Connection to Dynamic Cache Component
system.l2cache.mem_side = system.dynamic_cache.cpu_side

system.cache_small = L3Cache()
system.cache_medium = L3Cache()
system.cache_large = L3Cache()


system.dynamic_cache.connectCaches(
    system.membus, 
    system.cache_small, 
    system.cache_medium, 
    system.cache_large)

system.dynamic_cache.cpu_object = system.cpu

#=================================================================
# Other system configs

system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.master
system.cpu.interrupts[0].int_master = system.membus.slave
system.cpu.interrupts[0].int_slave = system.membus.master

system.mem_ctrl = DDR3_1600_8x8()
system.mem_ctrl.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master

system.system_port = system.membus.slave

system.cpu.workload = process
system.cpu.createThreads()
system.cpu.max_insts_any_thread = sys.argv[2]

root = Root(full_system = False, system = system)
m5.instantiate()

print ("Beginning simulation!")
exit_event = m5.simulate()
print('Exiting @ tick %i because %s' % (m5.curTick(), exit_event.getCause()))
