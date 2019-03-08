---
layout: default
title: Help
parent: PAI Core Apis
grand_parent: Developer Reference
---

Help
========================

The `help` RPC lists all available public RPC commands, or gets help for the specified RPC. Commands which are unavailable will not be listed, such as wallet RPCs if wallet support is disabled.

*Parameter---the name of the RPC to get help for*

{% itemplate ntpd1 %}
- n: "RPC"
  t: "string"
  p: "Optional<br>(0 or 1)"
  d: "The name of the RPC to get help for.  If omitted, pai Core 0.9x will display an alphabetical list of commands; Pai Core 0.10.0 will display a categorized list of commands"

{% enditemplate %}

*Result---a list of RPCs or detailed help for a specific RPC*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "string"
  p: "Required<br>(exactly 1)"
  d: "The help text for the specified RPC or the list of commands.  The `pai-cli` command will parse this text and format it as human-readable text"

{% enditemplate %}

*Example from Pai Core 0.10.0*

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
