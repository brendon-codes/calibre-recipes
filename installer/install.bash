#!/bin/bash

##
## Download the calibre installer
##
wget https://download.calibre-ebook.com/linux-installer.py -O linux_installer.py

##
## Remove old install
##
sudo rm -r /usr/local/opt/calibre

##
## Run our custom installer
##
sudo python2 ./custom_installer.py

##
## Patch some buggy code
##
#sudo bash ./apply_patches.bash
