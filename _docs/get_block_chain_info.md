---
title: 'Get Block Chain Info'
image: '/docs/noun_591323.png'
---

The `getblockchaininfo` RPC provides information about the current state of the block chain.

*Parameters: none*

*Result---A JSON object providing information about the block chain*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
|`result`  |object | Required<br>(exactly 1) | Information about the current state of the local block chain
| →<br>`chain` | string | Required<br>(exactly 1) | The name of the block chain.  One of `main` for mainnet, `test` for testnet, or `regtest`<!--noref--> for regtest
| →<br>`blocks` | number(int) | Required<br>(exactly 1) | The number of validated blocks in the local best block chain.  For a new node with just the hardcoded genesis block, this will be 0
| →<br>`headers` | number(int) | Required<br>(exactly 1) | The number of validated headers in the local best headers chain.  For a new node with just the hardcoded genesis block, this will be zero.  This number may be higher than the number of *blocks*
| →<br>`bestblockhash` | string(hex) | Required<br>(exactly 1) | The hash of the header of the highest validated block in the best block chain, encoded as hex in RPC byte order.  This is identical to the string returned by the `getbestblockhash` RPC
| →<br>`difficulty` | number(real) | Required<br>(exactly 1) | The difficulty of the highest-height block in the best block chain
| →<br>`mediantime` | number(int) | Required<br>(exactly 1) | The median time of the 11 blocks before the most recent block on the blockchain.  Used for validating transaction locktime under BIP113
| →<br>`verificationprogress` | number(real) | Required<br>(exactly 1) | Estimate of what percentage of the block chain transactions have been verified so far, starting at 0.0 and increasing to 1.0 for fully verified.  May slightly exceed 1.0 when fully synced to account for transactions in the memory pool which have been verified before being included in a block
| →<br>`chainwork` | string(hex) | Required<br>(exactly 1) | The estimated number of block header hashes checked from the genesis block to this block, encoded as big-endian hex
| →<br>`pruned` | bool | Required<br>(exactly 1) | Indicates if the blocks are subject to pruning
| →<br>`pruneheight` | number(int) | Optional<br>(0 or 1) | The lowest-height complete block stored if prunning is activated
| →<br>`softforks` | array | Required<br>(exactly 1) | An array of objects each describing a current or previous soft fork
| → →<br>Softfork | object | Required<br>(3 or more) | A specific softfork
| → → →<br>`id` | string | Required<br>(exactly 1) | The name of the softfork
| → → →<br>`version` | numeric<br>(int) | Required<br>(exactly 1) | The block version used for the softfork
| → → →<br>`enforce` | string = object | Optional<br>(0 or 1) | The progress toward enforcing the softfork rules for new-version blocks
| → → → →<br>`status` | bool | Required<br>(exactly 1) | Indicates if the threshold was reached
| → → → →<br>`found` | numeric<br>(int) | Optional<br>(0 or 1) | Number of blocks that support the softfork
| → → → →<br>`required` | numeric<br>(int) | Optional<br>(0 or 1) | Number of blocks that are required to reach the threshold
| → → → →<br>`window` | numeric<br>(int) | Optional<br>(0 or 1) | The maximum size of examined window of recent blocks
| → → →<br>`reject` | object | Optional<br>(0 or 1) | The progress toward enforcing the softfork rules for new-version blocks
| → → → →<br>`status` | bool | Optional<br>(0 or 1) | Indicates if the threshold was reached
| → → → →<br>`found` | numeric<br>(int) | Optional<br>(0 or 1) | Number of blocks that support the softfork
| → → → →<br>`required` | numeric<br>(int) | Optional<br>(0 or 1) | Number of blocks that are required to reach the threshold
| → → → →<br>`window` | numeric<br>(int) | Optional<br>(0 or 1) | The maximum size of examined window of recent blocks
| →<br>`bip9_softforks` | object | Required<br>(exactly 1) | The status of BIP9 softforks in progress
| → →<br>Name | string : object | Required<br>(2 or more) | A specific BIP9 softfork
| → → →<br>`status` | string | Required<br>(exactly 1) | Set to one of the following reasons=<br>• `defined` if voting hasn't started yet<br>• `started` if the voting has started <br>• `locked_in` if the voting was successful but the softfort hasn't been activated yet<br>• `active` if the softfork was activated<br>• `failed` if the softfork has not receieved enough votes
| → → →<br>`bit` | numeric<br>(int) | Optional<br>(0 or 1) | The bit (0-28) in the block version field used to signal this softfork.  Field is only shown when status is `started`
| → → →<br>`startTime` | numeric<br>(int) | Required<br>(exactly 1) | The Unix epoch time when the softfork voting begins
| → → →<br>`timeout` | numeric<br>(int) | Required<br>(exactly 1) | The Unix epoch time at which the deployment is considered failed if not yet locked in
| → → →<br>`since` | numeric<br>(int) | Required<br>(exactly 1) | The height of the first block to which the status applies


*Example*

```
pai-cli getblockchaininfo
```

Result:

```
{
  "chain": "main",
  "blocks": 464562,
  "headers": 464562,
  "bestblockhash": "00000000000000000085bd56990c579a36bade6ea427646612f13476edb30ceb",
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
