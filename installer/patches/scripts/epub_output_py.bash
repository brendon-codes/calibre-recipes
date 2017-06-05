#!/bin/bash

FILEDIR="/usr/local/opt/calibre/lib/python2.7/site-packages/calibre/ebooks/conversion/plugins"
wget https://raw.githubusercontent.com/kovidgoyal/calibre/master/src/calibre/ebooks/conversion/plugins/epub_output.py -O "patches/builds/epub_output.py"
patch "patches/builds/epub_output.py" "patches/diffs/epub_output_py.patch"
sudo mv "${FILEDIR}/epub_output.pyo" "${FILEDIR}/epub_output_orig.pyo"
sudo mv "patches/builds/epub_output.py" "${FILEDIR}/epub_output.py"
