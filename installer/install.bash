#!/bin/bash

##
## Download the calibre installer
##
wget https://download.calibre-ebook.com/linux-installer.py -O linux_installer.py

##
## Run our custom installer
##
sudo python2 ./custom_installer.py

##
## Patch some buggy code
##
sudo bash ./apply_patches.bash
