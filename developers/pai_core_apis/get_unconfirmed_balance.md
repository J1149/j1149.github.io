---
layout: default
title: GetUnconfirmedBalance
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetUnconfirmedBalance
========================

*Requires wallet support.*

The `getunconfirmedbalance` RPC returns the wallet’s total unconfirmed balance.

*Parameters: none*

*Result---the balance of unconfirmed transactions paying this wallet*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "number (pai's)"
  p: "Required<br>(exactly 1)"
  d: "The total number of pai's paid to this wallet in unconfirmed transactions"

{% enditemplate %}

*Example from Pai Core 0.10.0*

```
pai-cli -testnet getunconfirmedbalance
```

Result (no unconfirmed incoming payments):

```
0.00000000
```

*See also*

* `GetBalance`: gets the balance in decimal pai's across all accounts or for a particular account.
