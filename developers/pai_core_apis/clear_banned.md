---
layout: default
title: Clear Banned
parent: PAI Core Apis
grand_parent: Developer Reference
---

Clear Banned
======================

*Added in PAI Core 0.12.0*

The clearbanned RPC clears list of banned nodes.

*Parameters: none*

*Result---`null` on success*

| Name  | Type | Presence            | Description
|-------|------|---------------------|-------------
|result |null  | Required(Exactly 1) | JSON null when the list was cleared

*Example from PAI Core 0.13.1*

Clears the ban list.

```
PAI-cli clearbanned
```

Result (no output from `PAI-cli` because result is set to `null`).

*See also*

* ListBanned: lists all banned IPs/Subnets.
* SetBan: attempts add or remove a IP/Subnet from the banned list.

