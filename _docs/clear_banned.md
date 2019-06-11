---
title: 'Clear Banned'
image: '/docs/noun_591323.png'
---

The clearbanned RPC clears list of banned nodes.

*Parameters: none*

*Result---`null` on success*

| Name  | Type | Presence            | Description
|-------|------|---------------------|-------------
|result |null  | Required(Exactly 1) | JSON null when the list was cleared

*Example*

Clears the ban list.

```
PAI-cli clearbanned
```

Result (no output from `PAI-cli` because result is set to `null`).

*See also*

* `ListBanned`: lists all banned IPs/Subnets.
* `SetBan`: attempts add or remove a IP/Subnet from the banned list.

