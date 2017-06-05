#!/usr/bin/env python2

import linux_installer

INSTALLDIR = "/usr/local/opt"

if __name__ == "__main__":
    linux_installer.main(install_dir=INSTALLDIR)
