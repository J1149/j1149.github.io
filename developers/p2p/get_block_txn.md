---
layout: default
title: GetBlockTxn
parent: Developer Reference
nav_order: 4
---

GetBlockTxn
============

The `getblocktxn` message is defined as a message containing a serialized 
`BlockTransactionsRequest` message. Upon receipt of a properly-formatted `getblocktxn` message, 
nodes which recently provided the sender of such a message a `cmpctblock` message for the 
block hash identified in this message must respond with either an appropriate `blocktxn` message, 
or a full block message. 

A `blocktxn` message response must contain exactly and only each transaction 
which is present in the appropriate block at the index specified in the `getblocktxn` message
indexes list, in the order requested.

The structure of `BlockTransactionsRequest` is defined below.

| Bytes    | Name                 | Data Type              | Description
|----------|----------------------|------------------------|----------------
| 32       | block hash           | binary blob            | The blockhash of the block which the transactions being requested are in.
| *Varies* | indexes length       | compactSize uint       | The number of transactions being requested.
| *Varies* | indexes              | compactSize uint[]     | Vector of compactSize containing the indexes of the transactions being requested in the block. **In version 2 of compact blocks, the *wtxid* should be used instead of the *txid* as defined by *BIP141***
