---
layout: default
title: FeeFilter
parent: P2P
grand_parent: Developer Reference
---

FeeFilter
===========

*Added in protocol version 70013 as described by BIP133.*

The `feefilter` message is a request to the receiving peer to not relay any
transaction inv messages to the sending peer where the fee rate for the
transaction is below the fee rate specified in the feefilter message.

`feefilter` was introduced in Pai Core 0.13.0 following the introduction
of mempool limiting in Pai Core 0.12.0. Mempool limiting provides protection against
attacks and spam transactions that have low fee rates and are unlikely to be
included in mined blocks. The `feefilter` messages allows a node to inform its
peers that it will not accept transactions below a specified fee rate into
its mempool, and therefore that the peers can skip relaying inv messages for
transactions below that fee rate to that node.

| Bytes | Name    | Data Type | Description
|-------|---------|-----------|---------------
| 8     | feerate | uint64_t  | The fee rate (in satoshis per kilobyte) below which transactions should not be relayed to this peer.

The receiving peer may choose to ignore the message and not filter transaction
inv messages.

The fee filter is additive with bloom filters. If an SPV client loads a bloom
filter and sends a feefilter message, transactions should only be relayed if
they pass both filters.

Note however that feefilter has no effect on block propagation or responses to
getdata messages. For example, if a node requests a merkleblock from its peer
by sending a getdata message with inv type MSG_FILTERED_BLOCK and it has
previously sent a feefilter to that peer, the peer should respond with a
merkleblock containing *all* the transactions matching the bloom filter, even
if they are below the feefilter fee rate.

inv messages generated from a mempool message are subject to a fee filter if it exists.

The annotated hexdump below shows a `feefilter` message. (The message
header has been omitted.)

`7cbd000000000000 ... satoshis per kilobyte: 48,508`