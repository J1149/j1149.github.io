---
layout: default
title: GetBalance
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetBalance
========================

*Requires wallet support.*

The `getbalance` RPC gets the balance in decimal pais across all accounts or for a particular account.

*Parameter #1---an account name*

{% itemplate ntpd1 %}
- n: "Account"
  t: "string"
  p: "Optional<br>(0 or 1)"
  d: "*Deprecated: will be removed in a later version of pai Core*<br><br>The name of an account to get the balance for.  An empty string (\"\") is the default account.  The string `*` will get the balance for all accounts (this is the default behavior)"

{% enditemplate %}

*Parameter #2---the minimum number of confirmations*

{{INCLUDE_CONFIRMATIONS_PARAMETER}}

*Parameter #3---whether to include watch-only addresses*

{{INCLUDE_INCLUDE_WATCH_ONLY_PARAMETER}}

*Result---the balance in pais*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "number (pais)"
  p: "Required<br>(exactly 1)"
  d: "The balance of the account (or all accounts) in pais"

{% enditemplate %}

*Examples from pai Core 0.10.0*

Get the balance for the "test1" account, including transactions with
at least one confirmation and those spent to watch-only addresses in
that account.

```
pai-cli -testnet getbalance "test1" 1 true
```

Result:

```
1.99900000
```

*See also*

* `ListAccounts`: lists accounts and their balances.
* `GetReceivedByAccount`:  returns the total amount received by addresses in a particular account from transactions with the specified number of confirmations. It does not count coinbase transactions.
* `GetReceivedByAddress`: returns the total amount received by the specified address in transactions with the specified number of confirmations. It does not count coinbase transactions. 
