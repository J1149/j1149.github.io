---
layout: service
title: GetNetworkInfo
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `getnetworkinfo` RPC returns information about the node’s connection to the network.

*Parameters: none*

*Result---information about the node's connection to the network*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  | object | Required<br>(exactly 1) | Information about this node's connection to the network
| →<br>`version` | number(int) | Required<br>(exactly 1) | This node's version of Pai Core in its internal integer format.
| →<br>`subversion` | string | Required<br>(exactly 1) | The user agent this node sends in its `version` message
| →<br>`protocolversion` | number(int) | Required<br>(exactly 1) | The protocol version number used by this node.
| →<br>`localservices` | string (hex) | Required<br>(exactly 1) | The services supported by this node as advertised in its `version` message
| →<br>`localrelay` | bool | Required<br>(exactly 1) | The services supported by this node as advertised in its `version` message
| <br>`timeoffset` | number(int) | Required<br>(exactly 1) | The offset of the node's clock from the computer's clock (both in UTC) in seconds.  The offset may be up to 4200 seconds (70 minutes)
| →<br>`connections` | number(int) | Required<br>(exactly 1) | The total number of open connections (both outgoing and incoming) between this node and other nodes
| →<br>`networks` | array | Required<br>(exactly 1) | An array with three objects: one describing the IPv4 connection, one describing the IPv6 connection, and one describing the Tor hidden service (onion) connection
| → →<br>Network | object | Optional<br>(0 to 3) | An object describing a network.  If the network is unroutable, it will not be returned
| → → →<br>`name` | string | Required<br>(exactly 1) | The name of the network.  Either `ipv4`, `ipv6`, or `onion`
| → → →<br>`limited` | bool | Required<br>(exactly 1) | Set to `true` if only connections to this network are allowed according to the `-onlynet` Pai Core command-line/configuration-file parameter.  Otherwise set to `false`
| → → →<br>`reachable` | bool | Required<br>(exactly 1) | Set to `true` if connections can be made to or from this network.  Otherwise set to `false`
| → → →<br>`proxy` | string | Required<br>(exactly 1) | The hostname and port of any proxy being used for this network.  If a proxy is not in use, an empty string
| → → →<br>`proxy_randomize_credentials` | bool | Required<br>(exactly 1) | Set to `true` if randomized credentials are set for this proxy. Otherwise set to `false`
| →<br>`relayfee` | number(pai's) | Required<br>(exactly 1) | The minimum fee a low-priority transaction must pay in order for this node to accept it into its memory pool
| →<br>`localaddresses` | array | Required<br>(exactly 1) | An array of objects each describing the local addresses this node believes it listens on
| → →<br>Address | object | Optional<br>(0 or more) | An object describing a particular address this node believes it listens on
| → → →<br>`address` | string | Required<br>(exactly 1) | An IP address or .onion address this node believes it listens on.  This may be manually configured, auto detected, or based on `version` messages this node received from its peers
| → → →<br>`port` | number(int) | Required<br>(exactly 1) | The port number this node believes it listens on for the associated `address`.  This may be manually configured, auto detected, or based on `version` messages this node received from its peers
| → → →<br>`score` | number(int) | Required<br>(exactly 1) | The number of incoming connections during the uptime of this node that have used this address in their `version` message
| →<br>`warnings` | string | Required<br>(exactly 1) | A plain-text description of any network warnings. If there are no warnings, an empty string will be returned.

*Example*

```
pai-cli getnetworkinfo
```

Result (actual addresses have been replaced with reserved addresses):

```
{
  "version": 130100,
  "subversion": "/Satoshi:0.13.1/",
  "protocolversion": 70014,
  "localservices": "000000000000000d",
  "localrelay": true,
  "timeoffset": -19,
  "connections": 8,
  "networks": [
    {
      "name": "ipv4",
      "limited": false,
      "reachable": true,
      "proxy": "",
      "proxy_randomize_credentials": false
    }, 
    {
      "name": "ipv6",
      "limited": false,
      "reachable": true,
      "proxy": "",
      "proxy_randomize_credentials": false
    }, 
    {
      "name": "onion",
      "limited": true,
      "reachable": false,
      "proxy": "",
      "proxy_randomize_credentials": false
    }
  ],
  "relayfee": 5000.00000000,
  "localaddresses": [
    {
      "address": "0600:3c03::f03c:91ff:fe89:dfc4",
      "port": 8333,
      "score": 4
    }
  ],
  "warnings": ""
}
```

*See also*

* `GetPeerInfo`: returns data about each connected network node.
* `GetNetTotals`: returns information about network traffic, including bytes in, bytes out, and the current time.

