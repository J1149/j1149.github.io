---
title: 'Abandon Transaction'
image: '/docs/noun_327190.png'
---

The `abandontransaction` RPC marks an in-wallet transaction and all its in-wallet descendants as abandoned. This allows their inputs to be respent.

*Parameter #1---a transaction identifier (TXID)*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
|TXID  |String(hex)| Required(Exactly 1) | The TXID of the transaction that you want to abandon. The TXID must be encoded as hex in RPC byte order

*Result---`null` on success*

| Name  | Type | Presence            | Description
|------ |------|---------------------|-------------
|Result |null  | Required(Exactly 1) | JSON null when the transaction and all descendants were abandoned

Abandons the transaction on your node.

*Example*

```
PAI-cli abandontransaction fa3970c341c9f5de6ab13f128cbfec58d732e736a505fe32137ad551c799ecc4
```

Result (no output from `PAI-cli` because result is set to `null`).

*See also*

* `SendRawTransaction`:  validates a transaction and broadcasts it to the peer-to-peer network.
