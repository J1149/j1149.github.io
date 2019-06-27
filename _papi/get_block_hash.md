---
title: 'Get Block Hash'
image: '/docs/noun_591323.png'
---

The `getblockhash` RPC returns the header hash of a block at the given height in the local best block chain.

*Parameter---a block height*

{% include table_header.md
  n= "Block Height"
  t= "number (int)"
  p= "Required<br>(exactly 1)"
  d= "The height of the block whose header hash should be returned.  The height of the hardcoded genesis block is 0"
%}

*Result---the block header hash*

{% include table_header.md
  n= "`result`"
  t= "string (hex)/null"
  p= "Required<br>(exactly 1)"
  d= "The hash of the block at the requested height, encoded as hex in RPC byte order, or JSON `null` if an error occurred"
%}

*Example*

```
pai-cli -testnet getblockhash 240886
```

Result:

```
00000000a0faf83ab5799354ae9c11da2a2bd6db44058e03c528851dee0a3fff
```

*See also*

* `GetBlock`: gets a block with a particular header hash from the local block database either as a JSON object or as a serialized block.
* `GetBestBlockHash`: returns the header hash of the most recent block on the best block chain.
