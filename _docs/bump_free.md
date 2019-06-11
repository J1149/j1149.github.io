---
title: 'Bump Free'
---

*Requires wallet support. Wallet must be unlocked.*

The `bumpfee` RPC {{summary_bumpFee}} The increased fee is deducted from the change output. The command fails if the change output is too small to increase the fee or 
if the wallet or mempool contains a transaction that spends one of the transaction's outputs. The `-walletrbf` option needs to be enabled (default is `false`).

*Parameter #1---The TXID of the transaction*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
|TXID  |String(hex)| Required(Exactly 1) | The id of the transaction

*Parameter #2---Additional options*

| Name           | Type              | Presence         | Description
|----------------|-------------------|------------------|-------------
|Options         | Object            | Optional(0 or 1) | Additional options
|→ `confTarget`  | numeric(int)      | Optional(0 or 1) | The confirmation target in blocks. Based on this value the new fee will be calculated using the same code as the estimatefee RPC. If not set, the default target of ´6´ blocks will be used
|→ `totalFree`   | numeric(satoshis) | Optional(0 or 1) | The total fee to pay in satoshis (not the feerate). The actual fee can be higher in rare cases if the change output is close to the dust limit
|→ `replaceable` | bool              | Optional(0 or 1) | Whether the new transaction should still be BIP 125 replaceable. Even if set to false the transaction may still be replacable, for example if it has unconfirmed ancestors which are replaceable. The default is true

*Result---information about the new transaction*

| Name      | Type              | Presence            | Description
|-----------|-------------------|---------------------|-------------
|result     | Object            | Optional(0 or 1)    | An object including information about the new transaction
|→ `txid`   | string(hex)       | Optional(0 or 1)    | The id of the new transaction
|→ `origFee`| numeric(satoshis) | Optional(0 or 1)    | The fee of the replaced transaction
|→ `fee`    | bool              | Optional(0 or 1)    | The fee of the new transaction
|→ `errors` | array             | Required(exactly 1) | Errors encountered during processing (may be empty)

*Example*

```
PAI-cli -testnet bumpfee d4a33e0cabaz723149e1fcab4e033a40173\
88a644c65370e3cb06ba2f0e13975\
'{
    "totalFee": 4000,
    "replaceable": false
}'
```

Result:

```
{
	"txid": "37a55ce49636977k79bcb04ee1143573b570b1743e09660e79e7ec3320968ca54",
	"origfee": 0.00002450,
	"fee": 0.00004000,
	"errors": ""
}
```

*See also*

* `CreateRawTransaction`:  creates an unsigned serialized transaction that spends a previous output to a new output with a P2PKH or P2SH address. The transaction is not stored in the wallet or transmitted to the network.
* `FundRawTransaction`:adds inputs to a transaction until it has enough in value to meet its out value.
* `SignRawTransaction`: signs a transaction in the serialized transaction format using private keys stored in the wallet or provided in the call.
* `SendRawTransaction`: validates a transaction and broadcasts it to the peer-to-peer network.
* `Serialized Transaction Format`