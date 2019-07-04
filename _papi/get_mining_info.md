---
layout: service
title: GetMiningInfo
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `getmininginfo` RPC returns various mining-related information.

*Parameters: none*

*Result---various mining-related information*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  |object | Required<br>(exactly 1) | Various mining-related information
| →<br>`blocks` | number (int) | Required<br>(exactly 1) | The height of the highest block on the local best block chain
| →<br>`currentblocksize` | number (int) | Required<br>(exactly 1) | If generation was enabled since the last time this node was restarted, this is the size in bytes of the last block built by this node for header hash checking.  Otherwise, the value `0`
| →<br>`currentblocktx` | number (int) | Required<br>(exactly 1) | If generation was enabled since the last time this node was restarted, this is the number of transactions in the last block built by this node for header hash checking.  Otherwise, this is the value `0`
| →<br>`difficulty` | number (real) | Required<br>(exactly 1) | If generation was enabled since the last time this node was restarted, this is the difficulty of the highest-height block in the local best block chain.  Otherwise, this is the value `0`
| →<br>`errors` | string | Required<br>(exactly 1) | A plain-text description of any errors this node has encountered or detected.  If there are no errors, an empty string will be returned.  This is not related to the JSON-RPC `error` field
| →<br>`genproclimit` | number (int) | Required<br>(exactly 1) | The limit on the number of processors to use for generation.  If generation was enabled since the last time this node was restarted, this is the number used in the second parameter of the `setgenerate` RPC (or the default).  Otherwise, it is `-1`
| →<br>`networkhashps` |  number (int) | Required<br>(exactly 1) | An estimate of the number of hashes per second the network is generating to maintain the current difficulty.  See the `getnetworkhashps` RPC for configurable access to this data
| →<br>`pooledtx` | |  number (int) | Required<br>(exactly 1) | The number of transactions in the memory pool
| →<br>`testnet` | bool | Required<br>(exactly 1) | Set to `true` if this node is running on testnet.  Set to `false` if this node is on mainnet or a regtest
| →<br>`chain` | string | Required<br>(exactly 1) | Set to `main` for mainnet, `test` for testnet, and `regtest` for regtest
| →<br>`generate` | bool | Optional<br>(0 or 1) | Set to `true` if generation is currently enabled; set to `false` if generation is currently disabled.  Only returned if the node has wallet support enabled
| →<br>`hashespersec` | number (int) | Optional<br>(0 or 1) | The approximate number of hashes per second this node is generating across all CPUs, if generation is enabled.  Otherwise `0`.  Only returned if the node has wallet support enabled

*Example*

```
pai-cli getmininginfo
```

Result:

```
{
    "blocks": 464545,
    "currentblocksize": 0,
    "currentblockweight": 0,
    "currentblocktx": 0,
    "difficulty": 521974519553.6282,
    "errors": "",
    "networkhashps": 4.126888339085874e+18,
    "pooledtx": 31241,
    "chain": "main"
}
```

*See also*

* `GetMemPoolInfo`:  returns information about the node’s current transaction memory pool.
* `GetRawMemPool`: returns all transaction identifiers (TXIDs) in the memory pool as a JSON array, or detailed information about each transaction in the memory pool as a JSON object.
* `GetBlockTemplate`: gets a block template or proposal for use with mining software.
* `Generate`: nearly instantly generates blocks.
