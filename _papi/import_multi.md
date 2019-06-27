---
layout: service
title: ImportMulti
parent: PAI Core Apis
grand_parent: Developer Reference
---


*Requires wallet support.  Wallet must be unlocked.*

The `importmulti` RPC imports addresses or scripts (with private keys, public keys, or P2SH redeem scripts) and optionally performs the minimum necessary rescan for all imports.

*Parameter #1---the addresses/scripts to import*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| Imports  | array | Required<br>(exactly 1) | An array of JSON objects, each one being an address or script to be imported
| → Import | object | Required<br>(1 or more) | A JSON object describing a particular import
| → →<br>`scriptPubKey` | string (hex) | Optional<br>(0 or 1) | The script (string) to be imported.  Must have either this field or `address` below
| → →<br>`address` | string (base58) | Optional<br>(0 or 1) | The P2PKH or P2SH address to be imported.  Must have either this field or `scriptPubKey` above
| → →<br>`timestamp` | number (int) / string | Required<br>(exactly 1) | The creation time of the key in Unix epoch time or the string “now” to substitute the current synced block chain time. The timestamp of the oldest key will determine how far back block chain rescans need to begin. Specify `now` to bypass scanning for keys which are known to never have been used.  Specify `0` to scan the entire block chain. Blocks up to 2 hours before the earliest key creation time will be scanned
| → →<br>`redeemscript` | string | Optional<br>(0 or 1) | A redeem script. Only allowed if either the `address` field is a P2SH address or the `scriptPubKey` field is a P2SH scriptPubKey
| → →<br>`pubkeys` | array | Optional<br>(0 or 1) | Array of strings giving pubkeys that must occur in the scriptPubKey or redeemscript
| → →<br>`keys` | array | Optional<br>(0 or 1) | Array of strings giving private keys whose corresponding public keys must occur in the scriptPubKey or redeemscript
| → →<br>`internal` | bool | Optional<br>(0 or 1) | Stating whether matching outputs should be treated as change rather than incoming payments. The default is `false`
| → →<br>`watchonly` | bool | Optional<br>(0 or 1) | Stating whether matching outputs should be considered watched even when they're not spendable. This is only allowed if keys are empty. The default is `false`
| → →<br>`label` | string | Optional<br>(0 or 1) | Label to assign to the address, only allowed with `internal` set to `false`. The default is an empty string (“”)


*Parameter #2---options regarding the import*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| Option  | object | Optional<br>(0 or 1) | JSON object with options regarding the import
| → <br>`rescan` | bool | Optional<br>(0 or 1) | Set to `true` (the default) to rescan the entire local block chain for transactions affecting any imported address or script. Set to `false` to not rescan after the import. Rescanning may take a considerable amount of time and may require re-downloading blocks if using block chain pruning


*Result---execution result*

| Name | Type      | Presence            | Description
|------|-----------|---------------------|-------------
| `result`  | array | Required<br>(exactly 1) | An array of JSON objects, with each object describing the execution result of each import
| → Result | object | Required<br>(1 or more) | A JSON object describing the execution result of an imported address or script
| → → <br>`success` | string | Required<br>(exactly 1) | Displays `true` if the import has been successful or `false` if it failed
| → → <br>`error` | string : object | Optional<br>(0 or 1) | A JSON object containing details about the error. Only displayed if the import fails
| → → → <br>`code` | number (int) | Optional<br>(0 or 1) | The error code
| → → → <br>`message` | string | Optional<br>(0 or 1) | The error message

*Example*

Import the address PaXVxzkruFZPidQjsDft9CW174Tr99xngu (giving it a label and scanning the entire block chain) and the scriptPubKey 76a9149e857da0a5b397559c78c98c9d3f7f655d19c68688ac (giving a specific timestamp and label):

```
pai-cli importmulti '
  [
    {
      "scriptPubKey" : { "address": "PaXVxzkruFZPidQjsDft9CW174Tr99xngu" },
      "timestamp" : 0,
      "label" : "Personal"
    },
    {
      "scriptPubKey" : "76a9149e857da0a5b397559c78c98c9d3f7f655d19c68688ac",
      "timestamp" : 1493912405,
      "label" : "TestFailure"
    }
  ]' '{ "rescan": true }'
```

Result (scriptPubKey import failed because `internal` was not set to `true`):

```
  [
    {
      "success": true
    }, 
    {
      "success": false,
      "error": {
      "code": -8,
      "message": "Internal must be set for hex scriptPubKey"
      }
    }
  ]
```

*See also*

* `ImportPrivKey`: adds a private key to your wallet. The key should be formatted in the wallet import format created by the dumpprivkey RPC.
* `ImportAddress`: adds an address or pubkey script to the wallet without the associated private key, allowing you to watch for transactions affecting that address or pubkey script without being able to spend any of its outputs.
* `ImportWallet`: imports private keys from a file in wallet dump file format (see the dumpwallet RPC). These keys will be added to the keys currently in the wallet. This call may need to rescan all or parts of the block chain for transactions affecting the newly-added keys, which may take several minutes.
