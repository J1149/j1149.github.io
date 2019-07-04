---
layout: service
title: Move
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.*

The `move` RPC moves a specified amount from one account in your wallet to another using an off-block-chain transaction.

{{WARNING}} `move` will be removed in a later version of Pai
Core.  Use the RPCs listed in the See Also subsection below instead.

{{WARNING}} it's allowed to move more funds than are in an account,
giving the sending account a negative balance and giving the receiving
account a balance that may exceed the number of pai's in the wallet
(or the number of pai's in existence).

*Parameter #1---from account*

{% include table_header.md
  n= "From Account"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The name of the account to move the funds from"
%}

*Parameter #2---to account*

{% include table_header.md
  n= "To Account"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The name of the account to move the funds to"
%}

*Parameter #3---amount to move*

{% include table_header.md
  n= "Amount"
  t= "number (pai's)"
  p= "Required<br>(exactly 1)"
  d= "The amount of pai's to move"
%}

*Parameter #4---an unused parameter*

{% include table_header.md
  n= "*Unused*"
  t= "number (int)"
  p= "Optional<br>(0 or 1)"
  d= "This parameter is no longer used. If parameter #5 needs to be specified, this can be any integer"
%}

*Parameter #5---a comment*

{% include table_header.md
  n= "Comment"
  t= "string"
  p= "Optional<br>(0 or 1)"
  d= "A comment to assign to this move payment"
%}

*Result---`true` on success*

{% include table_header.md
  n= "`result`"
  t= "bool"
  p= "Required<br>(exactly 1)"
  d= "Set to `true` if the move was successful"
%}

*Example*

Move 0.1 pai's from "doc test" to "test1", giving the transaction the
comment "Example move":

```
pai-cli -testnet move "doc test" "test1" 0.1 0 "Example move"
```

Result:

```
true
```

*See also*

* `ListAccounts`: lists accounts and their balances.
* `SendFrom`: spends an amount from a local account to a pai address.
* `SendToAddress`: spends an amount to a given address.
 