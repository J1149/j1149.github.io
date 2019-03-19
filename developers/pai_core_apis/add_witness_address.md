---
layout: default
title: Add Witness Address
parent: PAI Core Apis
grand_parent: Developer Reference
---

Add Witness Address
====================

*Requires wallet support. Requires an unlocked wallet or an unencrypted wallet.*

The `addwitnessaddress` RPC adds a witness address for a script (with pubkey or redeem script known).

*Parameter #1---the witness address*

| Name   | Type         | Presence            | Description
|--------|--------------|---------------------|-------------
|Address |String(base58)| Required(Exactly 1) | A witness address that gets added to a script. Needs to be in the wallet and uncompressed

*Result---the witness script*

| Name  | Type         | Presence            | Description
|-------|--------------|---------------------|-------------
|result |String(base58)| Required(Exactly 1) | The value of the new address (P2SH of witness script)

*Example*

```
PAI-cli addwitnessaddress PaXVxzkruFZPidQjsDft9CW174Tr99xngu
```

Result:

The RPC is disabled by default on mainnet as long as Segregated Witness has not been activated.
`-walletprematurewitness` enables the RPC.

```
3LfAujMsBHgQKoxLn59dVbeYPmfUrHSAQb
```

*See also*

* `BIP-141` - Segregated Witness
* `BIP-142` - Address Format for Segregated Witness