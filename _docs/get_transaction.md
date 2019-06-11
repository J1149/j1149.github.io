---
layout: service
title: GetTransaction
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.*

The `gettransaction` RPC gets detailed information about an in-wallet transaction.

*Parameter #1---a transaction identifier (TXID)*

{% include table_header.md
  n= "TXID"
  t= "string (hex)"
  p= "Required<br>(exactly 1)"
  d= "The TXID of the transaction to get details about.  The TXID must be encoded as hex in RPC byte order"
%}

*Parameter #2---whether to include watch-only addresses in details and calculations*

*Result---a description of the transaction*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  | object | Required<br>(exactly 1) | An object describing how the transaction affects the wallet
| →<br>`amount` | number (pai's) | Required<br>(exactly 1) | A positive number of pai's if this transaction increased the total wallet balance; a negative number of pai's if this transaction decreased the total wallet balance, or `0` if the transaction had no net effect on wallet balance
| →<br>`fee` | number (pai's) | Optional<br>(0 or 1) | If an outgoing transaction, this is the fee paid by the transaction reported as negative pai's
| →<br>`details` | array | Required<br>(exactly 1) | An array containing one object for each input or output in the transaction which affected the wallet
| → → <br>`involvesWatchonly` | bool | Optional<br>(0 or 1) | Set to `true` if the input or output involves a watch-only address.  Otherwise not returned
| → →<br>`account` | string | Required<br>(exactly 1) | The account which the payment was credited to or debited from.  May be an empty string (\"\") for the default account
| → →<br>`address` | string (base58) | Optional<br>(0 or 1) | If an output, the address paid (may be someone else's address not belonging to this wallet).  If an input, the address paid in the previous output.  May be empty if the address is unknown, such as when paying to a non-standard pubkey script
| → →<br>`category` | string | Required<br>(exactly 1) | Set to one of the following values:<br>• `send` if sending payment<br>• `receive` if this wallet received payment in a regular transaction<br>• `generate` if a matured and spendable coinbase<br>• `immature` if a coinbase that is not spendable yet<br>• `orphan` if a coinbase from a block that's not in the local best block chain
| → →<br>`amount` | number (pai's) | Required<br>(exactly 1) | A negative pai amount if sending payment; a positive pai amount if receiving payment (including coinbases)
| → →<br>`vout` | number(int) | Required<br>(exactly 1) | For an output, the output index (vout) for this output in this transaction.  For an input, the output index for the output being spent in its transaction.  Because inputs list the output indexes from previous transactions, more than one entry in the details array may have the same output index
| → →<br>`fee` | number (pai's) | Optional<br>(0 or 1) | If sending payment, the fee paid as a negative pai's value.  May be `0`.  Not returned if receiving payment
| → →<br>`abandoned` | bool | Optional<br>(0 or 1) | *Indicates if a transaction is was abandoned:<br>• `true` if it was abandoned (inputs are respendable)<br>• `false`  if it was not abandoned<br>Only returned by *send* category payments
| →<br>`hex` | string (hex) | Required<br>(exactly 1) | The transaction in serialized transaction format


*Example*

```
pai-cli -testnet gettransaction \
  5a7d24cd665108c66b2d56146f244932edae4e2376b561b3d396d5ae017b9589
```

Result:

```
{
    "amount" : 0.00000000,
    "fee" : 0.00000000,
    "confirmations" : 106670,
    "blockhash" : "000000008b630b3aae99b6fe215548168bed92167c47a2f7ad4df41e571bcb51",
    "blockindex" : 1,
    "blocktime" : 1396321351,
    "txid" : "5a7d24cd665108c66b2d56146f244932edae4e2376b561b3d396d5ae017b9589",
    "walletconflicts" : [
    ],
    "time" : 1396321351,
    "timereceived" : 1418924711,
    "bip125-replaceable" : "no",
    "details" : [
        {
            "account" : "",
            "address" : "mjSk1Ny9spzU2fouzYgLqGUD8U41iR35QN",
            "category" : "send",
            "amount" : -0.10000000,
            "vout" : 0,
            "fee" : 0.00000000
        },
        {
            "account" : "doc test",
            "address" : "mjSk1Ny9spzU2fouzYgLqGUD8U41iR35QN",
            "category" : "receive",
            "amount" : 0.10000000,
            "vout" : 0
        }
    ],
    "hex" : "0100000001cde58f2e37d000eabbb60d9cf0b79ddf67cede6dba58732539983fa341dd5e6c010000006a47304402201feaf12908260f666ab369bb8753cdc12f78d0c8bdfdef997da17acff502d321022049ba0b80945a7192e631c03bafd5c6dc3c7cb35ac5c1c0ffb9e22fec86dd311c01210321eeeb46fd878ce8e62d5e0f408a0eab41d7c3a7872dc836ce360439536e423dffffffff0180969800000000001976a9142b14950b8d31620c6cc923c5408a701b1ec0a02088ac00000000"
}
```

*See also*

* `GetRawTransaction`: gets a hex-encoded serialized transaction or a JSON object describing the transaction. By default, Pai Core only stores complete transaction data for UTXOs and your own transactions, so the RPC may fail on historic transactions unless you use the non-default txindex=1 in your Pai Core startup settings.

