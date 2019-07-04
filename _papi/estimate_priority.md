---
title: 'Estimate Priority'
image: '/docs/noun_591323.png'
---

The `estimatepriority` RPC estimates the priority (coin age) that a transaction needs in order to be included within a certain number of blocks as a free high-priority transaction. This should not to be confused with the prioritisetransaction RPC which will remain supported for adding fee deltas to transactions.

Transaction priority is relative to a transaction's byte size.

*Parameter #1---how many blocks the transaction may wait before being included as a free high-priority transaction*

| Name    | Type   | Presence                | Description
|---------|--------|-------------------------|-------------
|Blocks | number (int) | Required<br>(exactly 1) | The maximum number of blocks a transaction should have to wait before it is predicted to be included in a block based purely on its priority 


*Result---the priority a transaction needs*

| Name    | Type   | Presence                | Description
|---------|--------|-------------------------|-------------
|`result` | number (real) | Required<br>(exactly 1) | The estimated priority the transaction should have in order to be included within the specified number of blocks.  If the node doesn't have enough information to make an estimate, the value `-1` will be returned


*Examples*

```
pai-cli estimatepriority 6
```

Result:

```
718158904.10958910
```

Requesting data the node can't calculate yet:

```
pai-cli estimatepriority 100
```

Result:

```
-1.00000000
```

*See also*

* `EstimateFee`: estimates the transaction fee per kilobyte that needs to be paid for a transaction to be included within a certain number of PAIs
