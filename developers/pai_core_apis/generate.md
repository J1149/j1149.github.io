---
layout: default
title: Generate
parent: PAI Core Apis
grand_parent: Developer Reference
---

Generate
========================

*Requires wallet support.*

The `generate` RPC nearly instantly generates PAIs.

*Parameter #1---the number of blocks to generate*

{% itemplate ntpd1 %}
- n: "Blocks"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The number of blocks to generate.  The RPC call will not return until all blocks have been generated or the maxium number of iterations has been reached"
  
{% enditemplate %}

*Parameter #2---the maximum number of iterations to try*

{% itemplate ntpd1 %}
- n: "Maxtries"
  t: "number (int)"
  p: "Optional<br>(0 or 1)"
  d: "The maximum number of iterations that are tried to create the requested number of blocks. Default is `1000000`"

{% enditemplate %}

*Result---the generated PAI header hashes*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "array"
  p: "Required<br>(exactly 1)"
  d: "An array containing the block header hashes of the generated PAIs (may be empty if used with `generate 0`)"

- n: "→<br>Header Hashes"
  t: "string (hex)"
  p: "Required<br>(1 or more)"
  d: "The hashes of the headers of the blocks generated in regtest mode, as hex in RPC byte order"
{% enditemplate %}

*Example from PAI Core 0.13.1*

Using regtest mode (also works in normal mode), generate 2 blocks:

```
pai-cli -regtest generate 2 500000
```

Result:

```
[
    "36252b5852a5921bdfca8701f936b39edeb1f8c39fffe73b0d8437921401f9af",
    "5f2956817db1e386759aa5794285977c70596b39ea093b9eab0aa4ba8cd50c06"
]
```

*See also*

* `GenerateToAddress`: mines blocks immediately to a specified address.
* `GetMiningInfo`: returns various mining-related information.
* `GetPAITemplate`: gets a block template or proposal for use with mining software.
