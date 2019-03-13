---
layout: default
title: GetNetworkHashPS
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetNetworkHashPS
========================

The `getnetworkhashps` RPC returns the estimated current or historical network hashes per second based on the last n blocks.

*Parameter #1---number of blocks to average*

{% itemplate ntpd1 %}
- n: "Blocks"
  t: "number (int)"
  p: "Optional<br>(0 or 1)"
  d: "The number of blocks to average together for calculating the estimated hashes per second.  Default is `120`.  Use `-1` to average all blocks produced since the last difficulty change"

{% enditemplate %}

*Parameter #2---block height*

{% itemplate ntpd1 %}
- n: "Height"
  t: "number (int)"
  p: "Optional<br>(0 or 1)"
  d: "The height of the last block to use for calculating the average.  Defaults to `-1` for the highest-height block on the local best block chain.  If the specified height is higher than the highest block on the local best block chain, it will be interpreted the same as `-1`"

{% enditemplate %}

*Result---estimated hashes per second*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The estimated number of hashes per second based on the parameters provided.  May be 0 (for Height=`0`, the genesis block) or a negative value if the highest-height block averaged has a block header time earlier than the lowest-height block averaged"

{% enditemplate %}

*Example from PAI Core 0.10.0*

Get the average hashes per second for all the blocks since the last
difficulty change before block 227255.

```
pai-cli -testnet getnetworkhashps -1 227255
```

Result:

```
79510076167
```

*See also*

* `GetDifficulty`: returns the proof-of-work difficulty as a multiple of the minimum difficulty.
* `GetBlock`: gets a block with a particular header hash from the local block database either as a JSON object or as a serialized block.
