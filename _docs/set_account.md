---
layout: service
title: SetAccount
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.*

The `setaccount` RPC puts the specified address in the given account.

`setaccount will be removed in a later version of Pai Core.  Use the RPCs listed in the See Also subsection below instead.`

*Parameter #1---a pai address*

{% include table_header.md
  n= "Address"
  t= "string (base58)"
  p= "Required<br>(exactly 1)"
  d= "The P2PKH or P2SH address to put in the account.  Must already belong to the wallet"
%}

*Parameter #2---an account*

{% include table_header.md
  n= "Account"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The name of the account in which the address should be placed.  May be the default account, an empty string (\"\")"
%}

*Result---`null` if successful*

{% include table_header.md
  n= "`result`"
  t= "null"
  p= "Required<br>(exactly 1)"
  d= "Set to JSON `null` if the address was successfully placed in the account"
%}

*Example*

Put the address indicated below in the "doc test" account.

```
pai-cli -testnet setaccount \
    mmXgiR6KAhZCyQ8ndr2BCfEq1wNG2UnyG6 "doc test"
```

(Success: no result displayed.)

*See also*

* `GetAccount`: returns the name of the account associated with the given address.
* `ListAccounts`: lists accounts and their balances.
* `GetAddressesByAccount`: returns a list of every address assigned to a particular account.
