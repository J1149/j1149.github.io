---
layout: default
title: FundRawTransaction
parent: PAI Core Apis
grand_parent: Developer Reference
---

FundRawTransaction
========================

*Requires wallet support.*

The `fundrawtransaction` RPC adds inputs to a transaction until it has enough in value to meet its out value. This will not modify existing inputs, and will add one change output to the outputs. Note that inputs which were signed may need to be resigned after completion since in/outputs have been added. The inputs added will not be signed, use signrawtransaction for that. 

All existing inputs must have their previous output transaction be in the wallet.

*Parameter #1---The hex string of the raw transaction*

{% itemplate ntpd1 %}
- n: "Hexstring"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The hex string of the raw transaction"

{% enditemplate %}

*Parameter #2---Additional options*

{% itemplate ntpd1 %}
- n: "Options"
  t: "Object"
  p: "Optional<br>(0 or 1)"
  d: "*Added in pai Core 0.13.0*<br><br>Additional options"

- n: "→ <br>`changeAddress`"
  t: "string"
  p: "Optional<br>(0 or 1)"
  d: "The pai address to receive the change. If not set, the address is chosen from address pool"
  
- n: "→ <br>`changePosition`"
  t: "nummeric (int)"
  p: "Optional<br>(0 or 1)"
  d: "The index of the change output. If not set, the change position is randomly chosen"

- n: "→ <br>`includeWatching`"
  t: "bool"
  p: "Optional<br>(0 or 1)"
  d: "Inputs from watch-only addresses are also considered. The default is `false`"
  
- n: "→ <br>`lockUnspents`"
  t: "bool"
  p: "Optional<br>(0 or 1)"
  d: "The selected outputs are locked after running the rpc call. The default is `false`"

- n: "→ <br>`reserveChangeKey`"
  t: "bool"
  p: "Optional<br>(0 or 1)"
  d: "*Added in pai Core 0.14.0*<br><br>Reserves the change output key from the keypool. The default is `true`. Before 0.14.0, the used keypool key was never marked as change-address key and directly returned to the keypool (leading to address reuse)."  
  
- n: "→ <br>`feeRate`"
  t: "numeric (pais)"
  p: "Optional<br>(0 or 1)"
  d: "The specific feerate  you are willing to pay(BTC per KB). If not set, the wallet determines the fee"

- n: "→ <br>`subtractFeeFromOutputs`"
  t: "array"
  p: "Optional<br>(0 or 1)"
  d: "A json array of integers. The fee will be equally deducted from the amount of each specified output. The outputs are specified by their zero-based index, before any change output is added."

- n: "→ →<br>Output index"
  t: numeric (int)
  p: Optional<br>(0 or more)
  d: "A output index number (vout) from which the fee should be subtracted.
  If multiple vouts are provided, the total fee will be divided by the
  numer of vouts listed and each vout will have that amount subtracted
  from it"

{% enditemplate %}

*Result---information about the created transaction*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "object"
  p: "Required<br>(exactly 1)"
  d: "An object including information about the created transaction"

- n: "→ <br>hex"
  t: "string (hex)"
  p: "Required<br>(Exactly 1)"
  d: "The resulting unsigned raw transaction in serialized transaction format encoded as hex"

- n: "→ <br>fee"
  t: "numeric (pais)"
  p: "Required<br>(Exactly 1)"
  d: "Fee in BTC the resulting transaction pays"

- n: "→ <br>changepos"
  t: "numeric (int)"
  p: "Required<br>(Exactly 1)"
  d: "The position of the added change output, or `-1` if no change output was added"

{% enditemplate %}

*Example from pai Core 0.13.1*

```
pai-cli -testnet fundrawtransaction 01000000011da9283b4ddf8d\
89eb996988b89ead56cecdc44041ab38bf787f1206cd90b51e0000000000ffff\
ffff01405dc600000000001976a9140dfc8bafc8419853b34d5e072ad37d1a51\
59f58488ac00000000 
'{
    "changeAddress": "15gJiApWFGTN2iTteQwQbqasdT6dwGWwv6",
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
* Serialized Transaction Format.
