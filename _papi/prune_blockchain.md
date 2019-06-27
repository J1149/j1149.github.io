---
layout: service
title: PruneBlockChain
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `pruneblockchain` RPC prunes the blockchain up to a specified height or timestamp. The -prune option needs to be enabled (disabled by default).

*Parameter #1---the block height or timestamp*

{% include table_header.md
  n= "Height"
  t= "number (int)"
  p= "Required<br>(exactly 1)"
  d= "The block height to prune up to. May be set to a particular height, or a unix timestamp to prune blocks whose block time is at least 2 hours older than the provided timestamp"
%}

*Result---the height of the last block pruned*

{% include table_header.md
  n= "`result`"
  t= "number (int)"
  p= "Required<br>(exactly 1)"
  d= "The height of the last block pruned"
%}

*Examples*

```
pai-cli pruneblockchain 413555
```

Result:

```
413555
```

*See also*

* `ImportPrunedFunds`: imports funds without the need of a rescan. Meant for use with pruned wallets.
