---
layout: service
title: GetMemoryInfo
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `getmemoryinfo` RPC returns information about memory usage.

*Parameters: none*

*Result---information about memory usage*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
|`result`  |object | Required<br>(exactly 1) | An object containing information about memory usage
| →<br>`locked` | string : object | Required<br>(exactly 1) | An object containing information about locked memory manager
| →→<br>`used` | number (int) | Required<br>(exactly 1) | Number of bytes used
| →→<br>`free` | number (int) | Required<br>(exactly 1) | Number of bytes available in current arenas
| →→<br>`total` | number (int) | Required<br>(exactly 1) | Total number of bytes managed
| →→<br>`locked` | number (int) | Required<br>(exactly 1) | Amount of bytes that succeeded locking
| →→<br>`chunks_used` | number (int) | Required<br>(exactly 1) | Number allocated chunks
| →→<br>`chunks_free` | number (int) | Required<br>(exactly 1) | Number unused chunks

*Example*

```
pai-cli getmemoryinfo
```

Result:

```
{
  "locked": {
    "used": 0,
    "free": 65536,
    "total": 65536,
    "locked": 65536,
    "chunks_used": 0,
    "chunks_free": 1
  }
}

```

*See also*

* `GetMemPoolInfo`:
