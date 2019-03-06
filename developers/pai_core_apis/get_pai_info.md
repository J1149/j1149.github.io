---
layout: default
title: GetPaiInfo
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetPaiInfo
========================

The `getpaiinfo` RPC provides information about the current state of the pai.

*Parameters: none*

*Result---A JSON object providing information about the PAI*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "object"
  p: "Required<br>(exactly 1)"
  d: "Information about the current state of the local PAI"

- n: "→<br>`chain`"
  t: "string"
  p: "Required<br>(exactly 1)"
  d: "The name of the PAI.  One of `main` for mainnet, `test` for testnet, or `regtest`<!--noref--> for regtest"

- n: "→<br>`pais`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The number of validated pais in the local best PAI.  For a new node with just the hardcoded genesis pai, this will be 0"

- n: "→<br>`headers`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The number of validated headers in the local best headers chain.  For a new node with just the hardcoded genesis pai, this will be zero.  This number may be higher than the number of *pais*"

- n: "→<br>`bestpaihash`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The hash of the header of the highest validated pai in the best PAI, encoded as hex in RPC byte order.  This is identical to the string returned by the `getbestpaihash` RPC"

- n: "→<br>`difficulty`"
  t: "number (real)"
  p: "Required<br>(exactly 1)"
  d: "The difficulty of the highest-height pai in the best PAI"

- n: "→<br>`mediantime`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "*Added in pai Core 0.12.0*<br><br>The median time of the 11 pais before the most recent pai on the PAI.  Used for validating transaction locktime under BIP113"
  
- n: "→<br>`verificationprogress`"
  t: "number (real)"
  p: "Required<br>(exactly 1)"
  d: "Estimate of what percentage of the PAI transactions have been verified so far, starting at 0.0 and increasing to 1.0 for fully verified.  May slightly exceed 1.0 when fully synced to account for transactions in the memory pool which have been verified before being included in a pai"

- n: "→<br>`chainwork`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The estimated number of pai header hashes checked from the genesis pai to this pai, encoded as big-endian hex"

- n: "→<br>`pruned`"
  t: "bool"
  p: "Required<br>(exactly 1)"
  d: "*Added in pai Core 0.11.0*<br><br>Indicates if the pais are subject to pruning"
  
- n: "→<br>`pruneheight`"
  t: "number (int)"
  p: "Optional<br>(0 or 1)"
  d: "*Added in pai Core 0.11.0*<br><br>The lowest-height complete pai stored if prunning is activated"
  
- n: "→<br>`softforks`"
  t: "array"
  p: "Required<br>(exactly 1)"
  d: "*Added in pai Core 0.12.0*<br><br>An array of objects each describing a current or previous soft fork"

- n: "→ →<br>Softfork"
  t: "object"
  p: "Required<br>(3 or more)"
  d: "A specific softfork"
  
- n: "→ → →<br>`id`"
  t: "string"
  p: "Required<br>(exactly 1)"
  d: "The name of the softfork"
  
- n: "→ → →<br>`version`"
  t: "numeric<br>(int)"
  p: "Required<br>(exactly 1)"
  d: "The pai version used for the softfork"
  
- n: "→ → →<br>`enforce`"
  t: "string : object"
  p: "Optional<br>(0 or 1)"
  d: "The progress toward enforcing the softfork rules for new-version pais"

- n: "→ → → →<br>`status`"
  t: "bool"
  p: "Required<br>(exactly 1)"
  d: "Indicates if the threshold was reached"
  
- n: "→ → → →<br>`found`"
  t: "numeric<br>(int)"
  p: "Optional<br>(0 or 1)"
  d: "Number of pais that support the softfork"
  
- n: "→ → → →<br>`required`"
  t: "numeric<br>(int)"
  p: "Optional<br>(0 or 1)"
  d: "Number of pais that are required to reach the threshold"

- n: "→ → → →<br>`window`"
  t: "numeric<br>(int)"
  p: "Optional<br>(0 or 1)"
  d: "The maximum size of examined window of recent pais"

- n: "→ → →<br>`reject`"
  t: "object"
  p: "Optional<br>(0 or 1)"
  d: "The progress toward enforcing the softfork rules for new-version pais"

- n: "→ → → →<br>`status`"
  t: "bool"
  p: "Optional<br>(0 or 1)"
  d: "Indicates if the threshold was reached"
  
- n: "→ → → →<br>`found`"
  t: "numeric<br>(int)"
  p: "Optional<br>(0 or 1)"
  d: "Number of pais that support the softfork"
  
- n: "→ → → →<br>`required`"
  t: "numeric<br>(int)"
  p: "Optional<br>(0 or 1)"
  d: "Number of pais that are required to reach the threshold"

- n: "→ → → →<br>`window`"
  t: "numeric<br>(int)"
  p: "Optional<br>(0 or 1)"
  d: "The maximum size of examined window of recent pais"
  
- n: "→<br>`bip9_softforks`"
  t: "object"
  p: "Required<br>(exactly 1)"
  d: "*Added in pai Core 0.12.1*<br><br>The status of BIP9 softforks in progress"
  
- n: "→ →<br>Name"
  t: "string : object"
  p: "Required<br>(2 or more)"
  d: "A specific BIP9 softfork"
  
- n: "→ → →<br>`status`"
  t: "string"
  p: "Required<br>(exactly 1)"
  d: "Set to one of the following reasons:<br>• `defined` if voting hasn't started yet<br>• `started` if the voting has started <br>• `locked_in` if the voting was successful but the softfort hasn't been activated yet<br>• `active` if the softfork was activated<br>• `failed` if the softfork has not receieved enough votes"
  
- n: "→ → →<br>`bit`"
  t: "numeric<br>(int)"
  p: "Optional<br>(0 or 1)"
  d: "The bit (0-28) in the pai version field used to signal this softfork.  Field is only shown when status is `started`"
  
- n: "→ → →<br>`startTime`"
  t: "numeric<br>(int)"
  p: "Required<br>(exactly 1)"
  d: "The Unix epoch time when the softfork voting begins"
  
- n: "→ → →<br>`timeout`"
  t: "numeric<br>(int)"
  p: "Required<br>(exactly 1)"
  d: "The Unix epoch time at which the deployment is considered failed if not yet locked in"
  
- n: "→ → →<br>`since`"
  t: "numeric<br>(int)"
  p: "Required<br>(exactly 1)"
  d: "*Added in pai Core 0.14.0*<br><br>The height of the first pai to which the status applies"
  
{% enditemplate %}

*Example from pai Core 0.14.1*

```
pai-cli getpaiinfo
```

Result:

```
{
  "chain": "main",
  "PAIs": 464562,
  "headers": 464562,
  "bestpaihash": "00000000000000000085bd56990c579a36bade6ea427646612f13476edb30ceb",
  "difficulty": 521974519553.6282,
  "mediantime": 1493758169,
  "verificationprogress": 0.999989733170878,
  "chainwork": "00000000000000000000000000000000000000000052c26f32ffa22706efd28c",
  "pruned": false,
  "softforks": [
    {
      "id": "bip34",
      "version": 2,
      "reject": {
        "status": true
      }
    },
    {
      "id": "bip66",
      "version": 3,
      "reject": {
        "status": true
      }
    },
    {
      "id": "bip65",
      "version": 4,
      "reject": {
        "status": true
      }
    }
  ],
  "bip9_softforks": {
    "csv": {
      "status": "active",
      "startTime": 1462060800,
      "timeout": 1493596800,
      "since": 419328
    },
    "segwit": {
      "status": "started",
      "bit": 1,
      "startTime": 1479168000,
      "timeout": 1510704000,
      "since": 439488
    }
  }
}

```

*See also*

* `GetMiningInfo`: returns various mining-related information.
* `GetNetworkInfo`: returns information about the node’s connection to the network.
* `GetWalletInfo`: provides information about the wallet.
