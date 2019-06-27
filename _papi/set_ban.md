---
layout: service
title: SetBan
parent: PAI Core Apis
grand_parent: Developer Reference
---



The `setban` RPC attempts add or remove a IP/Subnet from the banned list.

*Parameter #1---IP/Subnet of the node*

{% include table_header.md
  n= "IP(/Netmask)"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The node to add or remove as a string in the form of `<IP address>`.  The IP address may be a hostname resolvable through DNS, an IPv4 address, an IPv4-as-IPv6 address, or an IPv6 address"
%}

*Parameter #2---whether to add or remove the node*

{% include table_header.md
  n= "Command"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "What to do with the IP/Subnet address above.  Options are:<br>• `add` to add a node to the addnode list<br>• `remove` to remove a node from the list.  If currently connected, this will disconnect immediately"
%}

*Parameter #3---time how long the ip is banned*

{% include table_header.md
  n= "Bantime"
  t= "numeric<br>(int)"
  p= "Optional<br>(0 or 1)"
  d= "Time in seconds how long (or until when if `absolute` is set) the entry is banned. The default is 24h which can also be overwritten by the -bantime startup argument"
%}

*Parameter #4---whether a relative or absolute timestamp*

{% include table_header.md
  n= "Absolute"
  t= "bool"
  p= "Optional<br>(0 or 1)"
  d= "If set, the bantime must be a absolute timestamp in seconds since epoch (Jan 1 1970 GMT)"
%}

*Result---`null` on success*

{% include table_header.md
  n= "`result`"
  t= "null"
  p= "Required<br>(exactly 1)"
  d= "Always JSON `null`"
%}

*Example*

Ban the following node.

```
pai-cli -testnet setban 192.0.2.113:18333 add 2592000
```

Result (no output from `pai-cli` because result is set to `null`).

*See also*

* `ListBanned`: lists all banned IPs/Subnets.
* `ClearBanned`: clears list of banned nodes.
