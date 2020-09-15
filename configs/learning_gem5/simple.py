import m5
from m5.objects import *
from caches import *
from optparse import OptionParser

parser = OptionParser()

parser.add_option('--l1i_size')
parser.add_option('--l1d_size')
parser.add_option('--l2_size')

(options, args) = parser.parse_args()

############################################

system = System()


# clock domain
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '10GHz'
system.clk_domain.voltage_domain = VoltageDomain(voltage = "5V")

# memory setup
system.mem_mode = 'atomic'
system.mem_ranges = [AddrRange('512MB'), AddrRange('512MB', '1024MB')]


# Memory Bus
system.membus = SystemXBar()
system.l2bus = L2XBar()

# CPU
system.cpu = AtomicSimpleCPU()
system.cpu.icache = L1ICache(options)
system.cpu.dcache = L1DCache(options)

system.cpu.icache_port = system.cpu.icache.cpu_side
system.cpu.dcache_port = system.cpu.dcache.cpu_side

system.cpu.icache.mem_side = system.l2bus.slave

system.cpu.dcache.mem_side = system.l2bus.slave

system.l2cache = L2Cache(options)
system.l2cache.cpu_side = system.l2bus.master
system.l2cache.mem_side = system.membus.slave

# Interrupt Port
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.master
system.cpu.interrupts[0].int_master = system.membus.slave
system.cpu.interrupts[0].int_slave = system.membus.master
system.system_port = system.membus.slave

# DDR3 Memory Controller
system.mem_ctrl = DDR3_1600_8x8()
system.mem_ctrl.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master

# SRAM Memory Controller
system.scratchpad = DDR3_1600_8x8()
system.scratchpad.range = system.mem_ranges[1]
system.scratchpad.port = system.membus.master

# Process
process = Process()
process.cmd = ['/home/nanoproj/michael/gem5/configs/learning_gem5/sieve_of_eratosthenes', '5']
system.cpu.workload = process 
system.cpu.createThreads()

root = Root(full_system = False, system = system)
m5.instantiate()
m5.simulate()