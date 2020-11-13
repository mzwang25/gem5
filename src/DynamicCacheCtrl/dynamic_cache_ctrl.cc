#include "dynamic_cache_ctrl.hh"
#include "debug/DynamicCacheCtrl.hh"
#include "base/statistics.hh"

#define LOG(X) DPRINTF(DynamicCacheCtrl, "%s\n\n", X);

#define USING_CACHE 0
#define USING_NONE 1

DynamicCacheCtrl::DynamicCacheCtrl(DynamicCacheCtrlParams* params) : 
    SimObject(params),
    cpu_side(params->name + ".cpu_side", this),
    mem_side(params->name + ".mem_side", this),
    cache_side_small(params->name + ".cache_side_small", this),
    cache_side_medium(params->name + ".cache_side_medium", this),
    cache_side_large(params->name + ".cache_side_large", this),
    cache_small(params->cache_small),
    cache_medium(params->cache_medium),
    cache_large(params->cache_large),
    cpu_object(params->cpu_object),
    blocked_packet(0),
    current_state(USING_NONE),
    lastStatDump(0)
{}

DynamicCacheCtrl*
DynamicCacheCtrlParams::create() 
{
    return new DynamicCacheCtrl(this);
}

Port&
DynamicCacheCtrl::getPort(const std:: string& if_name, PortID idx)
{
    panic_if(idx != InvalidPortID, "No vector ports support");
    if (if_name == "cpu_side") 
        return cpu_side;
    else if (if_name == "mem_side") 
        return mem_side;
    else if (if_name == "cache_side_small") 
        return cache_side_small;
    else if (if_name == "cache_side_medium") 
        return cache_side_medium;
    else if (if_name == "cache_side_large") 
        return cache_side_large;
    else
        return SimObject::getPort(if_name, idx);
}

bool
DynamicCacheCtrl::CPUSidePort::recvTimingReq(PacketPtr pkt)
{

    return owner->handleTimingReq(pkt);
}

DynamicCacheCtrl::MemSidePort*
DynamicCacheCtrl::mem_port_to_use()
{
    bool next_state;

    /* Setting next_state depending on stats */
    Counter current_inst = cpu_object -> numSimulatedInsts();

    //Right it starts with no cache -> cache -> no cache
    if(current_inst < 2000000)
    {
        next_state = USING_CACHE;
    }
    else
    {
        next_state = USING_CACHE;
    }

    //current_inst may never reach 1mil so mod won't work
    if(current_inst > lastStatDump + 1000000) 
    {
        LOG("Dumping Stats");
        Stats::dump();
        lastStatDump += 1000000;
    }


    /* Handle Cache writebacks / invalidations */
    if(current_state == USING_CACHE && next_state == USING_NONE)
    {
        LOG("Switching from USING_CACHE to USING_NONE");

        Tick tickNow = curTick();


        //cache_small->memWriteback();
        //cache_small->memInvalidate();
        
        invalidation_ticks = curTick() - tickNow;
    }

    else if(current_state == USING_NONE && next_state == USING_CACHE)
    {
        LOG("Switching from USING_NONE to USING_CACHE");
        invalidation_ticks = 0;
    }

    current_state = next_state;


    /* return port object */
    if(next_state == USING_NONE)
        return &mem_side;
    else
        return &cache_side_small;


}

/* handleTimingReq handles sending packets */
bool
DynamicCacheCtrl::handleTimingReq(PacketPtr pkt)
{

    //Right now the switch occurs based on the current Tick
    MemSidePort* port_to_use = mem_port_to_use();

    bool result = false; 
    if(curTick() > 15037700000)
    {
        RequestPtr req = std::make_shared<Request>(0, 10, 0, 0);
        Packet* newpkt = new Packet(req, MemCmd::FlushReq);
        //std::cout <<"hello " +  newpkt->cmdString() << std::endl;

        result = (port_to_use) -> sendTimingReq(newpkt);
    }
    else
        result = (port_to_use) -> sendTimingReq(pkt);

    // if mem_side is unable to send packet, store/retry
    if (!result) 
    {
        blocked_packet = pkt;    
    }

    //TODO: Figure out what to return
    return true;
}

void
DynamicCacheCtrl::MemSidePort::recvReqRetry()
{

    panic_if(owner->blocked_packet == 0, "No packet to retry!");

    if (sendTimingReq(owner->blocked_packet)) 
        owner->blocked_packet = 0;
}

bool
DynamicCacheCtrl::handleRecvTimingResp(PacketPtr pkt)
{
    return cpu_side.sendTimingResp(pkt);
}

bool
DynamicCacheCtrl::MemSidePort::recvTimingResp(PacketPtr pkt) 
{
    return owner->handleRecvTimingResp(pkt); 
}


void
DynamicCacheCtrl::regStats()
{
    SimObject::regStats();
    invalidation_ticks.name(name() + ".invTick").desc("Ticks taken to invalidate");
}
