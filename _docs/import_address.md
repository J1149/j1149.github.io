---
layout: service
title: ImportAddress
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.*

The `importaddress` RPC adds an address or pubkey script to the wallet without the associated private key, allowing you to watch for transactions affecting that address or pubkey script without being able to spend any of its outputs.

*Parameter #1---the address or pubkey script to watch*

{% include table_header.md
  n= "Address or Script"
  t= "string (base58 or hex)"
  p= "Required<br>(exactly 1)"
  d= "Either a P2PKH or P2SH address encoded in base58check, or a pubkey script encoded as hex"
%}

*Parameter #2---The account into which to place the address or pubkey script*

{% include table_header.md
  n= "Account"
  t= "string"
  p= "Optional<br>(0 or 1)"
  d= "An account name into which the address should be placed.  Default is the default account, an empty string(\"\")"
%}

*Parameter #3---whether to rescan the block chain*

{% include table_header.md
  n= "Rescan"
  t= "bool"
  p= "Optional<br>(0 or 1)"
  d= "Set to `true` (the default) to rescan the entire local block database for transactions affecting any address or pubkey script in the wallet (including transaction affecting the newly-added address or pubkey script).  Set to `false` to not rescan the block database (rescanning can be performed at any time by restarting Pai Core with the `-rescan` command-line argument).  Rescanning may take several minutes."
%}

*Result---`null` on success*

{% include table_header.md
  n= "`result`"
  t= "null"
  p= "Required<br>(exactly 1)"
  d= "If the address or pubkey script is added to the wallet (or is already part of the wallet), JSON `null` will be returned"
%}

*Example*

Add an address, rescanning the local block database for any transactions
matching it.

```
pai-cli -testnet importaddress \
  muhtvdmsnbQEPFuEmxcChX58fGvXaaUoVt "watch-only test" true
```

Result:

(No output<!--noref-->; success.)

Show that the address has been added:

```
pai-cli -testnet getaccount muhtvdmsnbQEPFuEmxcChX58fGvXaaUoVt
```

Result:

```
watch-only test
```

*See also*

* `ImportPrivKey`:  adds a private key to your wallet. The key should be formatted in the wallet import format created by the dumpprivkey RPC.
* `ListReceivedByAddress`: lists the total number of pai's received by each address.
