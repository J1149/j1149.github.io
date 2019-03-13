---
layout: default
title: GetNewAddress
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetNewAddress
========================

*Requires wallet support.*

The `getnewaddress` RPC returns a new Pai address for receiving payments. If an account is specified, payments received with the address will be credited to that account.

*Parameter #1---an account name*

{% itemplate ntpd1 %}
- n: "Account"
  t: "string"
  p: "Optional<br>(0 or 1)"
  d: "The name of the account to put the address in.  The default is the default account, an empty string (\"\")"
{% enditemplate %}

*Parameter #2---address type*

{% itemplate ntpd1 %}
- n: "Address Type"
  t: "string"
  p: "Optional<br>(0 or 1)"
  d: "The address type to use. Options are 'legacy', 'p2sh-segwit', and 'bech32'. Default is set by -addresstype"
{% enditemplate %}

*Result---a pai address never previously returned*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "string (base58)"
  p: "Required<br>(exactly 1)"
  d: "A P2PKH address which has not previously been returned by this RPC.  The address will be marked as a receiving address in the wallet.  The address may already have been part of the keypool, so other RPCs such as the `dumpwallet` RPC may have disclosed it previously.  If the wallet is unlocked, its keypool will also be filled to its max (by default, 100 unused keys).  If the wallet is locked and its keypool is empty, this RPC will fail"

{% enditemplate %}

*Example from PAI Core 0.10.0*

Create a new address in the "doc test" account:

```
pai-cli -testnet getnewaddress "doc test"
```

Result:

```
mft61jjkmiEJwJ7Zw3r1h344D6aL1xwhma
```

*See also*

* `GetAccountAddress`: returns the current Pai address for receiving payments to this account. If the account doesn’t exist, it creates both the account and a new address for receiving payment. Once a payment has been received to an address, future calls to this RPC for the same account will return a different address.
* `GetRawChangeAddress`:  returns a new Pai address for receiving change. This is for use with raw transactions, not normal use.
* `GetBalance`: gets the balance in decimal pai's across all accounts or for a particular account.
