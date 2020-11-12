from m5.params import *
from m5.proxy import *
from m5.SimObject import SimObject

class DynamicCacheCtrl(SimObject):
    type = "DynamicCacheCtrl"
    cxx_header = "DynamicCacheCtrl/dynamic_cache_ctrl.hh"

    cpu_side = SlavePort("CPU side port, receives requests")
    cache_side_small = MasterPort("CPU side port, receives requests")
    cache_side_medium = MasterPort("CPU side port, receives requests")
    cache_side_large = MasterPort("CPU side port, receives requests")
    mem_side = MasterPort("Memory side port, sends requests")


    cache_small = Param.Cache("A Cache Object")
    cache_medium = Param.Cache("A Cache Object")
    cache_large = Param.Cache("A Cache Object")

    cpu_object = Param.BaseCPU("A CPU Object")

    def connectCaches(self, membus, cache1, cache2, cache3):
        self.cache_small = cache1
        self.cache_medium = cache2
        self.cache_large = cache3

        self.mem_side = membus.slave
        self.cache_side_small = cache1.cpu_side
        self.cache_side_medium = cache2.cpu_side
        self.cache_side_large = cache3.cpu_side

        cache1.mem_side = membus.slave
        cache2.mem_side = membus.slave
        cache3.mem_side = membus.slave
