---
layout: default
title: ListAddressGrouping
parent: PAI Core Apis
grand_parent: Developer Reference
---

ListAddressGrouping
========================

*Requires wallet support.*

The `listaddressgroupings` RPC lists groups of addresses that may have had their common ownership made public by common use as inputs in the same transaction or from being used as change from a previous transaction.

*Parameters: none*

*Result---an array of arrays describing the groupings*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "array"
  p: "Required<br>(exactly 1)"
  d: "An array containing the groupings.  May be empty"

- n: "→<br>Groupings"
  t: "array"
  p: "Optional<br>(0 or more)"
  d: "An array containing arrays of addresses which can be associated with each other"

- n: "→ →<br>Address Details"
  t: "array"
  p: "Required<br>(1 or more)"
  d: "An array containing information about a particular address"

- n: "→ → →<br>Address"
  t: "string (base58)"
  p: "Required<br>(exactly 1)"
  d: "The address in base58check format"

- n: "→ → →<br>Balance"
  t: "number (pai's)"
  p: "Required<br>(exactly 1)"
  d: "The current spendable balance of the address, not counting unconfirmed transactions"

- n: "→ → →<br>Account"
  t: "string"
  p: "Optional<br>(0 or 1)"
  d: "*Deprecated: will be removed in a later version of Pai Core*<br><br>The account the address belongs to, if any.  This field will not be returned for change addresses.  The default account is an empty string (\"\")"

{% enditemplate %}

*Example from Pai Core 0.10.0*

```
pai-cli -testnet listaddressgroupings
```

Result (edited to only the first two results):

```
[
    [
        [
            "mgKgzJ7HR64CrB3zm1B4FUUCLtaSqUKfDb",
            0.00000000
        ],
        [
            "mnUbTmdAFD5EAg3348Ejmonub7JcWtrMck",
            0.00000000,
            "test1"
        ]
    ]
]
```

*See also*

* `GetAddressesByAccount`: returns a list of every address assigned to a particular account.
* `GetTransaction`:  gets detailed information about an in-wallet transaction.
