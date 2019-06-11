---
title: 'Encrypt Wallet'
image: '/docs/noun_591323.png'
---

*Requires wallet support.*

The encryptwallet RPC encrypts the wallet with a passphrase. This is only to enable encryption for the first time. After encryption is enabled, you will need to enter the passphrase to use private keys.


{{WARNING}} if using this RPC on the command line, remember
that your shell probably saves your command lines (including the value
of the passphrase parameter). In addition, there is no RPC to completely
disable encryption. If you want to return to an unencrypted wallet, you
must create a new wallet and restore your data from a backup made with
the `dumpwallet` RPC.

*Parameter #1---a passphrase*

| Name    | Type   | Presence                | Description
|---------|--------|-------------------------|-------------
|Passphrase | string | Required<br>(exactly 1) | The passphrase to use for the encrypted wallet. Must be at least one character

*Result---a notice (with program shutdown)*

| Name    | Type   | Presence                | Description
|---------|--------|-------------------------|-------------
|`result` | string | Required<br>(exactly 1) | A notice that the server is stopping and that you need to make a new backup.  The wallet is now encrypted


*Example*

```
pai-cli -testnet encryptwallet "test"
```

Result:

```
wallet encrypted; pai server stopping, restart to run with encrypted
wallet. The keypool has been flushed, you need to make a new backup.
```

*See also*

* `WalletPassphrase`: stores the wallet decryption key in memory for the indicated number of seconds. Issuing the walletpassphrase command while the wallet is already unlocked will set a new unlock time that overrides the old one.
* `WalletLock`:  removes the wallet encryption key from memory, locking the wallet. After calling this method, you will need to call walletpassphrase again before being able to call any methods which require the wallet to be unlocked.
* `WalletPassphraseChange`: changes the wallet passphrase from ‘old passphrase’ to ‘new passphrase’.
