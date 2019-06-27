---
layout: service
title: SetTxFee
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.*

The `settxfee` RPC sets the transaction fee per kilobyte paid by transactions created by this wallet.

*Parameter #1---the transaction fee amount per kilobyte*

{% include table_header.md
  n= "Transaction Fee Per Kilobyte"
  t= "number (pai's)"
  p= "Required<br>(exactly 1)"
  d= "The transaction fee to pay, in pai's, for each kilobyte of transaction data.  Be careful setting the fee too low---your transactions may not be relayed or included in blocks"
%}

*Result: `true` on success*

{% include table_header.md
  n= "`result`"
  t= "bool (true)"
  p= "Required<br>(exactly 1)"
  d= "Set to `true` if the fee was successfully set"
%}

*Example*

Set the transaction fee per kilobyte to 100,000 satoshis.

```
pai-cli -testnet settxfee 0.00100000
```

Result:

```
true
```

*See also*

* `GetWalletInfo`: provides information about the wallet.
* `GetNetworkInfo`: returns information about the node’s connection to the network.
