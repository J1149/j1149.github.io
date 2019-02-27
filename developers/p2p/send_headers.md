---
layout: default
title: SendHeaders
parent: P2P
grand_parent: Developer Reference
---

SendHeaders
==============

The `sendheaders` message tells the receiving peer to send new block
announcements using a `headers` message rather than an `inv` message.

There is no payload in a `sendheaders` message.  See the [message header
section][section message header] for an example of a message without a payload.
