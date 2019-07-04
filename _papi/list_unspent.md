---
layout: service
title: ListUnspent
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.*

The `listunspent` RPC returns an array of unspent transaction outputs belonging to this wallet.

*Parameter #1---the minimum number of confirmations an output must have*

{% include table_header.md
  n= "Minimum Confirmations"
  t= "number (int)"
  p= "Optional<br>(0 or 1)"
  d= "The minimum number of confirmations the transaction containing an output must have in order to be returned.  Use `0` to return outputs from unconfirmed transactions. Default is `1`"
%}

*Parameter #2---the maximum number of confirmations an output may have*

{% include table_header.md
  n= "Maximum Confirmations"
  t= "number (int)"
  p= "Optional<br>(0 or 1)"
  d= "The maximum number of confirmations the transaction containing an output may have in order to be returned.  Default is `9999999` (~10 million)"
%}

*Parameter #3---the addresses an output must pay*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| Addresses  | array | Optional<br>(0 or 1) | If present, only outputs which pay an address in this array will be returned
| →<br>Address | string (base58) | Required<br>(1 or more) | A P2PKH or P2SH address


*Result---the list of unspent outputs*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  | array | Required<br>(exactly 1) | An array of objects each describing an unspent output.  May be empty
| →<br>Unspent Output | object | Optional<br>(0 or more) | An object describing a particular unspent output belonging to this wallet
| → →<br>`txid` | string (hex) | Required<br>(exactly 1) | The TXID of the transaction containing the output, encoded as hex in RPC byte order
| → →<br>`vout` | number (int) | Required<br>(exactly 1) | The output index number (vout) of the output within its containing transaction
| → →<br>`address` | string (base58) | Optional<br>(0 or 1) | The P2PKH or P2SH address the output paid.  Only returned for P2PKH or P2SH output scripts
| → →<br>`account` | string | Optional<br>(0 or 1) | If the address returned belongs to an account, this is the account.  Otherwise not returned
| → →<br>`scriptPubKey` | string (hex) | Required<br>(exactly 1) | The output script paid, encoded as hex
| → →<br>`redeemScript` | string (hex) | Optional<br>(0 or 1) | If the output is a P2SH whose script belongs to this wallet, this is the redeem script
| → →<br>`amount` | number (int) | Required<br>(exactly 1) | The amount paid to the output in pai's
| → →<br>`confirmations` | number (int) | Required<br>(exactly 1) | The number of confirmations received for the transaction containing this output
| → →<br>`spendable` | bool | Required<br>(exactly 1) | Set to `true` if the private key or keys needed to spend this output are part of the wallet.  Set to `false` if not (such as for watch-only addresses)
| → →<br>`solvable` | bool | Required<br>(exactly 1) | Set to `true` if the wallet knows how to spend this output.  Set to `false` if the wallet does not know how to spend the output.  It is ignored if the private keys are available


*Example*

Get all outputs confirmed at least 6 times for a particular
address:

```
pai-cli -testnet listunspent 6 99999999 '''
  [
    "mgnucj8nYqdrPFh2JfZSB1NmUThUGnmsqe"
  ]
'''
```

Result:

```
[
    {
        "txid" : "d54994ece1d11b19785c7248868696250ab195605b469632b7bd68130e880c9a",
        "vout" : 1,
        "address" : "mgnucj8nYqdrPFh2JfZSB1NmUThUGnmsqe",
        "account" : "test label",
        "scriptPubKey" : "76a9140dfc8bafc8419853b34d5e072ad37d1a5159f58488ac",
        "amount" : 0.00010000,
        "confirmations" : 6210,
        "spendable" : true,
        "solvable" : true
    }
]
```

*See also*

* `ListTransactions`: returns the most recent transactions that affect the wallet.
* `LockUnspent`: temporarily locks or unlocks specified transaction outputs. A locked transaction output will not be chosen by automatic coin selection when spending pai's. Locks are stored in memory only, so nodes start with zero locked outputs and the locked output list is always cleared when a node stops or fails.
