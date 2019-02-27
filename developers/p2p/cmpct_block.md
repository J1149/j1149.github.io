---
layout: default
title: CmpctBlock
parent: P2P
grand_parent: Developer Reference
---

CmpctBlock
==============

*Added in protocol version 70014 as described by BIP152.*

**Version 1 compact blocks are pre-segwit (txids)**
**Version 2 compact blocks are post-segwit (wtxids)**

The `cmpctblock` message is a reply to a `getdata` message which 
requested a block using the inventory type `MSG_CMPCT_BLOCK`. If the 
requested block was recently announced and is close to the tip of the
best chain of the receiver and after having sent the requesting peer 
a `sendcmpct` message, nodes respond with a `cmpctblock` message containing 
data for the block. 

**If the requested block is too old, the node responds with a *full non-compact block***

Upon receipt of a `cmpctblock` message, after sending a `sendcmpct` message, 
nodes should calculate the short transaction ID for each unconfirmed 
transaction they have available (ie in their mempool) and compare each 
to each short transaction ID in the `cmpctblock` message. After finding 
already-available transactions, nodes which do not have all transactions 
available to reconstruct the full block should request the missing transactions 
using a `getblocktxn` message.

A node must not send a `cmpctblock` message unless they are able to respond to 
a `getblocktxn` message which requests every transaction in the block. A node 
must not send a `cmpctblock` message without having validated that the header properly 
commits to each transaction in the block, and properly builds on top of the existing, 
fully-validated chain with a valid proof-of-work either as a part of the current most-work 
valid chain, or building directly on top of it. A node may send a `cmpctblock` message before 
validating that each transaction in the block validly spends existing UTXO set entries.

The `cmpctblock` message contains a vector of `PrefilledTransaction` whose structure is defined below.

| Bytes    | Name                 | Data Type        | Description
|----------|----------------------|------------------|----------------
| *Varies* | index                | compactSize uint | The index into the block at which this transaction is located. 
| *Varies* | tx                   | Transaction      | The transaction which is in the block at the index.

The `cmpctblock` message is compromised of a serialized `HeaderAndShortIDs` 
structure which is defined below. A `HeaderAndShortIDs` structure is used to 
relay a block header, the short transactions IDs used for matching 
already-available transactions, and a select few transactions which 
we expect a peer may be missing.

| Bytes    | Name                 | Data Type              | Description
|----------|----------------------|------------------------|----------------
| 80       | block header         | block_header           | The block header in the format described in the [block header section][section block header].
| 8        | nonce                | uint64_t               | A nonce for use in short transaction ID calculations.
| *Varies* | shortids length      | compactSize uint       | The number of short transaction IDs in the following field.
| *Varies* | shortids             | byte[]                 | The short transaction IDs calculated from the transactions which were not provided explicitly in prefilledtxn. Vector of 6-byte integers in the spec, padded with two null-bytes so it can be read as an 8-byte integer. **In version 2 of compact blocks, shortids should use the *wtxid* instead of *txid* as defined by *BIP141***
| *Varies* | prefilled txn length | compactSize uint       | The number of prefilled transactions in the following field.
| *Varies* | prefilled txn        | PrefilledTransaction[] | Used to provide the coinbase transaction and a select few which we expect a peer may be missing. Vector of `PrefilledTransaction` structures defined above.

**Important protocol version 70015 notes regarding Compact Blocks**

New banning behavior was added to the compact block logic in protocol version 70015 to prevent node abuse,
the new changes are outlined below as defined in **BIP152**.

Any undefined behavior in this spec may cause failure to transfer block to, peer disconnection by, or 
self-destruction by the receiving node. A node receiving non-minimally-encoded CompactSize encodings 
should make a best-effort to eat the sender's cat.

As high-bandwidth mode permits relaying of `cmpctblock` messages prior to full validation 
(requiring only that the block header is valid before relay), nodes SHOULD NOT ban a peer 
for announcing a new block with a `cmpctblock` message that is invalid, but has a valid header.  

For avoidance of doubt, nodes SHOULD bump their peer-to-peer protocol version to 70015 or 
higher to signal that they will not ban or punish a peer for announcing compact blocks prior 
to full validation, and nodes SHOULD NOT announce a `cmpctblock` message to a peer with a version number 
below 70015 before fully validating the block.

**Version 2 compact blocks notes**

Transactions inside `cmpctblock` messages (both those used as direct announcement and those in response to getdata) and 
in `blocktxn` messages should include witness data, using the same format as responses to getdata `MSG_WITNESS_TX`, specified in **BIP144**.

Upon receipt of a `getdata` message containing a request for a `MSG_CMPCT_BLOCK` object for which a `cmpctblock` message is not sent in response, 
the block message containing the requested block in non-compact form MUST be encoded with witnesses (as is sent in reply to a `MSG_WITNESS_BLOCK`) 
if the protocol version used to encode the `cmpctblock` message would have been 2, and encoded without witnesses (as is sent in response to a `MSG_BLOCK`) 
if the protocol version used to encode the `cmpctblock` message would have been 1.

**Short Transaction ID calculation**

Short transaction IDs are used to represent a transaction without sending a full 256-bit hash. They are calculated as follows,

* A single-SHA256 hashing the block header with the nonce appended (in little-endian)
* Running SipHash-2-4 with the input being the transaction ID (**wtxid in version 2 of compact blocks**) and the keys (k0/k1) set to the first two little-endian 64-bit integers from the above hash, respectively.
* Dropping the 2 most significant bytes from the SipHash output to make it 6 bytes.
* Two null-bytes appended so it can be read as an 8-byte integer.

