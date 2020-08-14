#include "SimpleMemoryObject/SimpleMemoryObject.hh"
#include "debug/SimpleMemoryObject.hh"

SimpleMemoryObject::SimpleMemoryObject(SimpleMemoryObjectParams* params)
    : SimObject(params)
{
    DPRINTF(SimpleMemoryObject, "Hello I am a SimpleMemoryObject!\n");
}

SimpleMemoryObject*
SimpleMemoryObjectParams::create() 
{
    return new SimpleMemoryObject(this);
}