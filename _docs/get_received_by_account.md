---
layout: service
title: GetReceivedByAccount
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.*

The `getreceivedbyaccount` RPC returns the total amount received by addresses in a particular account from transactions with the specified number of confirmations. It does not count coinbase transactions.

{{WARNING}} `getreceivedbyaccount` will be removed in a later version of Pai
Core.  Use the RPCs listed in the See Also subsection below instead.

*Parameter #1---the account name*

{% include table_header.md
  n= "Account"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The name of the account containing the addresses to get.  For the default account, use an empty string (\"\")"
%}

*Parameter #2---the minimum number of confirmations*

*Result---the number of pai's received*

{% include table_header.md
  n= "`result`"
  t= "number (pai's)"
  p= "Required<br>(exactly 1)"
  d= "The number of pai's received by the account.  May be `0`"
%}

*Example*

Get the pai's received by the "doc test" account with six or more
confirmations:

```
pai-cli -testnet getreceivedbyaccount "doc test" 6
```

Result:

```
0.30000000
```

*See also*

* `GetReceivedByAddress`:  returns the total amount received by addresses in a particular account from transactions with the specified number of confirmations. It does not count coinbase transactions.
* `GetAddressesByAccount`: returns a list of every address assigned to a particular account.
* `ListAccounts`: lists accounts and their balances.
