---
layout: default
title: GetBestBlockHash
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetBestBlockHash
========================

The `getbestblockhash` RPC returns the header hash of the most recent block on the best block chain.

*Parameters: none*

*Result---hash of the tip from the best block chain*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The hash of the block header from the most recent block on the best block chain, encoded as hex in RPC byte order"

{% enditemplate %}

*Example from PAI Core 0.10.0*

```
pai-cli -testnet getbestblockhash
```

Result:

```
0000000000075c58ed39c3e50f99b32183d090aefa0cf8c324a82eea9b01a887
```

*See also*

* `GetBlock`: gets a block with a particular header hash from the local block database either as a JSON object or as a serialized block.
* `GetBlockHash`: returns the header hash of a block at the given height in the local best block chain.

