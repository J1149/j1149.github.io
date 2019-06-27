---
layout: service
title: Ping
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `ping` RPC sends a P2P ping message to all connected nodes to measure ping time. Results are provided by the getpeerinfo RPC pingtime and pingwait fields as decimal seconds. The P2P ping message is handled in a queue with all other commands, so it measures processing backlog, not just network ping.

*Parameters: none*

*Result---`null`*

{% include table_header.md
  n= "`result`"
  t= "null"
  p= "Required"
  d= "Always JSON `null`"
%}

*Example*

```
pai-cli -testnet ping
```

(Success: no result printed.)

Get the results using the `getpeerinfo` RPC:

```
pai-cli -testnet getpeerinfo | grep ping
```

Results:

```
        "pingtime" : 0.11790800,
        "pingtime" : 0.22673400,
        "pingtime" : 0.16451900,
        "pingtime" : 0.12465200,
        "pingtime" : 0.13267900,
        "pingtime" : 0.23983300,
        "pingtime" : 0.16764700,
        "pingtime" : 0.11337300,
```

*See also*

* `GetPeerInfo`: returns data about each connected network node.
* `P2P Ping Message`
