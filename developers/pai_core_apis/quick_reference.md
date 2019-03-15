---
layout: default
title: Quick Reference
parent: PAI Core Apis
grand_parent: Developer Reference
---

Quick Reference
===================

`PAI RPCs`

* GetBestBlockHash: returns the header hash of the most recent block on the best block chain.

* GetBlock: gets a block with a particular header hash from the local block database either as a JSON object or as a serialized block. Updated in 0.13.0

* GetBlockChainInfo: provides information about the current state of the block chain. Updated in 0.12.1

* GetBlockCount: returns the number of blocks in the local best block chain.

* GetBlockHash: returns the header hash of a block at the given height in the local best block chain.

* GetBlockHeader: gets a block header with a particular header hash from the local block database either as a JSON object or as a serialized block header. New in 0.12.0

* GetChainTips: returns information about the highest-height block (tip) of each local block chain.

* GetDifficulty: returns the proof-of-work difficulty as a multiple of the minimum difficulty.

* GetMemPoolAncestors: returns all in-mempool ancestors for a transaction in the mempool. New in 0.13.0

* GetMemPoolDescendants: returns all in-mempool descendants for a transaction in the mempool. New in 0.13.0

* GetMemPoolEntry: returns mempool data for given transaction (must be in mempool). New in 0.13.0

* GetMemPoolInfo: returns information about the node’s current transaction memory pool. Updated in 0.12.0

* GetRawMemPool: returns all transaction identifiers (TXIDs) in the memory pool as a JSON array, or detailed information about each transaction in the memory pool as a JSON object. Updated in 0.13.0

* GetTxOut: returns details about a transaction output. Only unspent transaction outputs (UTXOs) are guaranteed to be available.

* GetTxOutProof: returns a hex-encoded proof that one or more specified transactions were included in a block. New in 0.11.0

* GetTxOutSetInfo: returns statistics about the confirmed unspent transaction output (UTXO) set. Note that this call may take some time and that it only counts outputs from confirmed transactions—it does not count outputs from the memory pool.

* PreciousBlock: treats a block as if it were received before others with the same work. New in 0.14.0

* PruneBlockChain: prunes the block chain up to a specified height or timestamp. New in 0.14.0

* VerifyChain: verifies each entry in the local block chain database.

* VerifyTxOutProof: verifies that a proof points to one or more transactions in a block, returning the transactions the proof commits to and throwing an RPC error if the block is not in our best block chain. New in 0.11.0

`CONTROL RPCs`

* GetInfo: prints various information about the node and the network. Deprecated

* Help: lists all available public RPC commands, or gets help for the specified RPC. Commands which are unavailable will not be listed, such as wallet RPCs if wallet support is disabled.

* Stop: safely shuts down the PAI Core server.

`Generating RPCs`

* Generate: nearly instantly generates blocks. New in 0.11.0, Updated in 0.13.0

* GenerateToAddress: mines blocks immediately to a specified address. New in 0.13.0

`Mining RPCs`

* GetBlockTemplate: gets a block template or proposal for use with mining software.

* GetMiningInfo: returns various mining-related information. Updated in 0.14.0

* GetNetworkHashPS: returns the estimated current or historical network hashes per second based on the last n blocks.

* PrioritiseTransaction: adds virtual priority or fee to a transaction, allowing it to be accepted into blocks mined by this node (or miners which use this node) with a lower priority or fee. (It can also remove virtual priority or fee, requiring the transaction have a higher priority or fee to be accepted into a locally-mined block.)

* SubmitBlock: accepts a block, verifies it is a valid addition to the block chainPAI, and broadcasts it to the network. Extra parameters are ignored by PAI Core but may be used by mining pools or other programs.

`Network RPCs`

* AddNode: attempts to add or remove a node from the addnode list, or to try a connection to a node once. Updated in 0.14.0

* ClearBanned: clears list of banned nodes. New in 0.12.0

* DisconnectNode: immediately disconnects from a specified node. New in 0.12.0

* GetAddedNodeInfo: returns information about the given added node, or all added nodes (except onetry nodes). Only nodes which have been manually added using the addnode RPC will have their information displayed. Updated in 0.14.0

* GetConnectionCount: returns the number of connections to other nodes.

* GetNetTotals: returns information about network traffic, including bytes in, bytes out, and the current time. Updated in 0.12.0

* GetNetworkInfo: returns information about the node’s connection to the network. Updated in 0.13.0

* GetPeerInfo: returns data about each connected network node. Updated in 0.13.0

* ListBanned: lists all banned IPs/Subnets. New in 0.12.0

* Ping: sends a P2P ping message to all connected nodes to measure ping time. Results are provided by the getpeerinfo RPC pingtime and pingwait fields as decimal seconds. The P2P ping message is handled in a queue with all other commands, so it measures processing backlog, not just network ping.

* SetBan: attempts add or remove a IP/Subnet from the banned list. New in 0.12.0

* SetNetworkActive: disables/enables all P2P network activity. New in 0.14.0

`Raw Transaction RPCs`

* CreateRawTransaction: creates an unsigned serialized transaction that spends a previous output to a new output with a P2PKH or P2SH address. The transaction is not stored in the wallet or transmitted to the network.

* FundRawTransaction: adds inputs to a transaction until it has enough in value to meet its out value. New in 0.12.0, Updated in 0.14.0

* DecodeRawTransaction: decodes a serialized transaction hex string into a JSON object describing the transaction. Updated in 0.13.0

* DecodeScript: decodes a hex-encoded P2SH redeem script.

* GetRawTransaction: gets a hex-encoded serialized transaction or a JSON object describing the transaction. By default, PAI Core only stores complete transaction data for UTXOs and your own transactions, so the RPC may fail on historic transactions unless you use the non-default txindex=1 in your PAI Core startup settings. Updated in 0.14.0

* SendRawTransaction: validates a transaction and broadcasts it to the peer-to-peer network.

* SignRawTransaction: signs a transaction in the serialized transaction format using private keys stored in the wallet or provided in the call.

`Utility RPCs`

* CreateMultiSig: creates a P2SH multi-signature address.

* EstimateFee: estimates the transaction fee per kilobyte that needs to be paid for a transaction to be included within a certain number of blocks. Updated in 0.14.0Deprecated

* EstimatePriority: estimates the priority that a transaction needs in order to be included within a certain number of blocks as a free high-priority transaction. Deprecated

* GetMemoryInfo: returns information about memory usage.

* ValidateAddress: returns information about the given PAI address. Updated in 0.13.0

* VerifyMessage: verifies a signed message.

`Wallet RPCs`

Note: the wallet RPCs are only available if PAI Core was built with wallet support, which is the default.

* AbandonTransaction: marks an in-wallet transaction and all its in-wallet descendants as abandoned. This allows their inputs to be respent. New in 0.12.0

* AddWitnessAddress: adds a witness address for a script (with pubkey or redeemscript known). New in 0.13.0

* AddMultiSigAddress: adds a P2SH multisig address to the wallet.

* BackupWallet: safely copies wallet.dat to the specified file, which can be a directory or a path with filename.

* BumpFee: replaces an unconfirmed wallet transaction that signaled RBF with a new transaction that pays a higher fee. New in 0.14.0

* DumpPrivKey: returns the wallet-import-format (WIP) private key corresponding to an address. (But does not remove it from the wallet.)

* DumpWallet: creates or overwrites a file with all wallet keys in a human-readable format.
* EncryptWallet: encrypts the wallet with a passphrase. This is only to enable encryption for the first time. After encryption is enabled, you will need to enter the passphrase to use private keys.

* GetAccountAddress: returns the current PAI address for receiving payments to this account. If the account doesn’t exist, it creates both the account and a new address for receiving payment. Once a payment has been received to an address, future calls to this RPC for the same account will return a different address. Deprecated

* GetAccount: returns the name of the account associated with the given address.

* GetAddressesByAccount: returns a list of every address assigned to a particular account. Deprecated

* GetBalance: gets the balance in decimal PAIs across all accounts or for a particular account.

* GetNewAddress: returns a new PAI address for receiving payments. If an account is specified, payments received with the address will be credited to that account.

* GetRawChangeAddress: returns a new PAI address for receiving change. This is for use with raw transactions, not normal use.

* GetReceivedByAccount: returns the total amount received by addresses in a particular account from transactions with the specified number of confirmations. It does not count coinbase transactions. Deprecated

* GetReceivedByAddress: returns the total amount received by the specified address in transactions with the specified number of confirmations. It does not count coinbase transactions.

* GetTransaction: gets detailed information about an in-wallet transaction. Updated in 0.12.0

* GetUnconfirmedBalance: returns the wallet’s total unconfirmed balance.

* GetWalletInfo: provides information about the wallet.

* ImportAddress: adds an address or pubkey script to the wallet without the associated private key, allowing you to watch for transactions affecting that address or pubkey script without being able to spend any of its outputs.

* ImportMulti: imports addresses or scripts (with private keys, public keys, or P2SH redeem scripts) and optionally performs the minimum necessary rescan for all imports. New in 0.14.0

* ImportPrunedFunds: imports funds without the need of a rescan. Meant for use with pruned wallets. New in 0.13.0

* ImportPrivKey: adds a private key to your wallet. The key should be formatted in the wallet import format created by the dumpprivkey RPC.

* ImportWallet: imports private keys from a file in wallet dump file format (see the dumpwallet RPC). These keys will be added to the keys currently in the wallet. This call may need to rescan all or parts of the block chain for transactions affecting the newly-added keys, which may take several minutes.

* KeyPoolRefill: fills the cache of unused pre-generated keys (the keypool).

* ListAccounts: lists accounts and their balances. Deprecated

* ListAddressGroupings: lists groups of addresses that may have had their common ownership made public by common use as inputs in the same transaction or from being used as change from a previous transaction.

* ListLockUnspent: returns a list of temporarily unspendable (locked) outputs.

* ListReceivedByAccount: lists the total number of PAIs received by each account. Deprecated

* ListReceivedByAddress: lists the total number of PAIs received by each address.

* ListSinceBlock: gets all transactions affecting the wallet which have occurred since a particular block, plus the header hash of a block at a particular depth.

* ListTransactions: returns the most recent transactions that affect the wallet. Updated in 0.12.1

* ListUnspent: returns an array of unspent transaction outputs belonging to this wallet. Updated in 0.13.0

* LockUnspent: temporarily locks or unlocks specified transaction outputs. A locked transaction output will not be chosen by automatic coin selection when spending PAIs. Locks are stored in memory only, so nodes start with zero locked outputs and the locked output list is always cleared when a node stops or fails.

* Move: moves a specified amount from one account in your wallet to another using an off-block-chain transaction. Deprecated

* RemovePrunedFunds: deletes the specified transaction from the wallet. Meant for use with pruned wallets and as a companion to importprunedfunds. New in 0.13.0

* SendFrom: spends an amount from a local account to a PAI address. Deprecated

* SendMany: creates and broadcasts a transaction which sends outputs to multiple addresses.

* SendToAddress: spends an amount to a given address.

* SetAccount: puts the specified address in the given account. Deprecated

* SetTxFee: sets the transaction fee per kilobyte paid by transactions created by this wallet.

* SignMessage: signs a message with the private key of an address.

* SignMessageWithPrivKey: signs a message with a given private key. New in 0.13.0

* WalletLock: removes the wallet encryption key from memory, locking the wallet. After calling this method, you will need to call walletpassphrase again before being able to call any methods which require the wallet to be unlocked.

* WalletPassphrase: stores the wallet decryption key in memory for the indicated number of seconds. Issuing the walletpassphrase command while the wallet is already unlocked will set a new unlock time that overrides the old one.

* WalletPassphraseChange: changes the wallet passphrase from ‘old passphrase’ to ‘new passphrase’.

`Removed RPCs`

* GetGenerate: was removed in PAI Core 0.13.0.

* GetHashesPerSec: was removed in PAI Core 0.11.0.

* GetWork: was removed in PAI Core 0.10.0.

* SetGenerate: was removed in PAI Core 0.13.0.