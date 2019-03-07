---
layout: default
title: GetMemPoolInfo
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetMemPoolInfo
========================

The `getmempoolinfo` RPC returns information about the node’s current transaction memory pool.

*Parameters: none*

*Result---information about the transaction memory pool*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "object"
  p: "Required<br>(exactly 1)"
  d: "A object containing information about the memory pool"

- n: "→<br>`size`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The number of transactions currently in the memory pool"

- n: "→<br>`bytes`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The total number of bytes in the transactions in the memory pool"

- n: "→<br>`usage`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "*Added in Pai Core 0.11.0*<br><br>Total memory usage for the mempool in bytes"

- n: "→<br>`maxmempool`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "*Added in Pai Core 0.12.0*<br><br>Maximum memory usage for the mempool in bytes"

- n: "→<br>`mempoolminfee`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "*Added in Pai Core 0.12.0*<br><br>The lowest fee per kilobyte paid by any transaction in the memory pool"

{% enditemplate %}

*Example from PAI Core 0.14.1*

```
pai-cli -testnet getmempoolinfo
```

Result:

```
{
  "size": 1237,
  "bytes": 591126,
  "usage": 1900416,
  "maxmempool": 300000000,
  "mempoolminfee": 0.00000000
}
```

*See also*

* `GetBlockChainInfo`:
* `GetRawMemPool`:
* `GetTxOutSetInfo`:
