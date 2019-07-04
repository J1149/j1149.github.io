---
layout: service
title: ImportWallet
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support. Requires an unlocked wallet or an
unencrypted wallet.*

The `importwallet` RPC imports private keys from a file in wallet dump file format (see the dumpwallet RPC). These keys will be added to the keys currently in the wallet. This call may need to rescan all or parts of the block chain for transactions affecting the newly-added keys, which may take several minutes.

*Parameter #1---the file to import*

{% include table_header.md
  n= "Filename"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The file to import.  The path is relative to Pai Core's working directory"
%}

*Result---`null` on success*

{% include table_header.md
  n= "`result`"
  t= "null"
  p= "Required<br>(exactly 1)"
  d= "If all the keys in the file are added to the wallet (or are already part of the wallet), JSON `null` will be returned"
%}

*Example*

Import the file shown in the example subsection of the `dumpwallet` RPC.

```
pai-cli -testnet importwallet /tmp/dump.txt
```

(Success: no result displayed.)

*See also*

* `DumpWallet`: creates or overwrites a file with all wallet keys in a human-readable format.
* `ImportPrivKey`: adds a private key to your wallet. The key should be formatted in the wallet import format created by the dumpprivkey RPC.
