---
title: 'Get Chain Tips'
image: '/docs/noun_591323.png'
---

The `getchaintips` RPC returns information about the highest-height block (tip) of each local block chain.

*Parameters: none*

*Result---an array of block chain tips*

{% include table_header.md
  n= "`result`"
  t= "array"
  p= "Required<br>(exactly 1)"
  d= "An array of JSON objects, with each object describing a chain tip.  At least one tip---the local best block chain---will always be present"
%}

{% include table_content.md
  n= "→<br>Tip"
  t= "object"
  p= "Required<br>(1 or more)"
  d= "An object describing a particular chain tip.  The first object will always describe the active chain (the local best block chain)"
%}

{% include table_content.md
  n= "→ →<br>`height`"
  t= "number (int)"
  p= "Required<br>(exactly 1)"
  d= "The height of the highest block in the chain.  A new node with only the genesis block will have a single tip with height of 0"
%}

{% include table_content.md
  n= "→ →<br>`hash`"
  t= "string (hex)"
  p= "Required<br>(exactly 1)"
  d= "The hash of the highest block in the chain, encoded as hex in RPC byte order"
%}

{% include table_content.md
  n= "→ →<br>`branchlen`"
  t= "number (int)"
  p= "Required<br>(exactly 1)"
  d= "The number of blocks that are on this chain but not on the main chain.  For the local best block chain, this will be `0`; for all other chains, it will be at least `1`"
%}

{% include table_content.md
  n= "→ →<br>`status`"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The status of this chain.  Valid values are <br>• `active` for the local best block chain<br>• `invalid` for a chain that contains one or more invalid blocks<br>• `headers-only`<!--noref--> for a chain with valid headers whose corresponding blocks both haven't been validated and aren't stored locally<br>• `valid-headers` for a chain with valid headers whose corresponding blocks are stored locally, but which haven't been fully validated<br>• `valid-fork` for a chain which is fully validated but which isn't part of the local best block chain (it was probably the local best block chain at some point)<br>• `unknown` for a chain whose reason for not being the active chain is unknown"
%}

*Example*

```
pai-cli -testnet getchaintips
```

```
[
    {
        "height" : 312647,
        "hash" : "000000000b1be96f87b31485f62c1361193304a5ad78acf47f9164ea4773a843",
        "branchlen" : 0,
        "status" : "active"
    },
    {
        "height" : 282072,
        "hash" : "00000000712340a499b185080f94b28c365d8adb9fc95bca541ea5e708f31028",
        "branchlen" : 5,
        "status" : "valid-fork"
    },
    {
        "height" : 281721,
        "hash" : "000000006e1f2a32199629c6c1fbd37766f5ce7e8c42bab0c6e1ae42b88ffe12",
        "branchlen" : 1,
        "status" : "valid-headers"
    },
]
```

*See also*

* `GetBestBlockHash`: returns the header hash of the most recent block on the best block chain.
* `GetBlock`:  gets a block with a particular header hash from the local block database either as a JSON object or as a serialized block.
* `GetBlockChainInfo`: provides information about the current state of the block chain.
