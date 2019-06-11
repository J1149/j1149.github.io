---
title: 'Create Raw Transaction'
image: '/docs/noun_591323.png'
---

The createrawtransaction RPC creates an unsigned serialized transaction that spends a previous output to a new output with a P2PKH or P2SH address. The transaction is not stored in the wallet or transmitted to the network.

*Parameter #1---Inputs*

| Name        | Type       | Presence            | Description
|-------------|------------|---------------------|-------------
|Inputs       |array       | Required(Exactly 1) | An array of objects, each one to be used as an input to the transaction
|→ Input      |object      | Required(Exactly 1) | An object describing a particular input
|→ → txid     |string (hex)| Required(Exactly 1) | The TXID of the outpoint to be spent encoded as hex in RPC byte order
|→ → vout     |number(int) | Required(Exactly 1) | The output index number (vout) of the outpoint to be spent; the first output in a transaction is index 0
|→ → sequence |number(int) | Optional (0 or 1)   | The sequence number to use for the input

*Parameter #2---P2PKH or P2SH addresses and amounts*

| Name            | Type                     | Presence            | Description
|-----------------|--------------------------|---------------------|-------------
|Outputs          |object                    | Required(Exactly 1) | The addresses and amounts to pay
|→ Address/Amount |string: number (PAIs) | Required (1 or more)| A key/value pair with the address to pay as a string (key) and the amount to pay that address (value) in PAIs

*Parameter #3---locktime*

| Name    | Type       | Presence            | Description
|---------|------------|---------------------|-------------
|Locktime |numeric(int)| Optional(0 or 1)    | Indicates the earliest time a transaction can be added to the block chain

*Result---the unsigned raw transaction in hex*

| Name        | Type       | Presence            | Description
|-------------|------------|---------------------|-------------
|result       |string       | Required(Exactly 1) | The resulting unsigned raw transaction in serialized transaction format encoded as hex. If the transaction couldn’t be generated, this will be set to JSON null and the JSON-RPC error field may contain an error message

*Example*

```
PAI-cli -testnet createrawtransaction '''
  [
    {
      "txid": "1eb590cd06127f78bf38ab4140c4cdce56ad9eb8886999eb898ddf4d3b28a91d",
      "vout" : 0
    }
  ]''' '{ "mgnucj8nYqdrPFh2JfZSB1NmUThUGnmsqe": 0.13 }'
```

Result (wrapped):

```
01000000011da9283b4ddf8d89eb996988b89ead56cecdc44041ab38bf787f12\
06cd90b51e0000000000ffffffff01405dc600000000001976a9140dfc8bafc8\
419853b34d5e072ad37d1a5159f58488ac00000000
```

*See also*

* `DecodeRawTransaction`: decodes a serialized transaction hex string into a JSON object describing the transaction.
* `SignRawTransaction`: signs a transaction in the serialized transaction format using private keys stored in the wallet or provided in the call.
* `SendRawTransaction`: validates a transaction and broadcasts it to the peer-to-peer network.
* `Serialized Transaction Format`