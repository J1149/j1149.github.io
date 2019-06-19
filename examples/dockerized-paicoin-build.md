# Dockerized Block Explorer

To run the dockerized block chain, you must first install docker. Note, the 
normal docker executable might be incompatible with certain operating systems 
(like Windows 10 Home). If you have an incompatible operating system this might 
be resolved by installing docker toolbox from:
    
	https://github.com/docker/toolbox
	
After installing docker, you will need to download the following files and 
place them in the same directory:

* [Dockerfile](https://github.com/J1149/j1149.github.io/raw/master/examples/paicoin_build/docker/Dockerfile) (Your web browser may save this as a "txt" file, make sure to rename it to "Dockerfile" if it does)
* [paicoin_cli.py](https://github.com/J1149/j1149.github.io/raw/master/examples/paicoin_build/docker/paicoin_cli.py)
* [debugging_tools_install.sh](https://github.com/J1149/j1149.github.io/raw/master/examples/paicoin_build/docker/debugging_tools_install.sh)
* [miniconda_install.sh](https://github.com/J1149/j1149.github.io/raw/master/examples/paicoin_build/docker/miniconda_install.sh)
* [paicoin.conf](https://github.com/J1149/j1149.github.io/raw/master/examples/paicoin_build/docker/paicoin.conf)
* [paicoin_install.sh](https://github.com/J1149/j1149.github.io/raw/master/examples/paicoin_build/docker/paicoin_install.sh)
* [rpcauth.py](https://github.com/J1149/j1149.github.io/raw/master/examples/paicoin_build/docker/rpcauth.py)


After downloading the files, open up the command-line in the directory they were 
downloaded into. Then use the following commands in the command-line:

1. `docker build -t "block_explorer:v1" .`
2. `docker run -i -t --name blk_explr "block_explorer:v1" /bin/bash

The last command should allow you to use the command line interface of paicoin. 