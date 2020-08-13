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
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

# Memory Bus
system.membus = SystemXBar()
system.l2bus = L2XBar()

# CPU
system.cpu = [TimingSimpleCPU(), TimingSimpleCPU()]

# instantiate i and d cache
system.cpu[0].icache = L1ICache(options)
system.cpu[0].dcache = L1DCache(options)

system.cpu[1].icache = L1ICache(options)
system.cpu[1].dcache = L1DCache(options)

# connect the caches
system.cpu[0].icache_port = system.cpu[0].icache.cpu_side
system.cpu[0].dcache_port = system.cpu[0].dcache.cpu_side

system.cpu[1].icache_port = system.cpu[1].icache.cpu_side
system.cpu[1].dcache_port = system.cpu[1].dcache.cpu_side

system.l2cache = L2Cache(options)
system.l2cache.cpu_side = system.l2bus.master
system.l2cache.mem_side = system.membus.slave

system.cpu[0].icache.mem_side = system.l2bus.slave
system.cpu[0].dcache.mem_side = system.l2bus.slave

system.cpu[1].icache.mem_side = system.membus.slave
system.cpu[1].dcache.mem_side = system.membus.slave

# Interrupt Port
for i in range(2):
    system.cpu[i].createInterruptController()
    system.cpu[i].interrupts[0].pio = system.membus.master
    system.cpu[i].interrupts[0].int_master = system.membus.slave
    system.cpu[i].interrupts[0].int_slave = system.membus.master

system.system_port = system.membus.slave

# DDR3 Memory Controller
system.mem_ctrl = DDR3_1600_8x8()
system.mem_ctrl.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master

# Process
processes = [Process(pid = 100), Process(pid = 101)]
processes[0].cmd = ['/home/nanoproj/michael/gem5/configs/learning_gem5/sieve_of_eratosthenes', '10']
processes[1].cmd = ['/home/nanoproj/michael/gem5/configs/learning_gem5/sieve_of_eratosthenes', '20']

# assign processes to cpu
system.cpu[0].workload = processes[0]
system.cpu[0].createThreads()

system.cpu[1].workload = processes[1]
system.cpu[1].createThreads()

root = Root(full_system = False, system = system)
m5.instantiate()
m5.simulate()