#!/bin/bash

FILEDIR="/usr/local/opt/calibre/lib/python2.7/site-packages/cssutils/css"
wget https://bitbucket.org/cthedot/cssutils/raw/default/src/cssutils/css/value.py -O "patches/builds/value.py"
patch "patches/builds/value.py" "patches/diffs/value_py.patch"
sudo mv "${FILEDIR}/value.pyo" "${FILEDIR}/value_orig.pyo"
sudo mv "patches/builds/value.py" "${FILEDIR}/value.py"
