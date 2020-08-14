#ifndef __SIMPLE_MEMORY_OBJECT_HH
#define __SIMPLE_MEMORY_OBJECT_HH

#include "params/SimpleMemoryObject.hh"
#include "sim/sim_object.hh"
#include "mem/port.hh"


class SimpleMemoryObject : public SimObject
{
    private:
        class CPUSidePort : public SlavePort 
        {
            private:
                SimpleMemoryObject* owner;
                bool needRetry; //If cpu sends a request but SimpleMemoryObject is busy, set this to true. Once free, if this is true, send a request to retry to cpu
                PacketPtr blockedPacket; //Packet attempted to be sent but the receiever isn't ready yet.
            public:
                CPUSidePort(const std::string& name, SimpleMemoryObject* owner)
                    : SlavePort(name, owner), owner(owner), needRetry(false), blockedPacket(nullptr)
                {}

                AddrRangeList getAddrRanges() const override {return owner->getAddrRanges();};

                void sendPacket(PacketPtr pkt);
                void trySendRetry();

            protected:
                Tick recvAtomic(PacketPtr pkt) override {panic("recvAtomic unimplemented");}
                void recvFunctional(PacketPtr pkt) override {return owner->handleFunctional(pkt);};
                bool recvTimingReq(PacketPtr pkt) override;
                void recvRespRetry() override;
        };

        class MemSidePort : public MasterPort
        {
            private:
                SimpleMemoryObject* owner;
                PacketPtr blockedPacket;
            
            public:
                MemSidePort(const std::string& name, SimpleMemoryObject* owner) 
                    : MasterPort(name, owner), owner(owner), blockedPacket(nullptr)
                {}

                void sendPacket(PacketPtr pkt);

            protected:
                bool recvTimingResp(PacketPtr pkt) override {return owner->handleResponse(pkt);};
                void recvReqRetry() override;
                void recvRangeChange() override {owner->sendRangeChange();};
        };

        CPUSidePort instPort;
        CPUSidePort dataPort;
        MemSidePort memPort;

        bool handleRequest(PacketPtr pkt);
        bool handleResponse(PacketPtr pkt);
        void handleFunctional(PacketPtr pkt) {memPort.sendFunctional(pkt);};
        AddrRangeList getAddrRanges() const {return memPort.getAddrRanges();};
        void sendRangeChange() {instPort.sendRangeChange(); dataPort.sendRangeChange();};

        bool blocked;

    public:
        SimpleMemoryObject(SimpleMemoryObjectParams* params);
        Port &getPort(const std::string& if_name, PortID idx=InvalidPortID) override;
};

#endif