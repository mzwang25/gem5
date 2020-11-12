from m5.params import *
from m5.SimObject import SimObject

class HelloObject(SimObject):
    type = "HelloObject"
    cxx_header = "simplesimobj/hello_object.hh"

    latency = Param.Latency("Time in between firing")
    number_of_fires = Param.Int(1, "times to fire")
