---
layout: service
title: GetRawTransaction
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `getrawtransaction` RPC gets a hex-encoded serialized transaction or a JSON object describing the transaction. By default, Pai Core only stores complete transaction data for UTXOs and your own transactions, so the RPC may fail on historic transactions unless you use the non-default txindex=1 in your Pai Core startup settings.

*Parameter #1---the TXID of the transaction to get*

{% include table_header.md
  n= "TXID"
  t= "string (hex)"
  p= "Required<br>(exactly 1)"
  d= "The TXID of the transaction to get, encoded as hex in RPC byte order"
%}

*Parameter #2---whether to get the serialized or decoded transaction*

{% include table_header.md
  n= "Format"
  t= "bool"
  p= "Optional<br>(0 or 1)"
  d= "Set to `false` (the default) to return the serialized transaction as hex.  Set to `true` to return a decoded transaction."
%}

*Result (if transaction not found)---`null`*

{% include table_header.md
  n= "`result`"
  t= "null"
  p= "Required<br>(exactly 1)"
  d= "If the transaction wasn't found, the result will be JSON `null`.  This can occur because the transaction doesn't exist in the block chain or memory pool, or because it isn't part of the transaction index.  See the Pai Core `-help` entry for `-txindex`"
%}

*Result (if verbose=`false`)---the serialized transaction*

{% include table_header.md
  n= "`result`"
  t= "string (hex)"
  p= "Required<br>(exactly 1)"
  d= "If the transaction was found, this will be the serialized transaction encoded as hex"
%}

*Result (if verbose=`true`)---the decoded transaction*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  | object | Required<br>(exactly 1) | If the transaction was found, this will be an object describing it
| →<br>`hex` | string (hex) | Required<br>(exactly 1) | The serialized, hex-encoded data for the provided `txid`
| →<br>`blockhash` | string (hex) | Optional<br>(0 or 1) | If the transaction has been included in a block on the local best block chain, this is the hash of that block encoded as hex in RPC byte order
| →<br>`confirmations` | number (int) | Required<br>(exactly 1) | If the transaction has been included in a block on the local best block chain, this is how many confirmations it has.  Otherwise, this is `0`
| →<br>`time` | number (int) | Optional<br>(0 or 1) | If the transaction has been included in a block on the local best block chain, this is the block header time of that block (may be in the future)
| →<br>`blocktime` | number (int) | Optional<br>(0 or 1) | This field is currently identical to the time field described above


*Examples*

A transaction in serialized transaction format:

```
pai-cli getrawtransaction \
  52309405287e737cf412fc42883d65a392ab950869fae80b2a5f1e33326aca46
```

Result (wrapped):

```
0100000001bafe2175b9d7b3041ebac529056b393cf2997f7964485aa382ffa4\
49ffdac02a000000008a473044022013d212c22f0b46bb33106d148493b9a972\
3adb2c3dd3a3ebe3a9c9e3b95d8cb00220461661710202fbab550f973068af45\
c294667fc4dc526627a7463eb23ab39e9b01410479be667ef9dcbbac55a06295\
ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc\
0e1108a8fd17b448a68554199c47d08ffb10d4b8ffffffff01b0a86a00000000\
001976a91401b81d5fa1e55e069e3cc2db9c19e2e80358f30688ac00000000
```

Get the same transaction in JSON:

```
pai-cli getrawtransaction \
ef7c0cbf6ba5af68d2ea239bba709b26ff7b0b669839a63bb01c2cb8e8de481e \
true
```

Result:

```
{
    "hex": "0100000001bafe2175b9d7b3041ebac529056b393cf2997f7964485aa382ffa449ffdac02a000000008a473044022013d212c22f0b46bb33106d148493b9a9723adb2c3dd3a3ebe3a9c9e3b95d8cb00220461661710202fbab550f973068af45c294667fc4dc526627a7463eb23ab39e9b01410479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8ffffffff01b0a86a00000000001976a91401b81d5fa1e55e069e3cc2db9c19e2e80358f30688ac00000000",
    "txid": "52309405287e737cf412fc42883d65a392ab950869fae80b2a5f1e33326aca46",
    "hash": "52309405287e737cf412fc42883d65a392ab950869fae80b2a5f1e33326aca46",
    "size": 223,
    "vsize": 223,
    "version": 1,
    "locktime": 0,
    "vin": [
        {
            "txid": "2ac0daff49a4ff82a35a4864797f99f23c396b0529c5ba1e04b3d7b97521feba",
            "vout": 0,
            "scriptSig": {
                "asm": "3044022013d212c22f0b46bb33106d148493b9a9723adb2c3dd3a3ebe3a9c9e3b95d8cb00220461661710202fbab550f973068af45c294667fc4dc526627a7463eb23ab39e9b[ALL] 0479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8",
                "hex": "473044022013d212c22f0b46bb33106d148493b9a9723adb2c3dd3a3ebe3a9c9e3b95d8cb00220461661710202fbab550f973068af45c294667fc4dc526627a7463eb23ab39e9b01410479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8"
            },
            "sequence": 4294967295
        }
    ],
    "vout": [
        {
            "value": 0.06990000,
            "n": 0,
            "scriptPubKey": {
                "asm": "OP_DUP OP_HASH160 01b81d5fa1e55e069e3cc2db9c19e2e80358f306 OP_EQUALVERIFY OP_CHECKSIG",
                "hex": "76a91401b81d5fa1e55e069e3cc2db9c19e2e80358f30688ac",
                "reqSigs": 1,
                "type": "pubkeyhash",
                "addresses": [
                    "1A6Ei5cRfDJ8jjhwxfzLJph8B9ZEthR9Z"
                ]
            }
        }
    ],
    "blockhash": "0000000000000000015955e197fc362502a32f76290e5b5e5be822f9f161b3f3",
    "confirmations": 374,
    "time": 1483591778,
    "blocktime": 1483591778
}
```

*See also*

* `GetTransaction`: gets detailed information about an in-wallet transaction.
