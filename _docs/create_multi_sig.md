---
title: 'Create Multi Sig'
image: '/docs/noun_591323.png'
---

The createmultisig RPC creates a P2SH multi-signature address.

*Parameter #1---the number of signatures required*

| Name     | Type      | Presence            | Description
|----------|-----------|---------------------|-------------
|Required  |number(int)| Required(Exactly 1) | The minimum (m) number of signatures required to spend this m-of-n multisig script

*Parameter #2---the full public keys, or addresses for known public keys*

| Name             | Type      | Presence            | Description
|------------------|-----------|---------------------|-------------
|Keys Or Addresses |array      | Required(Exactly 1) | An array of strings with each string being a public key or address

*Result---P2SH address and hex-encoded redeem script*

| Name     | Type            | Presence            | Description
|----------|-----------------|---------------------|-------------
|result    |object           | Required(Exactly 1) | An object describing the multisig address
|→ address |string (base58)  | Required(Exactly 1) | The P2SH address for this multisig redeem script
|→ redeemScript |string (hex)| Required(Exactly 1) | The multisig redeem script encoded as hex

*Example*

Creating a 2-of-3 P2SH multisig address by mixing two P2PKH addresses and
one full public key:

```
PAI-cli -testnet createmultisig 2 '''
  [
    "mjbLRSidW1MY8oubvs4SMEnHNFXxCcoehQ",
    "02ecd2d250a76d204011de6bc365a56033b9b3a149f679bc17205555d3c2b2854f",
    "mt17cV37fBqZsnMmrHnGCm9pM28R1kQdMG"
  ]
'''
```

Result:

```
{
  "address" : "PaXVxzkruFZPidQjsDft9CW174Tr99xngu",
  "redeemScript" : "522103ede722780d27b05f0b1169efc90fa15a601a32fc6c3295114500c586831b6aaf2102ecd2d250a76d204011de6bc365a56033b9b3a149f679bc17205555d3c2b2854f21022d609d2f0d359e5bc0e5d0ea20ff9f5d3396cb5b1906aa9c56a0e7b5edc0c5d553ae"
}
```

*See also*

* `AddMultiSigAddress`: adds a P2SH multisig address to the wallet.
* `DecodeScript`: decodes a hex-encoded P2SH redeem script.
* `Pay-To-Script-Hash` (P2SH)
