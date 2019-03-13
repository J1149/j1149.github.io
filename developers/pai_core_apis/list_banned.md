---
layout: default
title: ListBanned
parent: PAI Core Apis
grand_parent: Developer Reference
---

ListBanned
========================

*Added in Pai Core 0.12.0*

The `listbanned` RPC lists all banned IPs/Subnets.

*Parameters: none*

*Result---information about each banned IP/Subnet*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "object"
  p: "Required<br>(exactly 1)"
  d: "An array of objects each describing one entry. If there are no entries in the ban list, the array will be empty"

- n: "→<br>Node"
  t: "object"
  p: "Optional<br>(0 or more)"
  d: "A ban list entry"
  
- n: "→ →<br>`address`"
  t: "string"
  p: "Required<br>(exactly 1)"
  d: "The IP/Subnet of the entry"

- n: "→ →<br>`banned_until`"
  t: "number<br>(int)"
  p: "Required<br>(exactly 1)"
  d: "The Unix epoch time when the entry was added to the ban list"

- n: "→ →<br>`ban_created`"
  t: "number<br>(int)"
  p: "Required<br>(exactly 1)"
  d: "The Unix epoch time until the IP/Subnet is banned"
 
- n: "→ →<br>`ban_reason`"
  t: "string"
  p: "Required<br>(exactly 1)"
  d: "Set to one of the following reasons:<br>• `node<!--noref--> misbehaving` if the node was banned by the client because of DoS violations<br>• `manually added` if the node was manually banned by the user"

{% enditemplate %}

*Examples from Pai Core 0.12.1*

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


