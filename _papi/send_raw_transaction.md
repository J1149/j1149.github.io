---
layout: service
title: SendRawTransaction
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `sendrawtransaction` RPC validates a transaction and broadcasts it to the peer-to-peer network.

*Parameter #1---a serialized transaction to broadcast*

{% include table_header.md
  n= "Transaction"
  t= "string (hex)"
  p= "Required<br>(exactly 1)"
  d= "The serialized transaction to broadcast encoded as hex"
%}

*Parameter #2--whether to allow high fees**

{% include table_header.md
  n= "Allow High Fees"
  t= "bool"
  p= "Optional<br>(0 or 1)"
  d= "Set to `true` to allow the transaction to pay a high transaction fee.  Set to `false` (the default) to prevent Pai Core from broadcasting the transaction if it includes a high fee.  Transaction fees are the sum of the inputs minus the sum of the outputs, so this high fees check helps ensures user including a change address to return most of the difference back to themselves"
%}

*Result---a TXID or error message*

{% include table_header.md
  n= "`result`"
  t= "null/string (hex)"
  p= "Required<br>(exactly 1)"
  d= "If the transaction was accepted by the node for broadcast, this will be the TXID of the transaction encoded as hex in RPC byte order.  If the transaction was rejected by the node, this will set to `null`, the JSON-RPC error field will be set to a code, and the JSON-RPC message field may contain an informative error message"
%}

*Examples*

Broadcast a signed transaction:

```
pai-cli -testnet sendrawtransaction 01000000011da9283b4ddf8d\
89eb996988b89ead56cecdc44041ab38bf787f1206cd90b51e000000006a4730\
4402200ebea9f630f3ee35fa467ffc234592c79538ecd6eb1c9199eb23c4a16a\
0485a20220172ecaf6975902584987d295b8dddf8f46ec32ca19122510e22405\
ba52d1f13201210256d16d76a49e6c8e2edc1c265d600ec1a64a45153d45c29a\
2fd0228c24c3a524ffffffff01405dc600000000001976a9140dfc8bafc84198\
53b34d5e072ad37d1a5159f58488ac00000000
```

Result:

```
f5a5ce5988cc72b9b90e8d1d6c910cda53c88d2175177357cc2f2cf0899fbaad
```

*See also*

* `CreateRawTransaction`:  creates an unsigned serialized transaction that spends a previous output to a new output with a P2PKH or P2SH address. The transaction is not stored in the wallet or transmitted to the network.
* `DecodeRawTransaction`: decodes a serialized transaction hex string into a JSON object describing the transaction.
* `SignRawTransaction`: signs a transaction in the serialized transaction format using private keys stored in the wallet or provided in the call.
