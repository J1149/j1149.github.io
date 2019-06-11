---
layout: service
title: ListTransactions
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.*

The `listtransactions` RPC returns the most recent transactions that affect the wallet.

*Parameter #1---an account name to get transactions from*

{% include table_header.md
  n= "Account"
  t= "string"
  p= "Optional<br>(0 or 1)"
  d= "The name of an account to get transactinos from.  Use an empty string (\"\") to get transactions for the default account.  Default is `*` to get transactions for all accounts."
%}

*Parameter #2---the number of transactions to get*

{% include table_header.md
  n= "Count"
  t= "number (int)"
  p= "Optional<br>(0 or 1)"
  d= "The number of the most recent transactions to list.  Default is `10`"
%}

*Parameter #3---the number of transactions to skip*

{% include table_header.md
  n= "Skip"
  t= "number (int)"
  p= "Optional<br>(0 or 1)"
  d= "The number of the most recent transactions which should not be returned.  Allows for pagination of results.  Default is `0`"
%}

*Parameter #4---whether to include watch-only addresses in details and calculations*

{% include table_header.md
  n= "Include Watch Only"
  t= "bool"
  p= "Optional<br>(0 or 1)"
  d= "If set to true, include watch-only addresses in details and calculations as if they were regular addresses belonging to the wallet. If set to false (the default), treat watch-only addresses as if they didn’t belong to this wallet"
%}


*Result---payment details*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  | array | Required<br>(exactly 1) | An array containing objects, with each object describing a **payment** or internal accounting entry (not a transaction).  More than one object in this array may come from a single transaction.  Array may be empty
| →<br>Payment | object | Optional<br>(0 or more) | A payment or internal accounting entry
| → →<br>`account` | string | Required<br>(exactly 1) | The account which the payment was credited to or debited from.  May be an empty string (\"\") for the default account
| → →<br>`address` | string (base58) | Optional<br>(0 or 1) | The address paid in this payment, which may be someone else's address not belonging to this wallet.  May be empty if the address is unknown, such as when paying to a non-standard pubkey script or if this is in the *move* category
| → →<br>`category` | string | Required<br>(exactly 1) | Set to one of the following values:<br>• `send` if sending payment<br>• `receive` if this wallet received payment in a regular transaction<br>• `generate` if a matured and spendable coinbase<br>• `immature` if a coinbase that is not spendable yet<br>• `orphan` if a coinbase from a block that's not in the local best block chain<br>• `move` if an off-block-chain move made with the `move` RPC
| → →<br>`amount` | number (pai's) | Required<br>(exactly 1) | A negative pai amount if sending payment; a positive pai amount if receiving payment (including coinbases)
| → →<br>`label` | string | Optional<br>(0 or 1) | A comment for the address/transaction
| → →<br>`vout` | number (int) | Optional<br>(0 or 1) | For an output, the output index (vout) for this output in this transaction.  For an input, the output index for the output being spent in its transaction.  Because inputs list the output indexes from previous transactions, more than one entry in the details array may have the same output index.  Not returned for *move* category payments
| → →<br>`fee` | number (pai's) | Optional<br>(0 or 1) | If sending payment, the fee paid as a negative pai's value.  May be `0`. Not returned if receiving payment or for *move* category payments
| → →<br>`confirmations` | number (int) | Optional<br>(0 or 1) | The number of confirmations the transaction has received.  Will be `0` for unconfirmed and `-1` for conflicted.  Not returned for *move* category payments
| → →<br>`trusted` | bool | Optional<br>(0 or 1) | Indicates whether we consider the outputs of this unconfirmed transaction safe to spend.  Only returned for unconfirmed transactions
| → →<br>`generated` | bool | Optional<br>(0 or 1) | Set to `true` if the transaction is a coinbase.  Not returned for regular transactions or *move* category payments
| → →<br>`blockhash` | string (hex) | Optional<br>(0 or 1) | The hash of the block on the local best block chain which includes this transaction, encoded as hex in RPC byte order.  Only returned for confirmed transactions
| → →<br>`blockindex` | number (int) | Optional<br>(0 or 1) | The index of the transaction in the block that includes it.  Only returned for confirmed transactions
| → →<br>`blocktime` | number (int) | Optional<br>(0 or 1) | The block header time (Unix epoch time) of the block on the local best block chain which includes this transaction.  Only returned for confirmed transactions
| → →<br>`txid` | string (hex) | Optional<br>(0 or 1) | The TXID of the transaction, encoded as hex in RPC byte order.  Not returned for *move* category payments
| → →<br>`walletconflicts` | array | Optional<br>(0 or 1) | An array containing the TXIDs of other transactions that spend the same inputs (UTXOs) as this transaction.  Array may be empty.  Not returned for *move* category payments
| → → →<br>TXID | string (hex) | Optional<br>(0 or more) | The TXID of a conflicting transaction, encoded as hex in RPC byte order
| → →<br>`time` | number (int) | Required<br>(exactly 1) | A Unix epoch time when the transaction was added to the wallet
| → →<br>`timereceived` | number (int) | Optional<br>(0 or 1) | A Unix epoch time when the transaction was detected by the local node, or the time of the block on the local best block chain that included the transaction.  Not returned for *move* category payments
| → →<br>`comment` | string | Optional<br>(0 or 1) | For transaction originating with this wallet, a locally-stored comment added to the transaction.  Only returned in regular payments if a comment was added.  Always returned in *move* category payments.  May be an empty string
| → →<br>`to` | string | Optional<br>(0 or 1) | For transaction originating with this wallet, a locally-stored comment added to the transaction identifying who the transaction was sent to.  Only returned if a comment-to was added.  Never returned by *move* category payments.  May be an empty string
| → →<br>`otheraccount` | string | Optional<br>(0 or 1) | This is the account the pai's were moved from or moved to, as indicated by a negative or positive *amount* field in this payment.  Only returned by *move* category payments
| → →<br>`bip125-replaceable` | string | Required<br>(exactly 1) | Indicates if a transaction is replaceable under BIP125:<br>• `yes` replaceable<br>• `no` not replaceable<br>• `unknown` for unconfirmed transactions not in the mempool
| → →<br>`abandoned` | bool | Optional<br>(0 or 1) | Indicates if a transaction is was abandoned:<br>• `true` if it was abandoned (inputs are respendable)<br>• `false`  if it was not abandoned<br>Only returned by *send* category payments


*Example*

List the most recent transaction from all accounts including watch-only addresses.

```
pai-cli listtransactions "*" 1 0 true
```

Result:

```
[
    {
        "involvesWatchonly" : true,
        "account" : "",
        "address" : "PaXVxzkruFZPidQjsDft9CW174Tr99xngu",
        "category" : "send",
        "amount" : -3.45902877,
        "vout" : 0,
        "fee" : -0.00032890,
        "confirmations" : 29710,
        "blockhash" : "0000000000000000008b9cb38cd3105e75af94b3af79d0a59cbe4edb618fb814",
        "blockindex" : 1705,
        "blocktime" : 1463173519,
        "txid" : "9b32d4315ac4c5e0d3a5fb947b9a198d3641698badc820643a7df23081f99695e",
        "walletconflicts" : [
        ],
        "time" : 1418695703,
        "timereceived" : 1418925580,
	"bip125-replaceable" : "no",
	"abandoned": false
    }
]
```

*See also*

* `GetTransaction`: gets detailed information about an in-wallet transaction.
* `ListSinceBlock`: gets all transactions affecting the wallet which have occurred since a particular block, plus the header hash of a block at a particular depth.
