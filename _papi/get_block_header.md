---
title: 'Get Block Header'
image: '/docs/noun_591323.png'
---

The `getblockheader` RPC gets a block header with a particular header hash from the local block database either as a JSON object or as a serialized block header.

*Parameter #1---header hash*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
|Header Hash  |string (hex) | Required<br>(exactly 1) | The hash of the block header to get, encoded as hex in RPC byte order
| Format | bool | Optional<br>(0 or 1) | Set to `false` to get the block header in serialized block format; set to `true` (the default) to get the decoded block header as a JSON object


*Parameter #2---JSON or hex output*

{% include table_header.md
  n= "Format"
  t= "bool"
  p= "Optional<br>(0 or 1)"
  d= ""
%}

*Result (if format was `false`)---a serialized block header*

{% include table_header.md
  n= "`result`"
  t= "string (hex)/null"
  p= "Required<br>(exactly 1)"
  d= "The requested block header as a serialized block, encoded as hex, or JSON `null` if an error occurred"
%}

*Result (if format was `true` or omitted)---a JSON block header*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result` |object/null | Required<br>(exactly 1) | An object containing the requested block, or JSON `null` if an error occurred
| →<br>`hash` | string (hex) | Required<br>(exactly 1) | The hash of this block's block header encoded as hex in RPC byte order.  This is the same as the hash provided in parameter #1
| →<br>`confirmations` | number (int) | Required<br>(exactly 1) | The number of confirmations the transactions in this block have, starting at 1 when this block is at the tip of the best block chain.  This score will be -1 if the the block is not part of the best block chain
| →<br>`height` | number (int) | Required<br>(exactly 1) | The height of this block on its block chain
| →<br>`version` | number (int) | Required<br>(exactly 1) | This block's version number.
| →<br>`versionHex` | number (int) | Required<br>(exactly 1) | This block's hex version number.
| <br>`merkleroot` | string (hex) | Required<br>(exactly 1) | The merkle root for this block, encoded as hex in RPC byte order
| →<br>`time` | number (int) | Required<br>(exactly 1) | The value of the time field in the block header, indicating approximately when the block was created
| →<br>`mediantime` | number (int) | Required<br>(exactly 1) | The computed median time of the previous 11 blocks.  Used for validating transaction locktime under BIP113
| →<br>`nonce` | number (int) | Required<br>(exactly 1) | The nonce which was successful at turning this particular block into one that could be added to the best block chain
| →<br>`bits` | string (hex) | Required<br>(exactly 1) | The value of the *nBits* field in the block header, indicating the target threshold this block's header had to pass
| →<br>`difficulty` | number (real) | Required<br>(exactly 1) | The estimated amount of work done to find this block relative to the estimated amount of work done to find block 0
| →<br>`chainwork` | string (hex) | Required<br>(exactly 1) | The estimated number of block header hashes miners had to check from the genesis block to this block, encoded as big-endian hex
| →<br>`previousblockhash` | string (hex) | Optional<br>(0 or 1) | The hash of the header of the previous block, encoded as hex in RPC byte order.  Not returned for genesis block
| →<br>`nextblockhash` | string (hex) | Optional<br>(0 or 1) | The hash of the next block on the best block chain, if known, encoded as hex in RPC byte order


*Example*

Get a block header in raw hex:

```
pai-cli -testnet getblockheader \
            00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09 \
            false
```

Result (wrapped):

```
010000007de867cc8adc5cc8fb6b898ca4462cf9fd667d7830a275277447e608\
00000000338f121232e169d3100edd82004dc2a1f0e1f030c6c488fa61eafa93\
0b0528fe021f7449ffff001d36b4af9a

```

Get the same block in JSON:

```
pai-cli -testnet getblockheader \
            00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09
```

Result:

```

{
  "hash": "00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09",
  "confirmations": 437926,
  "height": 1000,
  "version": 1,
  "versionHex": "00000001",
  "merkleroot": "fe28050b93faea61fa88c4c630f0e1f0a1c24d0082dd0e10d369e13212128f33",
  "time": 1232346882,
  "mediantime": 1232344831,
  "nonce": 2595206198,
  "bits": "1d00ffff",
  "difficulty": 1,
  "chainwork": "000000000000000000000000000000000000000000000000000003e903e903e9",
  "previousblockhash": "0000000008e647742775a230787d66fdf92c46a48c896bfbc85cdc8acc67e87d",
  "nextblockhash": "00000000a2887344f8db859e372e7e4bc26b23b9de340f725afbf2edb265b4c6"
}

```

*See also*

* `GetBlock`: gets a block with a particular header hash from the local block database either as a JSON object or as a serialized block.
* `GetBlockHash`: returns the header hash of a block at the given height in the local best block chain.
* `GetBestBlockHash`: eturns the header hash of the most recent block on the best block chain.
