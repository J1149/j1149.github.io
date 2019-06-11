---
layout: service
title: ListLockUnspent
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.*

The `listlockunspent` RPC returns a list of temporarily unspendable (locked) outputs.

*Parameters: none*

*Result---an array of locked outputs*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  | array | Required<br>(exactly 1) | An array containing all locked outputs.  May be empty
| →<br>Output | object | Optional<br>(1 or more) | An object describing a particular locked output
| → →<br>`txid` | string (hex) | Required<br>(exactly 1) | The TXID of the transaction containing the locked output, encoded as hex in RPC byte order
| → →<br>`vout` | number (int) | Required<br>(exactly 1) | The output index number (vout) of the locked output within the transaction.  Output index `0` is the first output within the transaction


*Example*

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
