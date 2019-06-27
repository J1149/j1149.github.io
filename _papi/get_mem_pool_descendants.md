---
layout: service
title: GetMemPoolDescendants
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `getmempooldescendants` RPC returns all in-mempool descendants for a transaction in the mempool.

*Parameter #1---a transaction identifier (TXID)*

{% include table_header.md
  n= "TXID"
  t= "string (hex)"
  p= "Required<br>(exactly 1)"
  d= "The TXID of the transaction. The TXID must be encoded as hex in RPC byte order"
%}

*Parameter #2---desired output format*

{% include table_header.md
  n= "Format"
  t= "bool"
  p= "Optional<br>(0 or 1)"
  d= "Set to `true` to get json objects describing each transaction in the memory pool; set to `false` (the default) to only get an array of TXIDs"
%}

*Result---list of descendant transactions*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
|`result`  |array     | Required<br>(exactly 1) | An array of TXIDs belonging to transactions in the memory pool.  The array may be empty if there are no transactions in the memory pool
|→<br>TXID | string | Optional<br>(0 or more) | The TXID of a transaction in the memory pool, encoded as hex in RPC byte order
| `result` | object | equired<br>(exactly 1) | A object containing transactions currently in the memory pool.  May be empty
| →<br>TXID | string : object | Optional<br>(0 or more) | The TXID of a transaction in the memory pool, encoded as hex in RPC byte order
| → →<br>`size` | number (int) | Required<br>(exactly 1) | The size of the serialized transaction in bytes
| → →<br>`fee` | number (pai's) | Required<br>(exactly 1) | The transaction fee paid by the transaction in decimal pai's
| → →<br>`modifiedfee` | number (pai's) | Required<br>(exactly 1) | The transaction fee with fee deltas used for mining priority in decimal pai's
| → →<br>`time` | number (int) | Required<br>(exactly 1) | The time the transaction entered the memory pool, Unix epoch time format
| → →<br>`height` | number (int) | Required<br>(exactly 1) | The block height when the transaction entered the memory pool
| → →<br>`startingpriority` | number (int) | Required<br>(exactly 1) | The priority of the transaction when it first entered the memory pool
| → →<br>`currentpriority` | number (int) | Required<br>(exactly 1) | The current priority of the transaction
| → →<br>`descendantcount` | number (int) | Required<br>(exactly 1) | The number of in-mempool descendant transactions (including this one)
| → →<br>`descendantsize` | number (int) | Required<br>(exactly 1) | The size of in-mempool descendants (including this one)
| → →<br>`descendantfees` | number (int) | Required<br>(exactly 1) | The modified fees (see `modifiedfee` above) of in-mempool descendants (including this one)
| → →<br>`ancestorcount` | number (int) | Required<br>(exactly 1) | The number of in-mempool ancestor transactions (including this one)
| → →<br>`ancestorsize` | number (int) | Required<br>(exactly 1) | he size of in-mempool ancestors (including this one)
| → →<br>`ancestorfees` | number (int) | Required<br>(exactly 1) | The modified fees (see `modifiedfee` above) of in-mempool ancestors (including this one)
| → →<br>`depends` | array | Required<br>(exactly 1) | An array holding TXIDs of unconfirmed transactions this transaction depends upon (parent transactions).  Those transactions must be part of a block before this transaction can be added to a block, although all transactions may be included in the same block.  The array may be empty
| → → →<br>Depends TXID | string | Optional (0 or more) | The TXIDs of any unconfirmed transactions this transaction depends upon, encoded as hex in RPC byte order

*Result (format: `true`)---a JSON object describing each transaction*


*Example*

The default (`false`):

```
pai-cli getmempooldescendants 52273e0ce6cf3452932cfbc1c517c0\
ce1af1d255fda67a6e3bd63ba1d908c8c2
```

Result:

```
[
    "b104586f229e330caf42c475fd52684e9eb5e2d02f0fcd216d9554c5347b0873",
    "094f7dcbc7494510d4daeceb2941ed73b1bd011bf527f6c3b7c897fee85c11d4"
]
```

Verbose output (`true`):

```
pai-cli getmempooldescendants 52273e0ce6cf3452932cfbc1c517c0\
ce1af1d255fda67a6e3bd63ba1d908c8c2 true
```

Result:

```
{
  "b104586f229e330caf42c475fd52684e9eb5e2d02f0fcd216d9554c5347b0873": {
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
  },
  "094f7dcbc7494510d4daeceb2941ed73b1bd011bf527f6c3b7c897fee85c11d4": {
    "size": 554,
    "fee": 0.00005540,
    "modifiedfee": 0.00005540,
    "time": 1479423327,
    "height": 439430,
    "startingpriority": 85074.91071428571,
    "currentpriority": 3497174.4375,
    "descendantcount": 1,
    "descendantsize": 554,
    "descendantfees": 5540,
    "ancestorcount": 1,
    "ancestorsize": 554,
    "ancestorfees": 5540,
    "depends": [
    ]
  }
}
```

*See also*

* `GetMemPoolAncestors`: returns all in-mempool ancestors for a transaction in the mempool.
* `GetRawMemPool`: returns all transaction identifiers (TXIDs) in the memory pool as a JSON array, or detailed information about each transaction in the memory pool as a JSON object.
