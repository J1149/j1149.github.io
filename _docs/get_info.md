---
layout: service
title: GetInfo
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `getinfo` RPC prints various information about the node and the network.

*Parameters: none*

*Result---information about the node and network*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
|`result`  |object | Required<br>(exactly 1) | Information about this node and the network
| →<br>`version` | number (int) | Required<br>(exactly 1) | This node's version of Pai Core in its internal integer format.
| →<br>`protocolversion` | number (int) | Required<br>(exactly 1) | The protocol version number used by this node.  See the [protocol versions section][section protocol versions] for more information
| →<br>`walletversion` |  number (int) | Optional<br>(0 or 1) | The version number of the wallet.  Only returned if wallet support is enabled
| →<br>`balance` |  number (int) | Optional<br>(0 or 1) | The balance of the wallet in pai's.  Only returned if wallet support is enabled
| →<br>`blocks` |  number (int) | Required<br>(exactly 1) | The number of blocks in the local best block chain.  A new node with only the hardcoded genesis block will return `0`
| →<br>`timeoffset` | number (int) | Required<br>(exactly 1) | The offset of the node's clock from the computer's clock (both in UTC) in seconds.  The offset may be up to 4200 seconds (70 minutes)
| →<br>`connections` | number (int) | Required<br>(exactly 1) | The total number of open connections (both outgoing and incoming) between this node and other nodes
| →<br>`proxy` | string | Required<br>(exactly 1) | The hostname/IP address and port number of the proxy, if set, or an empty string if unset
| →<br>`difficulty` | number (real) | Required<br>(exactly 1) | The difficulty of the highest-height block in the local best block chain
| →<br>`testnet` | bool | Required<br>(exactly 1) | Set to `true` if this node is on testnet; set to `false` if this node is on mainnet or a regtest
| →<br>`keypoololdest` | number(int) | Optional<br>(0 or 1) | The date as Unix epoch time when the oldest key in the wallet key pool was created; useful for only scanning blocks created since this date for transactions.  Only returned if wallet support is enabled
| →<br>`keypoolsize` | number(int) | Optional<br>(0 or 1) | The number of keys in the wallet keypool.  Only returned if wallet support is enabled
| →<br>`paytxfee` |  number(pai) | Optional<br>(0 or 1) | The minimum fee to pay per kilobyte of transaction; may be `0`.  Only returned if wallet support is enabled
| →<br>`relayfee` |  number(pai) | Required<br>(exactly 1) | The minimum fee a low-priority transaction must pay in order for this node to accept it into its memory pool
| →<br>`unlocked_until` | number (int) | Optional<br>(0 or 1) | The Unix epoch time when the wallet will automatically re-lock.  Only displayed if wallet encryption is enabled.  Set to `0` if wallet is currently locked
| →<br>`errors` | string | Required<br>(exactly 1) | A plain-text description of any errors this node has encountered or detected.  If there are no errors, an empty string will be returned.  This is not related to the JSON-RPC `error` field


*Example*

```
pai-cli -testnet getinfo
```

Result:

```
{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 1.27007770,
    "blocks" : 315281,
    "timeoffset" : 0,
    "connections" : 9,
    "proxy" : "",
    "difficulty" : 1.00000000,
    "testnet" : true,
    "keypoololdest" : 1418924649,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}
```

*See also*

* `GetBlockChainInfo`: provides information about the current state of the block chain.
* `GetMemPoolInfo`:  returns information about the node’s current transaction memory pool.
* `GetMiningInfo`: returns various mining-related information.
* `GetNetworkInfo`: returns information about the node’s connection to the network.
* `GetWalletInfo`: provides information about the wallet.
