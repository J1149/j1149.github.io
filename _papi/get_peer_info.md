---
layout: service
title: GetPeerInfo
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `getpeerinfo` RPC returns data about each connected network node.

*Parameters: none*

*Result---information about each currently-connected network node*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  | array | Required<br>(exactly 1) | An array of objects each describing one connected node.  If there are no connections, the array will be empty
| →<br>Node | object | Optional<br>(0 or more) | An object describing a particular connected node
| → →<br>`id` | number (int) | Required<br>(exactly 1) | The node's index number in the local node address database
| → →<br>`addr` | string | Required<br>(exactly 1) | The IP address and port number used for the connection to the remote node
| → →<br>`addrlocal` | string | Optional<br>(0 or 1) | Our IP address and port number according to the remote node.  May be incorrect due to error or lying.  Most SPV nodes set this to `127.0.0.1:8333`
| → →<br>`services` | string (hex) | Required<br>(exactly 1) | The services advertised by the remote node in its `version` message
| → →<br>`lastsend` | number (int) | Required<br>(exactly 1) | The Unix epoch time when we last successfully sent data to the TCP socket for this node
| → →<br>`lastrecv` | number (int) | Required<br>(exactly 1) | The Unix epoch time when we last received data from this node
| → →<br>`bytessent` | number (int) | Required<br>(exactly 1) | The total number of bytes we've sent to this node
| → →<br>`bytesrecv` | number (int) | Required<br>(exactly 1) | The total number of bytes we've received from this node
| → →<br>`conntime` | number (int) | Required<br>(exactly 1) | The Unix epoch time when we connected to this node
| → →<br>`timeoffset` | number (int) | Required<br>(exactly 1) | The time offset in seconds
| → →<br>`pingtime` | number (int) | Required<br>(exactly 1) | The number of seconds this node took to respond to our last P2P `ping` message
| → →<br>`minping` | number (int) | Optional<br>(0 or 1) | The minimum observed ping time (if any at all)
| → →<br>`pingwait` | number (real) | Optional<br>(0 or 1) | The number of seconds we've been waiting for this node to respond to a P2P `ping` message.  Only shown if there's an outstanding `ping` message
| → →<br>`version` | number (int) | Required<br>(exactly 1) | The protocol version number used by this node.
| → →<br>`subver` | string | Required<br>(exactly 1) | The user agent this node sends in its `version` message.  This string will have been sanitized to prevent corrupting the JSON results.  May be an empty string
| → →<br>`inbound` | bool | Required<br>(exactly 1) | Set to `true` if this node connected to us; set to `false` if we connected to this node
| → →<br>`startingheight` | number (int) | Required<br>(exactly 1) | The height of the remote node's block chain when it connected to us as reported in its `version` message
| → →<br>`banscore` | number (int) | Required<br>(exactly 1) | The ban score we've assigned the node based on any misbehavior it's made.  By default, Pai Core disconnects when the ban score reaches `100`
| → →<br>`synced_headers` | number (int) | Required<br>(exactly 1) | The highest-height header we have in common with this node based the last P2P `headers` message it sent us.  If a `headers` message has not been received, this will be set to `-1`
| → →<br>`synced_blocks` | number (int) | Required<br>(exactly 1) | The highest-height block we have in common with this node based on P2P `inv` messages this node sent us.  If no block `inv` messages have been received from this node, this will be set to `-1`
| → →<br>`inflight` | array | Required<br>(exactly 1) | An array of blocks which have been requested from this peer.  May be empty
| → → →<br>Blocks | number (int) | Optional<br>(0 or more) | The height of a block being requested from the remote peer
| → →<br>`whitelisted` | bool | Required<br>(exactly 1) | Set to `true` if the remote peer has been whitelisted; otherwise, set to `false`.  Whitelisted peers will not be banned if their ban score exceeds the maximum (100 by default).  By default, peers connecting from localhost are whitelisted
| → →<br>`bytessent_per_msg` | string : <br>object | Required<br>(exactly 1) | Information about total sent bytes aggregated by message type
| → → →<br>Message Type | number(int) | Required<br>(1 or more) | Total sent bytes aggregated by message type. One field for every used message type
| → →<br>`bytesrecv_per_msg` | string : <br>object | Required<br>(exactly 1) | Information about total received bytes aggregated by message type
| → → →<br>Message Type | number (int) | Required<br>(1 or more) | Total received bytes aggregated by message type. One field for every used message type

*Example*

```
pai-cli getpeerinfo
```

Result (edited to show only a single entry, with IP addresses changed to
[RFC5737][] reserved IP addresses):

```
[
    {
    "id": 3,
    "addr": "192.0.2.113:43132",
    "addrlocal": "127.0.0.1:8333",
    "services": "0000000000000000",
    "relaytxes": true,
    "lastsend": 1481158534,
    "lastrecv": 1481158534,
    "bytessent": 142772,
    "bytesrecv": 14167,
    "conntime": 1481158420,
    "timeoffset": 11,
    "pingtime": 0.226368,
    "minping": 0.226368,
    "version": 70001,
    "subver": "/Satoshi:0.12.1/",
    "inbound": true,
    "startingheight": 0,
    "banscore": 0,
    "synced_headers": -1,
    "synced_blocks": -1,
    "inflight": [
    ],
    "whitelisted": false,
    "bytessent_per_msg": {
      "addr": 55,
      "inv": 12161,
      "ping": 32,
      "pong": 1824,
      "tx": 128549,
      "verack": 24,
      "version": 127
    },
    "bytesrecv_per_msg": {
      "getdata": 12161,
      "ping": 1824,
      "pong": 32,
      "verack": 24,
      "version": 126
    }
  }
]
```

*See also*

* `GetAddedNodeInfo`: returns information about the given added node, or all added nodes (except onetry nodes). Only nodes which have been manually added using the addnode RPC will have their information displayed.
* `GetNetTotals`: returns information about network traffic, including bytes in, bytes out, and the current time.
* `GetNetworkInfo`: returns information about the node’s connection to the network.
