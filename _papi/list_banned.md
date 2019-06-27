---
layout: service
title: ListBanned
parent: PAI Core Apis
grand_parent: Developer Reference
---



The `listbanned` RPC lists all banned IPs/Subnets.

*Parameters: none*

*Result---information about each banned IP/Subnet*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  | object | Required<br>(exactly 1) | An array of objects each describing one entry. If there are no entries in the ban list, the array will be empty
| →<br>Node | object | Optional<br>(0 or more) | A ban list entry
| → →<br>`address` | string | Required<br>(exactly 1) | The IP/Subnet of the entry
| → →<br>`banned_until` | number<br>(int) | Required<br>(exactly 1) | The Unix epoch time when the entry was added to the ban list
| → →<br>`ban_created` | number<br>(int) | Required<br>(exactly 1) | The Unix epoch time until the IP/Subnet is banned
| → →<br>`ban_reason` | string | Required<br>(exactly 1) | Set to one of the following reasons:<br>• `node<!--noref--> misbehaving` if the node was banned by the client because of DoS violations<br>• `manually added` if the node was manually banned by the user


*Examples*

The default (`false`):

```
pai-cli listbanned
```

Result:

```

[
  {
    "address": "83.84.25.82/32",
    "banned_until": 1487269503,
    "ban_created": 1478629503,
    "ban_reason": "node misbehaving"
  },
  {
    "address": "111.111.0.111/32",
    "banned_until": 1487791655,
    "ban_created": 1479151655,
    "ban_reason": "manually added"
  }
]
```

*See also*

* `SetBan`: attempts add or remove a IP/Subnet from the banned list.
* `ClearBanned`:  clears list of banned nodes.


