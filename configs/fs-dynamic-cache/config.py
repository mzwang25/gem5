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

addToPath("/home/nanoproj/michael/gem5/configs/dynamic-cache")
addToPath("/home/nanoproj/michael/gem5/configs/common")

from getBenchmark import getBenchmark

process = None

parser = OptionParser()
parser.add_option("-b", "--benchmark", dest="benchmark", help="name of benchmark")
parser.add_option("-i", "--maxinst", dest="maxinst", help="max insts", default=3000000)

(options, _) = parser.parse_args()

if(options.benchmark == None):
    print("! benchmark is a required argument")
    sys.exit(1)

process = getBenchmark(options.benchmark)


#=================================================================
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
    size = '256kB'
    tag_latency = 20
    data_latency = 20
    response_latency = 20
    mshrs = 20
    tgts_per_mshr = 12


    def __init__(self, options=None):
        super(L2Cache, self).__init__()
        pass
 

class L3Cache(Cache):
    assoc = 1
    size = "512kB"
    tag_latency = 51
    data_latency = 51
    response_latency = 51
    mshrs = 4
    tgts_per_mshr = 20
    clusivity = Param.Clusivity("mostly_excl")


    def __init__(self, options=None):
        super(L3Cache, self).__init__()
        pass

class L4Cache(Cache):
    assoc = 1
    size = "512kB"
    tag_latency = 130
    data_latency = 130
    response_latency = 130
    mshrs = 4
    tgts_per_mshr = 20
    clusivity = Param.Clusivity("mostly_excl")

    #will double size and assoc at ticks in list
    tags = BaseSetAssoc(addWayAt=[19]) 

    def __init__(self, options=None):
        super(L4Cache, self).__init__()
        pass


#=================================================================
system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

system.cpu = TimingSimpleCPU()
system.dcache = L1Cache()
system.icache = L1Cache()
system.l2cache = L2Cache()
system.l3Dram = L3Cache()
system.DynamicCache = L4Cache()
system.membus = SystemXBar()
system.l2bar = L2XBar()

# CPU 
system.cpu.icache_port = system.icache.cpu_side
system.cpu.dcache_port = system.dcache.cpu_side

system.dcache.mem_side = system.l2bar.slave
system.icache.mem_side = system.l2bar.slave

system.l2bar.master = system.l2cache.cpu_side
system.l2cache.mem_side = system.l3Dram.cpu_side

system.l3Dram.mem_side = system.DynamicCache.cpu_side

system.DynamicCache.mem_side = system.membus.slave
#=================================================================
# Add a memory delay component to simulated slow PCM

system.mem_delay = SimpleMemDelay(
    read_req = "130ns",
    read_resp = "130ns",
    write_req = "185ns",
    write_resp = "185ns"

)

system.mem_delay.slave = system.membus.master

system.mem_ctrl = DDR3_1600_8x8()
system.mem_ctrl.range = system.mem_ranges[0]
system.mem_ctrl.port = system.mem_delay.master
#=================================================================
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.master
system.cpu.interrupts[0].int_master = system.membus.slave
system.cpu.interrupts[0].int_slave = system.membus.master


system.system_port = system.membus.slave

system.cpu.workload = process
system.cpu.createThreads()
system.cpu.max_insts_any_thread = options.maxinst

root = Root(full_system = True, system = system)
m5.instantiate()

print ("Beginning simulation!")
exit_event = m5.simulate()
print('Exiting @ tick %i because %s' % (m5.curTick(), exit_event.getCause()))
