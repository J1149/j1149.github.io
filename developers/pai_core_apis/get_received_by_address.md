---
layout: default
title: GetReceivedByAddress
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetReceivedByAddress
========================

*Requires wallet support.*

The `getreceivedbyaddress` RPC returns the total amount received by the specified address in transactions with the specified number of confirmations. It does not count coinbase transactions.

*Parameter #1---the address*

{% itemplate ntpd1 %}
- n: "Address"
  t: "string"
  p: "Required<br>(exactly 1)"
  d: "The address whose transactions should be tallied"

{% enditemplate %}

*Parameter #2---the minimum number of confirmations*

{{INCLUDE_CONFIRMATIONS_PARAMETER}}

*Result---the number of pai's received*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "number (pai's)"
  p: "Required<br>(exactly 1)"
  d: "The number of pai's received by the address, excluding coinbase transactions.  May be `0`"

{% enditemplate %}

*Example from Pai Core 0.10.0*

Get the pai's received for a particular address, only counting
transactions with six or more confirmations:

```
pai-cli -testnet getreceivedbyaddress mjSk1Ny9spzU2fouzYgLqGUD8U41iR35QN 6
```

Result:

```
0.30000000
```

*See also*

* `GetReceivedByAccount`: 
* `GetAddressesByAccount`:
* `ListAccounts`:
