---
layout: service
title: LockUnspent
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.*

The `lockunspent` RPC temporarily locks or unlocks specified transaction outputs. A locked transaction output will not be chosen by automatic coin selection when spending pai's. Locks are stored in memory only, so nodes start with zero locked outputs and the locked output list is always cleared when a node stops or fails.

*Parameter #1---whether to lock or unlock the outputs*

{% include table_header.md
  n= "Unlock"
  t= "bool"
  p= "Required<br>(exactly 1)"
  d= "Set to `false` to lock the outputs specified in the following parameter.  Set to `true` to unlock the outputs specified.  If this is the only argument specified and it is set to `true`, all outputs will be unlocked; if it is the only argument and is set to `false`, there will be no change"
%}

*Parameter #2---the outputs to lock or unlock*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| Outputs  | array | Optional<br>(0 or 1) | An array of outputs to lock or unlock
| →<br>Output | object | Required<br>(1 or more) | An object describing a particular output
| → →<br>`txid` | string | Required<br>(exactly 1) | The TXID of the transaction containing the output to lock or unlock, encoded as hex in internal byte order
| → →<br>`vout` | number (int) | Required<br>(exactly 1) | The output index number (vout) of the output to lock or unlock.  The first output in a transaction has an index of `0`


*Result---`true` if successful*

{% include table_header.md
  n= "`result`"
  t= "bool"
  p= "Required<br>(exactly 1)"
  d= "Set to `true` if the outputs were successfully locked or unlocked.  If the outputs were already locked or unlocked, it will also return `true`"
%}

*Example*

Lock two outputs:

```
pai-cli -testnet lockunspent false '''
  [
    {
      "txid": "5a7d24cd665108c66b2d56146f244932edae4e2376b561b3d396d5ae017b9589",
      "vout": 0
    },
    {
      "txid": "6c5edd41a33f9839257358ba6ddece67df9db7f09c0db6bbea00d0372e8fe5cd",
      "vout": 0
    }
  ]
'''
```

Result:

```
true
```

Verify the outputs have been locked:

```
pai-cli -testnet listlockunspent
```

Result

```
[
  {
    "txid": "5a7d24cd665108c66b2d56146f244932edae4e2376b561b3d396d5ae017b9589",
    "vout": 0
  },
  {
    "txid": "6c5edd41a33f9839257358ba6ddece67df9db7f09c0db6bbea00d0372e8fe5cd",
    "vout": 0
  }
]
```

Unlock one of the above outputs:

```
pai-cli -testnet lockunspent true '''
[
  {
    "txid": "5a7d24cd665108c66b2d56146f244932edae4e2376b561b3d396d5ae017b9589",
    "vout": 0
  }
]
'''
```

Result:

```
true
```

Verify the output has been unlocked:

```
pai-cli -testnet listlockunspent
```

Result:

```
[
  {
    "txid": "6c5edd41a33f9839257358ba6ddece67df9db7f09c0db6bbea00d0372e8fe5cd",
    "vout": 0
  }
]
```

*See also*

* `ListLockUnspent`: returns a list of temporarily unspendable (locked) outputs.
* `ListUnspent`: returns an array of unspent transaction outputs belonging to this wallet.

