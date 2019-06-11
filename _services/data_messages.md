---
title: 'Data Messages'
image: '/docs/noun_591323.png'
---

The following network messages all request or provide data related to
transactions and blocks.

![Overview Of P2P Protocol Data Request And Reply Messages](https://bitcoin.org/img/dev/en-p2p-data-messages.svg?1551020757)

Many of the data messages use
[inventories][/en/glossary/inventory]{:#term-inventory}{:.term} as unique identifiers
for transactions and blocks.  Inventories have a simple 36-byte
structure:

| Bytes | Name            | Data Type | Description
|-------|-----------------|-----------|-------------
| 4     | type identifier | uint32_t  | The type of object which was hashed.  See list of type identifiers below.
| 32    | hash            | char[32]  | SHA256(SHA256()) hash of the object in internal byte order.

The currently-available type identifiers are:

| Type Identifier | Name                         | Description
|-----------------|----------------------------------------------------------------------------------------------------------------------
| 1               | `MSG_TX`                     | The hash is a TXID.
| 2               | `MSG_BLOCK`                  | The hash is of a block header.
| 3               | `MSG_FILTERED_BLOCK`         | The hash is of a block header; identical to `MSG_BLOCK`. When used in a `getdata` message, this indicates the response should be a `merkleblock` message rather than a `block` message (but this only works if a bloom filter was previously configured).  **Only for use in `getdata` messages.**
| 4               | `MSG_CMPCT_BLOCK`            | The hash is of a block header; identical to `MSG_BLOCK`. When used in a `getdata` message, this indicates the response should be a `cmpctblock` message. **Only for use in `getdata` messages.**
| 5               | `MSG_WITNESS_BLOCK`          | The hash is of a block header; identical to `MSG_BLOCK`. When used in a `getdata` message, this indicates the response should be a block message with transactions that have a witness using witness serialization. **Only for use in `getdata` messages.**
| 6               | `MSG_WITNESS_TX`             | The hash is a TXID. When used in a `getdata` message, this indicates the response should be a transaction message, if the witness structure is nonempty, the witness serialization will be used. **Only for use in `getdata` messages.**
| 7               | `MSG_FILTERED_WITNESS_BLOCK` | Reserved for future use, not used as of Protocol Version 70015.

Type identifier zero and type identifiers greater than three are reserved
for future implementations. Pai Core ignores all inventories with
one of these unknown types.
