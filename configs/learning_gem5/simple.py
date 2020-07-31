import m5
from m5.objects import *
from caches import *


system = System()

# clock domain
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain(voltage = "5V")

# memory setup
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

# Memory Bus
system.membus = SystemXBar()
system.l2bus = L2XBar()

# CPU
system.cpu = TimingSimpleCPU()
system.cpu.icache = L1ICache()
system.cpu.dcache = L1DCache()

system.cpu.icache_port = system.cpu.icache.cpu_side
system.cpu.dcache_port = system.cpu.dcache.cpu_side

system.cpu.icache.mem_side = system.l2bus.slave
system.cpu.dcache.mem_side = system.l2bus.slave

system.l2cache = L2Cache()
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

# Process
process = Process()
process.cmd = ['/home/nanoproj/michael/gem5/configs/learning_gem5/a.out']
system.cpu.workload = process 
system.cpu.createThreads()

root = Root(full_system = False, system = system)
m5.instantiate()
m5.simulate()