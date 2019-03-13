---
layout: default
title: GetAddedNodeInfo
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetAddedNodeInfo
========================

The `getaddednodeinfo` RPC returns information about the given added node, or all added nodes (except onetry nodes). Only nodes which have been manually added using the addnode RPC will have their information displayed.

*Parameter #1---whether to display connection information*

{% itemplate ntpd1 %}
- n: "Details"
  t: "bool"
  p: "Required<br>(exactly 1)"
  d: "*Removed in pai Core 0.14.0*<br><br>Set to `true` to display detailed information about each added node; set to `false` to only display the IP address or hostname and port added"

{% enditemplate %}

*Parameter #2---what node to display information about*

{% itemplate ntpd1 %}
- n: "Node"
  t: "string"
  p: "Optional<br>(0 or 1)"
  d: "The node to get information about in the same `<IP address>:<port>` format as the `addnode` RPC.  If this parameter is not provided, information about all added nodes will be returned"

{% enditemplate %}

*Result---a list of added nodes*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "array"
  p: "Required<br>(exactly 1)"
  d: "An array containing objects describing each added node.  If no added nodes are present, the array will be empty.  Nodes added with `onetry` will not be returned"

- n: "→<br>Added Node"
  t: "object"
  p: "Optional<br>(0 or more)"
  d: "An object containing details about a single added node"

- n: "→ →<br>`addednode`"
  t: "string"
  p: "Required<br>(exactly 1)"
  d: "An added node in the same `<IP address>:<port>` format as used in the `addnode` RPC.  This element is present for any added node whether or not the Details parameter was set to `true`"

- n: "→ →<br>`connected`"
  t: "bool"
  p: "Optional<br>(0 or 1)"
  d: "If the Details parameter was set to `true`, this will be set to `true` if the node is currently connected and `false` if it is not"

- n: "→ →<br>`addresses`"
  t: "array"
  p: "Optional<br>(0 or 1)"
  d: "If the Details parameter was set to `true`, this will be an array of addresses belonging to the added node"

- n: "→ → →<br>Address"
  t: "object"
  p: "Optional<br>(0 or more)"
  d: "An object describing one of this node's addresses"

- n: "→ → → →<br>`address`"
  t: "string"
  p: "Required<br>(exactly 1)"
  d: "An IP address and port number of the node.  If the node was added using a DNS address, this will be the resolved IP address"

- n: "→ → → →<br>`connected`"
  t: "string"
  p: "Required<br>(exactly 1)"
  d: "Whether or not the local node is connected to this addnode using this IP address.  Valid values are:<br>• `false` for not connected<br>• `inbound` if the addnode connected to us<br>• `outbound` if we connected to the addnode"

{% enditemplate %}

*Example from pai Core 0.14.1*

```
pai-cli getaddednodeinfo
```

Result (real hostname and IP address replaced):

```
[
    {
        "addednode" : "paid.example.com:8333",
        "connected" : true,
        "addresses" : [
            {
                "address" : "192.0.2.113:8333",
                "connected" : "outbound"
            }
        ]
    }
]
```

*See also*

* `AddNode`: attempts to add or remove a node from the addnode list, or to try a connection to a node once.
* `GetPeerInfo`: returns data about each connected network node.
