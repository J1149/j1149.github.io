---
title: 'Get Block Count'
image: '/docs/noun_591323.png'
---

The `getblockcount` RPC returns the number of blocks in the local best block chain.

*Parameters: none*

*Result---the number of blocks in the local best block chain*

{% include table_header.md
  n= "`result`"
  t= "number (int)"
  p= "Required<br>(exactly 1)"
  d= "The number of blocks in the local best block chain.  For a new node with only the hardcoded genesis block, this number will be 0"
%}

*Example*

```
pai-cli -testnet getblockcount
```

Result:

```
315280
```

*See also*

* `GetBlockHash`: returns the header hash of a block at the given height in the local best block chain.
* `GetBlock`: gets a block with a particular header hash from the local block database either as a JSON object or as a serialized block.
