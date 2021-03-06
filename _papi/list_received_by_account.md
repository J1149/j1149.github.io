---
layout: service
title: ListReceivedByAccount
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.*

The listreceivedbyaccount RPC lists the total number of pai's received by each account.

{{WARNING}} `listreceivedbyaccount` will be removed in a later version of Pai Core.Use the RPCs listed in the See Also subsection below instead.

*Parameter #1---the minimum number of confirmations a transaction must have to be counted*

{% include table_header.md
  n= "Confirmations"
  t= "number (int)"
  p= "Optional<br>(0 or 1)"
  d= "The minimum number of confirmations an externally-generated transaction must have before it is counted towards the balance. Transactions generated by this node are counted immediately. Typically, externally-generated transactions are payments to this wallet and transactions generated by this node are payments to other wallets. Use 0 to count unconfirmed transactions. Default is 1"
%}

*Parameter #2---whether to include empty accounts*

{% include table_header.md
  n= "Include Empty"
  t= "bool"
  p= "Optional<br>(0 or 1)"
  d= "Set to `true` to display accounts which have never received a payment.  Set to `false` (the default) to only include accounts which have received a payment.  Any account which has received a payment will be displayed even if its current balance is `0`"
%}

*Parameter #3---whether to include watch-only addresses in results*

{% include table_header.md
  n= "Include Watch Only"
  t= "bool"
  p= "Optional<br>(0 or 1)"
  d= "If set to true, include watch-only addresses in details and calculations as if they were regular addresses belonging to the wallet. If set to false (the default), treat watch-only addresses as if they didn’t belong to this wallet"
%}

*Result---account names, balances, and minimum confirmations*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  | array | Required<br>(exactly 1) | An array containing objects each describing an account.  At the very least, the default account (\"\") will be included
| →<br>Account | object | Required<br>(1 or more) | An object describing an account
| → →<br>`involvesWatchonly` | bool | Optional<br>(0 or 1) | Set to `true` if the balance of this account includes a watch-only address which has received a spendable payment (that is, a payment with at least the specified number of confirmations and which is not an immature coinbase).  Otherwise not returned
| → →<br>`account` | string | Required<br>(exactly 1) | The name of the account
| → →<br>`amount` | number (pai's) | Required<br>(exactly 1) | The total amount received by this account in pai's
| → →<br>`confirmations` | number (int) | Required<br>(exactly 1) | The number of confirmations received by the last transaction received by this account.  May be `0`


*Example*

Get the balances for all non-empty accounts, including only transactions
which have been confirmed at least six times:

```
pai-cli -testnet listreceivedbyaccount 6 false
```

Result (edited to only show the first two results):

```
[
    {
        "account" : "",
        "amount" : 0.19960000,
        "confirmations" : 53601
    },
    {
        "account" : "doc test",
        "amount" : 0.30000000,
        "confirmations" : 8991
    }
]
```

*See also*

* `ListReceivedByAddress`: lists the total number of pai's received by each address.
* `GetReceivedByAccount`: returns the total amount received by addresses in a particular account from transactions with the specified number of confirmations. It does not count coinbase transactions.
* `GetReceivedByAddress`: returns the total amount received by the specified address in transactions with the specified number of confirmations. It does not count coinbase transactions.

