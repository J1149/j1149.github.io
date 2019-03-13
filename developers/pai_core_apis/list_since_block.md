---
layout: default
title: ListSinceBlock
parent: PAI Core Apis
grand_parent: Developer Reference
---

ListSinceBlock
========================

*Requires wallet support.*

The `listsinceblock` RPC gets all transactions affecting the wallet which have occurred since a particular block, plus the header hash of a block at a particular depth.

*Parameter #1---a block header hash*

{% itemplate ntpd1 %}
- n: "Header Hash"
  t: "string (hex)"
  p: "Optional<br>(0 or 1)"
  d: "The hash of a block header encoded as hex in RPC byte order.  All transactions affecting the wallet which are not in that block or any earlier block will be returned, including unconfirmed transactions.  Default is the hash of the genesis block, so all transactions affecting the wallet are returned by default"

{% enditemplate %}

*Parameter #2---the target confirmations for the lastblock field*

{% itemplate ntpd1 %}
- n: "Target Confirmations"
  t: "number (int)"
  p: "Optional<br>(0 or 1)"
  d: "Sets the lastblock field of the results to the header hash of a block with this many confirmations.  This does not affect which transactions are returned.  Default is `1`, so the hash of the most recent block on the local best block chain is returned"

{% enditemplate %}

*Parameter #3---whether to include watch-only addresses in details and calculations*

{% itemplate ntpd1 %}
- n: "Include Empty"
  t: "bool"
  p: "Optional<br>(0 or 1)"
  d: "Set to `true` to display accounts which have never received a payment.  Set to `false` (the default) to only include accounts which have received a payment.  Any account which has received a payment will be displayed even if its current balance is `0`"

{% enditemplate %}


**Result**

{% assign DEPTH="→ → → " %}

{% itemplate ntpd1 %}
- n: "`result`"
  t: "object"
  p: "Required<br>(exactly 1)"
  d: "An object containing an array of transactions and the lastblock field"

- n: "→<br>`transactions`"
  t: "array"
  p: "Required<br>(exactly 1)"
  d: "An array of objects each describing a particular **payment** to or from this wallet.  The objects in this array do not describe an actual transactions, so more than one object in this array may come from the same transaction.  This array may be empty"

- n: "→ →<br>Payment"
  t: "object"
  p: "Optional<br>(0 or more)"
  d: "An payment which did not appear in the specified block or an earlier block"

- n: "→ →<br>involvesWatchOnly"
  t: "bool"
  p: "Optional<br>(0 or more)"
  d: "Set to true if the payment involves a watch-only address. Otherwise not returned"

- n: "→ →<br>account"
  t: "string"
  p: "Required<br>(exactly 1)"
  d: "*Deprecated: will be removed in a later version of Pai Core.* The account which the payment was credited to or debited from. May be an empty string (“”) for the default account"

- n: "→ →<br>address"
  t: "string(base58)"
  p: "Optional<br>(0 or 1)"
  d: "The address paid in this payment, which may be someone else’s address not belonging to this wallet. May be empty if the address is unknown, such as when paying to a non-standard pubkey script"

- n: "→ → →<br>category"
  t: "string"
  p: "required<br>(exactly 1)"
  d: "Set to one of the following values:
    • send if sending payment
    • receive if this wallet received payment in a regular transaction
    • generate if a matured and spendable coinbase
    • immature if a coinbase that is not spendable yet
    • orphan if a coinbase from a block that’s not in the local best block chain"

- n: "→ → →<br>amount"
  t: "number(pai's)"
  p: "Required<br>(exactly 1)"
  d: "A negative pai amount if sending payment; a positive pai amount if receiving payment (including coinbases)"


- n: "→ → →<br>vout"
  t: "number(int)"
  p: "Required<br>(exactly 1)"
  d: "For an output, the output index (vout) for this output in this transaction. For an input, the output index for the output being spent in its transaction. Because inputs list the output indexes from previous transactions, more than one entry in the details array may have the same output index"

- n: "→ → →<br>fee"
  t: "number(pai's)"
  p: "Optional<br>(0 or 1)"
  d: "If sending payment, the fee paid as a negative pai's value. May be 0. Not returned if receiving payment"

- n: "→ → →<br>confirmations"
  t: "number(int)"
  p: "Required<br>(exactly 1)"
  d: "The number of confirmations the transaction has received. Will be 0 for unconfirmed and -1 for conflicted"

- n: "→ → →<br>generated"
  t: "bool"
  p: "Optional<br>(0 or 1)"
  d: "Set to true if the transaction is a coinbase. Not returned for regular transactions"

- n: "→ → →<br>blockhash"
  t: "string(hex)"
  p: "Optional<br>(0 or 1)"
  d: "The hash of the block on the local best block chain which includes this transaction, encoded as hex in RPC byte order. Only returned for confirmed transactions"

- n: "→ → →<br>blockindex"
  t: "number(int)"
  p: "Optional<br>(0 or 1)"
  d: "The index of the transaction in the block that includes it. Only returned for confirmed transactions"

- n: "→ → →<br>blocktime"
  t: "number(int)"
  p: "Optional<br>(0 or 1)"
  d: "The block header time (Unix epoch time) of the block on the local best block chain which includes this transaction. Only returned for confirmed transactions"

- n: "→ → → →<br>TXID"
  t: "string(hex)"
  p: "Optional<br>(0 or more)"
  d: "The TXID of a conflicting transaction, encoded as hex in RPC byte order"

- n: "→ → → <br>time"
  t: "number(int)"
  p: "Required<br>(exactly 1)"
  d: "A Unix epoch time when the transaction was added to the wallet"

- n: "→ → → <br>timeeceived"
  t: "number(int)"
  p: "Required<br>(exactly 1)"
  d: "A Unix epoch time when the transaction was detected by the local node, or the time of the block on the local best block chain that included the transaction"

- n: "→ → → <br>bip 125-replaceable"
  t: "string"
  p: "Required<br>(exactly 1)"
  d: "Added in Pai Core 0.12.0

    Indicates if a transaction is replaceable under BIP 125:
    • yes is replaceable
    • no not replaceable
    • unknown for unconfirmed transactions not in the mempool"

- n: "→→→<br>comment"
  t: "string"
  p: "Optional<br>(0 or 1)"
  d: "For transaction originating with this wallet, a locally-stored comment added to the transaction. Only returned if a comment was added"

- n: "→→→<br>to"
  t: "string"
  p: "Optional<br>(0 or 1)"
  d: "For transaction originating with this wallet, a locally-stored comment added to the transaction identifying who the transaction was sent to. Only returned if a comment-to was added"

- n: "→<br>`lastblock`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The header hash of the block with the number of confirmations specified in the *target confirmations* parameter, encoded as hex in RPC byte order"

{% enditemplate %}

*Example from Pai Core 0.13.1*

Get all transactions since a particular block (including watch-only
transactions) and the header hash of the sixth most recent block.

```
pai-cli -testnet listsinceblock \
              00000000688633a503f69818a70eac281302e9189b1bb57a76a05c329fcda718 \
              6 true
```

Result (edited to show only two payments):

```
{
    "transactions" : [
        {
            "account" : "doc test",
            "address" : "mmXgiR6KAhZCyQ8ndr2BCfEq1wNG2UnyG6",
            "category" : "receive",
            "amount" : 0.10000000,
            "vout" : 0,
            "confirmations" : 76478,
            "blockhash" : "000000000017c84015f254498c62a7c884a51ccd75d4dd6dbdcb6434aa3bd44d",
            "blockindex" : 1,
            "blocktime" : 1399294967,
            "txid" : "85a98fdf1529f7d5156483ad020a51b7f3340e47448cf932f470b72ff01a6821",
            "walletconflicts" : [
            ],
            "time" : 1399294967,
            "timereceived" : 1418924714,
            "bip125-replaceable": "no"    
        },
        {
            "involvesWatchonly" : true,
            "account" : "someone else's address2",
            "address" : "n3GNqMveyvaPvUbH469vDRadqpJMPc84JA",
            "category" : "receive",
            "amount" : 0.00050000,
            "vout" : 0,
            "confirmations" : 34714,
            "blockhash" : "00000000bd0ed80435fc9fe3269da69bb0730ebb454d0a29128a870ea1a37929",
            "blockindex" : 11,
            "blocktime" : 1411051649,
            "txid" : "99845fd840ad2cc4d6f93fafb8b072d188821f55d9298772415175c456f3077d",
            "walletconflicts" : [
            ],
            "time" : 1418695703,
            "timereceived" : 1418925580,
            "bip125-replaceable": "no"
        }
    ],
    "lastblock" : "0000000000984add1a686d513e66d25686572c7276ec3e358a7e3e9f7eb88619"
}
```

*See also*

* `ListReceivedByAccount`: lists the total number of pai's received by each account.
* `ListReceivedByAddress`: lists the total number of pai's received by each address.
