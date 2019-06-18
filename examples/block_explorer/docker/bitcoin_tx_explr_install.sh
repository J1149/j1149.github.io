# SW needed for the block chain explorer
apt install -y openjdk-8-jdk-headless
apt-get install -y maven

cd /home
git clone https://github.com/yogh-io/bitcoin-transaction-explorer.git
cd /home/bitcoin-transaction-explorer
mvn install -X clean install
cp ./bitcoin-transactions-server/target/bitcoin-transactions-server-0.1.war /opt/tomcat/latest/webapps 
rm -rf /home/bitcoin-transaction-explorer