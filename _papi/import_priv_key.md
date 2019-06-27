---
layout: service
title: ImportPrivKey
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.  Wallet must be unlocked.*

The `importprivkey` RPC adds a private key to your wallet. The key should be formatted in the wallet import format created by the dumpprivkey RPC.

*Parameter #1---the private key to import*

{% include table_header.md
  n= "Private Key"
  t= "string (base58)"
  p= "Required<br>(exactly 1)"
  d= "The private key to import into the wallet encoded in base58check using wallet import format (WIF)"
%}

*Parameter #2---the account into which the key should be placed*

{% include table_header.md
  n= "Account"
  t= "string"
  p= "Optional<br>(0 or 1)"
  d= "The name of an account to which transactions involving the key should be assigned.  The default is the default account, an empty string (\"\")"
%}

*Parameter #3---whether to rescan the block chain*

{% include table_header.md
  n= "Rescan"
  t= "bool"
  p= "Optional<br>(0 or 1)"
  d= "Set to `true` (the default) to rescan the entire local block database for transactions affecting any address or pubkey script in the wallet (including transaction affecting the newly-added address for this private key).  Set to `false` to not rescan the block database (rescanning can be performed at any time by restarting Pai Core with the `-rescan` command-line argument).  Rescanning may take several minutes.  Notes: if the address for this key is already in the wallet, the block database will not be rescanned even if this parameter is set"
%}

*Result---`null` on success*

{% include table_header.md
  n= "`result`"
  t= "null"
  p= "Required<br>(exactly 1)"
  d= "If the private key is added to the wallet (or is already part of the wallet), JSON `null` will be returned"
%}

*Example*

Import the private key for the address
mgnucj8nYqdrPFh2JfZSB1NmUThUGnmsqe, giving it a label and scanning the
entire block chain:

```
pai-cli -testnet importprivkey \
              cU8Q2jGeX3GNKNa5etiC8mgEgFSeVUTRQfWE2ZCzszyqYNK4Mepy \
              "test label" \
              true
```

(Success: no result displayed.)

*See also*

* `DumpPrivKey`: returns the wallet-import-format (WIF) private key corresponding to an address. (But does not remove it from the wallet.)
* `ImportAddress`: adds an address or pubkey script to the wallet without the associated private key, allowing you to watch for transactions affecting that address or pubkey script without being able to spend any of its outputs.
* `ImportWallet`: imports private keys from a file in wallet dump file format (see the dumpwallet RPC). These keys will be added to the keys currently in the wallet. This call may need to rescan all or parts of the block chain for transactions affecting the newly-added keys, which may take several minutes.
