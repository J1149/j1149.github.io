---
layout: default
title: GetAccount
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetAccount
========================

*Requires wallet support.*

The `getaccount` RPC returns the name of the account associated with the given address.

*Parameter #1---a pai address*

{% itemplate ntpd1 %}
- n: "Address"
  t: "string (base58)"
  p: "Required<br>(exactly 1)"
  d: "A P2PKH or P2SH pai address belonging either to a specific account or the default account (\"\")"

{% enditemplate %}

*Result---an account name*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "string"
  p: "Required<br>(exactly 1)"
  d: "The name of an account, or an empty string (\"\", the default account)"

{% enditemplate %}

*Example from PAI Core 0.10.0*

```
pai-cli -testnet getaccount mjSk1Ny9spzU2fouzYgLqGUD8U41iR35QN
```

Result:

```
doc test
```

*See also*

* `GetAddressesByAccount`: returns a list of every address assigned to a particular account.
