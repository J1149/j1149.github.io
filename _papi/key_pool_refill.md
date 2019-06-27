---
layout: service
title: KeyPoolRefill
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.  Requires an unlocked wallet or an unencrypted
wallet.*

The `keypoolrefill` RPC fills the cache of unused pre-generated keys (the keypool).

*Parameter #1---the new keypool size*

{% include table_header.md
  n= "Key Pool Size"
  t= "number (int)"
  p= "Optional<br>(0 or 1)"
  d= "The new size of the keypool; if the number of keys in the keypool is less than this number, new keys will be generated.  Default is `100`.  The value `0` also equals the default.  The value specified is for this call only---the default keypool size is not changed"
%}

*Result---`null` on success*

{% include table_header.md
  n= "`result`"
  t= "null"
  p= "Required<br>(exactly 1)"
  d= "If the keypool is successfully filled, JSON `null` will be returned"
%}

*Example*

Generate one extra key than the default:

```
pai-cli -testnet keypoolrefill 101
```

(No result shown: success.)

*See also*

* `GetNewAddress`: returns a new Pai address for receiving payments. If an account is specified, payments received with the address will be credited to that account.
* `GetAccountAddress`: returns the current Pai address for receiving payments to this account. If the account doesn’t exist, it creates both the account and a new address for receiving payment. Once a payment has been received to an address, future calls to this RPC for the same account will return a different address.
* `GetWalletInfo`: provides information about the wallet.
