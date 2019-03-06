---
layout: default
title: GetAccountAddress
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetAccountAddress
========================

*Requires wallet support.*

The `getaccountaddress` RPC returns the current pai address for receiving payments to this account. If the account doesn’t exist, it creates both the account and a new address for receiving payment. Once a payment has been received to an address, future calls to this RPC for the same account will return a different address.

{{WARNING}} `getaccountaddress` will be removed in a later version of pai
Core.  Use the RPCs listed in the See Also subsection below instead.

*Parameter #1---an account name*

{% itemplate ntpd1 %}
- n: "Account"
  t: "string"
  p: "Required<br>(exactly 1)"
  d: "The name of an account.  Use an empty string (\"\") for the default account.  If the account doesn't exist, it will be created"

{% enditemplate %}

*Result---a pai address*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "string (base58)"
  p: "Required<br>(exactly 1)"
  d: "An address, belonging to the account specified, which has not yet received any payments"

{% enditemplate %}

*Example from pai Core 0.10.0*

Get an address for the default account:

{% highlight bash %}
pai-cli -testnet getaccountaddress ""
{% endhighlight %}

Result:

{% highlight text %}
msQyFNYHkFUo4PG3puJBbpesvRCyRQax7r
{% endhighlight %}

*See also*

* `GetNewAddress`: returns a new pai address for receiving payments. If an account is specified, payments received with the address will be credited to that account.
* `GetRawChangeAddress`: returns a new pai address for receiving change. This is for use with raw transactions, not normal use.
* `GetAddressesByAccount`: returns a list of every address assigned to a particular account.


