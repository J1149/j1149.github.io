---
layout: service
title: GetRawMemPool
parent: PAI Core Apis
grand_parent: Developer Reference
---

The `getrawmempool` RPC returns all transaction identifiers (TXIDs) in the memory pool as a JSON array, or detailed information about each transaction in the memory pool as a JSON object.

*Parameter---desired output format*

{% include table_header.md
  n= "Format"
  t= "bool"
  p= "Optional<br>(0 or 1)"
  d= "Set to `true` to get verbose output describing each transaction in the memory pool; set to `false` (the default) to only get an array of TXIDs for transactions in the memory pool"
%}

*Result (format `false`)---an array of TXIDs*

{% include table_header.md
  n= "`result`"
  t= "array"
  p= "Required<br>(exactly 1)"
  d= "An array of TXIDs belonging to transactions in the memory pool.  The array may be empty if there are no transactions in the memory pool"
%}

{% include table_content.md
  n= "→<br>TXID"
  t= "string"
  p= "Optional<br>(0 or more)"
  d= "The TXID of a transaction in the memory pool, encoded as hex in RPC byte order"
%}

*Result (format: `true`)---a JSON object describing each transaction*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  | object | Required<br>(exactly 1) | A object containing transactions currently in the memory pool.  May be empty
| →<br>TXID | string : object | Optional<br>(0 or more) | The TXID of a transaction in the memory pool, encoded as hex in RPC byte order
| → →<br>`size` | number (int) | Required<br>(exactly 1) | The size of the serialized transaction in bytes
| → →<br>`fee` | number (pai's) | Required<br>(exactly 1) | The transaction fee paid by the transaction in decimal pai's
| → →<br>`modifiedfee` | number (pai's) | Required<br>(exactly 1) | The transaction fee with fee deltas used for mining priority in decimal pai's
| → →<br>`time` | number (int) | Required<br>(exactly 1) | The time the transaction entered the memory pool, Unix epoch time format
| → →<br>`height` | number (int) | Required<br>(exactly 1) | The block height when the transaction entered the memory pool
| → →<br>`descendantcount` | number (int) | Required<br>(exactly 1) | The number of in-mempool descendant transactions (including this one)
| → →<br>`descendantsize` | number (int) | Required<br>(exactly 1) | The size of in-mempool descendants (including this one)
| → →<br>`descendantfees` | number (int) | Required<br>(exactly 1) | The modified fees (see `modifiedfee` above) of in-mempool descendants (including this one)
| → →<br>`ancestorcount` | number (int) | Required<br>(exactly 1) | The number of in-mempool ancestor transactions (including this one)
| → →<br>`ancestorsize` | number (int) | Required<br>(exactly 1) | The size of in-mempool ancestors (including this one)
| → →<br>`ancestorfees` | number (int) | Required<br>(exactly 1) | The modified fees (see `modifiedfee` above) of in-mempool ancestors (including this one)
| → →<br>`depends` | array | Required<br>(exactly 1) | An array holding TXIDs of unconfirmed transactions this transaction depends upon (parent transactions).  Those transactions must be part of a block before this transaction can be added to a block, although all transactions may be included in the same block.  The array may be empty
| → → →<br>Depends TXID | string | Optional (0 or more) | The TXIDs of any unconfirmed transactions this transaction depends upon, encoded as hex in RPC byte order


*Examples*

The default (`false`):

```
pai-cli getrawmempool
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
pai-cli getrawmempool true
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

* `GetMemPoolInfo`: returns information about the node’s current transaction memory pool.
* `GetMemPoolEntry`: returns mempool data for given transaction (must be in mempool).
* `GetTxOutSetInfo`: returns statistics about the confirmed unspent transaction output (UTXO) set. Note that this call may take some time and that it only counts outputs from confirmed transactions—it does not count outputs from the memory pool.

