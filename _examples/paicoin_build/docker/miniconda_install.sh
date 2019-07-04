apt-get install -y wget
mkdir /home/downloads
cd /home/downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-4.6.14-Linux-x86_64.sh
bash Miniconda3-4.6.14-Linux-x86_64.sh -b
rm Miniconda3-4.6.14-Linux-x86_64.sh
export PATH="/root/miniconda3/bin:$PATH"
conda update conda -n root
conda update --all