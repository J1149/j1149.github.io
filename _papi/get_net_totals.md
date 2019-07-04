---
layout: service
title: GetNetTotals
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `getnettotals` RPC returns information about network traffic, including bytes in, bytes out, and the current time.

*Parameters: none*

*Result---the current bytes in, bytes out, and current time*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  | object | Required<br>(exactly 1) | An object containing information about the node's network totals
| →<br>`totalbytesrecv` | number(int) | Required<br>(exactly 1) | The total number of bytes received since the node was last restarted
| →<br>`totalbytessent` | number(int) | Required<br>(exactly 1) | The total number of bytes sent since the node was last restarted
| →<br>`timemillis` | number(int) | Required<br>(exactly 1) | Unix epoch time in milliseconds according to the operating system's clock (not the node adjusted time)
| →<br>`uploadtarget` | string : <br>object | Required<br>(exactly 1) | The upload traget information
| → →<br>`timeframe` | number(int) | Required<br>(exactly 1) | Length of the measuring timeframe in seconds.  The timeframe is currently set to `24` hours
| → →<br>`target` | number(int) | Required<br>(exactly 1) | The maximum allowed outbound traffic in bytes.  The default is `0`.  Can be changed with `-maxuploadtarget`
| → →<br>`target_reached` | bool | Required<br>(exactly 1) | Indicates if the target is reached.  If the target is reached the node won't serve SPV and historical block requests anymore
| → →<br>`serve_historical_blocks` | bool | Required<br>(exactly 1) | Indicates if historical blocks are served
| → →<br>`bytes_left_in_cycle` | number(int) | Required<br>(exactly 1) | Amount of bytes left in current time cycle.  `0` is displayed if no upload target is set
| → →<br>`time_left_in_cycle` | number(int) | Required<br>(exactly 1) | Seconds left in current time cycle.  `0` is displayed if no upload target is set

*Example*

```
pai-cli getnettotals
```

Result:

```
{
  "totalbytesrecv": 7137052851,
  "totalbytessent": 211648636140,
  "timemillis": 1481227418585,
  "uploadtarget": {
    "timeframe": 86400,
    "target": 0,
    "target_reached": false,
    "serve_historical_blocks": true,
    "bytes_left_in_cycle": 0,
    "time_left_in_cycle": 0
  }
}
```

*See also*

* `GetNetworkInfo`: returns information about the node’s connection to the network.
* `GetPeerInfo`: returns data about each connected network node.
