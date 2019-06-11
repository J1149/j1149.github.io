---
layout: service
title: GetMemPoolEntry
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `getmempoolentry` RPC returns mempool data for given transaction (must be in mempool).

*Parameter #1---a transaction identifier (TXID)*

{% include table_header.md
  n= "TXID"
  t= "string (hex)"
  p= "Required (exactly 1)"
  d= "The TXID of the transaction. The TXID must be encoded as hex in RPC byte order"
%}

*Result ---a JSON object describing the transaction*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
|`result`  |object     | Required<br>(exactly 1) | A object containing transactions currently in the memory pool.  May be empty
|`size` | number (int) | Required<br>(exactly 1) | The size of the serialized transaction in bytes
| `fee`  | number (pai's) | Required<br>(exactly 1) | The transaction fee paid by the transaction in decimal pai's
| `modifiedfee` | number (pai's) | Required<br>(exactly 1) | The transaction fee with fee deltas used for mining priority in decimal pai's
| → <br>`time` | number (int) | Required<br>(exactly 1) | The time the transaction entered the memory pool, Unix epoch time format
| → <br>`height` | number (int) | Required<br>(exactly 1) | The block height when the transaction entered the memory pool
| → <br>`startingpriority` | number (int) | Required<br>(exactly 1) | The priority of the transaction when it first entered the memory pool
| → <br>`currentpriority` | number (int) | Required<br>(exactly 1) | The current priority of the transaction
| → <br>`descendantcount` | number (int) | Required<br>(exactly 1) | The number of in-mempool descendant transactions (including this one)
| → <br>`descendantsize` | number (int) | Required<br>(exactly 1) | The size of in-mempool descendants (including this one)
| → <br>`descendantfees` | number (int) | Required<br>(exactly 1) | The modified fees (see `modifiedfee` above) of in-mempool descendants (including this one)"
| → <br>`ancestorcount` | number (int) | Required<br>(exactly 1) | The number of in-mempool ancestor transactions (including this one)
| → <br>`ancestorsize` |  number (int) | Required<br>(exactly 1) | The size of in-mempool ancestors (including this one)
| → <br>`ancestorfees` |  number (int) | Required<br>(exactly 1) | The modified fees (see `modifiedfee` above) of in-mempool ancestors (including this one)
| → <br>`depends` | array | Required<br>(exactly 1) | An array holding TXIDs of unconfirmed transactions this transaction depends upon (parent transactions).  Those transactions must be part of a block before this transaction can be added to a block, although all transactions may be included in the same block.  The array may be empty
| → →<br>Depends TXID | string | Optional (0 or more) | The TXIDs of any unconfirmed transactions this transaction depends upon, encoded as hex in RPC byte order

*Example*

```
pai-cli getmempoolentry 52273e0ce6cf3452932cfbc1c517c0ce1af1\
d255fda67a6e3bd63ba1d908c8c2
```

Result:

```
{
    "size": 485,
    "fee": 0.00009700,
    "modifiedfee": 0.00009700,
    "time": 1479423635,
    "height": 439431,
    "startingpriority": 15327081.81818182,
    "currentpriority": 21536936.36363636,
    "descendantcount": 1,
    "descendantsize": 485,
    "descendantfees": 9700,
    "ancestorcount": 1,
    "ancestorsize": 485,
    "ancestorfees": 9700,
    "depends": [
    ]
}
```

*See also*

* `GetMemPoolAncestors`: returns all in-mempool ancestors for a transaction in the mempool.
* `GetMemPoolDescendants`: returns all in-mempool descendants for a transaction in the mempool.
* `GetRawMemPool`: returns all transaction identifiers (TXIDs) in the memory pool as a JSON array, or detailed information about each transaction in the memory pool as a JSON object.

