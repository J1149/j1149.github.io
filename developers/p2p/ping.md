---
layout: default
title: Ping
parent: Developer Reference
nav_order: 4
---

Ping
======

The `ping` message helps confirm that the receiving peer is still
connected. If a TCP/IP error is encountered when sending the `ping`
message (such as a connection timeout), the transmitting node can assume
that the receiving node is disconnected. The response to a `ping`
message is the `pong` message.

Before protocol version 60000, the `ping` message had no payload. As of
protocol version 60001 and all later versions, the message includes a
single field, the nonce.

| Bytes | Name  | Data Type | Description
|-------|-------|-----------|---------------
| 8     | nonce | uint64_t  | Random nonce assigned to this `ping` message.  The responding `pong` message will include this nonce to identify the `ping` message to which it is replying.

The annotated hexdump below shows a `ping` message. (The message
header has been omitted.)

```
0094102111e2af4d ... Nonce
```
