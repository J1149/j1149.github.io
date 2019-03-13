---
layout: default
title: GetWalletInfo
parent: PAI Core Apis
grand_parent: Developer Reference
---

GetWalletInfo
========================

*Parameters: none*

*Result---information about the wallet*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "object"
  p: "Required<br>(exactly 1)"
  d: "An object describing the wallet"
  
- n: "→<br>`walletname`"
  t: "string"
  p: "Required<br>(exactly 1)"
  d: "The name of the wallet"

- n: "→<br>`walletversion`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The version number of the wallet"

- n: "→<br>`balance`"
  t: "number (pai's)"
  p: "Required<br>(exactly 1)"
  d: "The balance of the wallet. The same as returned by the `getbalance` RPC with default parameters"
  
- n: "→<br>`unconfirmed_balance`"
  t: "number (pai's)"
  p: "Required<br>(exactly 1)"
  d: "The unconfirmed balance of the wallet"
  
- n: "→<br>`immature_balance`"
  t: "number (pai's)"
  p: "Required<br>(exactly 1)"
  d: "The total immature balance of the wallet"

- n: "→<br>`txcount`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The total number of transactions in the wallet (both spends and receives)"

- n: "→<br>`keypoololdest`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The date as Unix epoch time when the oldest key in the wallet key pool was created; useful for only scanning blocks created since this date for transactions"

- n: "→<br>`keypoolsize`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The number of keys in the wallet keypool"
  
- n: "→<br>`keypoolsize_hd_internal`"
  t: "number (int)"
  p: "Required<br>(exactly 1)"
  d: "The number of keys that are pre-generated for internal use (used for change outputs, only appears if the wallet is using this feature, otherwise external keys are used)"
  
- n: "→<br>`unlocked_until`"
  t: "number (int)"
  p: "Optional<br>(0 or 1)"
  d: "Only returned if the wallet was encrypted with the `encryptwallet` RPC. A Unix epoch date when the wallet will be locked, or `0` if the wallet is currently locked"
  
- n: "→<br>`paytxfee`"
  t: "number (pai's)"
  p: "Required<br>(exactly 1)"
  d: "The transaction fee configuration currently set"
  
- n: "→<br>`hdseedid`"
  t: "string"
  p: "Optional<br>(0 or 1)"
  d: "The Hash160 of the HD seed (only present when HD is enabled)"
  
- n: "→<br>`hdmasterkeyid`"
  t: "string"
  p: "Optional<br>(0 or 1)"
  d: "Alias for `hdseedid` retained for backwards-compatibility"
  
- n: "→<br>`private_keys_enabled`"
  t: "boolean"
  p: "Required<br>(exactly 1)"
  d: "False if privatekeys are disabled for this wallet (enforced watch-only wallet)"


{% enditemplate %}

*See also*

* `ListTransactions`: returns the most recent transactions that affect the wallet.
