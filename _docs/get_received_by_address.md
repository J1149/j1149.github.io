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

{% include table_header.md
  n= "Address"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The address whose transactions should be tallied"
%}

*Parameter #2---the minimum number of confirmations*

*Result---the number of pai's received*

{% include table_header.md
  n= "`result`"
  t= "number (pai's)"
  p= "Required<br>(exactly 1)"
  d= "The number of pai's received by the address, excluding coinbase transactions.  May be `0`"
%}

*Example*

Get the pai's received for a particular address, only counting
transactions with six or more confirmations:

```
pai-cli -testnet getreceivedbyaddress PaXVxzkruFZPidQjsDft9CW174Tr99xngu 6
```

Result:

```
0.30000000
```

*See also*

* `GetReceivedByAccount`: returns the total amount received by addresses in a particular account from transactions with the specified number of confirmations. It does not count coinbase transactions.
* `GetAddressesByAccount`: returns a list of every address assigned to a particular account.
* `ListAccounts`: lists accounts and their balances.
