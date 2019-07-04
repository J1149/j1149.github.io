---
layout: service
title: GetMemPoolInfo
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `getmempoolinfo` RPC returns information about the node’s current transaction memory pool.

*Parameters: none*

*Result---information about the transaction memory pool*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
|`result`  |object | Required<br>(exactly 1) | A object containing information about the memory pool
| →<br>`size` | number (int) | Required<br>(exactly 1) | The number of transactions currently in the memory pool
| →<br>`bytes` | number (int) | Required<br>(exactly 1) | The total number of bytes in the transactions in the memory pool
| →<br>`usage` | number (int) | Required<br>(exactly 1) | Total memory usage for the mempool in bytes
| →<br>`maxmempool` | number (int) | Required<br>(exactly 1) | Maximum memory usage for the mempool in bytes
| →<br>`mempoolminfee` | number (int) | Required<br>(exactly 1) | The lowest fee per kilobyte paid by any transaction in the memory pool


*Example*

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

* `GetBlockChainInfo`: provides information about the current state of the block chain.
* `GetRawMemPool`: returns all transaction identifiers (TXIDs) in the memory pool as a JSON array, or detailed information about each transaction in the memory pool as a JSON object.
* `GetTxOutSetInfo`: returns statistics about the confirmed unspent transaction output (UTXO) set. Note that this call may take some time and that it only counts outputs from confirmed transactions—it does not count outputs from the memory pool.

