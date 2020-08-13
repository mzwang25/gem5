#ifndef __SIMPLE_SIM_OBJECT_HH
#define __SIMPLE_SIM_OBJECT_HH

// Include path should be in sim directory
#include "sim/sim_object.hh"
#include "params/SimpleObj.hh"

class SimpleObj : public SimObject
{
    private:
        void processEvent();
        int timesCalled;
        int latency;
        EventFunctionWrapper event;

    public:
        SimpleObj(SimpleObjParams* p);
        void startup();
};



#endif