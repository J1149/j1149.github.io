---
layout: default
title: SignMessage
parent: PAI Core Apis
grand_parent: Developer Reference
---

SignMessage
=======================

*Requires wallet support. Requires an unlocked wallet or an
unencrypted wallet.*

The `signmessage` RPC signs a message with the private key of an address.

*Parameter #1---the address corresponding to the private key to sign with*

{% include table_header.md
  n= "Address"
  t= "string (base58)"
  p= "Required<br>(exactly 1)"
  d= "A P2PKH address whose private key belongs to this wallet"
%}

*Parameter #2---the message to sign*

{% include table_header.md
  n= "Message"
  t= "string"
  p= "Required<br>(exactly 1)"
  d= "The message to sign"
%}

*Result---the message signature*

{% include table_header.md
  n= "`result`"
  t= "string (base64)"
  p= "Required<br>(exactly 1)"
  d= "The signature of the message, encoded in base64.  Note that Pai Core before 0.10.0 creates signatures with random *k* values, so each time you sign the same message, it will create a different signature"
%}

*Example from Pai Core 0.13.1*

Sign a the message "Hello, World!" using the following address:

```
pai-cli signmessage 17fshh33qUze2yifiJ2sXgijSMzJ2KNEwu "Hello, World!"
```

Result:

```
ILypRih424AWRYXK1goB6mskx99aelWcVCTEKolaW7U4VPnwj6Khf+vJSED7pMtPQd3KnXuqq1JvavrQdPMFFB0=
```

*See also*

* `SignMessageWithPrivKey`: signs a message with a given private key.
* `VerifyMessage`: verifies a signed message.
