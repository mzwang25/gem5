#include "simplesimobj/SimpleObj.hh"
#include "debug/SimpleObj.hh"
#include <iostream>

SimpleObj::SimpleObj(SimpleObjParams* p)
    : SimObject(p), event([this]{processEvent();}, name())
{
    DPRINTF(SimpleObj, "Hello I am SimpleObj and I exist now!\n");
}

void
SimpleObj::processEvent() 
{
    DPRINTF(SimpleObj, "processEvent() has been called!\n");
}

void
SimpleObj::startup() 
{
    schedule(event, 100);
}

// The python script calls this function which instantiates a SimpleObj
SimpleObj*
SimpleObjParams::create()
{
    return new SimpleObj(this);
}