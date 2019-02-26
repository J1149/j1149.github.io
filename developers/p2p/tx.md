---
layout: default
title: Tx
parent: Developer Reference
nav_order: 4
---

Tx
=====

The `tx` message transmits a single transaction in the raw transaction
format. It can be sent in a variety of situations;

* **Transaction Response:** Pai Core and PaiJ will send it in
  response to a `getdata` message that requests the transaction with an
  inventory type of `MSG_TX`.

* **MerkleBlock Response:** Pai Core will send it in response to a
  `getdata` message that requests a merkle block with an inventory type
  of `MSG_MERKLEBLOCK`. (This is in addition to sending a `merkleblock`
  message.) Each `tx` message in this case provides a matched
  transaction from that block.

* **Unsolicited:** PaiJ will send a `tx` message unsolicited for
  transactions it originates.

For an example hexdump of the raw transaction format, see the [raw
transaction section][raw transaction format].
