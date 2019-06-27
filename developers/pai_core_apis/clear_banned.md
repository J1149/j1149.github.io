---
layout: default
title: Clear Banned
parent: PAI Core Apis
grand_parent: Developer Reference
---

Clear Banned
======================

The clearbanned RPC clears list of banned nodes.

*Parameters: none*

*Result---`null` on success*

| Name  | Type | Presence            | Description
|-------|------|---------------------|-------------
|result |null  | Required(Exactly 1) | JSON null when the list was cleared

*Example*

Clears the ban list.

```
paicoin-cli clearbanned
```

Result (no output from `paicoin-cli` because result is set to `null`).

*See also*

* `ListBanned`: lists all banned IPs/Subnets.
* `SetBan`: attempts add or remove a IP/Subnet from the banned list.

