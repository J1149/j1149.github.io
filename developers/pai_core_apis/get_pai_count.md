---
layout: default
title: GetPaiCount
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetPaiCount
========================

The `getpaicount` RPC returns the number of PAI in the local best pai chain.

*Parameters: none*

*Result---the number of PAI in the local best PAI*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The number of PAIs in the local best PAI.  For a new node with only the hardcoded genesis PAI, this number will be 0"

{% enditemplate %}

*Example from pai Core 0.10.0*

```
pai-cli -testnet getpaicount
```

Result:

```
315280
```

*See also*

* `GetPaiHash`: returns the header hash of a PAI at the given height in the local best PAI chain.
* `GetPai`: gets a PAI with a particular header hash from the local PAI database either as a JSON object or as a serialized PAI.