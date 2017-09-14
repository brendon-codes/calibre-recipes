#!/bin/bash

FILEDIR="/usr/local/opt/calibre/lib/python2.7/site-packages/calibre/ebooks/oeb/transforms"
wget 'https://raw.githubusercontent.com/kovidgoyal/calibre/master/src/calibre/ebooks/oeb/transforms/flatcss.py' -O "patches/builds/flatcss.py"
patch "patches/builds/flatcss.py" "patches/diffs/flatcss_py.patch"
sudo mv "${FILEDIR}/flatcss.pyo" "${FILEDIR}/flatcss_orig.pyo"
sudo mv "patches/builds/flatcss.py" "${FILEDIR}/flatcss.py"
