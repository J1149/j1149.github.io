---
layout: default
title: BlockTxn
parent: P2P
grand_parent: Developer Reference
---

BlockTxn
====================

*Added in protocol version 70014 as described by BIP152.*

The `blocktxn` message is defined as a message containing a serialized `BlockTransactions` message.
Upon receipt of a properly-formatted requested `blocktxn` message, nodes should attempt to 
reconstruct the full block by taking the prefilledtxn transactions from the original `cmpctblock` message 
and placing them in the marked positions, then for each short transaction ID from the original 
`cmpctblock` message, in order, find the corresponding transaction either from the `blocktxn` message or 
from other sources and place it in the first available position in the block then once the block 
has been reconstructed, it shall be processed as normal, keeping in mind that short transaction IDs 
are expected to occasionally collide, and that nodes must not be penalized for such collisions, 
wherever they appear.

The structure of `BlockTransactions` is defined below.

| Bytes    | Name                 | Data Type              | Description
|----------|----------------------|------------------------|----------------
| 32       | block hash           | binary blob            | The blockhash of the block which the transactions being provided are in.
| *Varies* | transactions length  | compactSize uint       | The number of transactions being provided.
| *Varies* | transactions         | Transactions[]         | Vector of transactions, for an example hexdump of the raw transaction format, see the [raw transaction section][raw transaction format].
