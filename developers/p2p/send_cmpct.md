---
layout: default
title: SendCmpct
parent: Developer Reference
nav_order: 4
---

SendCmpct
==========

The `sendcmpct` message is defined as a message containing a 1-byte 
integer followed by a 8-byte integer. The first integer is interpreted 
as a boolean and should have a value of either 1 or 0. The second integer
is be interpreted as a little-endian version number. 

Upon receipt of a `sendcmpct` message with the first and second integers 
set to 1, the node should announce new blocks by sending a `cmpctblock` message. 

Upon receipt of a `sendcmpct` message with the first integer set to 0, the node 
shouldn't announce new blocks by sending a `cmpctblock` message, but instead announce 
new blocks by sending invs or headers, as defined by **BIP130**. 

Upon receipt of a `sendcmpct` message with the second integer set to something other than 1, 
nodes should treat the peer as if they had not received the message (as it indicates the peer will provide an 
unexpected encoding in `cmpctblock` messages, and/or other, messages). This allows future 
versions to send duplicate `sendcmpct` messages with different versions as a part of 
a version handshake for future versions.

Nodes should check for a protocol version of >= 70014 before sending `sendcmpct` messages.
Nodes shouldn't send a request for a `MSG_CMPCT_BLOCK` object to a peer before having received 
a `sendcmpct` message from that peer. Nodes shouldn't request a `MSG_CMPCT_BLOCK` object before 
having sent all `sendcmpct` messages to that peer which they intend to send, as the 
peer cannot know what version protocol to use in the response.

The structure of a `sendcmpct` message is defined below.

| Bytes    | Name         | Data Type        | Description
|----------|--------------|------------------|----------------
| 1        | announce     | block_header     | An integer representing a boolean value, must be 1 or 0 (1 is true, 0 is false).
| 8        | version      | uint64_t         | A little-endian representation of a version number. **Version 2 compact blocks should be specified by setting version to 2**
