---
title: 'Get Block Template'
image: '/docs/noun_591323.png'
---

The `getblocktemplate` RPC gets a block template or proposal for use with mining software. For more information, please see the following resources:

* `PAI` 
* `BIP22`
* `BIP23`

*See also*

* `GetMiningInfo`: returns various mining-related information.
* `SubmitBlock`: accepts a block, verifies it is a valid addition to the block chain, and broadcasts it to the network. Extra parameters are ignored by pai Core but may be used by mining pools or other programs.
* `PrioritiseTransaction`: adds virtual priority or fee to a transaction, allowing it to be accepted into blocks mined by this node (or miners which use this node) with a lower priority or fee. (It can also remove virtual priority or fee, requiring the transaction have a higher priority or fee to be accepted into a locally-mined block.)
