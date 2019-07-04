---
title: 'Get Connection Count'
image: '/docs/noun_591323.png'
---

The `getconnectioncount` RPC returns the number of connections to other nodes.

*Parameters: none*

*Result---the number of connections to other nodes*

{% include table_header.md
  n= "`result`"
  t= "number (int)"
  p= "Required<br>(exactly 1)"
  d= "The total number of connections to other nodes (both inbound and outbound)"
%}

*Example*

```
pai-cli -testnet getconnectioncount
```

Result:

```
14
```

*See also*

* `GetNetTotals`: returns information about network traffic, including bytes in, bytes out, and the current time.
* `GetPeerInfo`: returns data about each connected network node.
* `GetNetworkInfo`: returns information about the node’s connection to the network.
