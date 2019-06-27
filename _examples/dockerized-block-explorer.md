---
layout: default
title: Dockerized Block Explorer
parent: Examples
nav_order: 7
---
# Dockerized Block Explorer

To run the dockerized block chain, you must first install docker. Note, the 
normal docker executable might be incompatible with certain operating systems 
(like Windows 10 Home). If you have an incompatible operating system this might 
be resolved by installing docker toolbox from:
    
	https://github.com/docker/toolbox
	
After installing docker, you will need to download the following files and 
place them in the same directory:

* [Dockerfile](https://github.com/J1149/j1149.github.io/raw/master/_examples/block_explorer/docker/Dockerfile) (Your web browser may save this as a "txt" file, make sure to rename it to "Dockerfile" if it does)
* [bitcoin_tx_explr_install.sh](https://github.com/J1149/j1149.github.io/raw/master/_examples/block_explorer/docker/bitcoin_tx_explr_install.sh)
* [block_explorer.py](https://github.com/J1149/j1149.github.io/raw/master/_examples/block_explorer/docker/block_explorer.py)
* [debugging_tools_install.sh](https://github.com/J1149/j1149.github.io/raw/master/_examples/block_explorer/docker/debugging_tools_install.sh)
* [miniconda_install.sh](https://github.com/J1149/j1149.github.io/raw/master/_examples/block_explorer/docker/miniconda_install.sh)
* [paicoin.conf](https://github.com/J1149/j1149.github.io/raw/master/_examples/block_explorer/docker/paicoin.conf)
* [paicoin_install.sh](https://github.com/J1149/j1149.github.io/raw/master/_examples/block_explorer/docker/paicoin_install.sh)
* [rpcauth.py](https://github.com/J1149/j1149.github.io/raw/master/_examples/block_explorer/docker/rpcauth.py)
* [tomcat.service](https://github.com/J1149/j1149.github.io/raw/master/_examples/block_explorer/docker/tomcat.service)
* [tomcat_install.sh](https://github.com/J1149/j1149.github.io/raw/master/_examples/block_explorer/docker/tomcat_install.sh)


After downloading the files, open up the command-line in the directory they were 
downloaded into. Then use the following commands in the command-line:

1. `docker build -t "block_explorer:v1" .`
2. `docker run -i -t -p 8080 --name blk_explr "block_explorer:v1"`
3. You should get a prompt asking you for a username and password for the 
JSON-RPC interface. Remember them as you will use them later.
4. Docker will map a port on the host that corresponds to a port on the 
container. To find out the address you should type into your web browser, enter
the following command into the command-line:

       docker port blk_explr 8080

    It should display an address similar to the following:
	
        0.0.0.0:32768
	
5. Enter the address in step 4 into a web browser with the suffix, paicoin-info.
	For example, if your address was 0.0.0.0:32768 you would enter:

        http://0.0.0.0:32768/paicoin-info/
	
	You might need to substitute "0.0.0.0" with "localhost" if your web browser 
	is not being cooperative.
        
6. Enter "config" into the search bar for this "site." (The search bar should 
	have the text "Insert anything, press enter" inside of it).
7. You should now be at a page asking you for a password. Enter a password 
	that you would like to use for this site. It can be different than the 
	password you entered earlier.
8. You should now see a page with the title of "Configuation" and a subtitle of
	"Blockchain source settings." 
	* In the "Host" field, enter `localhost`
	* In the "Port" field, enter `8566`
	* In the "RPC Username" field, use the username you had entered in step 3.
	* In the "RPC Password" field, use the password you had entered in step 3.
	* Leave the rest of the fields blank.

9. paicoind needs some time to download the entire blockchain so wait a few 
	minutes before doing any work.

10. Visit [http://chainquery.com/bitcoin-api](http://chainquery.com/bitcoin-api) 
for some of the commands available for the search bar.

