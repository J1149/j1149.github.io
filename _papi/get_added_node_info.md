---
title: 'Get Added Node Info'
image: '/docs/noun_591323.png'
---

The `getaddednodeinfo` RPC returns information about the given added node, or all added nodes (except onetry nodes). Only nodes which have been manually added using the addnode RPC will have their information displayed.

*Parameter #1---whether to display connection information*

{% include table_header.md
  n= "Details"
  t= "bool"
  p= "Required<br>(exactly 1)"
  d= "Set to `true` to display detailed information about each added node; set to `false` to only display the IP address or hostname and port added"

%}

*Parameter #2---what node to display information about*

{% include table_header.md
  n= "Node"
  t= "string"
  p= "Optional<br>(0 or 1)"
  d= "The node to get information about in the same `<IP address>:<port>` format as the `addnode` RPC.  If this parameter is not provided, information about all added nodes will be returned"

%}

*Result---a list of added nodes*

{% include table_header.md
  n= "`result`"
  t= "array"
  p= "Required<br>(exactly 1)"
  d= "An array containing objects describing each added node.  If no added nodes are present, the array will be empty.  Nodes added with `onetry` will not be returned"
%}

{% include table_content.md
  n= "→<br>Added Node"
  t= "object"
  p= "Optional<br>(0 or more)"
  d= "An object containing details about a single added node"
%}

{% include table_content.md
  n= "→ →<br>`addednode`"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "An added node in the same `<IP address>:<port>` format as used in the `addnode` RPC.  This element is present for any added node whether or not the Details parameter was set to `true`"
%}

{% include table_content.md
  n= "→ →<br>`connected`"
  t= "bool"
  p= "Optional<br>(0 or 1)"
  d= "If the Details parameter was set to `true`, this will be set to `true` if the node is currently connected and `false` if it is not"
%}

{% include table_content.md
  n= "→ →<br>`addresses`"
  t= "array"
  p= "Optional<br>(0 or 1)"
  d= "If the Details parameter was set to `true`, this will be an array of addresses belonging to the added node"
%}

{% include table_content.md
  n= "→ → →<br>Address"
  t= "object"
  p= "Optional<br>(0 or more)"
  d= "An object describing one of this node's addresses"
%}

{% include table_content.md
  n= "→ → → →<br>`address`"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "An IP address and port number of the node.  If the node was added using a DNS address, this will be the resolved IP address"
%}

{% include table_content.md
  n= "→ → → →<br>`connected`"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "Whether or not the local node is connected to this addnode using this IP address.  Valid values are:<br>• `false` for not connected<br>• `inbound` if the addnode connected to us<br>• `outbound` if we connected to the addnode"
%}

*Example*

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
