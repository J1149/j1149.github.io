---
title: 'Fund Raw Transaction'
image: '/docs/noun_591323.png'
---

*Requires wallet support.*

The `fundrawtransaction` RPC adds inputs to a transaction until it has enough in value to meet its out value. This will not modify existing inputs, and will add one change output to the outputs. Note that inputs which were signed may need to be resigned after completion since in/outputs have been added. The inputs added will not be signed, use signrawtransaction for that. 

All existing inputs must have their previous output transaction be in the wallet.

*Parameter #1---The hex string of the raw transaction*

| Name    | Type   | Presence                | Description
|---------|--------|-------------------------|-------------
|Hexstring | string (hex)| Required<br>(exactly 1) | The hex string of the raw transaction 


*Parameter #2---Additional options*

| Name    | Type   | Presence                | Description
|---------|--------|-------------------------|-------------
| Options | Object| Optional<br>(0 or 1) | Additional options
| → <br>`changeAddress` | string | Optional<br>(0 or 1) | The pai address to receive the change. If not set, the address is chosen from address pool
| → <br>`changePosition` | nummeric (int) | Optional<br>(0 or 1) | The index of the change output. If not set, the change position is randomly chosen
| → <br>`includeWatching` | bool | Optional<br>(0 or 1) | Inputs from watch-only addresses are also considered. The default is `false`
| → <br>`lockUnspents` | bool | Optional<br>(0 or 1) | The selected outputs are locked after running the rpc call. The default is `false`
| → <br>`reserveChangeKey` | bool | Optional<br>(0 or 1) | Reserves the change output key from the keypool. The default is `true`.
| → <br>`feeRate` | numeric (pai's) | Optional<br>(0 or 1) | The specific feerate  you are willing to pay(BTC per KB). If not set, the wallet determines the fee
| → <br>`subtractFeeFromOutputs` | array | Optional<br>(0 or 1) | A json array of integers. The fee will be equally deducted from the amount of each specified output. The outputs are specified by their zero-based index, before any change output is added.
| → →<br>Output index | numeric (int) | Optional<br>(0 or more) | A output index number (vout) from which the fee should be subtracted. If multiple vouts are provided, the total fee will be divided by the numer of vouts listed and each vout will have that amount subtracted from it


*Result---information about the created transaction*

| Name    | Type   | Presence                | Description
|---------|--------|-------------------------|-------------
| `result` | object| Required<br>(exactly 1) | An object including information about the created transaction
| → <br>hex | string (hex) | Required<br>(Exactly 1) | The resulting unsigned raw transaction in serialized transaction format encoded as hex
| → <br>fee | numeric (pais) | Required<br>(Exactly 1) | Fee in BTC the resulting transaction pays
| → <br>changepos | numeric (int) | Required<br>(Exactly 1) | The position of the added change output, or `-1` if no change output was added


*Example*

```
pai-cli -testnet fundrawtransaction 01000000011da9283b4ddf8d\
89eb996988b89ead56cecdc44041ab38bf787f1206cd90b51e0000000000ffff\
ffff01405dc600000000001976a9140dfc8bafc8419853b34d5e072ad37d1a51\
59f58488ac00000000 
'{
    "changeAddress": "PaXVxzkruFZPidQjsDft9CW174Tr99xngu",
    "changePosition" : 1,
    "includeWatching" : false,
    "lockUnspents" : true,
    "feeRate" : 0.0001
}'
```

Result:

```
{
	"hex": "01000000011da9283b4ddf8d89eb996988b89ead56cecdc44041ab38bf787f1206cd90b51e0000000000ffffffff01405dc600000000001976a9140dfc8bafc8419853b34d5e072ad37d1a5159f58488ac00000000",
	"fee": 0.0000245,
	"changepos": 2
}
```

*See also*

* `CreateRawTransaction`: creates an unsigned serialized transaction that spends a previous output to a new output with a P2PKH or P2SH address. The transaction is not stored in the wallet or transmitted to the network.
* `DecodeRawTransaction`:  decodes a serialized transaction hex string into a JSON object describing the transaction.
* `SignRawTransaction`: signs a transaction in the serialized transaction format using private keys stored in the wallet or provided in the call.
* `SendRawTransaction`: validates a transaction and broadcasts it to the peer-to-peer network.
* `Serialized Transaction Format.`
