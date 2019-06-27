---
layout: service
title: Stop
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `stop` RPC safely shuts down the Pai Core server.

*Parameters: none*

*Result---the server is safely shut down*

{% include table_header.md
  n= "`result`"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The string \"Pai server stopping\""
%}

*Example*

```
pai-cli -testnet stop
```

Result:

```
pai server stopping
```
