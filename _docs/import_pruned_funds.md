---
layout: service
title: ImportPrunedFunds
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.*

The `importprunedfunds` RPC imports funds without the need of a rescan. Meant for use with pruned wallets. Corresponding address or script must previously be included in wallet. The end-user is responsible to import additional transactions that subsequently spend the imported outputs or rescan after the point in the blockchain the transaction is included.

*Parameter #1---the raw transaction to import*

{% include table_header.md
  n= "Raw Transaction"
  t= "string<br>(hex)"
  p= "Required<br>(exactly 1)"
  d= "A raw transaction in hex funding an already-existing address in wallet"
%}

*Parameter #2---the tx out proof that cointains the transaction*

{% include table_header.md
  n= "TX Out Proof"
  t= "string<br>(hex)"
  p= "Required<br>(exactly 1)"
  d= "The hex output from gettxoutproof that contains the transaction"
%}

*Result---`null` on success*

{% include table_header.md
  n= "`result`"
  t= "null"
  p= "Required<br>(exactly 1)"
  d= "If the funds are added to wallet, JSON `null` will be returned"
%}

*Example*

```
pai-cli importprunedfunds "txhex" "txoutproof"
```

(Success: no result displayed.)

*See also*

* `ImportPrivKey`: adds a private key to your wallet. The key should be formatted in the wallet import format created by the dumpprivkey RPC.

* `RemovePrunedFunds`: deletes the specified transaction from the wallet. Meant for use with pruned wallets and as a companion to importprunedfunds.

