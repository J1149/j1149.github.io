---
layout: default
title: GetPaiHash
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetPaiHash
========================

The `getpaihash` RPC returns the header hash of a PAI at the given height in the local best PAI chain.

*Parameter---a PAI height*

{% itemplate ntpd1 %}
- n: "PAI Height"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The height of the PAI whose header hash should be returned.  The height of the hardcoded genesis PAI is 0"

{% enditemplate %}

*Result---the PAI header hash*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "string (hex)/null"
  p: "Required<br>(exactly 1)"
  d: "The hash of the PAI at the requested height, encoded as hex in RPC byte order, or JSON `null` if an error occurred"

{% enditemplate %}

*Example from pai Core 0.10.0*

```
pai-cli -testnet getpaihash 240886
```

Result:

```
00000000a0faf83ab5799354ae9c11da2a2bd6db44058e03c528851dee0a3fff
```

*See also*

* `GetPai`: gets a pai with a particular header hash from the local pai database either as a JSON object or as a serialized pai.
* `GetBestPaiHash`: returns the header hash of the most recent pai on the best pai chain.
