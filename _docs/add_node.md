---
title: 'Add Node'
image: '/docs/noun_591323.png'
---

The addnode RPC attempts to add or remove a node from the addnode list, or to try a connection to a node once.

*Parameter #1—hostname/IP address and port of node to add or remove*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
|Node  |string     | Required(Exactly 1) | The node to add as a string in the form of <IP address>:<port>. The IP address may be a hostname resolvable through DNS, an IPv4 address, an IPv4-as-IPv6 address, or an IPv6 address

*Parameter #2—whether to add or remove the node, or to try only once to connect*

| Name   | Type      | Presence            | Description
|--------|-----------|---------------------|-------------
|Command |string     | Required(Exactly 1) | What to do with the IP address above. Options are: `add`  to add a node to the addnode list. Up to 8 nodes can be added additional to the default 8 nodes. Not limited by -maxconnections. `remove`  to remove a node from the list. If currently connected, this will disconnect immediately. `onetry` to immediately attempt connection to the node even if the outgoing connection slots are full; this will only attempt the connection once.

*Result—null plus error on failed remove*

| Name   | Type      | Presence            | Description
|--------|-----------|---------------------|-------------
|result  |null       | Required(Exactly 1) | Always JSON null whether the node was added, removed, tried-and-connected, or tried-and-not-connected. The JSON-RPC error field will be set only if you try removing a node that is not on the addnodes list

*Example*

Try connecting to the following node.

```
PAI-cli -testnet addnode 192.0.2.113:18333 onetry
```

Result (no output from `PAI-cli` because result is set to `null`).

*See also*

* `GetAddedNodeInfo`: returns information about the given added node, or all added nodes (except onetry nodes). Only nodes which have been manually added using the addnode RPC will have their information displayed.