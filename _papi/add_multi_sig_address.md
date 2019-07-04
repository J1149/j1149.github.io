---
title: 'Add Multi Sig Address'
image: '/docs/noun_591323.png'
---

*Requires wallet support.*

The `addmultisigaddress` RPC adds a P2SH multisig address to the wallet.

*Parameter #1---the number of signatures required*

| Name   | Type      | Presence            | Description
|--------|-----------|---------------------|-------------
|Required|number(int)| Required(Exactly 1) | The minimum (m) number of signatures required to spend this m-of-n multisig script


*Parameter #2---the full public keys, or addresses for known public keys*

| Name            | Type | Presence            | Description
|-----------------|------|---------------------|-------------
|Keys Or Addresses|array | Required(Exactly 1) | An array of strings with each string being a public key or address
|→ Key Or Address |string|required(One or more)| A public key against which signatures will be checked. Alternatively, this may be a P2PKH address belonging to the wallet—the corresponding public key will be substituted. There must be at least as many keys as specified by the Required parameter, and there may be more keys


*Parameter #3---the account name*

| Name  | Type | Presence          | Description
|-------|------|-------------------|-------------
|Account|string | Optional(0 or 1) | The account name in which the address should be stored. Default is the default account, “” (an empty string)

*Result---a P2SH address printed and stored in the wallet*

| Name  | Type           | Presence            | Description
|-------|----------------|---------------------|-------------
|result |string (base58) | Required(exactly 1) | The P2SH multisig address. The address will also be added to the wallet, and outputs paying that address will be tracked by the wallet

*Example*

Adding a 2-of-3 P2SH multisig address to the "test account" by mixing
two P2PKH addresses and one full public key:

```
PAI-cli -testnet addmultisigaddress \
  2 \
  '''
    [
      "mjbLRSidW1MY8oubvs4SMEnHNFXxCcoehQ",
      "02ecd2d250a76d204011de6bc365a56033b9b3a149f679bc17205555d3c2b2854f",
      "mt17cV37fBqZsnMmrHnGCm9pM28R1kQdMG"
    ]
  ''' \
  'test account'
```

Result:

```
2MyVxxgNBk5zHRPRY2iVjGRJHYZEp1pMCSq
```

(New P2SH multisig address also stored in wallet.)

*See also*

* `CreateMultiSig`: creates a P2SH multi-signature address.
* `DecodeScript`:  decodes a hex-encoded P2SH redeem script.
* `Pay-To-Script-Hash` (P2SH)
