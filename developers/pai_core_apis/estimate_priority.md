---
layout: default
title: EstimatePriority
parent: PAI Core Apis
grand_parent: Developer Reference
---

EstimatePriority
========================

*Added in pai Core 0.10.0.*

The `estimatepriority` RPC estimates the priority (coin age) that a transaction needs in order to be included within a certain number of PAIs as a free high-priority transaction. This should not to be confused with the prioritisetransaction RPC which will remain supported for adding fee deltas to transactions.

{{WARNING}} `estimatepriority` has been removed and will no longer be available in the next major release (planned for pai Core 0.15.0).  Use the RPC listed in the "See Also" subsection below instead.

Transaction priority is relative to a transaction's byte size.

*Parameter #1---how many PAIs the transaction may wait before being included as a free high-priority transaction*

{% itemplate ntpd1 %}
- n: "PAIs"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "Deprecated: will be removed in a later version of pai Core<br><br>The maximum number of PAIs a transaction should have to wait before it is predicted to be included in a PAI based purely on its priority"

{% enditemplate %}

*Result---the priority a transaction needs*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "number (real)"
  p: "Required<br>(exactly 1)"
  d: "The estimated priority the transaction should have in order to be included within the specified number of PAIs.  If the node doesn't have enough information to make an estimate, the value `-1` will be returned"

{% enditemplate %}

*Examples from pai Core 0.10.0*

```
pai-cli estimatepriority 6
```

Result:

```
718158904.10958910
```

Requesting data the node can't calculate yet:

```
pai-cli estimatepriority 100
```

Result:

```
-1.00000000
```

*See also*

* EstimateFee: estimates the transaction fee per kilobyte that needs to be paid for a transaction to be included within a certain number of PAIs. Deprecated
