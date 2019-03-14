---
layout: default
title: VerAck
parent: P2P
grand_parent: Developer Reference
---

VerAck
=========

*Added in protocol version 209.*

The `verack` message acknowledges a previously-received `version`
message, informing the connecting node that it can begin to send
other messages. The `verack` message has no payload; for an example
of a message with no payload, see the [message headers
section][section message header].
