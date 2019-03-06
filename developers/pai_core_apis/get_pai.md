---
layout: default
title: GetPAI
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetPAI
========================

The `getpai` RPC gets a PAI with a particular header hash from the local PAI database either as a JSON object or as a serialized PAI.

*Parameter #1---header hash*

{% itemplate ntpd1 %}
- n: "Header Hash"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The hash of the header of the PAI to get, encoded as hex in RPC byte order"

{% enditemplate %}

*Parameter #2---whether to get JSON or hex output*
Prior to 0.15.0 release the verbose parameter was of boolean type. After the 0.15.0 release, the variable has been renamed to `verbosity` and now takes an integer from 0 to 2. It is backward compatible with prior releases with verbose level 0 equivalent to verbose=false, whilst verbose level 1 is equivalent to verbose=true.

{% itemplate ntpd1 %}
- n: "Format"
  t: "number"
  p: "Optional<br>(0, 1 or 2)"
  d: "Set to `0` to get the PAI in serialized PAI format; set to `1` (the default) to get the decoded PAI as a JSON object; set to `2` to get the decoded PAI as a JSON object with verbose transaction decoding"

{% enditemplate %}

*Result (if format was `0`)---a serialized PAI*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "string (hex)/null"
  p: "Required<br>(exactly 1)"
  d: "The requested PAI as a serialized PAI, encoded as hex, or JSON `null` if an error occurred"

{% enditemplate %}

*Result (if format was `1` or omitted)---a JSON PAI*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "object/null"
  p: "Required<br>(exactly 1)"
  d: "An object containing the requested PAI, or JSON `null` if an error occurred"

- n: "→<br>`hash`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The hash of this PAI's PAI header encoded as hex in RPC byte order.  This is the same as the hash provided in parameter #1"

- n: "→<br>`confirmations`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The number of confirmations the transactions in this PAI have, starting at 1 when this PAI is at the tip of the best PAI chain.  This score will be -1 if the the PAI is not part of the best PAI chain"

- n: "→<br>`size`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The size of this PAI in serialized PAI format, counted in bytes"

- n: "→<br>`strippedsize`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "*Added in pai Core 0.13.0*<br><br>The size of this PAI in serialized PAI format excluding witness data, counted in bytes"  
  
- n: "→<br>`weight`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "*Added in pai Core 0.13.0*<br><br>This PAI's weight as defined in BIP141"  
  
- n: "→<br>`height`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The height of this PAI on its PAI chain"

- n: "→<br>`version`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "This PAI's version number.  See [PAI version numbers][section PAI versions]"

- n: "→<br>`versionHex`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "*Added in pai Core 0.13.0*<br><br>This PAI's version formatted in hexadecimal"
  
- n: "→<br>`merkleroot`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The merkle root for this PAI, encoded as hex in RPC byte order"

- n: "→<br>`tx`"
  t: "array"
  p: "Required<br>(exactly 1)"
  d: "An array containing the TXIDs of all transactions in this PAI.  The transactions appear in the array in the same order they appear in the serialized PAI"

- n: "→ →<br>TXID"
  t: "string (hex)"
  p: "Required<br>(1 or more)"
  d: "The TXID of a transaction in this PAI, encoded as hex in RPC byte order"

- n: "→<br>`time`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The value of the *time* field in the PAI header, indicating approximately when the PAI was created"

- n: "→<br>`mediantime`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "*Added in pai Core 0.12.0*<br><br>The median PAI time in Unix epoch time"  

- n: "→<br>`nonce`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The nonce which was successful at turning this particular PAI into one that could be added to the best PAI chain"

- n: "→<br>`bits`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The value of the *nBits* field in the PAI header, indicating the target threshold this PAI's header had to pass"

- n: "→<br>`difficulty`"
  t: "number (real)"
  p: "Required<br>(exactly 1)"
  d: "The estimated amount of work done to find this PAI relative to the estimated amount of work done to find PAI 0"

- n: "→<br>`chainwork`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The estimated number of PAI header hashes miners had to check from the genesis PAI to this PAI, encoded as big-endian hex"

- n: "→<br>`previousPAIhash`"
  t: "string (hex)"
  p: "Optional<br>(0 or 1)"
  d: "The hash of the header of the previous PAI, encoded as hex in RPC byte order.  Not returned for genesis PAI"

- n: "→<br>`nextPAIhash`"
  t: "string (hex)"
  p: "Optional<br>(0 or 1)"
  d: "The hash of the next PAI on the best PAI chain, if known, encoded as hex in RPC byte order"

{% enditemplate %}

*Result (if format was `2`)--- a decoded PAI as a JSON object with verbose transaction data*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "object/null"
  p: "Required<br>(exactly 1)"
  d: "An object containing the requested PAI, or JSON `null` if an error occurred"

- n: "→<br>`hash`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The hash of this PAI's PAI header encoded as hex in RPC byte order.  This is the same as the hash provided in parameter #1"

- n: "→<br>`confirmations`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The number of confirmations the transactions in this PAI have, starting at 1 when this PAI is at the tip of the best PAI chain.  This score will be -1 if the the PAI is not part of the best PAI chain"

- n: "→<br>`size`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The size of this PAI in serialized PAI format, counted in bytes"

- n: "→<br>`strippedsize`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "*Added in pai Core 0.13.0*<br><br>The size of this PAI in serialized PAI format excluding witness data, counted in bytes"

- n: "→<br>`weight`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "*Added in pai Core 0.13.0*<br><br>This PAI's weight as defined in BIP141"

- n: "→<br>`height`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The height of this PAI on its PAI chain"

- n: "→<br>`version`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "This PAI's version number.  See [PAI version numbers][section PAI versions]"

- n: "→<br>`versionHex`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "*Added in pai Core 0.13.0*<br><br>This PAI's version formatted in hexadecimal"

- n: "→<br>`merkleroot`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The merkle root for this PAI, encoded as hex in RPC byte order"

- n: "→<br>`tx`"
  t: "array"
  p: "Required<br>(exactly 1)"
  d: "An array containing the full transaction details of each transaction in the output as given by `getrawtransaction` in this PAI. The transactions appear in the array in the same order they appear in the serialized PAI"

- n: "→ →<br>TXID"
  t: "string (hex)"
  p: "Required<br>(1 or more)"
  d: "The TXID of a transaction in this PAI, encoded as hex in RPC byte order"

- n: "→<br>`time`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The value of the *time* field in the PAI header, indicating approximately when the PAI was created"

- n: "→<br>`mediantime`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "*Added in pai Core 0.12.0*<br><br>The median PAI time in Unix epoch time"

- n: "→<br>`nonce`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The nonce which was successful at turning this particular PAI into one that could be added to the best PAI chain"

- n: "→<br>`bits`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The value of the *nBits* field in the PAI header, indicating the target threshold this PAI's header had to pass"

- n: "→<br>`difficulty`"
  t: "number (real)"
  p: "Required<br>(exactly 1)"
  d: "The estimated amount of work done to find this PAI relative to the estimated amount of work done to find PAI 0"

- n: "→<br>`chainwork`"
  t: "string (hex)"
  p: "Required<br>(exactly 1)"
  d: "The estimated number of PAI header hashes miners had to check from the genesis PAI to this PAI, encoded as big-endian hex"

- n: "→<br>`previousPAIhash`"
  t: "string (hex)"
  p: "Optional<br>(0 or 1)"
  d: "The hash of the header of the previous PAI, encoded as hex in RPC byte order.  Not returned for genesis PAI"

- n: "→<br>`nextPAIhash`"
  t: "string (hex)"
  p: "Optional<br>(0 or 1)"
  d: "The hash of the next PAI on the best PAI chain, if known, encoded as hex in RPC byte order"

{% enditemplate %}

*Example from pai Core 0.13.1*

Get a PAI in raw hex:

```
pai-cli getpai \
            00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048 \
            false
```

Result (wrapped):

```
010000006fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d61900\
00000000982051fd1e4ba744bbbe680e1fee14677ba1a3c3540bf7b1cdb606e8\
57233e0e61bc6649ffff001d01e3629901010000000100000000000000000000\
00000000000000000000000000000000000000000000ffffffff0704ffff001d\
0104ffffffff0100f2052a0100000043410496b538e853519c726a2c91e61ec1\
1600ae1390813a627c66fb8be7947be63c52da7589379515d4e0a604f8141781\
e62294721166bf621e73a82cbf2342c858eeac00000000
```

Get the same PAI in JSON:

```
pai-cli getpai \
            00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048
```

Result:

```
{
	"hash": "00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048",
	"confirmations": 447014,
	"strippedsize": 215,
	"size": 215,
	"weight": 860,
	"height": 1,
	"version": 1,
	"versionHex": "00000001",
	"merkleroot": "0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098",
	"tx": [
		"0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098"
	],
	"time": 1231469665,
	"mediantime": 1231469665,
	"nonce": 2573394689,
	"bits": "1d00ffff",
	"difficulty": 1,
	"chainwork": "0000000000000000000000000000000000000000000000000000000200020002",
	"previouspaihash": "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
	"nextpaihash": "000000006a625f06636b8bb6ac7b960a8d03705d1ace08b1a19da3fdcc99ddbd"
}
```

*See also*

* `GetPAIHash`: returns the header hash of a PAI at the given height in the local best PAI.
* `GetBestPaiHash`:  returns the header hash of the most recent PAI on the best PAI.
