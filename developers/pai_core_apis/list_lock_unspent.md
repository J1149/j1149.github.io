---
layout: default
title: ListLockUnspent
parent: PAI Core Apis
grand_parent: Developer Reference
---

ListLockUnspent
========================

*Requires wallet support.*

The `listlockunspent` RPC returns a list of temporarily unspendable (locked) outputs.

*Parameters: none*

*Result---an array of locked outputs*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "array"
  p: "Required<br>(exactly 1)"
  d: "An array containing all locked outputs.  May be empty"

- n: "→<br>Output"
  t: "object"
  p: "Optional<br>(1 or more)"
  d: "An object describing a particular locked output"

- n: "→ →<br>`txid`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The TXID of the transaction containing the locked output, encoded as hex in RPC byte order"

- n: "→ →<br>`vout`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The output index number (vout) of the locked output within the transaction.  Output index `0` is the first output within the transaction"

{% enditemplate %}

*Example from Pai Core 0.10.0*

```
pai-cli -testnet listlockunspent
```

Result:

```
[
    {
        "txid" : "ca7cb6a5ffcc2f21036879493db4530c0ce9b5bff9648f9a3be46e2dfc8e0166",
        "vout" : 0
    }
]
```

*See also*

* `LockUnspent`: temporarily locks or unlocks specified transaction outputs. A locked transaction output will not be chosen by automatic coin selection when spending pai's. Locks are stored in memory only, so nodes start with zero locked outputs and the locked output list is always cleared when a node stops or fails.
