---
title: 'Constants And Defaults'
image: '/docs/noun_591323.png'
---

The following constants and defaults are taken from Pai Core's
[chainparams.cpp][core chainparams.cpp] source code file.

| Network | Default Port | [Start String][/en/glossary/start-string]{:#term-start-string}{:.term} | Max nBits
|---------|--------------|-----------------------------------------------|---------------
| Mainnet | 8333         | 0xf9beb4d9                                    | 0x1d00ffff
| Testnet | 18333        | 0x0b110907                                    | 0x1d00ffff
| Regtest | 18444        | 0xfabfb5da                                    | 0x207fffff

Note: the testnet start string and nBits above are for testnet3; the
original testnet used a different string and higher (less difficult)
nBits.

Command line parameters can change what port a node listens on (see
`-help`). Start strings are hardcoded constants that appear at the start
of all messages sent on the Pai network; they may also appear in
data files such as Pai Core's block database.  The nBits displayed
above are in big-endian order; they're sent over the network in
little-endian order.

Pai Core's [chainparams.cpp][core chainparams.cpp] also includes
other constants useful to programs, such as the hash of the genesis
blocks for the different networks.
