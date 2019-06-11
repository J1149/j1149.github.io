---
layout: service
title: SendMany
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support. Requires an unlocked wallet or an
unencrypted wallet.*

The `sendmany` RPC creates and broadcasts a transaction which sends outputs to multiple addresses.

*Parameter #1---from account*

{% include table_header.md
  n= "From Account"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The name of the account from which the pai's should be spent.  Use an empty string (\"\") for the default account. Pai Core will ensure the account has sufficient pai's to pay the total amount in the *outputs* field described below (but the transaction fee paid is not included in the calculation, so an account can spend a total of its balance plus the transaction fee)"
%}

*Parameter #2---the addresses and amounts to pay*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| Outputs  | object | Required<br>(exactly 1) | An object containing key/value pairs corresponding to the addresses and amounts to pay
| →<br>Address/Amount | string (base58) : number (pai's) | Required<br>(1 or more) | A key/value pair with a base58check-encoded string containing the P2PKH or P2SH address to pay as the key, and an amount of pai's to pay as the value

*Parameter #3---minimum confirmations*

{% include table_header.md
  n= "Confirmations"
  t= "number (int)"
  p= "Optional<br>(0 or 1)"
  d= "The minimum number of confirmations an incoming transaction must have for its outputs to be credited to this account’s balance. Outgoing transactions are always counted, as are move transactions made with the move RPC. If an account doesn’t have a balance high enough to pay for this transaction, the payment will be rejected. Use 0 to spend unconfirmed incoming payments. Default is 1"
%}

**WARNING** `if account1 receives an unconfirmed payment and transfers it to account2 with the move RPC, account2 will be able to spend those pai's even if this parameter is set to 1 or higher.`

*Parameter #4---a comment*

{% include table_header.md
  n= "Comment"
  t= "string"
  p= "Optional<br>(0 or 1)"
  d= "A locally-stored (not broadcast) comment assigned to this transaction.  Default is no comment"
%}

*Parameter #5---automatic fee subtraction*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| Subtract Fee From Amount  | array | Optional<br>(0 or 1) | An array of addresses.  The fee will be equally divided by as many addresses as are entries in this array and subtracted from each address.  If this array is empty or not provided, the fee will be paid by the sender
| →<br>Address | string (base58) | Optional (0 or more) | An address previously listed as one of the recipients.


*Result---a TXID of the sent transaction*

{% include table_header.md
  n= "`result`"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The TXID of the sent transaction, encoded as hex in RPC byte order"
%}

*Example*

From the account *test1*, send 0.1 pai's to the first address and 0.2
pai's to the second address, with a comment of "Example Transaction".

```
pai-cli -testnet sendmany \
  "test1" \
  '''
    {
      "mjSk1Ny9spzU2fouzYgLqGUD8U41iR35QN": 0.1,
      "mgnucj8nYqdrPFh2JfZSB1NmUThUGnmsqe": 0.2
    } ''' \
  6       \
  "Example Transaction"
```

Result:

```
ec259ab74ddff199e61caa67a26e29b13b5688dc60f509ce0df4d044e8f4d63d
```

*See also*

* `SendFrom`: spends an amount from a local account to a Pai address.
* `SendToAddress`: spends an amount to a given address.
* `Move`: moves a specified amount from one account in your wallet to another using an off-block-chain transaction.
