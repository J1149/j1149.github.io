---
layout: default
title: Stop
parent: PAI Core Apis
grand_parent: Developer Reference
---

Stop
=======================

The `stop` RPC safely shuts down the Pai Core server.

*Parameters: none*

*Result---the server is safely shut down*

{% include table_header.md
  n= "`result`"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The string \"Pai server stopping\""
%}

*Example from Pai Core 0.10.0*

```
pai-cli -testnet stop
```

Result:

```
pai server stopping
```
