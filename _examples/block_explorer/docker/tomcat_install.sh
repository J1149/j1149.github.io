apt-get install -y wget
apt-get install -y systemd
useradd -r -m -U -d /opt/tomcat -s /bin/false tomcat
# tomcat seems to only keep the last two versions... this is not future proofed...
wget http://apache.org/dist/tomcat/tomcat-9/v9.0.21/bin/apache-tomcat-9.0.21.tar.gz -P /tmp
tar xf /tmp/apache-tomcat-9*.tar.gz -C /opt/tomcat
ln -s /opt/tomcat/apache-tomcat-9.0.21 /opt/tomcat/latest
chown -RH tomcat: /opt/tomcat/latest
sh -c 'chmod +x /opt/tomcat/latest/bin/*.sh'
systemctl enable tomcat
