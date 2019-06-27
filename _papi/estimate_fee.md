---
title: 'Estimate Fee'
image: '/docs/noun_591323.png'
---

The `estimatefee` RPC estimates the transaction fee per kilobyte that needs to be paid for a transaction to be included within a certain number of blocks.

*Parameter #1---how many blocks the transaction may wait before being included*

| Name    | Type       | Presence                | Description
|---------|------------|-------------------------|-------------
|Blocks | number (int) | Required<br>(exactly 1) | The maximum number of blocks a transaction should have to wait before it is predicted to be included in a block. Has to be between 2 and 25 blocks 

*Result---the fee the transaction needs to pay per kilobyte*

| Name    | Type   | Presence                        | Description
|---------|--------|---------------------------------|-------------
|`result` | number (pai's) | Required<br>(exactly 1) | The estimated fee the transaction should pay in order to be included within the specified number of blocks.  If the node doesn't have enough information to make an estimate, the value `-1` will be returned

*Examples*

```
pai-cli estimatefee 6
```

Result:

```
0.00162556
```

Requesting data the node can't calculate (out of range):

```
pai-cli estimatefee 100
```

Result:

```
-1
```

*See also*

* `SetTxFee`: sets the transaction fee per kilobyte paid by transactions created by this wallet.
