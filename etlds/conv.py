#!/usr/bin/env python3

import re
import sys
import json
from pprint import pprint


def clean(lin):
    a = lin.strip()
    parts = a.split(".")
    red = (
        filter(
            (
                lambda r: (
                    (r != "*") and
                    (not r.startswith("!"))
                )
            ),
            parts
        )
    )
    b = ".".join(red)
    return b


def main():
    items = list(map(clean, sys.stdin))
    tree = json.dumps(items, indent=None, sort_keys=True)
    ##
    ## Add unicode labels to each entry so this can be included in python2
    ## scripts.
    ##
    tree_uni = (
        re.sub(
            r"(?u)(?P<val>\u0022[^\u0022\s]+\u0022)",
            r"ur\g<val>",
            tree
        )
    )
    froze = "".join(["    DOMAINS = frozenset(\n        ", tree_uni, "\n    )"])
    print(froze)
    return True


if __name__ == "__main__":
    main()
    sys.exit(0)
