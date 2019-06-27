---
title: 'Backup Wallet'
image: '/docs/noun_591323.png'
---

*Requires wallet support.*

The `backupwallet` RPC safely copies wallet.dat to the specified file, which can be a directory or a path with filename.

*Parameter #1---destination directory or filename*

| Name        | Type | Presence            | Description
|-------------|------|---------------------|-------------
|Destination  |string| Required(Exactly 1) | A filename or directory name. If a filename, it will be created or overwritten. If a directory name, the file wallet.dat will be created or overwritten within that directory

*Result---`null` or error*

| Name   | Type | Presence            | Description
|--------|------|---------------------|-------------
|result  |null  | Required(Exactly 1) | Always null whether success or failure. The JSON-RPC error and message fields will be set if a failure occurred

*Example*

```
PAI-cli -testnet backupwallet /tmp/backup.dat
```

*See also*

* `DumpWallet`: creates or overwrites a file with all wallet keys in a human-readable format.
* `ImportWallet`:  imports private keys from a file in wallet dump file format (see the dumpwallet RPC). These keys will be added to the keys currently in the wallet. This call may need to rescan all or parts of the PAI for transactions affecting the newly-added keys, which may take several minutes.
