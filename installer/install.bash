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
sudo mv /usr/local/opt/calibre/lib/python2.7/site-packages/cssutils/css/value.pyo  /usr/local/opt/calibre/lib/python2.7/site-packages/cssutils/css/value_orig.pyo
sudo cp ./patches/cssutils/css/value.py /usr/local/opt/calibre/lib/python2.7/site-packages/cssutils/css/value.py
