#include "simplesimobj/SimpleObj.hh"
#include "debug/SimpleObj.hh"
#include <iostream>

SimpleObj::SimpleObj(SimpleObjParams* p)
    : SimObject(p), event([this]{processEvent();}, name())
{
    timesCalled = 0;
    latency = 100;
    DPRINTF(SimpleObj, "Hello I am SimpleObj and I exist now!\n");
}

void
SimpleObj::processEvent() 
{
    if(timesCalled < 10)
    {
        schedule(event, 100 + timesCalled * latency );
        DPRINTF(SimpleObj, "Scheduled new event\n");
        timesCalled++;
    }

    else 
    {
        DPRINTF(SimpleObj, "No new events scheduled\n");
    }
}

// startup is called when the simulation begins for the first time (simulate() in python config)
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