---
layout: service
title: WalletLock
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support. Requires an unlocked wallet.*

The `walletlock` RPC removes the wallet encryption key from memory, locking the wallet. After calling this method, you will need to call walletpassphrase again before being able to call any methods which require the wallet to be unlocked.

*Parameters: none*

*Result---`null` on success*

{% include table_header.md
  n= "`result`"
  t= "null"
  p= "Required<br>(exactly 1)"
  d= "Always set to JSON `null`"
%}

*Example*

```
pai-cli -testnet walletlock
```

(Success: nothing printed.)

*See also*

* `EncryptWallet`: encrypts the wallet with a passphrase. This is only to enable encryption for the first time. After encryption is enabled, you will need to enter the passphrase to use private keys.
* `WalletPassphrase`: stores the wallet decryption key in memory for the indicated number of seconds. Issuing the walletpassphrase command while the wallet is already unlocked will set a new unlock time that overrides the old one.
* `WalletPassphraseChange`:  changes the wallet passphrase from ‘old passphrase’ to ‘new passphrase’.
