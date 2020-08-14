#include "SimpleMemoryObject/SimpleMemoryObject.hh"
#include "debug/SimpleMemoryObject.hh"

SimpleMemoryObject::SimpleMemoryObject(SimpleMemoryObjectParams* params)
    : SimObject(params),
      instPort(params->name + ".inst_port", this),
      dataPort(params->name + ".data_port", this),
      memPort(params->name + ".mem_side", this)
{
    blocked = false;
    DPRINTF(SimpleMemoryObject, "Hello I am a SimpleMemoryObject!\n");
}

SimpleMemoryObject*
SimpleMemoryObjectParams::create() 
{
    return new SimpleMemoryObject(this);
}

Port&
SimpleMemoryObject::getPort(const std::string& if_name, PortID idx)
{
    panic_if(idx != InvalidPortID, "This object does not support vector ports");

    if(if_name == "mem_side") 
        return memPort;
    else if(if_name == "inst_port") 
        return instPort;
    else if(if_name == "data_port") 
        return dataPort;
    else
        return SimObject::getPort(if_name, idx);
    
}

bool
SimpleMemoryObject::CPUSidePort::recvTimingReq(PacketPtr pkt)
{
    if(!owner->handleRequest(pkt)) 
    {
        needRetry = true;
        return false;
    }

    else 
    {
        return true;
    }
}

bool
SimpleMemoryObject::handleRequest(PacketPtr pkt)
{
    if(blocked) return false;
    DPRINTF(SimpleMemoryObject, "Got request for addr %#x\n", pkt->getAddr());

    blocked = true;
    memPort.sendPacket(pkt);
    return true;
}

void
SimpleMemoryObject::MemSidePort::sendPacket(PacketPtr pkt)
{
    panic_if(blockedPacket != nullptr, "Should never try to send if blocked");

    if(!sendTimingReq(pkt))
    {
        blockedPacket = pkt;
    }
}

void
SimpleMemoryObject::MemSidePort::recvReqRetry()
{
    assert(blockedPacket != nullptr);

    PacketPtr pkt = blockedPacket;
    blockedPacket = nullptr;

    sendPacket(pkt);
}

bool
SimpleMemoryObject::handleResponse(PacketPtr pkt)
{
    assert(blocked);
    DPRINTF(SimpleMemoryObject, "Got response for addr %#x\n", pkt->getAddr());

    blocked = false;

    if(pkt->req->isInstFetch()) instPort.sendPacket(pkt);
    else dataPort.sendPacket(pkt);

    instPort.trySendRetry();
    dataPort.trySendRetry();
    
    return true;
}

void
SimpleMemoryObject::CPUSidePort::sendPacket(PacketPtr pkt)
{
    panic_if(blockedPacket != nullptr, "Should never try to send if blocked");

    if(!sendTimingResp(pkt)) 
    {
        blockedPacket = pkt;
    }
}

void
SimpleMemoryObject::CPUSidePort::recvRespRetry()
{
    assert(blockedPacket != nullptr);
    PacketPtr pkt = blockedPacket;
    blockedPacket = nullptr;

    sendPacket(pkt);
}

void
SimpleMemoryObject::CPUSidePort::trySendRetry()
{
    if(needRetry && blockedPacket == nullptr)
    {
        needRetry = false;
        DPRINTF(SimpleMemoryObject, "Sending retry request for %d\n", id);
        sendRetryReq();
    }
}
