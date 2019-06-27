---
title: 'Get Difficulty'
image: '/docs/noun_591323.png'
---

The `getdifficulty` RPC

*Parameters: none*

*Result---the current difficulty*

{% include table_header.md
  n= "`result`"
  t= "number (real)"
  p= "Required<br>(exactly 1)"
  d= "The difficulty of creating a block with the same target threshold (nBits) as the highest-height block in the local best block chain.  The number is a a multiple of the minimum difficulty"
%}

*Example*

```
pai-cli -testnet getdifficulty
```

Result:

```
1.00000000
```

*See also*

* `GetNetworkHashPS`: returns the estimated current or historical network hashes per second based on the last n blocks.
* `GetMiningInfo`: returns various mining-related information.
