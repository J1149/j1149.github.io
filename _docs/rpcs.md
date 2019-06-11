---
layout: service
title: RPCs
parent: PAI Core Apis
grand_parent: Developer Reference
---


The block chain and memory pool can include arbitrary data which several of the commands below will return in hex format. If you convert this data to another format in an executable context, it could be used in an exploit. For example, displaying a pubkey script as ASCII text in a webpage could add arbitrary Javascript to that page and create a cross-site scripting (XSS) exploit. To avoid problems, please treat PAI and memory pool data as an arbitrary input from an untrusted source.