---
layout: service
title: RemovePrunedFunds
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `removeprunedfunds` RPC deletes the specified transaction from the wallet. Meant for use with pruned wallets and as a companion to importprunedfunds. This will effect wallet balances.

*Parameter #1---the raw transaction to import*

{% include table_header.md
  n= "TXID"
  t= "string<br>(hex)"
  p= "Required<br>(exactly 1)"
  d= "The hex-encoded id of the transaction you are removing"
%}

*Result---`null` on success*

{% include table_header.md
  n= "`result`"
  t= "null"
  p= "Required<br>(exactly 1)"
  d= "If the funds are removed from the wallet, JSON `null` will be returned"
%}

*Example*

```
pai-cli removeprunedfunds a8d0c0184dde994a09ec054286f1ce581b\
ebf46446a512166eae7628734ea0a5
```

(Success: no result displayed.)

*See also*
 
* `ImportPrivKey`: adds a private key to your wallet. The key should be formatted in the wallet import format created by the dumpprivkey RPC.
* `ImportPrunedFunds`: imports funds without the need of a rescan. Meant for use with pruned wallets.
