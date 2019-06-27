---
layout: service
title: VerifyMessage
parent: PAI Core Apis
grand_parent: Developer Reference
---


The `verifymessage` RPC verifies a signed message.

*Parameter #1---the address corresponding to the signing key*

{% include table_header.md
  n= "Address"
  t= "string (base58)"
  p= "Required<br>(exactly 1)"
  d= "The P2PKH address corresponding to the private key which made the signature.  A P2PKH address is a hash of the public key corresponding to the private key which made the signature.  When the ECDSA signature is checked, up to four possible ECDSA public keys will be reconstructed from from the signature; each key will be hashed and compared against the P2PKH address provided to see if any of them match.  If there are no matches, signature validation will fail"
%}

*Parameter #2---the signature*

{% include table_header.md
  n= "Signature"
  t= "string (base64)"
  p= "Required<br>(exactly 1)"
  d= "The signature created by the signer encoded as base-64 (the format output by the `signmessage` RPC)"
%}

*Parameter #3---the message*

{% include table_header.md
  n= "Message"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The message exactly as it was signed (e.g. no extra whitespace)"
%}

*Result: `true`, `false`, or an error*

{% include table_header.md
  n= "`result`"
  t= "bool/null"
  p= "Required<br>(exactly 1)"
  d= "Set to `true` if the message was signed by a key corresponding to the provided P2PKH address; set to `false` if it was not signed by that key; set to JSON `null` if an error occurred"
%}

*Example*

Check the signature on the message created in the example for
`signmessage`:

```
pai-cli -testnet verifymessage \
  mgnucj8nYqdrPFh2JfZSB1NmUThUGnmsqe \
  IL98ziCmwYi5pL+dqKp4Ux+zCa4hP/xbjHmWh+Mk/lefV/0pWV1p/gQ94jgExSmgH2/+PDcCCrOHAady2IEySSI= \
  'Hello, World!'
```

Result:

```
true
```

*See also*

* `SignMessage`: signs a message with the private key of an address.
