FROM ubuntu:18.04

# To stop tzdata from pausing the install.
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update
RUN apt-get -y update
RUN apt-get -y upgrade

RUN mkdir /home/scripts
WORKDIR /home/scripts

# install paicoin
ADD paicoin_install.sh /home/scripts
RUN sh -e paicoin_install.sh

# Install Tomcat; probably should be replaced with a bash script...
ADD tomcat.service /etc/systemd/system/
ADD tomcat_install.sh /home/scripts
RUN sh -e tomcat_install.sh 

# Bitcoin-transaction-explorer install
ADD bitcoin_tx_explr_install.sh /home/scripts
RUN sh -e bitcoin_tx_explr_install.sh

# Add file needed to create username/password for paicoin RPC
RUN mkdir /root/.paicoin
ADD paicoin.conf /root/.paicoin

# debugging tools install
ADD debugging_tools_install.sh /home/scripts
RUN sh -e debugging_tools_install.sh

# Miniconda
ADD miniconda_install.sh /home/scripts
RUN sh -e miniconda_install.sh

ADD block_explorer.py /home/scripts
ADD rpcauth.py /home/scripts
WORKDIR /home/scripts
CMD python3 block_explorer.py
EXPOSE 8080 8009
