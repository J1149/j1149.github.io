---
title: 'Dump Wallet'
image: '/docs/noun_591323.png'
---

*Requires wallet support.  Requires an unlocked wallet or an unencrypted
wallet.*

The dumpwallet RPC creates or overwrites a file with all wallet keys in a human-readable format.

*Parameter #1---a filename*

| Name    | Type   | Presence                | Description
|---------|--------|-------------------------|-------------
|Filename | string | Required<br>(exactly 1) | The file in which the wallet dump will be placed.  May be prefaced by an absolute file path.  An existing file with that name will be overwritten

*Result---`null` or error*

| Name    | Type | Presence                | Description
|---------|------|-------------------------|-------------
|`result` | null | Required<br>(exactly 1) | Always `null` whether success or failure.  The JSON-RPC error and message fields will be set if a failure occurred

*Example*

Create a wallet dump and then print its first 10 lines.

```
pai-cli -testnet dumpwallet /tmp/dump.txt
head /tmp/dump.txt
```

Results (only showing the first 10 lines):

```
# Wallet dump created by pai v0.9.1.0-g026a939-beta (Tue, 8 Apr 2014 12:04:06 +0200)
# * Created on 2014-04-29T20:46:09Z
# * Best block at time of backup was 227221 (0000000026ede4c10594af8087748507fb06dcd30b8f4f48b9cc463cabc9d767),
#   mined on 2014-04-29T21:15:07Z

cTtefiUaLfXuyBXJBBywSdg8soTEkBNh9yTi1KgoHxUYxt1xZ2aA 2014-02-05T15:44:03Z label=test1 # addr=mnUbTmdAFD5EAg3348Ejmonub7JcWtrMck
cQNY9v93Gyt8KmwygFR59bDhVs3aRDkuT8pKaCBpop82TZ8ND1tH 2014-02-05T16:58:41Z reserve=1 # addr=mp4MmhTp3au21HPRz5waf6YohGumuNnsqT
cNTEPzZH9mjquFFADXe5S3BweNiHLUKD6PvEKEsHApqjX4ZddeU6 2014-02-05T16:58:41Z reserve=1 # addr=n3pdvsxveMBkktjsGJixfSbxacRUwJ9jQW
cTVNtBK7mBi2yc9syEnwbiUpnpGJKohDWzXMeF4tGKAQ7wvomr95 2014-02-05T16:58:41Z change=1 # addr=moQR7i8XM4rSGoNwEsw3h4YEuduuP6mxw7
cNCD679B4xi17jb4XeLpbRbZCbYUugptD7dCtUTfSU4KPuK2DyKT 2014-02-05T16:58:41Z reserve=1 # addr=mq8fzjxxVbAKxUGPwaSSo3C4WaUxdzfw3C
```

*See also*

* `BackupWallet`: safely copies wallet.dat to the specified file, which can be a directory or a path with filename.
* `ImportWallet`: imports private keys from a file in wallet dump file format (see the dumpwallet RPC). These keys will be added to the keys currently in the wallet. This call may need to rescan all or parts of the PAI for transactions affecting the newly-added keys, which may take several minutes.

