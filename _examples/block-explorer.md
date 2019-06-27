---
layout: service
title: Block Explorer
---

Build instructions for running a local PAIcoin block explorer on OSX. Kudos if you can create a docker files, [please see this issue](https://github.com/J1149/j1149.github.io/issues/12).

1. Run paicoin. See the configuration section in the navigation of this website.
2. Create a paicoin folder in `/Users/your-user-on-osx/Library/Application Support` -- the folder structure will be different depending on OS
3. Create a paicoin.conf file in that folder and set rpc user and password as described in the paicoin build documents
4. Add `txindex=1` to `paicoin.conf`
5. Duplicate that `paicoin.conf` file in the same folder and change filename to `bitcoin.conf` (not sure this is necessary but it helped at one point with the abe explorer.)
6. `git clone https://github.com/dermoth/bitcoin-abe.git`
7. `git checkout segwit` (want to use the experimental segwit branch.)
8. Put [this Californium.py file](https://github.com/bulwark-crypto/bitcoin-abe/blob/master/Abe/Chain/Californium.py) into the path `abe/chain/Californium.py` otherwise the launch will complain
9. In the abe folder try running `python setup.py install`
10. Create a `abe.conf` file in the abe folder using [this configuration file example](https://pastiebin.com/5b41326e96b34) (be sure to update yourname with your osx user account name)
Create a `abe-pg.conf` file in the abe folder with these values:
```config
dbtype psycopg2
connect-args {"database":"paiexplorer2"}
Upgrade
port 2750
```

11. Get postgresql running on the machine, create a user and database named paiexplorer2 (which is referenced in the two config files)
12. In the paicoin folder run `./src/paidcoind` to get the paicoin daemon running
Open a new tab to check that it’s running in the same folder run `./src/paicoin-cli getwalletinfo` or `./src/paicoin-cli help` to get a list of commands
13. Run in the paicoin folder `tail -f $HOME/Library/Application\ Support/PAIcoin/debug.log` or the relevant command in the build docs to let you see the chain sync process
14. After it is caught up, it’s time run ABE’s block parsing. In the abe folder run `python -m Abe.abe --config abe.conf --commit-bytes 100000 --no-serve`
15. That should start showing you block numbers increasing. If you open up a gui tool for postgres like navicat you should see that it is populating the psql database.
16. In the psql database there is a table called Chain where you should see values for PAI. Change the `chain_address_version` to 38, `chain_script_address_version` to 82, and `chain_magic` to 0b091107
17. When it is done syncing to psql run this command in the abe folder `python -m Abe.abe --config abe.conf`
18. Navigate to `http://localhost:2750/` in your browser
