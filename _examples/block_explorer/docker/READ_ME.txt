# To build the container, run the following command:
docker build -t "paicoin_build_block_explorer_18_04:v1" .

# To run the container, run the following command:
docker run -i -t -p 8080 --name blk_explr "paicoin_build_block_explorer_18_04:v1"

# You should get a prompt asking you for a username and password for the JSON-RPC interface.
# Remember them as you will use them later.

# To find what port docker mapped to port 8080 of the container, run the following command:
docker ps
# You should find something like:
CONTAINER ID        IMAGE                                   COMMAND                  CREATED             STATUS              PORTS                               NAMES
9191c922d5fe        paicoin_build_block_explorer_18_04:v1   "/bin/sh -c '/opt/to…"   5 minutes ago       Up 5 minutes        8009/tcp, 0.0.0.0:32768->8080/tcp   blk_explr
# In which case port 8080 is mapped to 32768 on the Host machine. 

# You can type the following address into your browser to get to the block chain explorer:
http://localhost:32768/paicoin-transactions-server/

# enter config into the search bar.
# setup a password for this "site"
# use the username and password you used for the prompt earlier
# use "localhost" as the host and "8566" as the port

# paicoind needs some time to download the entire blockchain so wait a few minutes before doing any work.

# visit http://chainquery.com/bitcoin-api for the commands available for the search bar.