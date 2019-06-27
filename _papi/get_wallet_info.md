---
layout: service
title: GetWalletInfo
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Parameters: none*

*Result---information about the wallet*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  | object | Required<br>(exactly 1) | An object describing the wallet
| →<br>`walletname` | string | Required<br>(exactly 1) | The name of the wallet
| →<br>`walletversion` | number (int) | Required<br>(exactly 1) | The version number of the wallet
| →<br>`balance` | number (pai's) | Required<br>(exactly 1) | The balance of the wallet. The same as returned by the `getbalance` RPC with default parameters
| →<br>`unconfirmed_balance` | number (pai's) | Required<br>(exactly 1) | The unconfirmed balance of the wallet
| →<br>`immature_balance` | number (pai's) | Required<br>(exactly 1) | The total immature balance of the wallet
| →<br>`txcount` | number (int) | Required<br>(exactly 1) | The total number of transactions in the wallet (both spends and receives)
| →<br>`keypoololdest` | number (int) | Required<br>(exactly 1) | The date as Unix epoch time when the oldest key in the wallet key pool was created; useful for only scanning blocks created since this date for transactions
| →<br>`keypoolsize` | number (int) | Required<br>(exactly 1) | The number of keys in the wallet keypool
| →<br>`keypoolsize_hd_internal` | number (int) | Required<br>(exactly 1) | The number of keys that are pre-generated for internal use (used for change outputs, only appears if the wallet is using this feature, otherwise external keys are used)
| →<br>`unlocked_until` | number (int) | Optional<br>(0 or 1) | Only returned if the wallet was encrypted with the `encryptwallet` RPC. A Unix epoch date when the wallet will be locked, or `0` if the wallet is currently locked
| →<br>`paytxfee` | number (pai's) | Required<br>(exactly 1) | The transaction fee configuration currently set
| →<br>`hdseedid` | string | Optional<br>(0 or 1) | The Hash160 of the HD seed (only present when HD is enabled)
| →<br>`hdmasterkeyid` | string | Optional<br>(0 or 1) | Alias for `hdseedid` retained for backwards-compatibility
| →<br>`private_keys_enabled` | boolean | Required<br>(exactly 1) | False if privatekeys are disabled for this wallet (enforced watch-only wallet)


*See also*

* `ListTransactions`: returns the most recent transactions that affect the wallet.
