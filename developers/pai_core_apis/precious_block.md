---
layout: default
title: PreciousBlock
parent: PAI Core Apis
grand_parent: Developer Reference
---

PreciousBlock
===================

*Added in Pai Core 0.14.0*

The `preciousblock` RPC treats a block as if it were received before others with the same work. A later preciousblock call can override the effect of an earlier one. The effects of preciousblock are not retained across restarts.

*Parameter #1---the block hash*

{% itemplate ntpd1 %}
- n: "Header Hash"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The hash of the block to mark as precious"

{% enditemplate %}

*Result---`null` or error on failure*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "null"
  p: "Required<br>(exactly 1)"
  d: "JSON `null`.  The JSON-RPC error field will be set only if you entered an invalid block hash"

{% enditemplate %}

*Example from Pai Core 0.14.1*

```
pai-cli preciousblock 000000000000000001517a0bac70b8cd6f27ee\
1b50a8f12bf606ea6fb6d561cd
```

Result (no output from `pai-cli` because result is set to `null`).
