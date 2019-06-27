---
layout: service
title: PrioritiseTransaction
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `prioritisetransaction` RPC adds virtual priority or fee to a transaction, allowing it to be accepted into blocks mined by this node (or miners which use this node) with a lower priority or fee. (It can also remove virtual priority or fee, requiring the transaction have a higher priority or fee to be accepted into a locally-mined block.)

*Parameter #1---the TXID of the transaction to modify*

{% include table_header.md
  n= "TXID"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The TXID of the transaction whose virtual priority or fee you want to modify, encoded as hex in RPC byte order"
%}

*Parameter #2---the change to make to the virtual priority*

{% include table_header.md
  n= "Priority"
  t= "number (real)"
  p= "Required<br>(exactly 1)"
  d= "If positive, the priority to add to the transaction in addition to its computed priority; if negative, the priority to subtract from the transaction's computed priory.  Computed priority is the age of each input in days since it was added to the block chain as an output (coinage) times the value of the input in satoshis (value) divided by the size of the serialized transaction (size), which is `coinage * value / size`"
%}

*Parameter #3---the change to make to the virtual fee*

{% include table_header.md
  n= "Fee"
  t= "number (int)"
  p= "Required<br>(exactly 1)"
  d= "**Warning:** this value is in satoshis, not pai's<br><br>If positive, the virtual fee to add to the actual fee paid by the transaction; if negative, the virtual fee to subtract from the actual fee paid by the transaction.  No change is made to the actual fee paid by the transaction"
%}

*Result---`true` if the priority is changed*

{% include table_header.md
  n= "`result`"
  t= "bool (true only)"
  p= "Required<br>(exactly 1)"
  d= "Always set to `true` if all three parameters are provided.  Will not return an error if the TXID is not in the memory pool.  If fewer or more than three arguments are provided, or if something goes wrong, will be set to `null`"
%}

*Example*

```
pai-cli -testnet prioritisetransaction \
    fe0165147da737e16f5096ab6c1709825217377a95a882023ed089a89af4cff9 \
    1234 456789
```

Result:

```
true
```

*See also*

* `GetRawMemPool`: returns all transaction identifiers (TXIDs) in the memory pool as a JSON array, or detailed information about each transaction in the memory pool as a JSON object.
* `GetBlockTemplate`: gets a block template or proposal for use with mining software.
