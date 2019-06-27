---
layout: service
title: SignMessageWithPrivKey
parent: PAI Core Apis
grand_parent: Developer Reference
---


The signmessagewithprivkey RPC signs a message with a given private key.

*Parameter #1---the private key to sign with*

{% include table_header.md
  n= "Privat Key"
  t= "string (base58)"
  p= "Required<br>(exactly 1)"
  d= "The private key to sign the message with encoded in base58check using wallet import format (WIF)"
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
  d= "The signature of the message, encoded in base64."
%}

*Example*

Sign a the message "Hello, World!" using the following private key:

```
pai-cli signmessagewithprivkey 5HpHagT65TZzG1PH3CSu63k8DbpvD\
8s5ip4nEB3kEsreKamq6aB "Hello, World!"
```

Result:

```
G+ZauMFgQExAJRKZSldbAVEaZo4i0p2AVivbFASo50PkUnynAMDUiNMVdXDlpYMWvatxCmYmLn8C9zygPRn3Y1c=
```

*See also*

* `SignMessage`:  signs a message with the private key of an address.
* `VerifyMessage`: verifies a signed message.


