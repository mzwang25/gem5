###############################################################################
# Usage:
#   gem5.opt --outdir=<> 
#            --debug-flags=DynamicCacheCtrl 
#            test.py
#            <Benchmark Name>
#            <Max Instructions>
#
###############################################################################

# change fully associative to direct mappend
# make sure it's not inclusive
# various performance by just using that as l3 / l4

import m5
import sys
import os
import subprocess
from m5.objects import *
from m5.util import addToPath
from optparse import OptionParser

#=================================================================
# SPEC BENCHMARKS

addToPath("/home/nanoproj/michael/gem5/src/DynamicCacheCtrl/")
addToPath("/home/nanoproj/michael/gem5/configs/common")

from getBenchmark import getBenchmark

process = None

parser = OptionParser()
parser.add_option("-b", "--benchmark", dest="benchmark", help="name of benchmark")
parser.add_option("-i", "--maxinst", dest="maxinst", help="max insts", default=3000000)
parser.add_option("-l", "--l3size", dest="l3size", help="l3size", default="8192kB")
parser.add_option("-f", "--flush", 
                   dest="flush", 
                   help="account flushing penalty", 
                   action="store_false", 
                   default=True)

(options, _) = parser.parse_args()

if(options.benchmark == None):
    print("! benchmark is a required argument")
    sys.exit(1)

process = getBenchmark(options.benchmark)


#=================================================================
# Some Caches

class L1Cache(NoncoherentCache):
    assoc = 1
    size = '16kB'
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20
    clusivity = Param.Clusivity("mostly_excl")

    def __init__(self, options=None):
        super(L1Cache, self).__init__()
        pass

class L2Cache(NoncoherentCache):
    assoc = 1
    size = '32kB'
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20
    clusivity = Param.Clusivity("mostly_excl")

    def __init__(self, options=None):
        super(L2Cache, self).__init__()
        pass
 

class L3Cache(NoncoherentCache):
    assoc = 1
    size = options.l3size
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 400000
    tgts_per_mshr = 2000
    clusivity = Param.Clusivity("mostly_excl")


    def __init__(self, options=None):
        super(L3Cache, self).__init__()
        pass

class DCXBar(NoncoherentXBar):
    width = 16 #bytes
    frontend_latency = 3
    forward_latency = 4
    response_latency = 2

#=================================================================
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
system.membus = DCXBar()
system.l2bar = DCXBar()

# CPU 
system.cpu.icache_port = system.icache.cpu_side
system.cpu.dcache_port = system.dcache.cpu_side

system.dcache.mem_side = system.l2bar.slave
system.icache.mem_side = system.l2bar.slave

system.l2bar.master = system.l2cache.cpu_side

#=================================================================
#Connection to Dynamic Cache Component
system.dynamic_cache.accountFlush = options.flush

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
system.cpu.max_insts_any_thread = options.maxinst

root = Root(full_system = False, system = system)
m5.instantiate()

print ("Beginning simulation!")
exit_event = m5.simulate()
print('Exiting @ tick %i because %s' % (m5.curTick(), exit_event.getCause()))
