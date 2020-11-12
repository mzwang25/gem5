#include "simplesimobj/hello_object.hh"
#include "debug/Hello.hh"
#include <iostream>

HelloObject::HelloObject(HelloObjectParams* params) :
    SimObject(params), event([this]{processEvent();}, name())
{
    m_times_fired = 0;
    m_max_fired = params->number_of_fires;
    m_latency = params->latency;
    DPRINTF(Hello, "HelloObject()\n");
}

void
HelloObject::processEvent()
{
    DPRINTF(Hello, "processEvent() %d\n", m_times_fired);
    m_times_fired++;

    if(m_times_fired < m_max_fired)
        schedule(event, curTick() + m_latency);
}

void
HelloObject::startup()
{
    DPRINTF(Hello, "startup()\n");
    schedule(event, 100);
}

HelloObject*
HelloObjectParams::create()
{
    return new HelloObject(this);
}
