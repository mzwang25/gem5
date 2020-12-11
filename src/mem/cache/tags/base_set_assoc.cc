/*
 * Copyright (c) 2012-2014 ARM Limited
 * All rights reserved.
 *
 * The license below extends only to copyright in the software and shall
 * not be construed as granting a license to any other intellectual
 * property including but not limited to intellectual property relating
 * to a hardware implementation of the functionality of the software
 * licensed hereunder.  You may use the software subject to the license
 * terms below provided that you ensure that this notice is replicated
 * unmodified and in its entirety in all distributions of the software,
 * modified or unmodified, in source code or in binary form.
 *
 * Copyright (c) 2003-2005,2014 The Regents of The University of Michigan
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met: redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer;
 * redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution;
 * neither the name of the copyright holders nor the names of its
 * contributors may be used to endorse or promote products derived from
 * this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

/**
 * @file
 * Definitions of a conventional tag store.
 */

#include "mem/cache/tags/base_set_assoc.hh"

#include <string>

#include "base/intmath.hh"

#include <iostream>
using namespace std;


BaseSetAssoc::BaseSetAssoc(const Params *p)
    :BaseTags(p), allocAssoc(p->assoc), blks(8 * p->size / p->block_size),
     sequentialAccess(p->sequential_access),
     replacementPolicy(p->replacement_policy),
     hello([this]{doubleSize();}, name())
{
    // Check parameters
    if (blkSize < 4 || !isPowerOf2(blkSize)) {
        fatal("Block size must be at least 4 and a power of 2");
    }

    current_assoc = 1;

    if(p->addWayAt.size() != 0)
    {
        for(auto i = p->addWayAt.begin(); i != p->addWayAt.end(); i++)
        {
            std::cout << "Increase assoc @ Tick " << *i << std::endl;
            auto event = new EventFunctionWrapper([this]{doubleSize();}, name());
            assocIncreaseEvents.push_back(event);
            schedule(event, *i);
        }

    }

    if(p->remWayAt.size() != 0)
    {
        for(auto i = p->remWayAt.begin(); i != p->remWayAt.end(); i++)
        {
            std::cout << "Decrease assoc @ Tick " << *i << std::endl;
            auto event = new EventFunctionWrapper([this]{halfSize();}, name());
            schedule(event, *i);
        }

    }
}

void
BaseSetAssoc::tagsInit()
{
    // Initialize all blocks
    for (unsigned blk_index = 0; blk_index < numBlocks; blk_index++) {
        // Locate next cache block
        CacheBlk* blk = &blks[blk_index];
        assert(!blk->isValid());
        assert(blk->tag);

        // Link block to indexing policy
        indexingPolicy->setEntry(blk, blk_index);

        // Associate a data chunk to the block
        blk->data = &dataBlks[blkSize*blk_index];

        // Associate a replacement data entry to the block
        blk->replacementData = replacementPolicy->instantiateEntry();
    }
}

void
BaseSetAssoc::invalidate(CacheBlk *blk)
{
    BaseTags::invalidate(blk);

    // Decrease the number of tags in use
    stats.tagsInUse--;

    // Invalidate replacement data
    replacementPolicy->invalidate(blk->replacementData);
}

void
BaseSetAssoc::halfSize()
{
    //starting index of the blocks we are going to remove
    unsigned start_index = numBlocks / 2;

    for(unsigned blk_index = start_index; blk_index < numBlocks; blk_index++)
    {
      ((BaseCache*) ownerCache)->writebackVisitor(blks[blk_index]);
      ((BaseCache*) ownerCache)->invalidateVisitor(blks[blk_index]);
    }

    indexingPolicy->decreaseAssociativity();

    current_assoc /= 2;
    numBlocks /= 2;

    std::cout << "Set Associativity to " << current_assoc << std::endl;

}

void
BaseSetAssoc::doubleSize()
{
    indexingPolicy->increaseAssociativity();

    for (unsigned blk_index = 0; blk_index < numBlocks; blk_index++) 
    {
        CacheBlk* blk = &blks[blk_index];
        //indexingPolicy->setEntry(blk, 2*blk_index);
        assert(blk->isValid() || !blk->isValid());
    }

    unsigned start_index = numBlocks;

    int a = current_assoc + 1;

    current_assoc *= 2;
    numBlocks *= 2;

    //                 1,3,5,7,9,11
    // 0123            2,3,6,7,10,11
    // 4567
    // 89(10)(11)

    int state = 1 ? current_assoc > 2 : 0;
    int idx = current_assoc / 2;

    for (unsigned blk_index = start_index; blk_index < numBlocks; blk_index++) {
        // locate next cache block
        CacheBlk* blk = &blks[blk_index];

        assert(!blk->isValid());
        assert(blk->tag);

        // link block to indexing policy
        indexingPolicy->setEntry(blk, idx);
        if(state == 0) idx += a;
        else idx += 1;
        state = (state + 1) % (a - 1);

        // associate a data chunk to the block
        blk->data = &dataBlks[blkSize*blk_index];

        // associate a replacement data entry to the block
        blk->replacementData = replacementPolicy->instantiateEntry();
    }

    std::cout << "Set Associativity to " << current_assoc << std::endl;

}

BaseSetAssoc *
BaseSetAssocParams::create()
{
    // There must be a indexing policy
    fatal_if(!indexing_policy, "An indexing policy is required");

    return new BaseSetAssoc(this);
}
