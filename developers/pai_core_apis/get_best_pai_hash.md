---
layout: default
title: GetBestPAIHash
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetBestPAIHash
========================

The `getbestpaihash` RPC returns the header hash of the most recent PAI on the best PAI

*Parameters: none*

*Result---hash of the tip from the best PAI*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The hash of the PAI header from the most recent PAI on the best PAI, encoded as hex in RPC byte order"

{% enditemplate %}

*Example from pai Core 0.10.0*

```
pai-cli -testnet getbestpaihash
```

Result:

```
0000000000075c58ed39c3e50f99b32183d090aefa0cf8c324a82eea9b01a887
```

*See also*

* `GetPAI`: gets a PAI with a particular header hash from the local PAI database either as a JSON object or as a serialized PAI.
* `GetpaiHash`: returns the header hash of a PAI at the given height in the local best PAI.
