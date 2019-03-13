---
layout: default
title: DisconnectNode
parent: PAI Core Apis
grand_parent: Developer Reference
---

DisconnectNode
========================

*Added in pai Core 0.12.0*

The `disconnectnode` RPC immediately disconnects from a specified node.

*Parameter #1---hostname/IP address and port of node to disconnect*

| Name   | Type   | Presence                | Description
|--------|--------|-------------------------|-------------
|Address | string | Required<br>(exactly 1) | *Updated in pai Core 0.14.1*<br><br>The node you want to disconnect from as a string in the form of `<IP address>:<port>`.  The IP address may be a hostname resolvable through DNS, an IPv4 address, an IPv4-as-IPv6 address, or an IPv6 address

*Result---`null` on success or error on failed disconnect*

| Name   | Type   | Presence                | Description
|--------|--------|-------------------------|-------------
|`result` | null | Required<br>(exactly 1) | JSON `null` when the node was disconnected

*Example from pai Core 0.14.1*

Disconnects following node from your node.

```
pai-cli -testnet disconnectnode 192.0.2.113:18333
```

Result (no output from `pai-cli` because result is set to `null`).

*See also*

* AddNode: attempts to add or remove a node from the addnode list, or to try a connection to a node once.
* GetAddedNodeInfo:  returns information about the given added node, or all added nodes (except onetry nodes). Only nodes which have been manually added using the addnode RPC will have their information displayed.
