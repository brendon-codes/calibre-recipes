#!/usr/bin/env python2

import sys
from urlparse import urlparse
from data.items import DOMAINS

def x_extract_domain(url):
    full_dom = urlparse(unicode(url)).netloc
    dom_parts = full_dom.split(u".")
    for i in range(len(dom_parts)):
        check = u".".join(dom_parts[i:])
        if check in DOMAINS:
            back_check = u".".join(dom_parts[i-1:])
            return back_check
    return u".".join(dom_parts[-2:])


def main():
    url = u"https://www.foobar.com"
    out = x_extract_domain(url)
    print(out)
    return True


if __name__ == u"__main__":
    main()
    sys.exit(0)
