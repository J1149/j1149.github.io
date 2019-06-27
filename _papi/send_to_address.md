---
layout: service
title: SendToAddress
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support. Requires an unlocked wallet or an
unencrypted wallet.*

The `sendtoaddress` RPC spends an amount to a given address.

*Parameter #1---to address*

{% include table_header.md
  n= "To Address"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "A P2PKH or P2SH address to which the pai's should be sent"
%}

*Parameter #2---amount to spend*

{% include table_header.md
  n= "Amount"
  t= "number (pai's)"
  p= "Required<br>(exactly 1)"
  d= "The amount to spent in pai's"
%}

*Parameter #3---a comment*

{% include table_header.md
  n= "Comment"
  t= "string"
  p= "Optional<br>(0 or 1)"
  d= "A locally-stored (not broadcast) comment assigned to this transaction.  Default is no comment"
%}

*Parameter #4---a comment about who the payment was sent to*

{% include table_header.md
  n= "Comment To"
  t= "string"
  p= "Optional<br>(0 or 1)"
  d= "A locally-stored (not broadcast) comment assigned to this transaction.  Meant to be used for describing who the payment was sent to. Default is no comment"
%}

*Parameter #5---automatic fee subtraction*

{% include table_header.md
  n= "Subtract Fee From Amount"
  t= "boolean"
  p= "Optional<br>(0 or 1)"
  d= "The fee will be deducted from the amount being sent. The recipient will receive less pai's than you enter in the amount field. Default is `false`"
%}

*Result---a TXID of the sent transaction*

{% include table_header.md
  n= "`result`"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The TXID of the sent transaction, encoded as hex in RPC byte order"
%}

*Example*

Spend 0.1 pai's to the address below with the comment "sendtoaddress
example" and the comment-to "Nemo From Example.com":

```
pai-cli -testnet sendtoaddress mmXgiR6KAhZCyQ8ndr2BCfEq1wNG2UnyG6 \
  0.1 "sendtoaddress example" "Nemo From Example.com"
```

Result:

```
a2a2eb18cb051b5fe896a32b1cb20b179d981554b6bd7c5a956e56a0eecb04f0
```

*See also*

* `SendFrom`: spends an amount from a local account to a pai address.
* `SendMany`: creates and broadcasts a transaction which sends outputs to multiple addresses.
* `Move`: moves a specified amount from one account in your wallet to another using an off-block-chain transaction.
