---
layout: default
title: ControlMessages
parent: P2P
grand_parent: Developer Reference
---

ControlMessages
======================

The following network messages all help control the connection between
two peers or allow them to advise each other about the rest of the
network.

![Overview Of P2P Protocol Control And Advisory Messages](https://bitcoin.org/img/dev/en-p2p-control-messages.svg?1551020757)

Note that almost none of the control messages are authenticated in any
way, meaning they can contain incorrect or intentionally harmful
information. In addition, this section does not yet cover P2P protocol
operation over the [Tor network][tor]; if you would like to contribute
information about Tor, please [open an issue][docs issue].
