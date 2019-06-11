---
title: 'Get Addresses by Account'
image: '/docs/noun_591323.png'
---

*Requires wallet support.*

The getaddressesbyaccount RPC returns a list of every address assigned to a particular account.

{{WARNING}} `getaddressesbyaccount` will be removed in a later version of pai
Core.  Use the RPCs listed in the See Also subsection below instead.

*Parameter #1---the account name*

{% include table_header.md
  n= "Account"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The name of the account containing the addresses to get.  To get addresses from the default account, pass an empty string (\"\")"

%}

*Result---a list of addresses*

{% include table_header.md
  n= "`result`"
  t= "array"
  p= "Required<br>(exactly 1)"
  d= "An array containing all addresses belonging to the specified account.  If the account has no addresses, the array will be empty"
%}

{% include table_content.md
  n= "Address"
  t= "string (base58)"
  p= "Optional<br>(1 or more)"
  d= "A P2PKH or P2SH address belonging to the account"
%}

*Example*

Get the addresses assigned to the account "doc test":

```
pai-cli -testnet getaddressesbyaccount "doc test"
```

Result:

```
[
    "mjSk1Ny9spzU2fouzYgLqGUD8U41iR35QN",
    "mft61jjkmiEJwJ7Zw3r1h344D6aL1xwhma",
    "mmXgiR6KAhZCyQ8ndr2BCfEq1wNG2UnyG6"
]
```

*See also*

* `GetAccount`: returns the name of the account associated with the given address.
* `GetBalance`: gets the balance in decimal pais across all accounts or for a particular account.

