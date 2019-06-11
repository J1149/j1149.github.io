---
layout: service
title: WalletPasshrase
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support. Requires an encrypted wallet.*

The `walletpassphrase` RPC stores the wallet decryption key in memory for the indicated number of seconds. Issuing the walletpassphrase command while the wallet is already unlocked will set a new unlock time that overrides the old one.

`WARNING: if using this RPC on the command line, remember
that your shell probably saves your command lines (including the
value of the passphrase parameter).`

*Parameter #1---the passphrase*

{% include table_header.md
  n= "Passphrase"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The passphrase that unlocks the wallet"
%}

*Parameter #2---the number of seconds to leave the wallet unlocked*

{% include table_header.md
  n= "Seconds"
  t= "number (int)"
  p= "Required<br>(exactly 1)"
  d= "The number of seconds after which the decryption key will be automatically deleted from memory"
%}

*Result---`null` on success*

{% include table_header.md
  n= "`result`"
  t= "null"
  p= "Required<br>(exactly 1)"
  d= "Always set to JSON `null`"
%}

*Example*

Unlock the wallet for 10 minutes (the passphrase is "test"):

```
pai-cli -testnet walletpassphrase test 600
```

(Success: no result printed.)

*See also*

* `EncryptWallet`: encrypts the wallet with a passphrase. This is only to enable encryption for the first time. After encryption is enabled, you will need to enter the passphrase to use private keys.
* `WalletPassphraseChange`: changes the wallet passphrase from ‘old passphrase’ to ‘new passphrase’.
* `WalletLock`: removes the wallet encryption key from memory, locking the wallet. After calling this method, you will need to call walletpassphrase again before being able to call any methods which require the wallet to be unlocked.
