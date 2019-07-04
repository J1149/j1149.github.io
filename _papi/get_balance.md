---
title: 'Get Balance'
image: '/docs/noun_591323.png'
---

*Requires wallet support.*

The `getbalance` RPC gets the balance in decimal pais across all accounts or for a particular account.

*Parameter #1---an account name*

{% include table_header.md
  n= "Account"
  t= "string"
  p= "Optional<br>(0 or 1)"
  d= "The name of an account to get the balance for.  An empty string (\"\") is the default account.  The string `*` will get the balance for all accounts (this is the default behavior)"

%}

*Parameter #2---the minimum number of confirmations*

{% include table_header.md
  n= "Confirmations"
  t= "number (int"
  p= "Required<br>(exactly 1)"
  d= "The number of confirmations the transactions in this block have, starting at 1 when this block is at the tip of the best block chain.  This score will be -1 if the the block is not part of the best block chain"

%}

*Parameter #3---whether to include watch-only addresses*

{% include table_header.md
  n= "→ →<br>`watchonly`"
  t= "bool"
  p= "Optional<br>(0 or 1)"
  d= "Stating whether matching outputs should be considered watched even when they're not spendable. This is only allowed if keys are empty. The default is `false`"

%}

*Result---the balance in pais*

{% include table_header.md
  n= "`result`"
  t= "number(int)"
  p= "Required<br>(exactly 1)"
  d= "The balance of the account (or all accounts) in pais"
%}

*Examples*

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
