---
layout: service
title: ListSinceBlock
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.*

The `listsinceblock` RPC gets all transactions affecting the wallet which have occurred since a particular block, plus the header hash of a block at a particular depth.

*Parameter #1---a block header hash*

{% include table_header.md
  n= "Header Hash"
  t= "string (hex)"
  p= "Optional<br>(0 or 1)"
  d= "The hash of a block header encoded as hex in RPC byte order.  All transactions affecting the wallet which are not in that block or any earlier block will be returned, including unconfirmed transactions.  Default is the hash of the genesis block, so all transactions affecting the wallet are returned by default"
%}

*Parameter #2---the target confirmations for the lastblock field*

{% include table_header.md
  n= "Target Confirmations"
  t= "number (int)"
  p= "Optional<br>(0 or 1)"
  d= "Sets the lastblock field of the results to the header hash of a block with this many confirmations.  This does not affect which transactions are returned.  Default is `1`, so the hash of the most recent block on the local best block chain is returned"
%}

*Parameter #3---whether to include watch-only addresses in details and calculations*

{% include table_header.md
  n= "Include Empty"
  t= "bool"
  p= "Optional<br>(0 or 1)"
  d= "Set to `true` to display accounts which have never received a payment.  Set to `false` (the default) to only include accounts which have received a payment.  Any account which has received a payment will be displayed even if its current balance is `0`"
%}


**Result**

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  | object | Required<br>(exactly 1) | An object containing an array of transactions and the lastblock field
| →<br>`transactions` | array | Required<br>(exactly 1) | An array of objects each describing a particular **payment** to or from this wallet.  The objects in this array do not describe an actual transactions, so more than one object in this array may come from the same transaction.  This array may be empty
| → →<br>Payment | object | Optional<br>(0 or more) | An payment which did not appear in the specified block or an earlier block
| → →<br>involvesWatchOnly | bool | Optional<br>(0 or more) | Set to true if the payment involves a watch-only address. Otherwise not returned
| → →<br>account | string | Required<br>(exactly 1) | The account which the payment was credited to or debited from. May be an empty string (“”) for the default account
| → →<br>address | string(base58) | Optional<br>(0 or 1) | The address paid in this payment, which may be someone else’s address not belonging to this wallet. May be empty if the address is unknown, such as when paying to a non-standard pubkey script
| → → →<br>category | string | required<br>(exactly 1) | Set to one of the following values: <br> • send if sending payment <br> • receive if this wallet received payment in a regular transaction <br> • generate if a matured and spendable coinbase <br> • immature if a coinbase that is not spendable yet <br> • orphan if a coinbase from a block that’s not in the local best block chain
| → → →<br>amount | number(pai's) | Required<br>(exactly 1) | A negative pai amount if sending payment; a positive pai amount if receiving payment (including coinbases)
| → → →<br>vout | number(int) | Required<br>(exactly 1) | For an output, the output index (vout) for this output in this transaction. For an input, the output index for the output being spent in its transaction. Because inputs list the output indexes from previous transactions, more than one entry in the details array may have the same output index
| → → →<br>fee | number(pai's) | Optional<br>(0 or 1) | If sending payment, the fee paid as a negative pai's value. May be 0. Not returned if receiving payment
| → → →<br>confirmations | number(int) | Required<br>(exactly 1) | The number of confirmations the transaction has received. Will be 0 for unconfirmed and -1 for conflicted
| → → →<br>generated | bool | Optional<br>(0 or 1) | Set to true if the transaction is a coinbase. Not returned for regular transactions
| → → →<br>blockhash | string(hex) | Optional<br>(0 or 1) | The hash of the block on the local best block chain which includes this transaction, encoded as hex in RPC byte order. Only returned for confirmed transactions
| → → →<br>blockindex | number(int) | Optional<br>(0 or 1) | The index of the transaction in the block that includes it. Only returned for confirmed transactions"
| → → →<br>blocktime | number(int) | Optional<br>(0 or 1) | The block header time (Unix epoch time) of the block on the local best block chain which includes this transaction. Only returned for confirmed transactions
| → → → →<br>TXID | string(hex) | Optional<br>(0 or more) | The TXID of a conflicting transaction, encoded as hex in RPC byte order
| → → → <br>time | number(int) | Required<br>(exactly 1) | A Unix epoch time when the transaction was added to the wallet
| → → → <br>timeeceived | number(int) | Required<br>(exactly 1) | A Unix epoch time when the transaction was detected by the local node, or the time of the block on the local best block chain that included the transaction
| → → → <br>bip 125-replaceable | string | Required<br>(exactly 1) | Indicates if a transaction is replaceable under BIP 125: <br> • yes is replaceable <br> • no not replaceable <br> • unknown for unconfirmed transactions not in the mempool"
| →→→<br>comment | string | Optional<br>(0 or 1) | For transaction originating with this wallet, a locally-stored comment added to the transaction. Only returned if a comment was added
| →→→<br>to | string | Optional<br>(0 or 1) | For transaction originating with this wallet, a locally-stored comment added to the transaction identifying who the transaction was sent to. Only returned if a comment-to was added
| →<br>`lastblock` | string (hex) | Required<br>(exactly 1) | The header hash of the block with the number of confirmations specified in the *target confirmations* parameter, encoded as hex in RPC byte order


*Example*

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
            "address" : "PaXVxzkruFZPidQjsDft9CW174Tr99xngu",
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
            "address" : "PFZPidQjsDft9CW174Tr99xnguJMPc84JA",
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
