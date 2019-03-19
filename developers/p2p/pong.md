---
layout: default
title: Pong
parent: P2P
grand_parent: Developer Reference
---

Pong
======

The `pong` message replies to a `ping` message, proving to the pinging
node that the ponging node is still alive. Pai Core will, by
default, disconnect from any clients which have not responded to a
`ping` message within 20 minutes.

To allow nodes to keep track of latency, the `pong` message sends back
the same nonce received in the `ping` message it is replying to.

The format of the `pong` message is identical to the `ping` message;
only the message header differs.
