---
layout: service
title: Help
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `help` RPC lists all available public RPC commands, or gets help for the specified RPC. Commands which are unavailable will not be listed, such as wallet RPCs if wallet support is disabled.

*Parameter---the name of the RPC to get help for*

{% include table_header.md
  n= "RPC"
  t= "string"
  p= "Optional<br>(0 or 1)"
  d= "The name of the RPC to get help for."
%}

*Result---a list of RPCs or detailed help for a specific RPC*

{% include table_header.md
  n= "`result`"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The help text for the specified RPC or the list of commands.  The `pai-cli` command will parse this text and format it as human-readable text"
%}

*Example*

Command to get help about the `help` RPC:

```
pai-cli -testnet help help
```

Result:

```
help ( "command" )

List all commands, or get help for a specified command.

Arguments:
1. "command"     (string, optional) The command to get help on

Result:
"text"     (string) The help text

```

*See also*

* `The RPC Quick Reference`
