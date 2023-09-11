#!/bin/sh -e
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
pip3 --version
python3 "-m" "pip" "install" "-U" "poetry==1.1.4" --only-binary cryptography
pip install paramiko
pip install difflib

sudo apt-get install git-all
git version

git clone https://github.com/rootlocos/ad-hoc-networking


