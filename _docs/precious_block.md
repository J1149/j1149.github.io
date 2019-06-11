---
layout: service
title: PreciousBlock
parent: PAI Core Apis
grand_parent: Developer Reference
---

The `preciousblock` RPC treats a block as if it were received before others with the same work. A later preciousblock call can override the effect of an earlier one. The effects of preciousblock are not retained across restarts.

*Parameter #1---the block hash*

{% include table_header.md
  n= "Header Hash"
  t= "string (hex)"
  p= "Required<br>(exactly 1)"
  d= "The hash of the block to mark as precious"
%}

*Result---`null` or error on failure*

{% include table_header.md
  n= "`result`"
  t= "null"
  p= "Required<br>(exactly 1)"
  d= "JSON `null`.  The JSON-RPC error field will be set only if you entered an invalid block hash"
%}

*Example*

```
pai-cli preciousblock 000000000000000001517a0bac70b8cd6f27ee\
PaXVxzkruFZPidQjsDft9CW174Tr99xngu
```

Result (no output from `pai-cli` because result is set to `null`).
