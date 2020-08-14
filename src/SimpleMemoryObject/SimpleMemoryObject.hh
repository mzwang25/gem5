#ifndef __SIMPLE_MEMORY_OBJECT_HH
#define __SIMPLE_MEMORY_OBJECT_HH

#include "params/SimpleMemoryObject.hh"
#include "sim/sim_object.hh"

class SimpleMemoryObject : public SimObject
{
    public:
        SimpleMemoryObject(SimpleMemoryObjectParams* params);
};

#endif