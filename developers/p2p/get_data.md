---
layout: default
title: GetData
parent: Developer Reference
nav_order: 4
---

GetData
========

The `getdata` message requests one or more data objects from another
node. The objects are requested by an inventory, which the requesting
node typically received previously by way of an `inv` message.

The response to a `getdata` message can be a `tx` message, `block`
message, `merkleblock` message, `cmpctblock` message, or `notfound` message.

This message cannot be used to request arbitrary data, such as historic
transactions no longer in the memory pool or relay set. Full nodes may
not even be able to provide older blocks if they've pruned old
transactions from their block database. For this reason, the `getdata`
message should usually only be used to request data from a node which
previously advertised it had that data by sending an `inv` message.

The format and maximum size limitations of the `getdata` message are
identical to the `inv` message; only the message header differs.
