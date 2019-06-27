---
title: 'Get Account'
image: '/docs/noun_591323.png'
---

*Requires wallet support.*

The `getaccount` RPC returns the name of the account associated with the given address.

*Parameter #1---a pai address*

{% include table_header.md
  n= "Address"
  t= "string (base58)"
  p= "Required<br>(exactly 1)"
  d= "A P2PKH or P2SH pai address belonging either to a specific account or the default account (\"\")"
%}

*Result---an account name*

{% include table_header.md
  n= "`result`"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The name of an account, or an empty string (\"\", the default account)"

%}

*Example*

```
pai-cli -testnet getaccount mjSk1Ny9spzU2fouzYgLqGUD8U41iR35QN
```

Result:

```
doc test
```

*See also*

* `GetAddressesByAccount`: returns a list of every address assigned to a particular account.
