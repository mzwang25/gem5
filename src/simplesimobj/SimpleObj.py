from m5.params import *
from m5.SimObject import SimObject 

class SimpleObj(SimObject):
    type = 'SimpleObj'
    cxx_header = "simplesimobj/SimpleObj.hh"