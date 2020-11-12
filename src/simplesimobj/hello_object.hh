#ifndef __SIMPLESIMOBJ_HELLO_OBJECT_HH__
#define __SIMPLESIMOBJ_HELLO_OBJECT_HH__

#include "params/HelloObject.hh"
#include "sim/sim_object.hh"

class HelloObject : public SimObject
{
    private:
        void processEvent();
        int m_times_fired, m_max_fired;
        Tick m_latency;
        EventFunctionWrapper event;

    public:
        HelloObject(HelloObjectParams* p);
        void startup();
};

#endif
