---
layout: default
title: SetGenerate
parent: PAI Core Apis
grand_parent: Developer Reference
---

SetGenerate
=======================

*Requires wallet support.*

The `setgenerate` RPC was removed in Pai Core 0.13.0. If you have an older version of Pai Core, use help setgenerate RPC to get help. For testing, the generate call can still be used to mine a block, and the generatetoaddress RPC call has been added to mine to a specific address. This works with wallet disabled.

*See also*

* `Generate`: nearly instantly generates blocks.
* `GenerateToAddress`: mines blocks immediately to a specified address.
* `GetMiningInfo`: returns various mining-related information.
* `GetBlockTemplate`: gets a block template or proposal for use with mining software.
