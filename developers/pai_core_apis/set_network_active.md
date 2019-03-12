---
layout: default
title: SetNetworkActive
parent: PAI Core Apis
grand_parent: Developer Reference
---

SetNetworkActive
=======================

*Added in Pai Core 0.14.0*

The `setnetworkactive` RPC disables/enables all P2P network activity.

*Parameter #1---whether to disable or enable all P2P network activity*

{% itemplate ntpd1 %}
- n: "Activate"
  t: "bool"
  p: "Required<br>(exactly 1)"
  d: "Set to `true` to enable all P2P network activity. Set to `false` to disable all P2P network activity"

{% enditemplate %}

*Result---`null` or error on failure*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "null"
  p: "Required<br>(exactly 1)"
  d: "JSON `null`.  The JSON-RPC error field will be set only if you entered an invalid parameter"

{% enditemplate %}

*Example from Pai Core 0.14.1*

```
pai-cli setnetworkactive true
```

Result (no output from `pai-cli` because result is set to `null`).

*See also*

* `GetNetworkInfo`: returns information about the node’s connection to the network.
