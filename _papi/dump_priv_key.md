---
title: 'Dump Priv Key'
image: '/docs/noun_591323.png'
---

*Requires wallet support. Requires an unlocked wallet or an
unencrypted wallet.*

The `dumpprivkey` RPC returns the wallet-import-format (WIF) private key corresponding to an address. (But does not remove it from the wallet.)

*Parameter #1---the address corresponding to the private key to get*

| Name         | Type            | Presence                | Description
|--------------|-----------------|-------------------------|-------------
|P2PKH Address | string (base58) | Required<br>(exactly 1) | The P2PKH address corresponding to the private key you want returned.  Must be the address corresponding to a private key in this wallet

*Result---the private key*

| Name         | Type            | Presence                | Description
|--------------|-----------------|-------------------------|-------------
|`result` | string (base58) | Required<br>(exactly 1) | The private key encoded as base58check using wallet import format

*Example*

```
pai-cli -testnet dumpprivkey moQR7i8XM4rSGoNwEsw3h4YEuduuP6mxw7
```

Result:

```
cTVNtBK7mBi2yc9syEnwbiUpnpGJKohDWzXMeF4tGKAQ7wvomr95
```

*See also*

* `ImportPrivKey`: adds a private key to your wallet. The key should be formatted in the wallet import format created by the dumpprivkey RPC.
* `DumpWallet`: creates or overwrites a file with all wallet keys in a human-readable format.
