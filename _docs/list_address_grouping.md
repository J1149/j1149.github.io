---
layout: service
title: ListAddressGrouping
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.*

The `listaddressgroupings` RPC lists groups of addresses that may have had their common ownership made public by common use as inputs in the same transaction or from being used as change from a previous transaction.

*Parameters: none*

*Result---an array of arrays describing the groupings*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  | array | Required<br>(exactly 1) | An array containing the groupings.  May be empty
| →<br>Groupings | array | Optional<br>(0 or more) | An array containing arrays of addresses which can be associated with each other
| → →<br>Address Details | array | Required<br>(1 or more) | An array containing information about a particular address
| → → →<br>Address | string (base58) | Required<br>(exactly 1) | The address in base58check format
| → → →<br>Balance | number (pai's) | Required<br>(exactly 1) | The current spendable balance of the address, not counting unconfirmed transactions
| → → →<br>Account | string | Optional<br>(0 or 1) | The account the address belongs to, if any.  This field will not be returned for change addresses.  The default account is an empty string (\"\")


*Example*

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
