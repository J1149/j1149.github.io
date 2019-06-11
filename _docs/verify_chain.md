---
layout: service
title: VerifyChain
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `verifychain` RPC verifies each entry in the local block chain database.

*Parameter #1---how thoroughly to check each block*

{% include table_header.md
  n= "Check Level"
  t= "number (int)"
  p= "Optional<br>(0 or 1)"
  d= "How thoroughly to check each block, from 0 to 4.  Default is the level set with the `-checklevel` command line argument; if that isn't set, the default is `3`.  Each higher level includes the tests from the lower levels<br><br>Levels are:<br>**0.** Read from disk to ensure the files are accessible<br>**1.**  Ensure each block is valid<br>**2.** Make sure undo files can be read from disk and are in a valid format<br>**3.** Test each block undo to ensure it results in correct state<br>**4.** After undoing blocks, reconnect them to ensure they reconnect correctly"
%}

*Parameter #2---the number of blocks to check*

{% include table_header.md
  n= "Number Of Blocks"
  t= "number (int)"
  p= "Optional<br>(0 or 1)"
  d= "The number of blocks to verify.  Set to `0` to check all blocks.  Defaults to the value of the `-checkblocks` command-line argument; if that isn't set, the default is `288`"
%}

*Result---verification results*

{% include table_header.md
  n= "`result`"
  t= "bool"
  p= "Required<br>(exactly 1)"
  d= "Set to `true` if verified; set to `false` if verification failed for any reason"
%}

*Example*

Verify the most recent 10,000 blocks in the most through way:

```
pai-cli -testnet verifychain 4 10000
```

Result (took 4 minutes and 25 seconds on a generic PC laptop; it
would've taken much longer on mainnet):

```
true
```

*See also*

* `GetBlockChainInfo`: provides information about the current state of the block chain.
* `GetTxOutSetInfo`: returns statistics about the confirmed unspent transaction output (UTXO) set. Note that this call may take some time and that it only counts outputs from confirmed transactions—it does not count outputs from the memory pool.
