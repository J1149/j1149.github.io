---
layout: default
title: Protocol Versions
parent: P2P
grand_parent: Developer Reference
---

ProtocolVersions
=================

The table below lists some notable versions of the P2P network protocol,
with the most recent versions listed first. (If you know of a protocol
version that implemented a major change but which is not listed here,
please [open an issue][docs issue].)

As of Pai Core 0.14.2, the most recent protocol version is 70015.

| Version | Initial Release                    | Major Changes
|---------|------------------------------------|--------------
| 70015   | Pai Core 0.13.2 <br>(Jan 2017) | • New banning behavior for invalid compact blocks [#9026](https://github.com/Pai/Pai/pull/9026) in v0.14.0, Backported to v0.13.2 in [#9048](https://github.com/Pai/Pai/pull/9048).
| 70014   | Pai Core 0.13.0 <br>(Aug 2016) | [BIP152][]: <br>• Added `sendcmpct`, `cmpctblock`, `getblocktxn`, `blocktxn` messages <br> • Added `MSG_CMPCT_BLOCK` inventory type to `getdata` message.
| 70013   | Pai Core 0.13.0 <br>(Aug 2016) | [BIP133][]: <br>• Added `feefilter` message.<br> • Removed `alert` message system. See [Alert System Retirement](https://Pai.org/en/alert/2016-11-01-alert-retirement)
| 70012   | Pai Core 0.12.0 <br>(Feb 2016) | [BIP130][]: <br>• Added `sendheaders` message.
| 70011   | Pai Core 0.12.0 <br>(Feb 2016) | [BIP111][]: <br>• `filter*` messages are disabled without NODE_BLOOM after and including this version.
| 70002   | Pai Core 0.9.0 <br>(Mar 2014)  | • Send multiple `inv` messages in response to a `mempool` message if necessary <br><br>[BIP61][]: <br>• Added `reject` message
| 70001   | Pai Core 0.8.0 <br>(Feb 2013)  | • Added `notfound` message. <br><br>[BIP37][]: <br>• Added `filterload` message. <br>• Added `filteradd` message. <br>• Added `filterclear` message. <br>• Added `merkleblock` message. <br>• Added relay field to `version` message <br>• Added `MSG_FILTERED_BLOCK` inventory type to `getdata` message.
| 60002   | Pai Core 0.7.0 <br>(Sep 2012)  | [BIP35][]: <br>• Added `mempool` message. <br>• Extended `getdata` message to allow download of memory pool transactions
| 60001   | Pai Core 0.6.1 <br>(May 2012)  | [BIP31][]: <br>• Added nonce field to `ping` message <br>• Added `pong` message
| 60000   | Pai Core 0.6.0 <br>(Mar 2012)  | [BIP14][]: <br>• Separated protocol version from Pai Core version
| 31800   | Pai Core 0.3.18 <br>(Dec 2010) | • Added `getheaders` message and `headers` message.
| 31402   | Pai Core 0.3.15 <br>(Oct 2010) | • Added time field to `addr` message.
| 311     | Pai Core 0.3.11 <br>(Aug 2010) | • Added `alert` message.
| 209     | Pai Core 0.2.9 <br>(May 2010)  | • Added checksum field to message headers, added `verack` message, and added starting height field to `version` message.
| 106     | Pai Core 0.1.6 <br>(Oct 2009)  | • Added transmitter IP address fields, nonce, and User Agent (subVer) to `version` message.
