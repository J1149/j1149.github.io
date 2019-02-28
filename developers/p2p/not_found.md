---
layout: default
title: NotFound
parent: P2P
grand_parent: Developer Reference
---

NotFound
==========

The `notfound` message is a reply to a `getdata` message which
requested an object the receiving node does not have available for
relay. (Nodes are not expected to relay historic transactions which
are no longer in the memory pool or relay set. Nodes may also have
pruned spent transactions from older blocks, making them unable to
send those blocks.)

The format and maximum size limitations of the `notfound` message are
identical to the `inv` message; only the message header differs.
