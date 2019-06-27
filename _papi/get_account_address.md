---
title: 'Get Account Address'
image: '/docs/noun_591323.png'
---

*Requires wallet support.*

The `getaccountaddress` RPC returns the current pai address for receiving payments to this account. If the account doesn’t exist, it creates both the account and a new address for receiving payment. Once a payment has been received to an address, future calls to this RPC for the same account will return a different address.

{{WARNING}} `getaccountaddress` will be removed in a later version of pai
Core.  Use the RPCs listed in the See Also subsection below instead.

*Parameter #1---an account name*

{% include table_header.md
  n= "Account"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The name of an account.  Use an empty string (\"\") for the default account.  If the account doesn't exist, it will be created"

%}

*Result---a pai address*

{% include table_header.md
  n= "`result`"
  t= "string (base58)"
  p= "Required<br>(exactly 1)"
  d= "An address, belonging to the account specified, which has not yet received any payments"

%}

*Example*

Get an address for the default account:

```
pai-cli -testnet getaccountaddress ""
```

Result:

```
msQyFNYHkFUo4PG3puJBbpesvRCyRQax7r
```

*See also*

* `GetNewAddress`: returns a new pai address for receiving payments. If an account is specified, payments received with the address will be credited to that account.
* `GetRawChangeAddress`: returns a new pai address for receiving change. This is for use with raw transactions, not normal use.
* `GetAddressesByAccount`: returns a list of every address assigned to a particular account.


